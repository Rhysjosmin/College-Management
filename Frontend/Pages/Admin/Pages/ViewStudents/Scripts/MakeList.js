
const Students = document.getElementById('Students')
StudentTemplate = document.getElementById('StudentTemplate')


StudentArray = [];
fetch(SERVER_URL + "/Student/List")
    .then((response) => response.json())
    .then((data) => {
        data.forEach((element) => {
            content = StudentTemplate.content.cloneNode(true)

            content.getElementById('RollNumber').innerText = element[0]
            content.getElementById('Name').innerText =element[1]
            content.getElementById('Year').innerText = element[2]
            content.getElementById('Department').innerText = element[3]
            content.getElementById('Mentor').innerText = element[4]
            Students.appendChild(content)

        });
    });