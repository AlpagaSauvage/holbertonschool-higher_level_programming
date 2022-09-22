$.get('https://fourtonfish.com/hellosalut/?lang=fr', window.onload = function (data) {
  $('DIV#hello').text(data.hello);
});
