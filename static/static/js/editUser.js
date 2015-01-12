$(document).ready(function(){
  $.resul=new Array();
  var defaults = {
        disabled: true,
  };
  $.extend($.fn.editable.defaults, defaults);
  $('#enable').click(function() {
    $('#user .editable').editable('toggleDisabled');
  }); 
  // $.getJSON("/employee/employee_type", function( json ) {
  //   var type=json.hnec;
  //   var type = json.employee;
  //   var i = 0;
  //   for(key in json.hnec){
  //     var k = new Object({id : i,value : key, text : json.hnec[key]});
  //     i++;
  //     $.type_h.push(k);

  //   }
  //   var i = 0;
  //   for(key in json.employee){
  //     var k = new Object({id : i,value : key, text : json.employee[key]});
  //     i++;
  //     $.type_e.push(k);

  //   }  
  //   $('#type_h').editable({
  //       url: '/employee/edit',
  //       source:$.type_h,
  //       pk: 1,
  //       name: 'type',
  //       validate: function(v) {
  //         if(!v) return 'الرجاء اختيار صفة الموظف';
  //       }
  //   }); 
  //   $('#type_e').editable({
  //   url: '/employee/edit',
  //   source:$.type_e,
  //   pk: 1,
  //   name: 'type',
  //   validate: function(v) {
  //     if(!v) return 'الرجاء اختيار صفة الموظف';
  //   }
  // });    
  // });
  
  //   $('#center_idcenter').editable({
  //       url: '/employee/edit',
  //       source: $.resul,
  //       select2: {
  //         width: 200,
  //         placeholder: 'Select center',
  //         allowClear: false
  //       } 
  //   });      
  // });
  // $('a[id^="p_type"]').editable({
  //   url: '/users/edit',
  //   source:[
  //     {value:"المفوضية",text:"المفوضية"},
  //     {value:"شخصي",text:"شخصي"},
  //   ]
  // });
  $('#username').editable({
    url: '../../edit/',
    type: 'text',
    pk: 1,
    name: 'username',
    title: 'Enter username',
    validate: function(v) {
      if(!v) return 'الرجاء ادخال اسم المستخدم';
    }
  });
  $('#first_name').editable({
    url: '../../edit/',
    type: 'text',
    pk: 1,
    name: 'first_name',
    title: 'Enter username',
    validate: function(v) {
      if(!v) return 'الرجاء ادخال الاسم';
    }
  });
  $('#last_name').editable({
    url: '../../edit/',
    type: 'text',
    pk: 1,
    name: 'last_name',
    title: 'Enter last_name',
    validate: function(v) {
      if(!v) return 'الرجاء ادخال اللقب';
    }
  });
  
    
  
 
  $('#email').editable({
    url: '../../edit/',
    type: 'text',
    pk: 1,
    name: 'email',
    title: 'Enter email',
    // success: function (res, newValue){
    //   return res.msg;
    // }
  });
  // $('#delete').click(function() {
  //   var id = $(this).val();
  //   $('#deleteemployee').val(id);
  // });
  // $('#deleteemployee').click(function() {
  //   var id = $(this).val();
  //   $.get('/employee/deleteemployee/'+id, function(result){
  //     window.location.href="/employee";
  //   });
  // });
  //  $('body').on('click', '#deletePhone ', function () {
  //   var id = $(this).val();
  //   $('#confphone').val(id);
  // }); 
  // $('#confphone').click(function() {
  //   var id = $(this).val();
  //   $.get('/root/deletePhone/'+id, function(result){
  //     window.location.href="/employee/editemployee/"+$('#confphone').data("id");;
  //   });
  // });
  // $("#form").validate({
  //   rules: {
  //     'phone[]': {
  //       required: true,
  //       minlength: 10,
  //       number: true,
  //     }
  //   },
  //   messages: {
  //     'phone[]': {
  //       required: "الرجاء ادخال رقم الهاتف",
  //       minlength: " يجب أن يكون الهاتف لا يقل عن 10 ارقام ",
  //       number: "الرجاء ادخال رقم الهاتف ",
  //     }
  //   },
  //   errorPlacement: function(error, element) {
  //     if (element.attr("name") == "phone[]") {
  //         error.insertAfter("#phone_input");
  //     } else {
  //         error.insertAfter(element);
  //     }
  //   }
  // });
});