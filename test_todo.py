import unittest
from app import app, db
from bson.objectid import ObjectId

class TestTodoAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Clearing database before runnign test cases 
        db.tasks.delete_many({})

    def tearDown(self):
        # Clearing database after running test cases
        db.tasks.delete_many({})
    
    def test_add_task(self):
        dummy_data = {"title": "Test Task", "description": "Test Description"}
        response = self.app.post('/tasks', json=dummy_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("Test Task", response.json["title"])

    def test_list_tasks(self):
        # Add a sample task
        dummy_data = {"title": "Sample Task", "description": "Sample Description", "completed": False}
        db.tasks.insert_one(dummy_data)
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json), 0)

    def test_edit_task(self):

        dummy_data = {"title": "Old Title", "description": "Old Description"}
        task_id = str(db.tasks.insert_one(dummy_data).inserted_id)

        updation = {"title": "New Title", "completed": True}
        response = self.app.put(f'/tasks/{task_id}', json=updation)
        self.assertEqual(response.status_code, 200)
        self.assertIn("New Title", response.json["title"])
        self.assertTrue(response.json["completed"])


    def test_delete_task(self):
        dummy_data = {"title": "Task to Delete"}
        task_id = str(db.tasks.insert_one(dummy_data).inserted_id)
        response = self.app.delete(f'/tasks/{task_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "Task deleted successfully")


    def test_delete_all_tasks(self):

        dummy_data = [
            {"title": "Task 1"},
            {"title": "Task 2"}
        ]
        db.tasks.insert_many(dummy_data)
        response = self.app.delete('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "All tasks deleted successfully")

