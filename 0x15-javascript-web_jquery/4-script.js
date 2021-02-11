#!/usr/bin/node
$('#toggle_header').click(function () {
  if (!window.$('header').hasClass('red', "green"))
    {
      window.$('header').addClass('green');
    }
  if (window.$('header').hasClass('red')) {
    window.$('header').removeClass('red');
    window.$('header').addClass('green');
  } else {
    window.$('header').removeClass('green');
    window.$('header').addClass('red');
  }
});
