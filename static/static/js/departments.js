$(document).ready(function(){
  
  var defaults = {
        disabled: true,
  };

  $.extend($.fn.editable.defaults, defaults);

  $('a[id^="department"]').editable({
    url: '../../editDepartment/',
    type: 'text',
    pk: 1,
    name: 'departmentName',
    validate: function(v) {
      if(!v) return 'الرجاء ادخال الحقل';
    }
  });
  
  $('#confdelete').click(function() {
    var id = $(this).val();
    $.get('../../deleteDepartment/'+id, function(result){
      window.location.href="/Departments/";
    });
  });
  
  $('body').on('click','#delete', function(){
    var id = $(this).val();
    $('#confdelete').val(id);
  });

  $('body').on('click','#enable', function(){
    id=$(this).parent().parent().data('id');
    $('#department'+id).editable('toggleDisabled');
  });

});