## flask/react - base project (boilerplate)


A full-stack web application (with integrated IoT communication) that uses `Python-Flask` on the backend (as an API) and `React.js` with `Redux` on the front end. This is a general application that can serve as boilerplate code, ready to be moulded into projects that serve a more specific purpose. 

`Template` & `Static` directories are included in flask API for debugging and development purposes and can be ignored if the developer chooses to use `react.js` on the frontend as I have done here. The database is a placeholder and is only an example for CRUD and communications across the full stack. `SocketIO` examples work well with raspberryPI devices and has been implemented in other projects using models `Raspberry Pi 4B` and `PiZero` across various use cases. Other IoT devices can be configured to communiate via `TCP`, `HTTP` or `MQTT`; examples used in other AIPal projects are `ESP8266`, `Arduino UNO`, `ESP32`, `NVIDIA Jetson Nano` and many other specially designed PCBs & components/assemblies.


### Useful links -->

[Javascript library source](https://cdnjs.com/), [Install npm (for react.js)](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm), [Documentation for Python-Flask](https://flask.palletsprojects.com/en/2.0.x/), [Documentation for React.js](https://reactjs.org/)


### Useful commands (from project root directory) -->

Create a new python environment: `python3 -m venv venv`

Activate the environment: `. venv/bin/activate`

Install python dependances: `pip install -r requirements.txt`

Run backend API: `flask run`

Install node modules and dependancies: `cd frontend`, `npm install package.json`

Run react.js frontend: `cd frontend`, `npm start`


## Amar Rajput, AIPal Ltd