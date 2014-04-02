function parseJson(json)
{
	var arraySchedule= new Array();
	
	$.each(json.schedule, function(i,schedule){
		arraySchedule[i] = [];
		$.each(json.schedule[i].course, function(j,course){
			arraySchedule[i][j]=json.schedule[i].course[j];
		});
	});
	
	return arraySchedule; 
	
}


function selectlectures()
{	

	var table = document.getElementById('dataTable');
	var rowCount = table.rows.length;
	var classString = "";
	if (document.getElementById("summer").checked){
		classString += 1;
	} 
	if (document.getElementById("fall").checked){
		classString += 2;
	} 
	if (document.getElementById("winter").checked){
		classString += 4;
	} 

	for(var i=0; i<rowCount; i++) {
			var row = table.rows[i];
			var input = row.cells[0].childNodes[0].nodeValue;
			classString += $.trim(input) + " ";
	}
	
	var postData = "courseStr="+classString;
	$.ajax
	({
		type: "POST",
		data: postData,
		url: "../php/schedule.php",
		success: function(data)
		{
			if (data != "")
			{
				var array = parseJson(JSON.parse(data));
				firstBuilder(array);
			}
			else
			{
				$("#calendar").html("No schedules available");
			}
		}
	});

	/*
	$.getJSON("schedule.js", function(jsonData){
		
		var array = parseJson(jsonData);
		firstBuilder(array);

	});
	*/
}

