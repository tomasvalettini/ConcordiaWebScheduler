function addRow() {


		var table = document.getElementById('dataTable');
		var rowCount = table.rows.length;
		var pass = true
		var  source = ["ENGR 107", "ENGR 108", "ENGR 201", "ENGR 202", "ENGR 207", "ENGR 208", "ENGR 107", "ENGR 213", "ENGR 233", "ENGR 243", "ENGR 244", "ENGR 251", "ENGR 301", "ENGR 307", "ENGR 308", "ENGR 311", "ENGR 361", "ENGR 371", "ENGR 392", "ENGR 411", "COMP 107","COMP 108","COMP 207", "COMP 208", "COMP 228", "COMP 232", "COMP 233", "COMP 248", "COMP 249", "COMP 335", "COMP 346", "COMP 348", "COMP 352", "COMP 353", "COMP 354", "COMP 371", "COMP 376", "COMP 490", "COMP 492", "ELEC 275", "ENCS 272", "ENCS 282", "SOEN 287"];
	
		var patt = /^[A-z][A-z][A-z][A-z]\s[0-9][0-9][0-9]/;
		
		if(rowCount < 7){
		
		 for(var i=0; i<rowCount; i++) {
			var row = table.rows[i];
			var input = row.cells[0].childNodes[0].nodeValue;
			if(input.toLowerCase() == document.getElementById("input").value.toLowerCase())
			{
				pass =false;
				alert("That course has already been added");
			}
			
			else if(patt.test(document.getElementById("input").value) == false)
			{
				pass = false;
				alert("Error-- Your input was not valid. Please ensure that the class name is in the AAAA ### format.");
			}
			
			else if(checkArray(document.getElementById("input").value, source) == false)
				alert("Error-- That class does not exist in the Database");
			}
			
		if(pass == true  && checkArray(document.getElementById("input").value, source) == true){
		
			var row = table.insertRow(rowCount);
            
			var cell1 = row.insertCell(0);
			var element2 = document.createElement("td");
			cell1.appendChild(document.createTextNode(document.getElementById("input").value));
			
			var cell2 = row.insertCell(1);
			var element1 = document.createElement("input");
			element1.type = "checkbox";
			cell2.appendChild(element1);

		}
		
		if(rowCount > 0 && pass == true && checkArray(document.getElementById("input").value, source) == true){ //shows or removes the "Remove Class" button
			document.getElementById("remove").style.visibility = 'visible';
			document.getElementById("generate").style.visibility = 'visible';
		}
		else{
			document.getElementById("remove").style.visibility = 'hidden';
			document.getElementById("generate").style.visibility = 'hidden';
		}
		}
		else{
		alert("can put more than 5 Courses");
		}
        
 }
 function addRow2() {

		var table = document.getElementById('dataTable');
		var rowCount = table.rows.length;
		var pass = true
		var source = ["COMP 108","COMP 201","COMP 208","COMP 218","COMP 228","COMP 232","COMP 233","COMP 248","COMP 249","COMP 335","COMP 339","COMP 345","COMP 346","COMP 348","COMP 352","COMP 353","COMP 354","COMP 371","COMP 361","COMP 376","COMP 445","COMP 451","COMP 472","COMP 473","COMP 474","COMP 478","COMP 479","COMP 490","COMP 492","COMP 495","ELEC 275","ENCS 282","ENGR 108","ENGR 201","ENGR 202","ENGR 208","ENGR 213","ENGR 233","ENGR 242","ENGR 251","ENGR 301","ENGR 308","ENGR 311","ENGR 361","ENGR 371","ENGR 391","ENGR 392","ENGR 411","ENGR 417","SOEN 287","SOEN 341","SOEN 342","SOEN 343","SOEN 384","SOEN 387","SOEN 422","SOEN 423","SOEN 490"];
		var patt = /^[A-z][A-z][A-z][A-z]\s[0-9][0-9][0-9]/;
		
		if(rowCount < 7){
		
		 for(var i=0; i<rowCount; i++) {
			var row = table.rows[i];
			var input2 = row.cells[0].childNodes[0].nodeValue;
			if(input2.toLowerCase() == document.getElementById("input2").value.toLowerCase())
			{
				pass =false;
				alert("That course has already been added");
			}
			
			else if(patt.test(document.getElementById("input2").value) == false)
			{
				pass = false;
				alert("Error-- Your input was not valid. Please ensure that the class name is in the AAAA ### format.");
			}
			
			else if(checkArray(document.getElementById("input2").value, source) == false)
				alert("Error-- That class does not exist in the Database");
			}
			
		if(pass == true  && checkArray(document.getElementById("input2").value, source) == true){
		
			var row = table.insertRow(rowCount);
            
			var cell1 = row.insertCell(0);
			var element2 = document.createElement("td");
			cell1.appendChild(document.createTextNode(document.getElementById("input2").value));
			
			// THIS IS NOT WORKING DUNNO WHY.
			var cell2 = row.insertCell(1);
			var element1 = document.createElement("input");
			element1.type = "checkbox";
			cell2.appendChild(element1);

		}
		
		if(rowCount > 0 && pass == true && checkArray(document.getElementById("input2").value, source) == true){ //shows or removes the "Remove Class" button
			document.getElementById("remove").style.visibility = 'visible';
			document.getElementById("generate").style.visibility = 'visible';
		}
		else{
			document.getElementById("remove").style.visibility = 'hidden';
			document.getElementById("generate").style.visibility = 'hidden';
		}
		}
		else{
		alert("can put more than 5 Courses");
		}
        
 }
 function addRow3() {

		var table = document.getElementById('dataTable');
		var rowCount = table.rows.length;
		var pass = true
		var source = ["COMP 201","COMP 218","COMP 228","COMP 232","COMP 248","COMP 233","COMP 249","COMP 326","COMP 335","COMP 345","COMP 346","COMP 348","COMP 352","COMP 353","COMP 354","COMP 361","COMP 367","COMP 371","COMP 426","COMP 428","COMP 442","COMP 445","COMP 465","COMP 472","COMP 474","COMP 476","COMP 477","COMP 490","COMP 492","COMP 495","SOEN 228","SOEN 287","SOEN 331","SOEN 341","SOEN 344","SOEN 345","SOEN 357","SOEN 385","SOEN 390","SOEN 487","ELEC 275","ENGR 201","ENGR 202","ENGR 213","ENGR 233","ENGR 242","ENGR 243","ENGR 244","ENGR 245","ENGR 251","ENGR 301","ENGR 361","ENGR 371","ENGR 391","ENGR 392","ENGR 411","ENGR 418","ENCS 282"];
		var patt = /^[A-z][A-z][A-z][A-z]\s[0-9][0-9][0-9]/;
		
		if(rowCount < 7){
		
		 for(var i=0; i<rowCount; i++) {
			var row = table.rows[i];
			var input3 = row.cells[0].childNodes[0].nodeValue;
			if(input3.toLowerCase() == document.getElementById("input3").value.toLowerCase())
			{
				pass =false;
				alert("That course has already been added");
			}
			
			else if(patt.test(document.getElementById("input3").value) == false)
			{
				pass = false;
				alert("Error-- Your input was not valid. Please ensure that the class name is in the AAAA ### format.");
			}
			
			else if(checkArray(document.getElementById("input3").value, source) == false)
				alert("Error-- That class does not exist in the Database");
			}
			
		if(pass == true  && checkArray(document.getElementById("input3").value, source) == true){
		
			var row = table.insertRow(rowCount);
            
			var cell1 = row.insertCell(0);
			var element2 = document.createElement("td");
			cell1.appendChild(document.createTextNode(document.getElementById("input3").value));
			
			// THIS IS NOT WORKING DUNNO WHY.
			var cell2 = row.insertCell(1);
			var element1 = document.createElement("input");
			element1.type = "checkbox";
			cell2.appendChild(element1);

		}
		
		if(rowCount > 0 && pass == true && checkArray(document.getElementById("input3").value, source) == true){ //shows or removes the "Remove Class" button
			document.getElementById("remove").style.visibility = 'visible';
			document.getElementById("generate").style.visibility = 'visible';
		}
		else{
			document.getElementById("remove").style.visibility = 'hidden';
			document.getElementById("generate").style.visibility = 'hidden';
		}
		}
		else{
		alert("can put more than 5 Courses");
		}
        
 }
 
 function deleteRow(tableID) {
            try {
            var table = document.getElementById(tableID);
            var rowCount = table.rows.length;
 
            for(var i=0; i<rowCount; i++) {
                var row = table.rows[i];
                var chkbox = row.cells[1].childNodes[0];
                if(null != chkbox && true == chkbox.checked) {
                    table.deleteRow(i);
                    rowCount--;
                    i--;
                }
			if(rowCount > 1){ //shows or removes the "Remove Class" button
				document.getElementById("remove").style.visibility = 'visible';
				document.getElementById("generate").style.visibility = 'visible';
			}
			else{
				document.getElementById("remove").style.visibility = 'hidden';
				document.getElementById("generate").style.visibility = 'hidden';
				document.getElementById("print").style.visibility = 'hidden';
			}
            }
            }catch(e) {
                alert(e);
            }
		
			
        }
		
