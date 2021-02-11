#!/usr/bin/node
window.$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  window.$('#hello').text(data.hello);
});
