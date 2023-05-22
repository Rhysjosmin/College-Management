function loadStudentData() {
    return fetch('students_data.json')
        .then(response => response.json());
}

// Login function
function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Simulate server-side authentication
    authenticateUser(username, password)
        .then(userData => {
            if (userData) {
                if (userData.role === 'teacher') {
                    // Teacher login
                    loadStudentData().then(studentData => {
                        displayStudentData(studentData);
                    });
                } else if (userData.role === 'student') {
                    // Student login
                    const studentName = userData.username; // Assuming student's username matches their name
                    loadStudentData().then(studentData => {
                        const student = studentData.find(student => student.Name === studentName);
                        if (student) {
                            displayStudentData([student]);
                        }
                    });
                }
            } else {
                // Invalid login
                alert('Invalid username or password');
            }
        })
        .catch(error => {
            console.error('Authentication error:', error);
        });
}

// Simulate server-side authentication
function authenticateUser(username, password) {
    return new Promise((resolve, reject) => {
        // Simulate an API call or database query to validate credentials
        setTimeout(() => {
            if (username === 'teacher' && password === 'teacherpass') {
                resolve({ role: 'teacher' });
            } else if (username === 'student' && password === 'studentpass') {
                resolve({ role: 'student', username: 'John Smith' }); // Replace with actual student username
            } else {
                resolve(null);
            }
        }, 500); // Simulated delay for demonstration
    });
}

// Display student data
function displayStudentData(data) {
    const studentTableBody = document.getElementById('student-table-body');
    studentTableBody.innerHTML = '';

    if (data) {
        data.forEach(student => {
            const row = document.createElement('tr');
            row.innerHTML = `<td>${student.Name}</td><td>${student.Department}</td><td>${student.RollNumber}</td><td>${student.EmailID}</td><td>${student.Mentor}</td><td>${student.CGPA}</td>`;
            studentTableBody.appendChild(row);
        });
    }

    document.getElementById('login-form').style.display = 'none';
    document.getElementById('student-data').style.display = 'block';
}

// Initially load student data
loadStudentData().then(studentData => {
    // Store the data globally for later use
    window.studentData = studentData;
});



















































































































































/* function loadStudentData() {
    return fetch('students_data.json')
        .then(response => response.json())
        .then(studentData => studentData)
        .catch(error => {
            console.error('Error loading student data:', error);
        });
}

// Login function
function login() {
    // Get input values
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Authenticate the user
    authenticateUser(username, password)
        .then(userData => {
            if (userData.role === 'teacher') {
                // Teacher login
                loadStudentData()
                    .then(studentData => {
                        displayStudentData(studentData);
                    })
                    .catch(error => {
                        console.error(error);
                    });
            } else if (userData.role === 'student') {
                // Student login
                loadStudentData()
                    .then(studentData => {
                        const student = studentData.find(student => student.username === userData.username);
                        if (student) {
                            displayStudentData([student]);
                        } else {
                            console.error('Student not found');
                        }
                    })
                    .catch(error => {
                        console.error(error);
                    });
            } else {
                // Invalid login
                alert('Invalid username or password');
            }
        })
        .catch(error => {
            console.error(error);
        });
}

// Simulate server-side authentication
function authenticateUser(username, password) {
    return new Promise((resolve, reject) => {
        // Simulated user data
        const users = [
            { username: 'teacher', password: 'teacherpass', role: 'teacher' },
            { username: 'Clarita', password: 'student1pass', role: 'student' },
            { username: 'Yolan', password: 'student2pass', role: 'student' }
        ];

        // Find the user with matching credentials
        const user = users.find(user => user.username === username && user.password === password);
        if (user) {
            resolve(user);
        } else {
            reject('Invalid username or password');
        }
    });
}

// Display student data
function displayStudentData(data) {
    const studentTableBody = document.getElementById('student-table-body');
    studentTableBody.innerHTML = '';

    if (data) {
        data.forEach(student => {
            const row = document.createElement('tr');
            row.innerHTML = `<td>${student.Name}</td><td>${student.Department}</td><td>${student.RollNumber}</td><td>${student.EmailID}</td><td>${student.Mentor}</td><td>${student.CGPA}</td>`;
            studentTableBody.appendChild(row);
        });
    }

    document.getElementById('login-form').style.display = 'none';
    document.getElementById('student-data').style.display = 'block';
}

// Initialize the login form
function initLoginForm() {
    document.getElementById('login-form').style.display = 'block';
}

// Load the student data when the page is ready
window.addEventListener('DOMContentLoaded', function () {
    initLoginForm();
}); */