function fillIfEmpty(content)
{
	if (content.value == "")
	{
		content.value = "Enter course number...";
	}
}

function eraseContent(content)
{
		content.value = "";
}

var clickConstraint = 0;
var clickSequences = 0;
function showConstraints(img)
{
	var down = 'images/Down Arrow.png';
	var right = 'images/Right Arrow.png';
	var changable;
	if (clickConstraint == 0)
	{
		img.src = down;
		document.getElementById("constraint-table").style.display = 'block';
		clickConstraint++;	
	}
	else
	{
		img.src = right;
		document.getElementById("constraint-table").style.display = 'none';
		clickConstraint--;
	}
	
}

function showSequences(img)
{
	var down = 'images/Down Arrow.png';
	var right = 'images/Right Arrow.png';
	var changable;
	if (clickSequences == 0)
	{
		img.src = down;
		document.getElementById("sequences").style.display = 'block';
		clickSequences++;	
	}
	else
	{
		img.src = right;
		document.getElementById("sequences").style.display = 'none';
		clickSequences--;
	}
	
}

function selectSeason(){
	
	if(document.getElementById("summer").checked){
		document.getElementById("Add-summer").style.display = 'block';
		document.getElementById("Add-Winter").style.display = 'none';
		document.getElementById("Add-Fall").style.display = 'none';
		
		document.getElementById("input").style.display = 'block';
		document.getElementById("input2").style.display = 'none';
		document.getElementById("input3").style.display = 'none';
	}
	if(document.getElementById("fall").checked){
		document.getElementById("Add-summer").style.display = 'none';
		document.getElementById("Add-Fall").style.display = 'block';
		document.getElementById("Add-Winter").style.display = 'none';
		
		document.getElementById("input").style.display = 'none';
		document.getElementById("input2").style.display = 'block';
		document.getElementById("input3").style.display = 'none';
		
	}
	if(document.getElementById("winter").checked){
		document.getElementById("Add-summer").style.display = 'none';
		document.getElementById("Add-Fall").style.display = 'none';
		document.getElementById("Add-Winter").style.display = 'block';
		
		document.getElementById("input").style.display = 'none';
		document.getElementById("input2").style.display = 'none';
		document.getElementById("input3").style.display = 'block';
	}
}

function checkArray(elt, array)
{
	for(var i = 0; i < array.length; i++)
	{
		if(array[i] == elt)
			return true;
	}
	
	return false;
}
 
/*
function addclass(){

var counter = 0;
var input1 = new Array();

input1[counter] = (document.getElementById("input").value);
counter += 1;
var output = "";
	output += "<div id=courses><table border='1'>";
	
	//var input = new Array();
	//input.push(input1);

	

	for(var r = 0; r < input1.length; r++){
	
	output += "<tr><td>" + input1[r] + "</td></tr>"
	}
	
	//output += "<tr>" + input1 + "</tr>"
	output += "</table></div>";
	
	document.getElementById('calendar').innerHTML=output;
	return false;
} 


function addRow1(id){
    var tbody = document.getElementById(id).getElementsByTagName("tbody")[0];
    var row = document.createElement("tr")
    var data1 = document.createElement("td")
    data1.appendChild(document.createTextNode(document.getElementById("input").value))
    var data2 = document.createElement("td")
    data2.appendChild (document.createTextNode("fosifsodifnsdiofn")
    row.appendChild(data1);
    row.appendChild(data2);
    tbody.appendChild(row);
    }
	*/
 