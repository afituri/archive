$(document).ready(function(){
    $('#search').on('click', function(){
        window.location.href="/department/"+$('#dept_id').val()+"/?q="+$('#query').val();
    });

$('#datetimepicker5').datetimepicker({
     pickTime: false,
        weekStart: 1,
        todayBtn:  1,
        autoclose: 1,
        todayHighlight: 1,
        startView: 2,
        minView: 2,
        forceParse: 0
    });
    $('#datetimepicker6').datetimepicker({
        pickTime: true,
        weekStart: 1,
        todayBtn:  1,
        autoclose: 1,
        todayHighlight: 1,
        startView: 2,
        minView: 2,
        forceParse: 0
    });
});