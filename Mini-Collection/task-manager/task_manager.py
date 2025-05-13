from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"
app = Flask(__name__)

# Load tasks from the file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []  # Return empty list if file doesn't exist

    try:
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
            return tasks
    except json.JSONDecodeError:
        return []  # Return empty list if JSON is invalid

# Save tasks to the file
def save_tasks(tasks):
    try:
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
    except IOError:
        return "Error: Unable to save tasks to file."

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def add_task():
    task_name = request.json.get('task')
    if not task_name:
        return jsonify({'error': 'Task name is required'}), 400

    tasks = load_tasks()
    task = {
        "task": task_name,
        "completed": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    save_tasks(tasks)
    return jsonify(task), 201

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def remove_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        removed_task = tasks.pop(task_id)
        save_tasks(tasks)
        return jsonify(removed_task), 200
    return jsonify({'error': 'Task not found'}), 404

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def complete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = True
        save_tasks(tasks)
        return jsonify(tasks[task_id]), 200
    return jsonify({'error': 'Task not found'}), 404

@app.route('/api/tasks/<int:task_id>', methods=['PATCH'])
def edit_task(task_id):
    new_name = request.json.get('task')
    if not new_name:
        return jsonify({'error': 'New task name is required'}), 400

    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]["task"] = new_name
        save_tasks(tasks)
        return jsonify(tasks[task_id]), 200
    return jsonify({'error': 'Task not found'}), 404

@app.route('/api/tasks/sort', methods=['GET'])
def sort_tasks():
    tasks = load_tasks()
    tasks.sort(key=lambda x: x["task"].lower())
    save_tasks(tasks)
    return jsonify(tasks)

@app.route('/api/tasks/search', methods=['GET'])
def search_tasks():
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({'error': 'Keyword is required'}), 400

    tasks = load_tasks()
    found_tasks = [task for task in tasks if keyword.lower() in task["task"].lower()]
    return jsonify(found_tasks)

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Default Flask port is 5000
