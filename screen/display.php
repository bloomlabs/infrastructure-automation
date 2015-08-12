<html>
<meta http-equiv="refresh" content="305">
<script src="js-lib/jquery-2.1.3.min.js"></script>
<script src="js-lib/unslider.min.js"></script>
<script src="js-lib/leap-0.6.4.js"></script>
<link href='http://fonts.googleapis.com/css?family=Muli' rel='stylesheet' type='text/css'>
<style>
* {
  text-align: center;
  font-family: 'Muli', sans-serif;
}

body, div, ul, li {
  padding: 0;
  margin: 0;
}

#logo { width: 80%; padding-top: 2.3em; }

#banner { position: relative; overflow: auto; padding:0; position: fixed; bottom: 0; }
#banner li { list-style: none; }
#banner ul li { float: left; }

.iframe-slide, .img-slide {
  width: 1080px;
  height: 1200px;
  border: 0;
  overflow: hidden;
}

#guest-pw {
  font-size: 35pt;
  margin: 0;
  margin-bottom: 10px;
}
</style>
<body>
<img id="logo" src="logo.png"/>

<p id="guest-pw">
<?php 
  $contents = @file_get_contents("http://router:81/guest_password.txt");
  if ($contents === false) {
    echo "Ask one of our volunteers for the Guest Wifi password!";
  } else {
    echo "Guest WiFi Password:<br/><strong>$contents</strong>";
  }
?>
</p>

<div id="banner">
<ul>
  <?php
    $slides = scandir('slideshow/');
    sort($slides);
    foreach ($slides as $file) {
      $ext = pathinfo($file, PATHINFO_EXTENSION);
      $uri = rawurlencode($file);

      if ($file != '.' && $file != '..') {
        if ($ext == 'jpg' || $ext == 'png') {
          echo "<li><img class='img-slide' src='slideshow/$uri'></li>";
        } elseif ($ext == 'htm' || $ext == 'html') {
          echo "<li><iframe src='slideshow/$uri' class='iframe-slide' seamless='seamless' scrolling='no'></iframe></li>";
        }
      }
    }
  ?>
</ul>
</div>

<script>
var slidey = $('#banner').unslider({
  speed: 1000,
  delay: 15000,
});

var data = slidey.data('unslider');
</script>
<script src="js/lm-swiper.js"></script>
</body>
</html>
