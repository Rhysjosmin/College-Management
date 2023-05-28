
const Students = document.getElementById('Students')
StudentTemplate = document.getElementById('StudentTemplate')


StudentArray = [];
fetch(SERVER_URL + "/StudentDetails")
    .then((response) => response.json())
    .then((data) => {
        data.forEach((element) => {
            content = StudentTemplate.content.cloneNode(true)
            console.log(element)
            content.getElementById('RollNumber').innerText = element['RollNumber']
            content.getElementById('Name').innerText =element['Username']
            content.getElementById('Year').innerText = element['Year']
            content.getElementById('Department').innerText = element['Stream']
            content.getElementById('Mentor').innerText = element['Mentor']
            Students.appendChild(content)
        });
    });