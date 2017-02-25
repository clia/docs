(function() {
  var interval = setInterval(function() {
    if (!document.querySelector('app-route')) {
      return;
    }
    clearInterval(interval);
    window.parent.postMessage(JSON.stringify({kind: 'iframeHeight', height: document.documentElement.scrollHeight + 5}), '*');
  }, 200);
})();
