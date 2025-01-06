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

http://<your-server-url>/test

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
