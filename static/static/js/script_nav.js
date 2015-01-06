$(function(){

	//Make menus drop automatically
	$('ul.nav li.dropdown').hover(function() {
		$('.dropdown-menu',this).fadeIn();
	}, function() {
		$('.dropdown-menu',this).fadeOut('fast');
	}); //hover

	$(function () {
		$('#datetimepicker1').datetimepicker({
			pickTime: false
		});
	});
	$(function () {
		$('#datetimepicker3').datetimepicker({
			pickTime: false
		});
	});
    
	
}); //jQuery is loaded