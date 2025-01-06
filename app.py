from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv

# Initialize the Flask app
load_dotenv()

app = Flask(__name__)
mongo_uri = os.getenv('MONGO_URI')
if not mongo_uri:
    raise ValueError("MONGO_URI is not set in your .env file. Please define it.")
try:
    client = MongoClient(mongo_uri, server_api=ServerApi('1'))
    client.admin.command('ping')  
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client["todo"]  
    tasks_collection = db["tasks"]
except Exception as e:
    raise ConnectionError(f"Failed to connect to MongoDB. Error: {e}")


def get_task_object(task):
    return {
        "id": str(task.get("_id")),
        "title": task.get("title"),
        "description": task.get("description", ""),
        "completed": task.get("completed", False),
    }

# API routes
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description', '')
    
    if not title:
        return jsonify({'error': 'Title is required'}), 400

    new_task = {
        "title": title,
        "description": description,
        "completed": False
    }

    result = tasks_collection.insert_one(new_task)
    return jsonify(get_task_object(tasks_collection.find_one({"_id": result.inserted_id}))), 201

@app.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = tasks_collection.find()
    return jsonify([get_task_object(task) for task in tasks]), 200

@app.route('/tasks/<task_id>', methods=['PUT'])
def edit_task(task_id):
    data = request.get_json()
    
    task = tasks_collection.find_one({"_id": ObjectId(task_id)})
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    updated_task = {
        "title": data.get('title', task['title']),
        "description": data.get('description', task.get('description', '')),
        "completed": data.get('completed', task.get('completed', False))
    }

    tasks_collection.update_one({"_id": ObjectId(task_id)}, {"$set": updated_task})
    return jsonify(get_task_object(tasks_collection.find_one({"_id": ObjectId(task_id)}))), 200

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = tasks_collection.find_one({"_id": ObjectId(task_id)})
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    tasks_collection.delete_one({"_id": ObjectId(task_id)})
    return jsonify({'message': 'Task deleted successfully'}), 200

@app.route('/tasks', methods=['DELETE'])
def delete_all_tasks():
    tasks_collection.delete_many({})
    return jsonify({'message': 'All tasks deleted successfully'}), 200

# Test cases
@app.route('/test', methods=['GET'])
def run_tests():
    import unittest
    import test_todo
    
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_todo)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return jsonify({
        'tests_run': result.testsRun,
        'failures': len(result.failures),
        'errors': len(result.errors),
    }), 200

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
