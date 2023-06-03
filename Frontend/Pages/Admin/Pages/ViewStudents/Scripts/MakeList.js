

StudentArray = [];
function MakeList(){
fetch(SERVER_URL + "/StudentDetails")
    .then((response) => response.json())
    .then((data) => {
        console.log(data)
        data.forEach((element) => {
            console.log(element['Username'])
            const Row = document.createElement('div')
            Row.innerHTML=`
            <ul>
            <li>${element['Username']}</li>
            <li>${element['RollNumber']}</li>
            <li>${element['Department']}</li>
            <li>${element['Email']}</li>
            <li>${element['Mentor']}</li>
            </ul>
            `
         
            document.getElementById('TableView').append(Row)
        });
    });
}

// AnnouncementView
function MakeListAnnouncements(){
fetch(SERVER_URL + "Student/Announcements")
    .then((response) => response.json())
    .then((data) => {
        document.getElementById('AnnouncementView').innerHTML=''
        data.forEach((element) => {

            const Row = document.createElement('div')
            Row.innerHTML=`
            <ul>
            <li>${element['Title']}</li>
            <li>${element['Body']}</li>

            </ul>
            `
         
            document.getElementById('AnnouncementView').append(Row)
        });
    });
}