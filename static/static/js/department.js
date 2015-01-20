$(document).ready(function(){
    $('#search').on('click', function(){
        window.location.href="/department/"+$('#dept_id').val()+"/?q="+$('#query').val();
    });


    
});