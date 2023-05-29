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
 
    <bx-input id='Announcement_Title_input'>
  <span slot="label-text">Title</span>
  <span slot="validity-message">Something isn't right</span>
</bx-input>
<bx-textarea placeholder="Enter your announcement here.." rows="4" cols="50" id="Announcement_Message_input">
<span slot="label-text">Announcement</span>
<span slot="helper-text"></span>
<span slot="validity-message">Something isn't right</span>
</bx-textarea>
 
</div>

<bx-btn onclick="SubmitAnnouncement()"> Post Announcement </bx-btn>


</section>
`;

Update_User = `<section id="UPDATE_USER_DETAILS_PAGE">
<div style="font-family: 'noto serif';">
    <h2>Update User</h2>
    <p style="font-family: 'noto sans';font-size: .9em;color: rgb(89, 89, 89);margin-bottom: 6px;">Only .csv and .json files. 500kb max file size</p>
 
   
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

function SubmitAnnouncement() {

const Title= document.getElementById('Announcement_Title_input').value
const Body= document.getElementById('Announcement_Message_input').value

//        let formData = new FormData();
//        formData.append("Title",Title);
//        formData.append("Body",Body);
console.log(Title,Body)
 const data = {
    "Title": Title,
    "Body": Body
  };
console.log(data)
console.log(JSON.stringify(data))
    
       fetch(SERVER_URL + "Admin/Announcement/Add", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  })
        .then(r=>{
Notification('Updated',File.name,'success')
})
      

    
  
}
