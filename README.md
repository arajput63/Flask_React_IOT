# flask_react_base


A full-stack web application (with integrated IoT communication) that uses `Python-Flask` on the backend (as an API) and `React.js` with `Redux` on the front end. This is a general application that can serve as boilerplate code, ready to be moulded into projects that serve a more specific purpose. 

`Template`/`Static` directories included in flask API for debugging and development purposes and can be ignored if the developer chooses to use react for front end as I have done here. The database is a placeholder and is only an example for CRUD and comms. SocketIO example will work with raspberryPI. Other IoT devices can be configured to communiate via `HTTP` or `MQTT`.




### Useful links -->


Javascript library source: https://cdnjs.com/


[Install npm (need for react.js)](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)


[Documentation for Python-Flask](https://flask.palletsprojects.com/en/2.0.x/)


[Documentation for React.js](https://reactjs.org/)




### Useful commands -->


Create a new python environment: 

### `python3 -m venv venv`



Activate the environment: 

### `. venv/bin/activate`



Install python dependances: 

### `pip install -r requirements.txt`



Run backend API: 

### `flask run`



Install node modules and dependancies: 

### `cd frontend`, `npm install package.json`



Run react.js frontend: 

### `cd frontend`, `npm start`



# Amar Rajput, AIPal Ltd