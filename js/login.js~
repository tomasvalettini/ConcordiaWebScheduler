$(document).ready(function()//When the dom is ready
{
	//icons used to swag up the ajax calls
	var errorPic = '<img src="/Website/img/not_available.png" align="absmiddle">';
	var loadingPic = '<img src="/Website/img/loading.gif" align="absmiddle">';
	var successPic = '<img src="/Website/img/available.png" align="absmiddle">';
	//**********
	$("#frm").submit(function()
	{
		var username = $("#user").val();//Get the value in the duser textbox
		var password = $("#pass").val();
		
		$("#msg").html(loadingPic+'&nbsp;Checking availability...');
		
		$.ajax
		({  //Make the Ajax Request
			type: "POST",
			url: "../php/login.php",  //file name
			data: "user="+username+"&pass="+ password,  //data
			success: function(server_response)
			{
				$("#msg").ajaxComplete(function(event, request)
				{
					if (server_response == "0")
					{
						$("#msg").html(errorPic+'<font color="red">Failed to log in</font>');
						$("#loginInfo").html("Hello Guest!");
						
					}
					else
					{
						$("#msg").html(successPic+'<font color="green">Successfully logged in!</font>');
						$("#loginInfo").html("Welcome "+username+"!");
						$("#close").click();
						$("#container").show();
						
					}
				});
			}
		});
		
		return false;
	});
});
