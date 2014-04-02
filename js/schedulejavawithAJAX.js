
function builder(schedArray2){


	var schedArray = schedArray2;
	
	for(var a = 0; a < schedArray.length; a++)
	{		
		for(var b = 0; b < schedArray[a].length; b++)
		{
			schedArray[a][b].real_start_time = parseInt(schedArray[a][b].start_hour) * 60 + parseInt(schedArray[a][b].start_minutes);
			
			schedArray[a][b].real_end_time = parseInt(schedArray[a][b].end_hour) * 60 + parseInt(schedArray[a][b].end_minutes);
		}
	}

/*
	var schedArray = new Array(2); 		// HARDCODE; SHOULD BE NUMSCHEDULES
	schedArray[0] = new Array(2);		// HARDCODE; SHOULD BE NUMCLASSES
	schedArray[1] = new Array(2);		// HARDCODE; SHOULD BE NUMCLASSES
	// DOUBLE ARRAY IS NOW MADE.
	
	var output = "";

	
	// THE FOLLOWING WILL BE MADE IN A LOOP. THIS IS HARDCODE.
	schedArray[0][0] = new Object();
	schedArray[0][0].name = "COMP 248";
	schedArray[0][0].date = 0;
	schedArray[0][0].start_hour = 8;
	schedArray[0][0].start_minutes = 45;
	schedArray[0][0].end_hour = 11;
	schedArray[0][0].end_minutes = 15;
	schedArray[0][0].real_start_time = schedArray[0][0].start_hour*60+schedArray[0][0].start_minutes;
	schedArray[0][0].real_end_time = schedArray[0][0].end_hour*60+schedArray[0][0].end_minutes;
	 
	schedArray[0][1] = new Object();
	schedArray[0][1].name = "COMP 248";
	schedArray[0][1].date = 2;
	schedArray[0][1].start_hour = 8;
	schedArray[0][1].start_minutes = 45;
	schedArray[0][1].end_hour = 11;
	schedArray[0][1].end_minutes = 15;
	schedArray[0][1].real_start_time = schedArray[0][1].start_hour*60+schedArray[0][1].start_minutes;
	schedArray[0][1].real_end_time = schedArray[0][1].end_hour*60+schedArray[0][1].end_minutes;
	
	schedArray[1][0] = new Object();
	schedArray[1][0].name = "COMP 346";
	schedArray[1][0].date = 0;
	schedArray[1][0].start_hour = 8;
	schedArray[1][0].start_minutes = 45;
	schedArray[1][0].end_hour = 11;
	schedArray[1][0].end_minutes = 15;
	schedArray[1][0].real_start_time = schedArray[0][0].start_hour*60+schedArray[0][0].start_minutes;
	schedArray[1][0].real_end_time = schedArray[0][0].end_hour*60+schedArray[0][0].end_minutes;
	
	schedArray[1][1] = new Object();
	schedArray[1][1].name = "ENGR 391";
	schedArray[1][1].date = 2;
	schedArray[1][1].start_hour = 8;
	schedArray[1][1].start_minutes = 45;
	schedArray[1][1].end_hour = 11;
	schedArray[1][1].end_minutes = 15;
	schedArray[1][1].real_start_time = schedArray[0][1].start_hour*60+schedArray[0][1].start_minutes;
	schedArray[1][1].real_end_time = schedArray[0][1].end_hour*60+schedArray[0][1].end_minutes;
*/	

	var output = "";
	for(var r = 0; r < schedArray.length; r++)
	{
		output+="<div id='text'><table>";
		output+="<tr><h2>SCHEDULE #" + (r+1) + "</h2></tr>";
		output+="<tr><h6>>>> CLASSES</h6></tr>";
		hasBeenPrinted = new Array();
		
		for(var m = 0; m < schedArray[r].length; m++)
		{
			if(existsInArray(schedArray[r][m].name, hasBeenPrinted) == false)
			{
				output+="<tr><td>"+"&nbsp;&nbsp;&raquo;&nbsp;"+ schedArray[r][m].name + "</td></tr>";
				hasBeenPrinted[m] = schedArray[r][m].name; 
			}
		}
		
		
		output+="</table></div>";
		
		
		
		
		var timeCounter = 525;
		var numClasses = schedArray[r].length;	
		var saveNames = new Array();
			
	
		classPrintCounter = new Array();	
		for(var i = 0; i < 5; i++)
		{
			classPrintCounter[i] = null;
		}								
	
		output += "<div id ='tables'><table class='scheduler'>";
		output += "<tr class='table-top'><td><center>Time</center></td><td><center>Mon</center></td><td><center>Tue</center></td><td><center>Wed</center></td><td><center>Thu</center></td><td><center>Fri</center></td></tr>";
	
	
		while(timeCounter < 1426)			
		{	
								
			newClassDates = new Array(5);		// "A NEW CLASS SHOULD BE ADDED TO THIS SLOT"
	
		
			for(var i = 0; i < numClasses; i++) 	
			{		
	
				
				if((schedArray[r][i].real_start_time - timeCounter) < 15 && (schedArray[r][i].real_start_time - timeCounter) >= 0)
				{					
					newClassDates[schedArray[r][i].date] = 0;					
					saveNames[schedArray[r][i].date] = schedArray[r][i].name;					
					classPrintCounter[schedArray[r][i].date] = (schedArray[r][i].real_end_time - schedArray[r][i].real_start_time)/15;    
					classPrintCounter[schedArray[r][i].date] = intval(classPrintCounter[schedArray[r][i].date]);
				}			
			}	
		
			
			output +=  "<tr>";		
			output +=  "<td>";
			output +=  getHour(timeCounter);				
			output +=  "</td>";								  // This <td> is always required; makes the TIME column
			
			for(var j = 0; j < 5; j++)					    
			{
				
				if(newClassDates[j] != null)   // IF A CLASS NEEDS TO BE ADDED...
				{
					output +=  "<td rowspan=" + classPrintCounter[j] + " style='background-color: #CCFFCC;'><center>" + saveNames[j] + "</center></td>";
					newClassDates[j] = null;
				}
							
				else if(classPrintCounter[j] != null)         // IF THIS COLUMN IS PRINTING A CLASS...
				{
															  // DO NOTHING. SKIP THIS ITERATION.
				}			
	
				else
					output +=  "<td width = 100px>&nbsp;</td>";	   // ELSE, PRINT AN EMPTY <TD>.
			}
			
			output +=  "</tr>";
			timeCounter += 15;							
			
			for(var i = 0; i < 5; i++)						// Decrement print counters
			{
				if(classPrintCounter[i] != null)
				{
					classPrintCounter[i]--;
					
					if(classPrintCounter[i] == 0)				// Delete if necessary
					{
						classPrintCounter[i] = null;
					}
				}
			}
															
		}
		 
		output += "</table></div><br \><br \><br \><br \><br \>";
	}
	

	
	document.getElementById('calendar').innerHTML=output;
	document.getElementById("print").style.visibility = 'visible';
}


function intval (mixed_var, base) {
    
    var tmp;
    var type = typeof(mixed_var);
    
    if (type === 'boolean') 
    {
       return +mixed_var;
    } 
    else if (type === 'string') 
    {
       tmp = parseInt(mixed_var, base || 10);
       return (isNaN(tmp) || !isFinite(tmp)) ? 0 : tmp;    } else if (type === 'number' && isFinite(mixed_var)) {
       return mixed_var | 0;
    } 
    else 
    {
       return 0;
    }
}

function existsInArray(element, array)
{
	for(var j = 0; j < array.length; j++)
	{
		if(element == array[j])
		{
			return true;
		}
	}	
	return false;
}

function getHour(time){

		var hour = intval(time/60);
		var minute = time % 60;

		if(minute == 0)
		{
			return hour + ":" + minute + "0";
		}
		else
		{
			return hour + ":" + minute;
		}
	}
	
