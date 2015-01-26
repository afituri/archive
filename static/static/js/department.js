$(document).ready(function(){
    $('#search').on('click', function(){
        window.location.href="/department/"+$('#dept_id').val()+"/?q="+$('#query').val();
    });

    $('#date').on('click', function(){
        window.location.href="/department/"+$('#dept_id').val()+"/?start_date="+$('#start_date').val()+"&end_date="+$('#end_date').val();
    });
    $('#datetimepicker5').datetimepicker({
         pickTime: false,
            weekStart: 1,
            todayBtn:  1,
            autoclose: 1,
            todayHighlight: 1,
            startView: 2,
            minView: 2,
            forceParse: 0,
            format: "yyyy-mm-dd",
            viewMode: "months", 
            minViewMode: "months"
        });
    $('#datetimepicker6').datetimepicker({
        weekStart: 1,
        todayBtn:  1,
        autoclose: 1,
        todayHighlight: 1,
        startView: 2,
        minView: 2,
        forceParse: 0,
        format: "yyyy-mm-dd",
        viewMode: "months", 
        minViewMode: "months"
    });
});