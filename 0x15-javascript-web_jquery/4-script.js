#!/usr/bin/node
$('#toggle_header').click(function () {
  if (!$('header').hasClass('red', "green"))
    {
      $('header').addClass('green');
    }
  if ($('header').hasClass('red')) {
    $('header').removeClass('red');
    $('header').addClass('green');
  } else {
    $('header').removeClass('green');
    $('header').addClass('red');
  }
});
