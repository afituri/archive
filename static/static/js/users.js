$(document).ready(function(){
  // validate signup form on keyup and submit
  $('#deptname').prop('disabled', true);
  $('#usertype').click(function() {
		var id = $('#usertype').val();
		if(id >0){
			$('#deptname').prop('disabled', false);
		}else{
			$('#deptname').prop('disabled', true);
		}
	});
  // $.validator.addMethod("checkUsername", function(value, element) {
  // 	$.resul=new Array();
  // 		$.ajax({
  //              type: "POST",
  //              url: "username/",
  //              data: {'username': $('#username').val(), 'csrfmiddlewaretoken': $('#username').data('params')},
  //              dataType: "text",
  //              success: function(response) {
  //              	alert(response);
  //                     if (response=='True'){
  //                         return true;
  //                     }
  //                     else{ 
		// 					return false;                 
		// 			}
  //               },
  //               error: function(rs,e) {
  //                      return false;
  //               }
  //         });
  // });
  $("#form").validate({ 
			 rules: {
				first_name: "required",
				last_name: "required",
				username: {
					required: true,
					minlength: 5,
			        // checkUsername:true,
			        remote: {
			        	type: "POST",
		                url: "username/",
		                data: {username:function() {return $('#username').val()}, csrfmiddlewaretoken:function() {return $('#username').data('params')}},

			        },
				},
				password: {
					required: true,
					minlength: 5
				},
				password_confirmation: {
					required: true,
					minlength: 5,
					equalTo: "#password"
				},
				email: {
					required: true,
					email: true,
					// remote: "emails.action"
				},
				usertype:{
					required: true,
				}
			},
			messages: {
				first_name: "الرجاء ادخال الاسم",
				last_name: "الرجاء ادخال اللقب",
				username: {
					required: "الرجاء إدخال اسم المستخدم",
					minlength: jQuery.validator.format("يجب أن تكون اسم المستخدم الخاصة بك على الأقل 5 أحرف"),
					remote :"هذا الاسم مستخدم "
				},
				password: {
					required: "الرجاء ادخال الرمز البسري",
					minlength: jQuery.validator.format("يجب أن تكون كلمة المرور الخاصة بك على الأقل 5 أحرف")
				},
				password_confirmation: {
					required: "الرجاء إدخال كلمة المور",
					minlength: jQuery.validator.format("يجب أن تكون كلمة المرور الخاصة بك على الأقل 5 أحرف"),
					equalTo: "يرجى إدخال كلمة المرور نفسها ."
				},
				email: {
					required: " هذا ليس بريد اليكتروني ",
					email:"هذا ليس بريد الكتروني"
				},
				usertype: {
					required: "الرجاء الاختيار ",
				},
			
			},
	
		});
  
});
