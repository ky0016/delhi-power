<?php
load_view("template/top.php");
load_view("template/navbarnew.php");
?>

<main>
	<div class="container">
	<br>
	  <div class="row">
	  	<div class="col s12 l6">
	  		<div class="card-panel" style="height:520px;">
	  		  <div class="row">
            <div class="col s12">
              <h4 class="teal-text text-darken-1 center">Contact Us</h4>
            </div>
          </div>
          <div class="row">
            <div class="col s6">
              <h6 class="teal-text text-darken-1">Address <i class="material-icons tiny">navigation</i></h6>
              <div class="grey-text">
                C-15<br>
                Aravali hostel<br>
                IIT Delhi<br>
                New Delhi - 110016<br>
                India
              </div>
            </div>
            <div class="col s6">
              <h6 class="teal-text text-darken-1">Mail <i class="material-icons tiny">mail</i></h6>
              <div class="grey-text">
                mohitsaini1196@gmail.com
              </div><br>
              <h6 class="teal-text text-darken-1">Call <i class="material-icons tiny">call</i></h6>
              <div class="grey-text">
                +91 750 375 9053
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col s12">
              <div class="card">
                <div id="map-canvas" style="height: 220px;"></div>
              </div>
            </div>
          </div>
	  		</div>
	  	</div>
	  	<div class="col s12 l6">
        <div class="card-panel" style="height:520px;">
	    		<div class="row">
		    		<?php
					    if(!empty($msg)) {
            ?>
            <div class="col s12">
					    <div class="light-blue card-panel">
                <h6 class="white-text"><?php echo $msg;?></h6>
              </div>
            </div>
					  <?php
              }
					    else {
					  ?>
	    		  <form id="contact-form" class="col s12" method="post">
	    		  	<div class="row">
	    		  	  <div class="col s12">
	    		  	  	<h5 class="teal-text">How can we help you?</h5><br>
	    		  	  </div>
	    		  	  <div class="input-field col s12">
	    		  	  	<input id="name" name="name" type="text" class="validate" required>
	    		  	  	<label for="name">Name</label>
	    		  	  </div>
	    		  	  <div class="input-field col s12">
	    		  	  	<input id="email" name="email" type="email" class="validate" required>
	    		  	  	<label for="email">Email</label>
	    		  	  </div>
	    		  	  <div class="input-field col s12">
	    		  	  	<input id="phone_number" name="phone" type="text" class="validate" required>
	    		  	  	<label for="phone_number">Phone Number</label>
	    		  	  </div>
	    		  	  <div class="input-field col s12">
	    		  	  	<textarea id="message" name="content" class="materialize-textarea" required></textarea>
          				<label for="message">Your Message</label>
	    		  	  </div>
	    		  	  <div class="col s12">
	    		  	  	<button type="submit" class="btn waves-light waves-effect" name="contactus" >Send
	    		  	  	  <i class="material-icons right">send</i>
	    		  	  	</button>
	    		  	  </div>
	    		  	</div>
	    		  </form>
	    		  <?php
				      }
			      ?>
	    		</div>
	    	</div>
	  	</div>
	  </div>
	</div>
</main>

<?php
load_view("template/footer.php");
load_view("template/bottom.php", Fun::mergeifunset($inp,array("js" => array("https://maps.googleapis.com/maps/api/js"), "curpage" => "contactus" )));
?>