$(document).ready(function(){
  var defaults = {
        disabled: true,
  };
  $.extend($.fn.editable.defaults, defaults);
  // $('#enable').click(function() {
  //   $('#section .editable').editable('toggleDisabled');
  // }); 
 
  $('a[id^="section"]').editable({
    url: '../editFolder/',
    type: 'text',
    pk: 1,
    name: 'sectionName',
    validate: function(v) {
      if(!v) return 'الرجاء ادخال الحقل';
    }
  });
  
  $('body').on('click','#enable', function(){
    id=$(this).parent().parent().data('id');
    $('#section'+id).editable('toggleDisabled');

  });
});