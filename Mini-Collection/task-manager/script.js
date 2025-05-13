// Function to fetch and display tasks
async function getTasks() {
    try {
        const response = await fetch('/api/tasks');
        if (!response.ok) {
            throw new Error('Failed to fetch tasks');
        }
        const tasks = await response.json();
        displayTasks(tasks);
    } catch (error) {
        console.error('Error:', error);
        alert(error.message);
    }
}

// Function to display tasks in the UI
function displayTasks(tasks) {
    const taskList = document.getElementById('task-list');
    taskList.innerHTML = ''; // Clear existing tasks

    tasks.forEach((task, index) => {
        const taskItem = document.createElement('li');
        taskItem.classList.add('task');
        taskItem.dataset.id = index;

        taskItem.innerHTML = `
            <span class="task-name">${task.task}</span>
            <span class="task-status">${task.completed ? 'Completed' : 'Pending'}</span>
            <button class="edit-btn" onclick="editTask(${index})">Edit</button>
            <button class="delete-btn" onclick="removeTask(${index})">Delete</button>
            <button class="complete-btn" onclick="toggleTaskStatus(${index})">${task.completed ? 'Undo' : 'Complete'}</button>
        `;
        taskList.appendChild(taskItem);
    });
}

// Function to add a new task
async function addTask() {
    const taskName = document.getElementById('new-task').value;
    if (!taskName) {
        alert('Please enter a task name');
        return;
    }

    try {
        const response = await fetch('/api/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ task: taskName })
        });

        if (!response.ok) {
            throw new Error('Failed to add task');
        }

        const newTask = await response.json();
        displayTasks(await fetchTasks()); // Re-fetch tasks
    } catch (error) {
        console.error('Error:', error);
        alert(error.message);
    }
}

// Function to remove a task
async function removeTask(taskId) {
    try {
        const response = await fetch(`/api/tasks/${taskId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error('Backend delete failed');
        }

        const deletedTask = await response.json();
        alert(`Task "${deletedTask.task}" deleted`);
        displayTasks(await fetchTasks()); // Re-fetch tasks
    } catch (error) {
        console.error('Error:', error);
        alert(error.message);
    }
}

// Function to update a task status (Complete/Undo)
async function toggleTaskStatus(taskId) {
    try {
        const response = await fetch(`/api/tasks/${taskId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ completed: true })
        });

        if (!response.ok) {
            throw new Error('Backend update failed');
        }

        const updatedTask = await response.json();
        alert(`Task "${updatedTask.task}" marked as completed`);
        displayTasks(await fetchTasks()); // Re-fetch tasks
    } catch (error) {
        console.error('Error:', error);
        alert(error.message);
    }
}

// Function to edit a task
async function editTask(taskId) {
    const newTaskName = prompt('Enter the new task name:');
    if (!newTaskName) {
        return;
    }

    try {
        const response = await fetch(`/api/tasks/${taskId}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ task: newTaskName })
        });

        if (!response.ok) {
            throw new Error('Backend update failed');
        }

        const updatedTask = await response.json();
        alert(`Task name updated to "${updatedTask.task}"`);
        displayTasks(await fetchTasks()); // Re-fetch tasks
    } catch (error) {
        console.error('Error:', error);
        alert(error.message);
    }
}

// Fetch tasks from the backend
async function fetchTasks() {
    try {
        const response = await fetch('/api/tasks');
        if (!response.ok) {
            throw new Error('Failed to fetch tasks');
        }
        return await response.json();
    } catch (error) {
        console.error('Error:', error);
        alert(error.message);
    }
}

// Event listener for form submission (add task)
document.getElementById('add-task-form').addEventListener('submit', (e) => {
    e.preventDefault();
    addTask();
});

// Initialize the task list on page load
window.addEventListener('DOMContentLoaded', getTasks);
