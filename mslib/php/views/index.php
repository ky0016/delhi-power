<?php
load_view("template/top.php", array("css" => array("css/custom-homestyle-v2.css") ));
load_view("template/navbarnew.php",$inp);
?>

<div id="index-banner" class="parallax-container">
  <div class="section no-pad-bot">
    <div class="container">
      <div class="row "  >
        <div class="col s12">
          <h1 class="header center white-text">
            <?php echo gi("myname"); ?>
          </h1>
        </div>
        <div class="col s12">
          <div class="rw-words-1">
            <h5 class="center">
              Get an Expert Adviser for
              <b>
                Any Sports, Any Time
              </b>
              !
            </h5>
            <h5 class="center">
              Be
              <b>
                Better
              </b>
              than what you are !
            </h5>
            <h5 class="center">
              We are for
              <b>
                Stud players just like you !
              </b>
            </h5>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="parallax" height="100%">
    <img src="images/banner.png" width="85%" alt="Banner" />
  </div>
</div>
<div class="container" id="container">
  <div class="section">
    <div class="row">
      <div class="col s12">
        <h3 class="header center teal-text text-darken-1" style="font-variant:small-caps">
          How it Works?
        </h3>
      </div>
      <div class="col s12 m4">
        <h2 class="header center">
          <i class="mdi-image-remove-red-eye large">
          </i>
        </h2>
        <h5 class="header center grey-text text-darken-2">
          Message us your problems.
        </h5>
      </div>
      <div class="col s12 m4">
        <h2 class="header center">
          <i class="mdi-device-access-time large">
          </i>
        </h2>
        <h5 class="header center grey-text text-darken-2">
          Schedule your goals
        </h5>
      </div>
      <div class="col s12 m4">
        <h2 class="header center">
          <i class="mdi-hardware-desktop-windows large">
          </i>
        </h2>
        <h5 class="header center grey-text text-darken-2">
          Start precticing
        </h5>
        <p class="light">
        </p>
      </div>
    </div>
  </div>
</div>
<div class="container-fluid">
  <div class="slider">
    <ul class="slides">
      <li>
        <img src="http://lorempixel.com/580/250/nature/1" />
        <!-- random image -->
        <div class="caption center-align">
          <h3>
            We are very stud people.
          </h3>
          <h5 class="light grey-text text-lighten-3">
            you will help you in playing.
          </h5>
        </div>
      </li>
      <li>
        <img src="http://lorempixel.com/580/250/nature/2" />
        <!-- random image -->
        <div class="caption left-align">
          <h3>
            Just message us very soon.
          </h3>
          <h5 class="light grey-text text-lighten-3">
            You need to pay us for help.
          </h5>
        </div>
      </li>
      <li>
        <img src="http://lorempixel.com/580/250/nature/3" />
        <!-- random image -->
        <div class="caption right-align">
          <h3>
            We will provide 24x7 help.
          </h3>
          <h5 class="light grey-text text-lighten-3">
            We help you so much.
          </h5>
        </div>
      </li>
      <li>
        <img src="http://lorempixel.com/580/250/nature/4" />
        <!-- random image -->
        <div class="caption center-align">
          <h3>
            We are good people.
          </h3>
          <h5 class="light grey-text text-lighten-3">
            here is our helpline.
          </h5>
        </div>
      </li>
    </ul>
  </div>
</div>


<div class="container" id="container">
  <div class="row">
    <div class="col s12 l6">
      <div class="row">
        <div class="col s12">
          <h5 class="header center teal-text text-darken-4 opensans-font">
            Why choose us
          </h5>
        </div>
      </div>
      <div class="row">
        <div class="col s12">
          <ul id="whyus_list" style="margin-top:0px;">
            <li>
              770+ Players and 57+ Sports are using us.
            </li>
            <li>
              Learn only from Expert people.
            </li>
            <li>
              Take help at the comfort of your time.
            </li>
            <li>
              Select the best Helpers.
            </li>
            <li>
              Because we care about Quality more.
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <div class="row">
    <div class="col s12">
      <div class="divider">
      </div>
    </div>
  </div>
</div>


<div class="row">
  <div class="col s12">
    <h3 class="header center teal-text text-darken-1" style="font-variant:small-caps">
      Why Us
    </h3>
  </div>
</div>
<div class="container" style='display:none;' >
  <div class="row border-bottom border-top" style="margin:0; padding:0;">
    <div class="col s12 m6 border-right">
      <h2 class="header center">
        <i class="mdi-communication-clear-all">
        </i>
      </h2>
      <p class=" center">
        Because we are stud.
      </p>
    </div>
    <div class="col s12 m6">
      <h2 class="header center">
        <i class="mdi-social-people">
        </i>
      </h2>
      <p class=" center">
        Because we are stud.
      </p>
    </div>
  </div>
  <div class="row border-bottom" style="margin:0; padding:0;">
    <div class="col s12 m6 border-right">
      <h2 class="header center">
        <i class="mdi-maps-place">
        </i>
      </h2>
      <p class=" center">
        Because we are stud.
      </p>
    </div>
    <div class="col s12 m6">
      <h2 class="header center">
        <i class="mdi-action-alarm">
        </i>
      </h2>
      <p class=" center">
        Because we are stud.
      </p>
    </div>
  </div>
</div>


<?php
load_view("template/footer.php",$inp);
load_view("template/bottom.php", $inp);
?>
