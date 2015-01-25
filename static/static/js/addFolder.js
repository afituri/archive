$(document).ready(function(){
  var defaults = {
        disabled: true,
  };
  $.extend($.fn.editable.defaults, defaults);
  // $('#enable').click(function() {
  //   $('#section .editable').editable('toggleDisabled');
  // }); 
 
  $('a[id^="section"]').editable({
    url: '../../editFolder/',
    type: 'text',
    pk: 1,
    name: 'sectionName',
    validate: function(v) {
      if(!v) return 'الرجاء ادخال الحقل';
    }
  });
  
  $('#confdelete').click(function() {
    var id = $(this).val();
    $.get('../../deleteFolder/'+id, function(result){
      result=result.split('$');
      if(result[0]=="True"){
        $("#massege").removeClass("hidden");
      }else{
        window.location.href="/addFolder/"+result[1];

      }
        
    });
  });
  
  $('body').on('click','#delete', function(){
    var id = $(this).val();
    $('#confdelete').val(id);

  });

  $('body').on('click','#enable', function(){
    id=$(this).parent().parent().data('id');
    $('#section'+id).editable('toggleDisabled');

  });
});