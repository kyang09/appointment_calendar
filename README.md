# Appointment Calendar
## by Kevin Yang
#### Simple calendar for appointments built using Django 1.8 and ReactJS.

###### If you want to run this on your machine, create a virtualenv (virtual enviroment) before running. Included are two shell scripts for Windows and Unix/Linux to creat a virtualenv and install dependencies.

The Django models and views exist in the 'appointments' directory.

### Concept

A user selects the month and year. An appropriate calendar will show with selectable days. By clicking on a day, a GET request is sent with the "date" information to the server. The server will find all appointments for that day and respond with JSON data. The front-end code will calculate available times and strongly discourage users to try to schedule a taken time period (in case they get around the front-end code). The back-end code should also have a protection against overriding appointments. 

A user can select a time period duration of 30 minutes or 1 hour. The front-end code will use the 'start_time' and 'end_time' information from the Appointment Django model to find open time slots for the preferred period duration. Once the user picks a time period, they need to fill out their name, select the host they want to see, and write their reason for the appointment. A POST request is sent to the server along with the appointment data. The server processes the POST request and creates a new appointment in the database. 

It is possible to update appointment information. Due to the lack of security and authorization for this project currently, anyone can modify any appointment. This is because Django Users Login hasn't been implemented given the short amount of time. In theory, a user signs up and has a user id. Their appointments will have their id on it, and they can only modify their own appointments. This can be done with a PATCH HTTP request. Deleting an appointment is similar. It'll use a DELETE HTTP request. All the HTTP requests are handled by the REST API.