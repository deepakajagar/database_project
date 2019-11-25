function edit_row(no)
{
 document.getElementById("edit_button"+no).style.display="none";
 document.getElementById("save_button"+no).style.display="block";
	
 var name=document.getElementById("name_row"+no);
 var usn=document.getElementById("usn_row"+no);
 var pos=document.getElementById("pos_row"+no);
 var ph=document.getElementById("ph_row"+no);
	
 var name_data=name.innerHTML;
 var usn_data=usn.innerHTML;
 var pos_data=pos.innerHTML;
 var ph_data=ph.innerHTML;
	
 name.innerHTML="<input type='text' id='name_text"+no+"' value='"+name_data+"'>";
 usn.innerHTML="<input type='text' id='usn_text"+no+"' value='"+usn_data+"'>";
 pos.innerHTML="<input type='text' id='pos_text"+no+"' value='"+pos_data+"'>";
 ph.innerHTML="<input type='text' id='ph_text"+no+"' value='"+ph_data+"'>";
}

function save_row(no)
{
 var name_val=document.getElementById("name_text"+no).value;
 var usn_val=document.getElementById("usn_text"+no).value;
 var pos_val=document.getElementById("pos_text"+no).value;
 var ph_val=document.getElementById("ph_text"+no).value;

 document.getElementById("name_row"+no).innerHTML=name_val;
 document.getElementById("usn_row"+no).innerHTML=usn_val;
 document.getElementById("pos_row"+no).innerHTML=pos_val;
 document.getElementById("ph_row"+no).innerHTML=ph_val;

 document.getElementById("edit_button"+no).style.display="block";
 document.getElementById("save_button"+no).style.display="none";
}

function delete_row(no)
{
 document.getElementById("row"+no+"").outerHTML="";
}

function add_row()
{
 var new_name=document.getElementById("new_name").value;
 var new_usn=document.getElementById("new_usn").value;
 var new_pos=document.getElementById("new_pos").value;
 var new_ph=document.getElementById("new_ph").value;
	
 var table=document.getElementById("data_table");
 var table_len=(table.rows.length)-1;
 var row = table.insertRow(table_len).outerHTML="<tr id='row"+table_len+"'><td id='name_row"+table_len+"'>"+new_name+"</td><td id='usn_row"+table_len+"'>"+new_usn+"</td><td id='pos_row"+table_len+"'>"+new_pos+"</td><td id='ph_row"+table_len+"'>"+new_ph+"</td><td><input type='button' id='edit_button"+table_len+"' value='Edit' class='edit' onclick='edit_row("+table_len+")'> <input type='button' id='save_button"+table_len+"' value='Save' class='save' onclick='save_row("+table_len+")'> <input type='button' value='Delete' class='delete' onclick='delete_row("+table_len+")'></td></tr>";

 document.getElementById("new_name").value="";
 document.getElementById("new_usn").value="";
 document.getElementById("new_pos").value="";
 document.getElementById("new_ph").value="";
}