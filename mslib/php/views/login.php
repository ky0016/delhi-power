<?php
load_view("template/top.php");
load_view("template/navbarnew.php");
?>

  <main>
    <div class="container">
    <br>
      <div class="row">
        <div class="col s12 l6">
          <div class="card-panel">
            <?php
              load_view('template/form_errors.php',array("msg"=>$loginmsg));
            ?>
            <div class="row">
              <div class="col s12 l4 offset-l1">
                <h3 class="teal-text text-darken-1">Login</h3>
              </div>
              <div class="col s12 l7">
                <div class="row grey-text">
                  <div class="col s12">
                    <ul>
                      <li>Login for Players.</li>
                      <li>Don't have an account?</li>
                      <li><i class="material-icons left tiny">chevron_right</i>
                       Sign Up <a href="<?php echo BASE."signup"; ?>">here</a>.
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            
            <div id="login_section">
              <div class="row">
                <form class="col s12 offset-l1" method="post">
                  <div class="row">
                    <div class="input-field col s12 l10">
                      <input id="email" name="email" type="email" class="validate" required>
                      <label for="email">Email</label>
                    </div>
                  </div>
                  <div class="row">
                    <div class="input-field col s12 l10">
                      <input id="password" name="password" type="password" class="validate" required>
                      <label for="password">Password</label>
                    </div>
                  </div>
                  <div class="row">
                    <div class="input-field col s12 l10">
                      <button class="btn waves-effect waves-light" type="submit" name="login" >Login
                        <i class="material-icons right">send</i>
                      </button>
                    </div>
                  </div>
                </form>
              </div>
            </div>

            <div class="row">
              <div class="col s12 l10 offset-l1" style='' >
                <h6>
                  <a onclick="hs_toggle(['forgot_pass_section', 'login_section'], 700);ms.changesym(this);" style="cursor:pointer;">
                    <span id="forgot_prefix_arrow"><i class="material-icons tiny">keyboard_arrow_up</i></span>&nbsp;Forgot Password
                  </a>
                </h6>
              </div>
              <form class="col s12 l10 offset-l1" id="forgot_pass_section" onsubmit='form.req(this);return false;' data-action="forgotpass" data-res='success.push("Password reseting link is sent. check your mail.");' style='display:none;' >
                <div class="row">
                  <div class="col s12">
                    <p class="grey-text">Enter your email to send verification link.</p>
                  </div>
                </div>
                <div class="row">
                  <div class="input-field col s12">
                    <input id="email_forgot_pass" name="email" type="email" class="validate" required>
                    <label for="email_forgot_pass">Email</label>
                  </div>
                </div>
                <div class="row">
                  <div class="input-field col s12">
                    <button class="btn waves-effect waves-light" type="submit"  >Send</button>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>

        <div class="col s12 l6" style='' >
          <div class="card-panel">
          <br>
            <div class="row">
              <div class="col s12 l10 offset-l1">
                <h5 class="teal-text">Sign up with other platforms</h5>
              </div>
            </div>
            <div class="row">
              <div class="col s12 l10 offset-l1">
                <h6 class="grey-text"><i class="material-icons tiny left">chevron_right</i>Only Students can sign up from this section.</h6>
              </div>
            </div>
            <div class="row">
              <div class="col s12 l10 offset-l1">
                <a href="<?php echo HOST.""; ?>" class="btn-large waves-effect waves-light blue darken-3" style="width:100%;">Sign Up with facebook</a>
              </div>
            </div>
            <div class="row" style='' >
              <div class="col s12 l10 offset-l1">
                <a href="<?php echo HOST.""; ?>" class="btn-large waves-effect waves-light red darken-1" style="width:100%;">Sign Up with google+</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>

<?php
load_view("template/footer.php");
load_view("template/bottom.php");
?>
