<?php
if($needpopup){
	load_view("popup.php",array("name"=>"alert"));
	load_view("popup.php",array("name"=>"confirm"));
	load_view("template/success.php");
}
?>
	<script src="js/jquery-2.1.1.min.js"></script>
	<script src="js/materialize.min.js"></script>
	<script src="js/jquery.bxslider.min.js"></script>
	<script src="js/custom-script.js"></script>
	<script src="js/jquery.easing.1.3.js"></script>
	<script src="js/jquery.raty.js"></script>

	<script src="assets/lib/select2/select2.min.js"></script>
<?php
	addall_js($js);
	echo "\n";
	addmyjs();
?>
	<script>
		runmypagecode("<?php echo g("curpage"); ?>");
	</script>

<?php
if($needbody){
?>

</body></html><?php
}
?>