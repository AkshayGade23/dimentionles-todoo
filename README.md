# README: How to Run Test Cases for Todo API

This document provides instructions on how to run test cases for the Todo API.

## Prerequisites

Before running the test cases, ensure the following:

1. **Python Environment**:

   - Install Python (version 3.7 or higher).
   - Ensure `pip` is installed for managing dependencies.

2. **Dependencies**:

   - Install required packages by running:

     ```bash
     pip install -r requirements.txt
     ```

3. **MongoDB**:

   - Ensure MongoDB is installed and running.
   - Update the database connection settings in the `app.py` configuration if needed.

4. **Application Code**:
   - Ensure the `app.py` file and associated modules are in place.

---

## Running Test Cases

### 1. Running Test Cases

#### Option 1: Running Tests via Web (Site-based)

Navigate to the following URL in your browser or use a tool like Postman to trigger the tests:

http://dimentionles-todoo.vercel.app/test

This will run all the test cases.

#### Option 2: Running Tests Locally

1. **Run the server**:

    Start the server by running the following command:

    ````bash
    python app.py
    ````


2. **Run the Test file**:

    Execute the test cases by running:

    ```bash
    python test.py
    ````




---

## Test Cases Covered
### 1. Add Task (POST /tasks)
Adds a new task to the database.
Verifies task creation with the correct title and description.
### 2. List Tasks (GET /tasks)
Fetches all tasks from the database.
Ensures at least one task is returned.
### 3. Edit Task (PUT /tasks/<task_id>)
Updates the title and completion status of a task.
Validates updated task details.
### 4. Delete Task (DELETE /tasks/<task_id>)
Deletes a specific task by its ID.
Confirms successful deletion with an appropriate message.
### 5. Delete All Tasks (DELETE /tasks)
Deletes all tasks in the database.
Verifies successful deletion with an appropriate message.