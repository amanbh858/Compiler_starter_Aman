How to Run the Application
1. Prerequisites
Before running the application, ensure you have the following installed:

Python (version 3.8 or higher)

PDM (Python Development Master, a package manager)

Installing PDM
If you haven't already installed PDM, you can do so by running:

bash
Copy
Edit
pip install pdm
2. Setting Up the Project
Ensure that you have cloned or downloaded the project and that you've navigated to the project directory in your terminal. Once inside the project folder, run the following command to install the dependencies:

bash
Copy
Edit
pdm install
This will install all the necessary libraries and dependencies required for both the local and web applications.

3. Running the Local App (GUI)
The local app is a GUI application built using PyQt6. To run it, follow these steps:

Open a terminal and navigate to the project directory.

Run the following command:
pdm run gui_app.py(kindly make sure when u input data give spaces between the operators and operands to get the results)for eg:(* + 3 4 5)

This command will start the local app, and the GUI should appear. You can interact with it and use the features for local computation.

4. Running the Web App
The web app is a Flask-based application. To run it, follow these steps:

Open a terminal and navigate to the project directory.

Run the following command:
pdm run web_app.py(kindly make sure when u input data give spaces between the operators and operands to get the results)for eg:(* + 3 4 5)

This will start the Flask web server, and you can access the web app in your browser by visiting:
http://127.0.0.1:5000

5. Troubleshooting
If you encounter issues while running the application, check if all dependencies are installed correctly by running pdm install again.

Ensure that the Flask web server is not being blocked by a firewall or another program occupying port 5000.

6. Stopping the Applications
For the local app (GUI), simply close the window or press Ctrl + C in the terminal.

For the web app, you can stop the Flask server by pressing Ctrl + C in the terminal.