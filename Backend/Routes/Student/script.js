const Details = document.getElementById('StudentDetails')
Student = document.getElementById('StudentTemplate')
StudentArray = []
let content = Student.content.cloneNode(true)
function fetchAppointments(Student){
fetch(`${SERVER_URL}/${Student}/Details`)
// fetch(`http://127.0.0.1:5500/APITest/Appointments2.json`)
  .then((response) => response.json())
  .then((data) => {
    StudentArray = data
  })
  .then(() => {



    for (let PersonName in StudentArray) {

      content = Student.content.cloneNode(true)

      content.getElementById('StudentName').innerText = PersonName
      content.getElementById('StudentDepartment').innerText = StudentArray[PersonName]['StudentDepartment']
      content.getElementById('StudentCGPA').innerText = StudentArray[PersonName]['StudentCGPA']
      content.getElementById('StudentMentor').innerText = StudentArray[PersonName]['StudentMentor']
      content.getElementById('StudentRollNumber').innerText = StudentArray[PersonName]['StudentRollNumber']
      Appointments.appendChild(content)
    }
  }
  )}