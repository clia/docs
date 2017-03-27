---
title: Release notes
---

<!-- toc -->

<style>
.breaking {
  color: red;
  text-transform: capitalize;
  }
</style>

## [Release 2.0.0.rc.1](https://github.com/Polymer/polymer/releases/tag/v2.0.0-rc.1) (2017-03-06) {#v-2-0-0-rc.1}

The following notable changes have been made since the 2.0 Preview announcement.

-   The `config` getter on element classes has been replaced by individual `properties` and
    `observers` getters, more closely resembling the 1.x syntax.

    ```js
    static get properties() {
      return {
        aProp: String,
        bProp: Number
      }
    }
    static get observers() {
      return [
        '_observeStuff(aProp,bProp)'
      ]
    }
    ```

-   1.x-style dirty checking has been reinstated for better performance. An optional mixin is
    available for elements to skip dirty checking of objects and arrays, which may be more easy to
    integrate with some state management systems. For details, see
    [Using the MutableData mixin](devguide/data-system#mutable-data) in Data system concepts.

-   Support for dynamically-created `custom-style` elements has been added.

-   Support for the external style sheet syntax, `<link rel="import" type="css">` has
    been added. This was deprecated in 1.x, but will be retained until an alternate solution is
    available for importing unprocessed CSS.

-   New properties `rootPath` and `basePath` were added to `Polymer.Element` to allow authors
    to configure how URLs are rewritten inside templates. For details, see the
    [Update URLs in templates](./upgrade#urls-in-templates) in the Upgrade guide.


