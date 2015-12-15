<?php
session_start();
require_once( 'Facebook/FacebookHttpable.php' );
require_once( 'Facebook/FacebookCurl.php' );
require_once( 'Facebook/FacebookCurlHttpClient.php' );

require_once( 'Facebook/FacebookSession.php' );
require_once( 'Facebook/FacebookRedirectLoginHelper.php' );
require_once( 'Facebook/FacebookRequest.php' );
require_once( 'Facebook/FacebookResponse.php' );
require_once( 'Facebook/FacebookSDKException.php' );
require_once( 'Facebook/FacebookRequestException.php' );
require_once( 'Facebook/FacebookAuthorizationException.php' );
require_once( 'Facebook/GraphObject.php' );

require_once 'Google/Google_Client.php'; // include the required calss files for google login
require_once 'Google/contrib/Google_PlusService.php';
require_once 'Google/contrib/Google_Oauth2Service.php';

use Facebook\FacebookSession;
use Facebook\FacebookRedirectLoginHelper;
use Facebook\FacebookRequest;
use Facebook\FacebookResponse;
use Facebook\FacebookSDKException;
use Facebook\FacebookRequestException;
use Facebook\FacebookAuthorizationException;
use Facebook\GraphObject;
 //App Id And Secret
FacebookSession::setDefaultApplication('757676021014496','6cb34db00433f66f30a3ad7a485defb8');

// Login Helper with redirect URI
$helper = new FacebookRedirectLoginHelper('http://getiitians.com/teaching/pankaj/signup.php');
 
try {
  $session = $helper->getSessionFromRedirect();
}
catch( FacebookRequestException $ex ) {
  echo "Session not found..";
  // Exception
}
catch( Exception $ex ) {
  echo "In this branch";

  // When validation fails or other local issues
}

// Checking Session
if(isset($session))
{

echo "Session is set";
  // Request for user data
  $request = new FacebookRequest( $session, 'GET', '/me' );
  $response = $request->execute();
  // Response
  $data = $response->getGraphObject(); 
  $fbid = $data->getProperty('id');              // To Get Facebook ID
  $fbfullname = $data->getProperty('name'); // To Get Facebook full name
  $femail = $data->getProperty('email'); 
  print_r($data,1);
}



/// google login

/*$client = new Google_Client();
$client->setApplicationName("getiitians"); // Set your applicatio name
$client->setScopes(array('https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/plus.me')); // set scope during user login
$client->setClientId('112208890022-17m8n130aji59c93iksv8o6jbm6uqqm8.apps.googleusercontent.com'); // paste the client id which you get from google API Console
$client->setClientSecret('9P2NVsZEJKVZI-phsNpKnyE'); // set the client secret
$client->setRedirectUri('http://www.getiitians.com/teaching/pankaj/signup.php'); // paste the redirect URI where you given in APi Console. You will get the Access Token here during login success
$client->setDeveloperKey('AIzaSyD1u8ruqCSoGIZfhJOIAIk9JDMz8JH6vWw'); // Developer key
$plus = new Google_PlusService($client);
$oauth2 	= new Google_Oauth2Service($client); // Call the OAuth2 class for get email address

if(isset($_GET['code'])) {
	$client->authenticate(); // Authenticate
        $_SESSION['token'] = $client->getAccessToken();
	header('Location: http://' . $_SERVER['HTTP_HOST'] . $_SERVER['PHP_SELF']);
}


if (isset($_SESSION['token'])) 
{ 
  $client->setAccessToken($_SESSION['token']);
}



if ($client->getAccessToken()) 
{
  $user 		= $oauth2->userinfo->get();
  $me 			= $plus->people->get('me');
  $optParams 	= array('maxResults' => 100);
  $activities 	= $plus->activities->listActivities('me', 'public',$optParams);
  // The access token may have been updated lazily.
  $_SESSION['token'] 		= $client->getAccessToken();
  

  $gemail=$user['email'];
  $gid=$me['id'];
  $gname=$me['displayName'];
  echo $gname ;
  
} 
else 
{
  $authUrl = $client->createAuthUrl(); 
}	

*/

?>
<a href="<?php echo $helper->getLoginUrl(array(
   'scope' => 'email')); ?>">Fb login</a>


