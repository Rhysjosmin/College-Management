User_Details = `<section id="ADD_USER_DETAILS_PAGE">
<div style="font-family: 'noto serif';">
    <h2>User Details</h2>
    <p style="font-family: 'noto sans';font-size: .9em;color: rgb(89, 89, 89);margin-bottom: 6px;">Only .csv and .json files. 500kb max file size</p>
 
    <input type="file" name="" id="csvFile" accept="text/csv" enctype="multipart/form-data">
</div>

<bx-btn onclick="SubmitCSV()"> Update Database </bx-btn>
<br>
<br>
<br>
<h2>Users</h2>

<section id="TableView">

</section>

</section>`;

Announcements = `<section id="ADD_ANNOUNCEMENTS_DETAILS_PAGE">
<div style="font-family: 'noto serif';">
    <h2>Announcements</h2>
    <p style="font-family: 'noto sans';font-size: .9em;color: rgb(89, 89, 89);margin-bottom: 6px;">Only .csv and .json files. 500kb max file size</p>
 
    <input type="file" name="" accept="text/csv" enctype="multipart/form-data">
</div>

<bx-btn onclick="SubmitCSV()"> Update Database </bx-btn>


</section>
`;

Update_User = `<section id="UPDATE_USER_DETAILS_PAGE">
<div style="font-family: 'noto serif';">
    <h2>Update User</h2>
    <p style="font-family: 'noto sans';font-size: .9em;color: rgb(89, 89, 89);margin-bottom: 6px;">Only .csv and .json files. 500kb max file size</p>
 
    <input type="file" name=""  accept="text/csv" enctype="multipart/form-data">
</div>

<bx-btn onclick="SubmitCSV()"> Update Database </bx-btn>


</section>`;




function SubmitCSV() {
  File = document.getElementById("csvFile").files[0];
//   console.log(File);
try {
    if (File.type == "text/csv") {
        document.getElementById("csvFile").style.borderColor = "black";
    
        let formData = new FormData();
        formData.append("file", File);
    
        fetch(SERVER_URL + "Student/Details/Add/CSV", {
          method: "POST",
          body: formData,
        })
        .then(r=>r.json())
        .then(d=>{
            document.getElementById("csvFile").value=''
            Notification('Updated',File.name,'success')
            MakeList()
        })
      } 
} catch (error) {
    Notification('ERROR','No File Or Incorrect File Type','error')
    document.getElementById("csvFile").style.borderColor = "Red";
    setTimeout(()=>{
    document.getElementById("csvFile").style.borderColor = "Black";

    },4000)
}
  
    
  
}
