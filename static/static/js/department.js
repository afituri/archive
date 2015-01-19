$(document).ready(function(){
    $('#search').on('input', function(){
        $.get('/search/'+$(this).val(), function(result){
            
        });
    });


    
});