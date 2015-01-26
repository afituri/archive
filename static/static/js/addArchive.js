$(document).ready(function(){
    $('#datetimepicker5').datetimepicker({
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
    $("#form").validate({ 
             rules: {
                name: "required",
                ref_num: "required",
                real_date: {
                    required: true,
                },
                
                section_id:{
                    required: true,
                }
            },
            messages: {
                name: "الرجاء ادخال الاسم",
                ref_num: "الرجاء ادخال الرقم الاشاري",
                real_date: {
                    required: "الرجاء إدخال التاريخ",
                },
                section_id: {
                    required: "الرجاء الاختيار ",
                },
            
            },
            errorPlacement: function(error, element) {
            if (element.attr("name") == "real_date") {
                    error.insertAfter("#datetimepicker5");
            } else {
                    error.insertAfter(element);
            }
        }
    
        });
});