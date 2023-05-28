

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