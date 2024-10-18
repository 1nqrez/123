async function registerUser(event) {
    event.preventDefault();
    const username = document.getElementById('student-username').value;
    const password = document.getElementById('student-password').value;

    const response = await fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
    });

    const result = await response.json();
    if (response.ok) {
        alert('Registration successful');
    } else {
        alert('Error: ' + result.detail);
    }
}

async function loginUser(event) {
    event.preventDefault();
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;

    const response = await fetch('/token', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`,
    });

    const result = await response.json();
    if (response.ok) {
        localStorage.setItem('access_token', result.access_token);
        alert('Login successful');
    } else {
        alert('Error: ' + result.detail);
    }
}

document.getElementById('register-student-form').addEventListener('submit', registerUser);
document.getElementById('login-form').addEventListener('submit', loginUser);
