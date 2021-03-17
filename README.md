# About the application

This application is the beginnings of a photo album application. Currently the application can only upload single photos. When a photo is selected to be uploaded, its metadata is stored within the database and the file is stored in /api/ImageRepo in order to fulfill the basic add functionality. This is a first past implementation to be improved upon in future iterations. 

# Future improvements

- Add multiple photo upload functionality.
- When photos are uploaded, show in library in the UI.
- Implement hashes to identify photos in the database rather than simple numbering to improve extensibility.
- Add multiple user functionalities and permissions. 
- Implement secure upload functionality.

# How to start the application

## The Database

- The application depends on a MySQL database called 'imageRepository': 
`create database imageRepository;`
- And a table within the database called images:
` CREATE TABLE images (number int, date varchar(255));`

## The API

- Navigate to the api folder.
- Visit requirements.txt and ensure all packages are installed.
- Activate the virtual environment: `source venv/bin/activate`
- Make sure Flask recognizes the api: `export FLASK_APP=api.py`
- Modify config.py with database credentials
- Start the api: `python -m flask run`

## React App

- Navigate to my-react-app directory
- Install modules: `npm install`
- Start the app: `npm start`
- Navigate to http://localhost:3000/
