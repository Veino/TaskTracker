# Task Tracker API

The Task Tracker API is a RESTful API for managing tasks and action items. It provides various endpoints for task and task action item management.

## API Endpoints

### Get All Tasks

- **HTTP Method:** GET
- **Endpoint:** `/api/tasks`
- **Description:** Retrieves a list of all tasks.

### Delete All Tasks

- **HTTP Method:** DELETE
- **Endpoint:** `/api/tasks`
- **Description:** Deletes all tasks.

### Create a New Task

- **HTTP Method:** POST
- **Endpoint:** `/api/tasks`
- **Description:** Creates a new task.

### Get a Single Task

- **HTTP Method:** GET
- **Endpoint:** `/api/tasks/{id}`
- **Description:** Retrieves a single task by its unique identifier.

### Update Task Priority

- **HTTP Method:** PUT
- **Endpoint:** `/api/tasks/{id}`
- **Description:** Updates the priority of a task.

### Delete a Task

- **HTTP Method:** DELETE
- **Endpoint:** `/api/tasks/{id}`
- **Description:** Deletes a task by its unique identifier.

### Update Action Item Progress

- **HTTP Method:** PATCH
- **Endpoint:** `/api/tasks/{id}/actionitems/{action_item_id}`
- **Description:** Updates the progress of an action item within a task.

### Delete an Action Item

- **HTTP Method:** DELETE
- **Endpoint:** `/api/tasks/{id}/actionitems/{action_item_id}`
- **Description:** Deletes an action item within a task.

## Getting Started

To get started with the Task Tracker API using Python and Django, follow these steps:

1. Clone the repository: `git clone https://github.com/Veino/TaskTracker.git`
2. Create a virtual environment (optional but recommended):
3. Install Python Dependencies: `pip install -r requirements.txt`
4. Configure your database settings and Run database migrations to create the database tables:

    ```
    python manage.py makemigrations

    ```

    ```
    python manage.py migrate

    ```
5. Create a superuser account to access the Django admin panel (optional):

    ```
    python manage.py createsuperuser

    ```
6. Start the Django development server:
    ```
    python manage.py runserver

    ```
7. Your Task Tracker API should now be running locally at (http://localhost:8000/), go to (http://localhost:8000/api) to get all routes.

8. You can access the Django admin panel at (http://localhost:8000/admin/) to manage tasks and action items.

## Usage

You can use the Task Tracker API to manage tasks and action items in your application. Make HTTP requests to the provided endpoints to interact with the API. For example, to retrieve all tasks, send a GET request to `/api/tasks`.


## Contributing

Contributions are welcome!
## License

This project is licensed under the [MIT License](https://opensource.org/license/mit/).

## Contact

For inquiries and feedback, please contact [pwaveinoc@gmail.com](mailto:pwaveinoc@gmail.com).
