$(document).ready(function(){
	   $('#search').on('click', function(){
        window.location.href="?q="+$('#query').val();
    });

});