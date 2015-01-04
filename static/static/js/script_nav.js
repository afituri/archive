$(function(){
	//highlight the current nav
	$("#home a:contains('Home')").parent().addClass('active');
	$("#home a:contains('addActive')").parent().addClass('active');
	$("#home a:contains('department')").parent().addClass('active');
	// $("#home a:contains('Home')").parent().addClass('active');
	// $("#home a:contains('Home')").parent().addClass('active');

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
    $(function () {
    	$('#datetimepicker9').datetimepicker({
			pickTime: false
		});
	});
	$(function () {
    	$('#datetimepicker10').datetimepicker({
			pickTime: false
		});
    });
	
}); //jQuery is loaded