<!doctype html>
<html lang="en_US">
<head>
	<?php
	opent("base",array("href"=>HOST));
	ocloset("title",$title);
	addall_css(array("mslib/css/materialize.min.css", "mslib/css/custom-stylesheet.css", "mslib/css/jquery.bxslider.css", "https://fonts.googleapis.com/icon?family=Material+Icons", "mslib/css/font-awesome.min.css", "assets/lib/select2/select2.css"));
	addall_css($css);
	addmycss();
	?>
	<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
	<meta charset="utf-8"/>
	<script type="text/javascript">
		var HOST="<?php echo HOST; ?>";
	</script>
</head>
