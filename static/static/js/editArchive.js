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
        url: '../editArchiveEditable/',
        type: 'text',
        pk: 1,
        name: 'name',
        title: 'Enter archive name',
    });

    


    $('#textarea1').editable({
        url: '../editArchiveEditable/',
        type: 'text',
        pk: 1,
        name: 'text',
        title: 'Enter text description',
        rows: 10,
        // success: function (res, newValue){
        //   return res.msg;
        // }
    });

    $('#ref_num').editable({
        url: '../editArchiveEditable/',
        type: 'text',
        pk: 1,
        name: 'ref_num',
        title: 'Enter ref_num ',
        // success: function (res, newValue){
        //   return res.msg;
        // }
    });

    $('#real_date').editable({
        url: '../editArchiveEditable/',
        format: 'yyyy-mm-dd hh:ii',    
        viewformat: 'dd/mm/yyyy hh:ii',    
        datetimepicker: {
            weekStart: 1
        }
    });

 

    $.get('../../getArchiveType/'+$("#idDept").val(),function(result){
        result=result.split('$');
        key =(result.length-1)/2;
            for ( var i = 0 ; i < key; i++){
                alert(result[i]);
                var k = new Object({id : i,value : result[key+i], text : result[i]});
                $.resul.push(k);
            }
        $('#type').editable({
            url: '../../editArchiveEditable/',
            source: $.resul

            
        });      
    });
  
});