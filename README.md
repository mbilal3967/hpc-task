# Ship CRUD Application

This is a simple Python application that allows users to perform CRUD operations on ships. Each ship has a name, length, width, and code. The code follows the format AAAA-1111-A1, where A is any character from the Latin alphabet, and 1 is a number from 0 to 9.

## Setup Instructions

1. Ensure you have Python 3.x installed on your system.
2. Clone this repository to your local machine or download the source code.
3. Open a terminal or command prompt and navigate to the project directory.

## Installation

1. Create a virtual environment:
   - For Windows:
     ```shell
     python -m venv venv
     venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```shell
     python3 -m venv venv
     source venv/bin/activate
     ```

2. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
   ```

## Running the Application

    Start the application by running the following command in the terminal:

    ```shell
    python app.py
    ```

The application will start running on http://localhost:5000.

Open your web browser and go to http://localhost:5000 to access the application.

Home Page:

    On the home page, you'll see a form to create a ship. Fill in the ship details, including the name, length, width, and code.
    Click the "Create Ship" button to add the ship. You will be redirected to the page that lists all the ships.

Ships Page:

    The ships page displays a table with all the ships in the database.
    Each ship is listed with its name, length, width, and code.
    The actions column provides links to view, edit, and delete each ship.

View Ship:

    Click the "View" link next to a ship to see the details of that ship.
    You will be redirected to a page that displays the ship's name, length, width, and code.

Edit Ship:

    To edit a ship's details, click the "Edit" link next to the ship.
    You will be redirected to an edit form pre-filled with the ship's current details.
    Modify any of the ship's details and click the "Update Ship" button to save the changes.

Delete Ship:

    To delete a ship, click the "Delete" button next to the ship.
    The ship will be removed from the list.

To stop the application, press Ctrl + C in the terminal.

# For running the app is  Docker, follow these steps:

    Save the Dockerfile in the root directory of your project, alongside the app.py and requirements.txt files.

    Open a terminal or command prompt and navigate to the project directory.

    Build the Docker image by running the following command:

    ```shell
    docker build -t ship-crud-app .
    ```

This command will build the Docker image using the provided Dockerfile and tag it with the name ship-crud-app.

Once the image is built, you can run a Docker container based on that image with the following command:

    ```shell
    docker run -p 5000:5000 ship-crud-app
    ```

    This command maps port 5000 of the container to port 5000 of the host system, allowing you to access the application through http://localhost:5000 in your web browser.

That's it! Your Ship CRUD application is now running in a Docker container. You can access it by opening your web browser and navigating to http://localhost:5000.