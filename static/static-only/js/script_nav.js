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
    
    $('#myModal').on('shown.bs.modal', function () {
    	$('#myInput').focus()
    })

    $('#myModalTwo').on('shown.bs.modal', function () {
    	$('#myInput').focus()
    })

    // $('body').on('click', '#delete ', function () {
    // 	var id = $(this).val();
    // 	$('#confdelete').val(id);
    // });

    // $('#confdelete').click(function() {
    // 	var id = $(this).val();
    // 	$.get('/root/deleteUser/'+id, function(result){
    // 		window.location.href="/root";
    // 	});
    // });

}); //jQuery is loaded