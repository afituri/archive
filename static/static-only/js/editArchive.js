$(document).ready(function(){
  $.resul=new Array();
  var defaults = {
    disabled: true,
  };

  $('body').on('click', '#radioBtn a', function () {
    var sel = $(this).data('title');
    var tog = $(this).data('toggle');
    var a=$(this).siblings("#p_type" );
    a.val(sel);
    $(this).siblings("a").removeClass('active').addClass('notActive');
    $(this).removeClass('notActive').addClass('active');
  })

  $('body').on('click', '#deletePhone ', function () {
    var id = $(this).val();
    $('#confphone').val(id);
  });

  $('#confphone').click(function() {
    var id = $(this).val();
    $.get('/root/deletePhone/'+id, function(result){
      window.location.href="/root/edituser/"+$('#confphone').data("id");;
    });
  });

  $.extend($.fn.editable.defaults, defaults);
  $('#enable').click(function() {
    $('#user .editable').editable('toggleDisabled');
  }); 
  
  $('#level').editable({
    url: '/users/edit',
    source:[
      {value:0,text:"root"},
      {value:1,text:"admin"},
      {value:2,text:"manager"}
    ]
  });
  
  $('a[id^="p_type"]').editable({
    url: '/users/edit',
    source:[
      {value:"المفوضية",text:"المفوضية"},
      {value:"شخصي",text:"شخصي"},
    ]
  });
  
  $('#name').editable({
    // url: '/users/edit',
    type: 'text',
    pk: 1,
    name: 'name',
    title: 'Enter archive name',
  });
  
  $("a[id^='phone_number']" ).editable({
    url: '/users/edit',
    type: 'text',
    pk: 1,
    name: 'phone_number',
    title: 'Enter phone',
    validate: function(v) { 
      var flag = /^[0-9\b]+$/.test(v);
      if(!v) return 'الرجاء ادخال رقم الهاتف';
      if(v.length<10) return "يجب أن يكون الهاتف  لا يقل عن 10 ارقام";
      if(!flag) return "هذا ليس رقم هاتف";
    }
  });
  

  $('#type').editable({
    // url: '/users/edit',
    type: 'text',
    pk: 1,
    name: 'type',
    title: 'Enter type section',
    success: function (res, newValue){
      return res.msg;
    }
  });
  


  $('#text').editable({
    // url: '/users/edit',
    type: 'text',
    pk: 1,
    name: 'text',
    title: 'Enter text description',
    success: function (res, newValue){
      return res.msg;
    }
  });
  

  $('#ref_num').editable({
    // url: '/users/edit',
    type: 'text',
    pk: 1,
    name: 'ref_num',
    title: 'Enter ref_num ',
    success: function (res, newValue){
      return res.msg;
    }
  });

  $('#real_date').editable({
    url: '/users/edit',
    type: 'text',
    pk: 1,
    name: 'real_date',
    title: 'Enter email',
    success: function (res, newValue){
      return res.msg;
    }
  });
  
  $.get('/admin/getoffice',function(result){
    for ( var i = 0 ; i< result.length; i++){
      var k = new Object({id : i,value : result[i].idoffice, text : result[i].office_name});
      $.resul.push(k);
    }
    $('#office_idoffice').editable({
        url: '/users/edit',
        source: $.resul,
        select2: {
          width: 200,
          placeholder: 'Select country',
          allowClear: false
        } 
    });      
  });
  
  $('#name').editable('option', 'validate', function(v) {
    if(!v) return 'الرجاء ادخال اسم المستخدم';
  });
  
  $('#real_date').editable('option', 'validate', function(v) {
    if(!v) return 'الرجاء ادخال بريد اليكتروني';
    var emailReg = new RegExp(/^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/i);
    var valid = emailReg.test(v);
    if(!valid) return 'هذا ليس بريد اليكتروني';
  });
  
  $("#form").validate({
    rules: {
      'phone[]': {
        required: true,
        minlength: 10,
        number: true,
      }
    },
    messages: {
      'phone[]': {
        required: "الرجاء ادخال رقم الهاتف",
        minlength: " يجب أن يكون الهاتف لا يقل عن 10 ارقام ",
        number: "الرجاء ادخال رقم الهاتف ",
      }
    },
    errorPlacement: function(error, element) {
      if (element.attr("name") == "phone[]") {
          error.insertAfter("#phone_input");
      } else {
          error.insertAfter(element);
      }
    }
  });
});