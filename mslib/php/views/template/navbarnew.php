<body>
	<!-- Dropdown for Create Account -->
	<ul id="dropdownaccount" class="dropdown-content">
		<li class="<?php pit('active', g("curpage")==='profile');?>"><a href="<?php echo BASE."profile" ;?>" >Profile&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size:13px;" class="grey-text">for myinfo</span></a></li>
		<li class="<?php pit('active', g("curpage")==='account');?>"><a href="<?php echo BASE."account" ;?>" >Account&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size:13px;" class="grey-text">for setting</span></a></li>
		<li class=""><a href="<?php echo HOST."?logout"; ?>" >Logout&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size:13px;" class="grey-text">for exit</span></a></li>
	</ul>

	<!-- NavBar -->
	<div class="navbar-fixed" >
		<nav class="teal darken-3" role="navigation">
			<div class="nav-wrapper">
				<a href="" class="brand-logo"><?php echo gi("myname"); ?></a>
				<a href="#" data-activates="mobile-demo" class="button-collapse"><i class="material-icons">menu</i></a>
				<ul id="nav-mobile" class="right hide-on-med-and-down">
					<li class="<?php pit('active', g("curpage")==='aboutus');?>"><a href="<?php echo BASE."aboutus"; ?>">About Us</a></li>
					<li class="<?php pit('active', g("curpage")==='contactus');?>"><a href="<?php echo BASE."contactus"; ?>">Contact Us</a></li>

					<?php
					if (User::islogin()) {
					?>
					<li>
						<a class="dropdown-button" href="#" data-beloworigin="true" data-activates="dropdownaccount">
							<?php echo Fun::smilymsg(fixedlen(getval("name", g("myf"), "My Profile"))); ?> <i class="material-icons right">arrow_drop_down</i>
						</a>
					</li>
					<?php
					}
					else {
					?>
					<li class="<?php pit('active', g("curpage")==='login');?>"><a href="<?php echo BASE."login"; ?>">Login</a></li>
					<li class="<?php pit('active', g("curpage")==='signup');?>"><a href="<?php echo BASE."signup"; ?>">Signup</a></li>
					<?php
					}
					?>

					<form class="right" action="<?php echo BASE."search"; ?>"  >
						<div class="input-field teal darken-4">
							<input id="search" type="search" placeholder="Search Tutors" autocomplete="off" name="q" >
							<label for="search"><i class="material-icons">search</i></label>
							<button type="button" style="display:none;" ></button>
						</div>
					</form>
				</ul>
			</div>
		</nav>
	</div>

	<!-- SideNav -->
	<ul class="side-nav" id="mobile-demo">
		<li class="<?php pit('active', g("curpage")==='aboutus');?>"><a href="<?php echo BASE."aboutus"; ?>">About Us</a></li>
		<li class="<?php pit('active', g("curpage")==='contactus');?>"><a href="<?php echo BASE."contactus"; ?>">Contact Us</a></li>

		<?php
		if (User::islogin()) {
		?>
		<li class="<?php pit('active', g("curpage")==='profile');?>"><a href="<?php echo BASE."profile" ;?>">Profile</a></li>
		<li><a href="<?php echo BASE."?logout"; ?>">Logout</a></li>
		<?php
		}
		else {
		?>
		<li class="<?php pit('active', g("curpage")==='login');?>"><a href="<?php echo BASE."login"; ?>">Login</a></li>
		<li class="<?php pit('active', g("curpage")==='signup');?>">
			<a href="<?php echo BASE."signup" ;?>">Signup&nbsp;&nbsp;&nbsp;&nbsp;
			<span style="font-size:13px;" class="grey-text">for Students</span></a>
		</li>
		<li class="<?php pit('active', g("curpage")==='joinus');?>">
			<a href="<?php echo BASE."joinus" ;?>">Joinus&nbsp;&nbsp;&nbsp;&nbsp;
			<span style="font-size:13px;" class="grey-text">for Tutors</span></a>
		</li>
		<?php
		}
		?>

		<div class="row grey lighten-3">
			<form class="col s12">
				<div class="row">
					<div class="input-field col s12">
						<input id="sidenav_search" type="text" name="q" autocomplete="off">
						<label for="sidenav_search">Search Tutors</label>
					</div>
				</div>
				<div class="row">
					<div class="col s12">
						<button type="button" class="btn waves-effect waves-light">Search
							<i class="material-icons right">search</i>
						</button>
					</div>
				</div>
			</form>
		</div>
	</ul>
