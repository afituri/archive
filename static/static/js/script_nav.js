$(function(){
	//highlight the current nav
	$("#addFolder a:contains('addFolder')").parent().addClass('active');
	$("#addDepartment a:contains('addDepartment')").parent().addClass('active');
	$("#addArchive a:contains('addArchive')").parent().addClass('active');
	$("#editArchive a:contains('editArchive')").parent().addClass('active');
	$("#department a:contains('department')").parent().addClass('active');
	$("#cpanel a:contains('cpanel')").parent().addClass('active');

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