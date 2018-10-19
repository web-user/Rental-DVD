$(function() {

    $('#login-form-link').click(function(e) {
		$("#login-form").delay(100).fadeIn(100);
 		$("#register-form").fadeOut(100);
		$('#register-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});
	$('#register-form-link').click(function(e) {
		$("#register-form").delay(100).fadeIn(100);
 		$("#login-form").fadeOut(100);
		$('#login-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});

});


jQuery(document).ready(function ($) {
  $(document).ready(function () {  
    $('#login-form-link').click(function(e) {
		$("#login-form").delay(100).fadeIn(100);
 		$("#register-form").fadeOut(100);
		$('#register-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});
	$('#register-form-link').click(function(e) {
		$("#register-form").delay(100).fadeIn(100);
 		$("#login-form").fadeOut(100);
		$('#login-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});


	    /* ------------------Ajax register----------------------- */

	        // Ajax
    $(document).on('submit', '#register-form', function (e) {
    	e.preventDefault();
    	var ajaxurl = $(this).attr('action')

    	var my_data = {}

    	  my_data.username = $("#username").val(),
          my_data.email = $("#email").val(),
          my_data.password = $("#password").val(),
          my_data.password2 = $("#password2").val(),

    	console.log(ajaxurl)

    	console.log(my_data)


      $.ajax({
        url: ajaxurl,
        type: 'post',
        data: my_data,
        success: function (res) {
          // $('#image-res').hide();
          console.log(res)
          console.log(res.responseText)

        },
        error: function (res) {
          console.log(res)
          console.log(res.responseText)
        }
      })
    });

    	/* ------------------Ajax register----------------------- */

    		        // Ajax
    $(document).on('submit', '#login-form', function (e) {
    	e.preventDefault();
    	var ajaxurl = $(this).attr('action')

    	var my_data = {}

    	  my_data.username = $("#username1").val(),
          my_data.password = $("#password1").val(),


    	console.log(ajaxurl)

    	console.log(my_data)


      $.ajax({
        url: ajaxurl,
        type: 'post',
        data: my_data,
        success: function (res) {
          // $('#image-res').hide();
          console.log(res)
          console.log(res.responseText)

        },
        error: function (res) {
          console.log(res)
          console.log(res.responseText)
        }
      })
    });

  })
})
