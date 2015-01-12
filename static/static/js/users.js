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
  $("#form").validate({ 
			 rules: {
				first_name: "required",
				last_name: "required",
				username: {
					required: true,
					minlength: 5,
					// remote: {
			  //         url :"/username/",
			  //         type : "post",
			  //         data: {
			  //           username: function() {
			  //             return $( "#username" ).val();
			  //           }
			  //         }
			  //       }
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
					// remote: jQuery.validator.format("{0} is already in use")
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
			// the errorPlacement has to take the table layout into account
			// errorPlacement: function(error, element) {
			// 	if (element.is(":radio"))
			// 		error.appendTo(element.parent().next().next());
			// 	else if (element.is(":checkbox"))
			// 		error.appendTo(element.next());
			// 	else
			// 		error.appendTo(element.parent().next());
			// },
			// // specifying a submitHandler prevents the default submit, good for the demo
			// submitHandler: function() {
			// 	alert("submitted!");
			// },
			// // set this class to error-labels to indicate valid fields
			// success: function(label) {
			// 	// set &nbsp; as text for IE
			// 	label.html("&nbsp;").addClass("checked");
			// },
			// highlight: function(element, errorClass) {
			// 	$(element).parent().next().find("." + errorClass).removeClass("checked");
			// }
		});
  
});
