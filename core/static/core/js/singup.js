$('#id_username').click(function(e) {
    alert("clicked");
});

    // form username validation,
    $('#id_username').change(function() {

        $.ajax({
            url: '/ajaxableusername',
            type: 'GET',
            dataType: 'json',
            data: {
                username: $('#id_username').val(),
            },
            success: function(data) {
                if (data.used) {
                    $("#username_validation_error").text(data.mssg);
                    $("#username_validation_error").css({
                        "visibility": "visible",
                    });
                } else {
                    $("#username_validation_error").css({
                        "visibility": "hidden",
                    });
                };
            }
        });
    });

    // form username validation,
    $('id_email').change(function() {
        $.ajax({
            url: '/ajaxableemail',
            type: 'GET',
            dataType: 'json',
            data: {
                username: $('#id_email').val(),
            },
            success: function(data) {
                if (data.used) {
                    $("#email_validation_error").text(data.mssg);
                    $("#email_validation_error").css({
                        "visibility": "visible",
                    });
                } else {
                    $("#email_validation_error").css({
                        "visibility": "hidden",
                    });
                };
            }
        });
    });
    // border color change

    $('form :input').focusin(function() {
        $(this).css({
            "border-bottom": "2px solid red"
        });
    });
    $('form :input').focusout(function() {
        $(this).css({
            "border-bottom": "2px solid black"
        });
    });

// screen size effect
var actions = function(){
    if ($(window).width()<640){
        $("#navbar").hide("slow");
        $(".left_side, .right_side").hide();
        $("#sidebar-button").css({"display":"flex"});
    }else {
        $("#navbar").show("slow");
        $(".left_side, .right_side").show();
        $("#sidebar-button").css({"display":"none"});
    }
};
$(window).on('load',actions());
$(window).resize(function(){actions();});

if ($("#sidebar-button")){
$("#sidebar-button").click(function(){
    alert("clicked");
});
};
