$(document).ready(function(){
  
    $.resul=new Array();
        var defaults = {
        disabled: true,
    };
    
    $.extend($.fn.editable.defaults, defaults);
        $('#enable').click(function() {
        $('#tableEditArchive .editable').editable('toggleDisabled');
    });
    
    $('#name').editable({
        url: '../../editArchiveEditable/',
        type: 'text',
        pk: 1,
        title: 'Enter archive name',
        validate: function(v) {
            if(!v) return 'الرجاء ادخال الحقل';
        }
    });

    $('#textarea').editable({
        url: '../../editArchiveEditable/',
        type: 'text',
        pk: 1,
        title: 'Enter text description',
        rows: 10,
        validate: function(v) {
            if(!v) return 'الرجاء ادخال الوصف';
        }
    });

    $('#ref_num').editable({
        url: '../../editArchiveEditable/',
        type: 'text',
        pk: 1,
        title: 'Enter ref_num ',
        validate: function(v) {
            if(!v) return 'الرجاء ادخال الرقم الايشاري';
        }
    });

    $('#real_date').editable({

        url: '../../editArchiveEditable/',
        format: 'yyyy-mm-dd',    
        viewformat: 'yyyy-mm-dd',    
        datetimepicker: {
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
        },
        validate: function(v) {
            if(!v) return 'الرجاء ادخال التاريخ';
        }
    });

    $.get('../../getArchiveType/'+$("#idDept").val(),function(result){
        result=result.split('$');
        key =(result.length-1)/2;
            for ( var i = 0 ; i < key; i++){
                var k = new Object({id : i,value : result[key+i], text : result[i]});
                $.resul.push(k);
            }
        $('#typesec').editable({
            url: '../../editArchiveEditable/',
            params:$('#typesec').data('params'),
            source: $.resul,
            success: function(response, newValue) {
                console.log(newValue);
            }
        });      
    });
    $('body').on('click','#deletefil', function(){
        var id = $(this).val();
        $('#fildelet').val(id);
    });
    $('#fildelet').click(function() {
    var id = $(this).val();
    $.get('../../deleteFile/'+id, function(result){
        $('#file'+id).remove()
    });
  });

    $('#dle').click(function() {
        $.get('../../deleteArchive/'+$('#dle').val(), function(result){
            window.location.href="/department/"+result;
    });
    });
});