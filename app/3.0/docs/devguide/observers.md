---
title: Observers and computed properties
---

<!-- toc -->


Observers are methods invoked when [observable changes](data-system#observable-changes) occur to the element's
data. There are two basic types of observers:


*   Simple observers observe a single property.
*   Complex observers can observe one or more properties *or paths*.

You use different syntax for declaring these two types of observers, but in most cases they function
the same way. Each observer has one or more _dependencies_. The observer method runs when an
observable change is made to a dependency.

Computed properties are virtual properties based on one or more pieces of the element's data. A
computed property is generated by a computing function—essentially, a complex observer that returns
a value.

Unless otherwise specified, notes about observers apply to simple observers, complex observers, and
computed properties.


### 观察者和元素初始化

The first call to an observer is deferred until the following criteria are met:

*   The element is fully configured (default values have been assigned and data bindings
    propagated).
*   **At least one** of the dependencies is *defined* (that is, they don't have the value
    `undefined`).

After the initial call, **each observable change** to a dependency generates a call to the
observer, **even if the new value for the dependency is <code>undefined</code>.**


This allows the element to avoid running observers in the default case.


### 观察者是同步的

Like all property effects, observers are synchronous. If the observer is likely to be invoked
frequently, consider deferring time-consuming work, like inserting or removing DOM. For example, you
can use the [`async`](/{{{polymer_version_dir}}}/docs/api/utils/async) module to defer work.

However, if you handle a data change asynchronously, note that the parameters passed to the observer
may not match the element's current property values.


## 简单的观察者 {#simple-observers}

Simple observers are declared in the `properties` object, and always observe a single property. You
shouldn't assume any particular initialization order for properties: if your observer depends on
multiple properties being initialized, use a complex observer instead.

Simple observers are fired the first time the property becomes defined (!= `undefined`), and on
every change thereafter, *_even if the property becomes undefined._*

Simple observers only fire when the property *itself* changes. They don't fire on subproperty
changes, or array mutation. If you need these changes, use a complex observer with a wildcard path,
as described in [Observe all changes related to a path](#deep-observation).

You specify an observer method by name. The host element must have a method with that name.

The observer method receives the new and old values of the property as arguments.

### 观察属物  {#change-callbacks}

Define a simple observer by adding an `observer` key to the property's declaration, identifying
the observer method by name.

Example { .caption }

```js
import { PolymerElement } from '@polymer/polymer/polymer-element.js';

class XCustom extends PolymerElement {
  static get properties() {
    return {
      active: {
        type: Boolean,
        // Observer method identified by name
        observer: '_activeChanged'
      }
    }
  }
  // Observer method defined as a class method
  _activeChanged(newValue, oldValue) {
    this.toggleClass('highlight', newValue);
  }
}
customElements.define('x-custom', XCustom);
```

The observer method is usually defined on the class itself, although an observer method can also be
defined by a superclass, subclass, or a class mixin, as long as the named method exists on the
element.

**Warning:**
A single property observer shouldn't rely on any other properties,
sub-properties, or paths because the observer can be called while these
dependencies are undefined. See [Always include dependencies
as observer arguments](#dependencies) for details.
{ .alert .alert-warning }



## 复杂的观察者 {#complex-observers}

Complex observers are declared in the `observers` array.
Complex observers can monitor one or more paths. These
paths are called the observer's *dependencies*.

```js
static get observers() {
  return [
    // Observer method name, followed by a list of dependencies, in parenthesis
    'userListChanged(users.*, filter)'
  ]
}
```

Each dependency represents:

*   A specific property (for example, `firstName`).

*   A specific subproperty (for example, `address.street`).

*   Mutations on a specific array (for example, `users.splices`).

*   All subproperty changes and array mutations below a given path (for example, `users.*`).

The observer method is called with one argument for each dependency. The argument type varies
depending on the path being observed.

*   For simple property or subproperty dependencies, the argument is the new value of the property
    or subproperty.

*   For array mutations the argument is a *change record* describing the change.

*   For wildcard paths, the argument is a change record describing the change, including the
    exact path that changed.

Note that any of the arguments can be `undefined` when the observer is called.

Complex observers should only depend on their declared dependencies.

Related tasks:

*   [Observe multiple properties or paths](#multi-property-observers)
*   [Observe array changes](#array-observation)
*   [Observe all changes to a path](#deep-observation)



### 观察对多个属物的更改 {#multi-property-observers}

To observe changes to a set of properties, use the `observers`
array.

These observers differ from single-property observers in a few ways:

*   Multi-property observers and computed properties run once at initialization if **any**
    dependencies are defined. After that, the observers run whenever there is an
    [observable change](data-system#observable-changes) to any dependency.

*   Observers do not receive `old` values as arguments, only new values.  Only single-property
    observers defined in the `properties` object receive both `old` and `new` values.

Example { .caption }

```js
import { PolymerElement } from '@polymer/polymer/polymer-element.js';

class XCustom extends PolymerElement {

  static get properties() {
    return {
        preload: Boolean,
        src: String,
        size: String
    }
  }

  // Each item of observers array is a method name followed by
  // a comma-separated list of one or more dependencies.
  static get observers() {
    return [
        'updateImage(preload, src, size)'
    ]
  }

  // Each method referenced in observers must be defined in
  // element prototype. The arguments to the method are new value
  // of each dependency, and may be undefined.
  updateImage(preload, src, size) {
    // ... do work using dependent values
  }
}

customElements.define('x-custom', XCustom);
```

In addition to properties, observers can also observe [paths to sub-properties](#observing-path-changes),
[paths with wildcards](#deep-observation), or [array changes](#array-observation).

### 观察子属物变化 {#observing-path-changes}

To observe changes in object sub-properties:

*   Define an `observers` array.
*   Add an item to the `observers` array. The item must be a method name
    followed by a comma-separated list of one or more paths. For example,
    `onNameChange(dog.name)` for one path, or
    `onNameChange(dog.name, cat.name)` for multiple paths. Each path is a
    sub-property that you want to observe.
*   Define the method in your element prototype. When the method is called,
    the argument to the method is the new value of the sub-property.

In order for Polymer to properly detect the sub-property change, the
sub-property must be updated in one of the following two ways:

*   Via a [property binding](data-binding#property-binding).
*   By calling [`set`](model-data#set-path).

Example { .caption }

```js
import { PolymerElement, html } from '@polymer/polymer/polymer-element.js';

class XCustom extends PolymerElement {
  static get template () {
    return html`
      <!-- Sub-property is updated via property binding. -->
      <input value="{{user.name::input}}">
    `;
  }
  static get properties() {
    return {
      user: {
        type: Object,
        value: function() {
          return {};
        }
      }
    }
  }
  // Observe the name sub-property on the user object
  static get observers() {
    return [
        'userNameChanged(user.name)'
    ]
  }
  // For a property or sub-property dependency, the corresponding
  // argument is the new value of the property or sub-property
  userNameChanged: function(name) {
    if (name) {
      console.log('new name: ' + name);
    } else {
      console.log('user name is undefined');
    }
  }
}
customElements.define('x-custom', XCustom);
```

### 观察数组突变 {#array-observation}

Use an array mutation observer to call an observer function whenever an array
item is added or deleted using Polymer's [array mutation methods](model-data#array-mutation).
Whenever the array is mutated, the observer receives a change record
representing the mutation as a set of array splices.

Polymer only calls the array mutation observer when the array items change, **not**
for changes to the top-level array

In many cases, you'll want to observe both array mutations *and* changes to
sub-properties of array items, in which case you should use a wildcard path,
as described in [Observe all changes related to a path](#deep-observation).

**Observable array mutation.**
Use Polymer's [array mutation methods](model-data#array-mutation) wherever possible to
ensure that elements with registered interest in the array mutations are
properly notified. If you can't avoid the native methods, you need to notify
Polymer about array changes as described in [Using native array mutation
methods](model-data#notifysplices).
{ .alert .alert-warning }

To create a splice observer, specify a path to an array followed by `.splices`
in your `observers` array.

``` js
static get observers() {
  return [
    'usersAddedOrRemoved(users.splices)'
  ]
}
```

Your observer method should accept a single argument. When your observer method
is called, it receives a change record of the mutations that
occurred on the array. Each change record provides the following property:

*   `indexSplices`. The set of changes that occurred to the array, in
     terms of array indexes. Each `indexSplices` record contains the following
     properties:

     -   `index`. Position where the splice started.
     -   `removed`. Array of `removed` items.
     -   `addedCount`. Number of new items inserted at `index`.
     -   `object`: A reference to the array in question.
     -   `type`: The string literal 'splice'.


**Change record may be undefined.** The change record may be undefined the first
time the observer is invoked, so your code should guard against this, as shown
in the example.
{ .alert .alert-info }

Example { .caption }

```js
import { PolymerElement } from '@polymer/polymer/polymer-element.js';

class XCustom extends PolymerElement {
  static get properties() {
    return {
      users: {
        type: Array,
        value: function() {
          return [];
        }
      }
    }
  }
  // Observe changes to the users array
  static get observers() {
    return [
      'usersAddedOrRemoved(users.splices)'
    ];
  }
  // For an array mutation dependency, the corresponding argument is a change record
  usersAddedOrRemoved(changeRecord) {
    if (changeRecord) {
      changeRecord.indexSplices.forEach(function(s) {
        s.removed.forEach(function(user) {
          console.log(user.name + ' was removed');
        });
        for (var i=0; i<s.addedCount; i++) {
          var index = s.index + i;
          var newUser = s.object[index];
          console.log('User ' + newUser.name + ' added at index ' + index);
        }
      }, this);
    }
  }
  ready() {
    super.ready();
    this.push('users', {name: "Jack Aubrey"});
  }
}
customElements.define('x-custom', XCustom);
```

### 观察数组的长度 

To create an observer on the length of an array, specify a path to an array followed by `.length` in your `observers` array:

``` js
static get observers() {
  return [
    'usersAddedOrRemoved(users.length)'
  ]
}
```

Your length observer method should accept a single argument (the new array length).

### 观察与路径相关的所有更改 {#deep-observation}

To call an observer when any (deep) sub-property of an
object or array changes, specify a path with a wildcard (`*`).

When you specify a path with a wildcard, the argument passed to your
observer is a change record object with the following properties:

*   `path`. Path to the property that changed. Use this to determine whether
    a property changed, a sub-property changed, or an array was mutated.
*   `value`. New value of the path that changed.
*   `base`. The object matching the non-wildcard portion of the path.

For array mutations, `path` is the path to the array that changed,
followed by `.splices`. The `value` field includes the `indexSplices`
property described in [Observe array mutations](#array-observation). 

Example { .caption }

```js
import { PolymerElement, html } from '@polymer/polymer/polymer-element.js';

class XCustom extends PolymerElement {
  static get template() {
    return html`
      <input value="{{user.name.first::input}}" placeholder="First Name">
      <input value="{{user.name.last::input}}" placeholder="Last Name">
    `;
  }
  static get properties() {
    return {
      user: {
        type: Object,
        value: function() {
          return {'name':{}};
        }
      }
    }
  }
  static get observers() {
    return [
        'userNameChanged(user.name.*)'
    ]
  }
  userNameChanged(changeRecord) {
    console.log('path: ' + changeRecord.path);
    console.log('value: ' + changeRecord.value);
  }
}
customElements.define('x-custom', XCustom);
```

**Array mutations may also raise a change record for the length of the array.**
If an array mutation also caused the length of the array to change, a wildcard observer on an array path raises a separate change record for the array length. The `path` field of the length change record is the path to the array that changed, followed by `.length`. The `value` field is the new array length. { .alert .alert-info }

### 识别所有依赖项 {#dependencies}

Observers shouldn't rely on any properties, sub-properties, or paths other
than those listed as dependencies of the observer. This creates "hidden" dependencies,
which can result in unexpected behavior:

-   The observer can be called before the hidden dependency is configured.
-   The observer isn't called when the hidden dependency changes.

For example:

```js
static get properties() {
  return {
    firstName: {
      type: String,
      observer: 'nameChanged'
    },
    lastName: {
      type: String
    }
  }
}

// WARNING: ANTI-PATTERN! DO NOT USE
nameChanged(newFirstName, oldFirstName) {
  // Not invoked when this.lastName changes
  var fullName = newFirstName + ' ' + this.lastName;
  // ...
}
```

Note that Polymer doesn't guarantee that properties are
initialized in any particular order.

In general, if your observer relies on multiple dependencies, use a
[multi-property observer](#multi-property-observers) and list every dependency
as an argument to the observer. This ensures that all dependencies are
configured before the observer is called.

```js
static get properties() {
  return {
    firstName: {
      type: String
    },
    lastName: {
      type: String
    }
  }
}

static get observers() {
  return [
    'nameChanged(firstName, lastName)'
  ]
}

nameChanged: function(firstName, lastName) {
  console.log('new name:', firstName, lastName);
}
```

If you must use a single property observer and must rely on other properties (for
example, if you need access to the old value of the observed property, which
you won't be able to access with a multi-property observer),
take the following precautions:

*   Check that all dependecies are defined
    (for example, `if this.lastName !== undefined`) before using them in your
    observer.

Keep in mind, however, that the observer is only called when one of the
dependencies listed in its arguments changes. For example, if an observer
relies on `this.firstName` but does not list it as a dependency, the observer
is not called when `this.firstName` changes.

## 被计算的属物 {#computed-properties}

Computed properties are virtual properties computed on the basis of one or more paths. The computing
function for a computed property follows the same rules as a complex observer, except that it
returns a value, which is used as the value of the computed property.

As with complex observers, the computing function is run once at initialization if **any**
dependencies are defined. After that, the function runs whenever there is an
[observable changes](data-system#observable-changes) to any dependency.

### 定义被计算的属物

Polymer supports virtual properties whose values are calculated from other properties.

To define a computed property, add it to the `properties` object with a
`computed` key mapping to a computing function:

```
fullName: {
  type: String,
  computed: 'computeFullName(first, last)'
}
```


The function is provided as a string with dependencies as arguments in parenthesis.

As with complex observers, the computing function is not invoked until at least one dependency is
defined (`!== undefined`). Subsequently, the function is called once for any
[observable change](data-system#observable-changes) to its dependencies.


**Note:**
The definition of a computing function looks like the
definition of a [multi-property observer](#multi-property-observers),
and the two act almost identically. The only difference is that the
computed property function returns a value that's exposed as a virtual property.
{ .alert .alert-info }

```js
import { PolymerElement, html } from '@polymer/polymer/polymer-element.js';

class XCustom extends PolymerElement {
  static get template() {
    return html`
      <p>My name is <span>{{fullName}}</span></p>
    `;
  }
  static get properties() {
    return {
      first: String,
      last: String,
      fullName: {
        type: String,
        // when `first` or `last` changes `computeFullName` is called once
        // and the value it returns is stored as `fullName`
        computed: 'computeFullName(first, last)'
      }
    }
  }
  computeFullName(first, last) {
    return first + ' ' + last;
  }
}
customElements.define('x-custom', XCustom);
```

Arguments to computing functions may be simple properties on the element, as
well as any of the arguments types supported by `observers`, including [paths](#observing-path-changes),
[paths with wildcards](#deep-observation), and [paths to array splices](#array-observation).
The arguments received by the computing function match those described in the sections referenced above.

**Note:**
If you only need a computed property for a data binding, you
can use a computed binding instead. See
[Computed bindings](data-binding#annotated-computed).
{ .alert .alert-info }

## 动态观察者方法 {#dynamic-observer-methods}

If the observer method is declared in the `properties` object, the method is considered _dynamic_:
the method itself may change during runtime. A dynamic method is considered an extra dependency of
the observer, so the observer re-runs if the method itself changes. For example:

```js
import { PolymerElement } from '@polymer/polymer/polymer-element.js';

class NameCard extends PolymerElement {
  static get properties() {
    return {
      // Override default format by assigning a new formatter
      // function
      formatter: {
        type: Function
      },
      formattedName: {
        computed: 'formatter(name.title, name.first, name.last)'
      },
      name: {
        type: Object,
        value() {
         return { title: "", first: "", last: "" };
        }
      }
    }
  }
  constructor() {
    super();
    this.formatter = this.defaultFormatter;
  }
  defaultFormatter(title, first, last) {
    return `${title} ${first} ${last}`
  }
}
customElements.define('name-card', NameCard);
```

Setting a new value for `formatter` causes the `formattedName` property to update, even if the `name`
property doesn't change:

```js
nameCard.name = { title: 'Admiral', first: 'Grace', last: 'Hopper'}
console.log(nameCard.formattedName); // Admiral Grace Hopper
nameCard.formatter = function(title, first, last) {
  return `${last}, ${first}`
}
console.log(nameCard.formattedName); // Hopper, Grace
```

Since a dynamic observer property counts as a dependency, if the method is defined, the
observer runs at initialization, even if none of the other dependencies are defined.

## 动态添加观察者和被计算的属物 {#dynamic-observers}

In some cases, you may want to add an observer or computed property dynamically. A set of instance
methods allow you to add a simple observer, complex observer, or computed property to the current
element _instance_.

### 动态添加简单的观察者

You can create a simple observer dynamically using the `_createPropertyObserver` instance method.
For example:

```js
this._observedPropertyChanged = (newVal) => { console.log('observedProperty changed to ' + newVal); };
this._createPropertyObserver('observedProperty', '_observedPropertyChanged', true);
```

The optional third argument determines whether the method itself (in this case, `_observedPropertyChanged`)
should be treated as a dependency.

### 动态添加复杂的观察者

You can create a computed property dynamically using the `_createMethodObserver` instance method.
For example:

```js
this._createMethodObserver('_observeSeveralProperties(prop1,prop2,prop3)', true);
```

The optional second argument determines whether the method itself (in this case, `_observeSeveralProperties`)
should be treated as a dependency.


### 动态添加被计算的属物

You can create a computed property dynamically using the `_createComputedProperty` instance method.
For example:

```js
this._createComputedProperty('newProperty', '_computeNewProperty(prop1,prop2)', true);
```

The optional third argument determines whether the method itself (in this case, `_computeNewProperty`)
should be treated as a dependency.
