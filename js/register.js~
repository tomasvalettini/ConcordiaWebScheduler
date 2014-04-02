$(document).ready(function()//When the dom is ready
{
	//icons used to swag up the ajax calls
	var errorPic = '<img src="../img/not_available.png" align="absmiddle">';
	var loadingPic = '<img src="../img/loader.gif" align="absmiddle">';
	var successPic = '<img src="../img/available.png" align="absmiddle">';
	//**********
	var usrErr=false;
	var pwdErr=false;
	
	//password validation
	$("#pwd2").change(function()
	{
		//get the 2 passwords
		var p1 = $("#pwd1").val();
		var p2 = $("#pwd2").val();
		
		if ((p1 != p2) || (p1 == '' || p2 == ''))
		{
			$("#msg").html(errorPic+'<font color="red">Passwords do not match</font>');
			pwdErr=true;
			return false;
		}
		else
		{
			$("#msg").html(successPic+'<font color="green">Passwords match!!</font>');
			pwdErr=false;
			return true;
		}
	});

	$("#duser").change(function()
	{ 
		//if theres a change in the duser textbox
		var username = $("#duser").val();//Get the value in the duser textbox
		
		if(username != '')//if the lenght greater than 3 characters
		{
			$("#msg").html(loadingPic+'&nbsp;Checking availability...');
			//Add a loading image in the span id="availability_status"
			$.ajax
			({//Make the Ajax Request
				type: "POST",
				url: "../php/checkUser.php",  //file name
				data: "username="+ username,  //data
				success: function(server_response)
				{
					$("#msg").ajaxComplete(function(event, request)
					{
						if(server_response == '0')//if ajax_check_duser.php return value "0"
						{
							$("#msg").html(successPic+'<font color="Green"> Available </font>  ');
							usrErr=false;
							//add this image to the span with id "availability_status"
						}
					 	else if(server_response == '1')//if it returns "1"
					 	{
					 		
					 		$("#msg").html(errorPic+'<font color="red">Not Available</font>');
							usrErr=true;
					 	}
					});
				}
			});
		}
		else
		{
			$("#msg").html('<font color="#cc0000">You must choose a username</font>');
			usrErr = true;
			//if in case the duser is less than or equal 3 characters only
		}
		return false;
	});
	
	$("#register").submit(function()
	{
		$("#pwd2").change();
		$("#duser").change();
		var user = $("#duser").val();
		var pass = $("#pwd1").val();
		
		if(usrErr)
		{
			$("#duser").focus();
			$("#duser").select();
			$("#msg").html(errorPic+'<font color="red">Please choose a different username</font>');
			return false;
		}
		else if(pwdErr)
		{
			$("#pwd2").val('');
			$("#pwd1").val('');
			$("#pwd1").focus();
			$("#msg").html(errorPic+'<font color="red">Passwords did not match, try again.</font>');
			return false;	
		}
		
		
		
		$.ajax
		({//Make the Ajax Request
			type: "POST",
			url: "../php/register.php",  //file name
			data: "user="+user+"&pwd="+pass,  //data
			success: function(server_response)
			{

				$("#msg").ajaxComplete(function(event, request)
				{

					if(server_response == '0')//if ajax_check_duser.php return value "0"
					{
                                               
						$("#msg").html(successPic+'<font color="Green">Successfully registered!<br/>Please 					sign in!</font>  ');
						//add this image to the span with id "availability_status"
					}
					else  if(server_response == '1')//if it returns "1"
					{
                                                
						$("#msg").html(errorPic+'<font color="red">COULD NOT REGISTER!<br />LOSER!!!</font>');
					}
				});
			}
		});
		return false;
	});
});
