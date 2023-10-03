# Daily weather report
author: @moumitbera<br>
date: 03.10.2023

This is a python program that uses Open Weather API to get weather data for a particular location (co-ordinates) and then sends a mail to the user email about the basic description of the weather for that particular day. 

## API used
Open weather map (onecall), api is used in this project.<br> 
The API KEY is stored as environment variable to make it more secure. 

## Predined Configuration
As of now, the fields that are pre-defined are as follows:<br>

OPENWM_EP = "https://api.openweathermap.org/data/2.8/onecall"<br>
OPENWM_API_KEY = os.environ.get("OPENWM_API_KEY").strip('"')<br>
USER_ID = Email address to send from<br>
PASSWORD = os.environ.get("GMAIL_PASSWORD").strip('"')<br>
MESSAGE = Message to be sent<br>
TO_MAIL = Email address to send to<br>

* PASSWORD i.e. email password of USER_ID has been stored as an environmental variable
* The OPENWM_EP specifies the end point of the open weather map api call.
* MESSAGE: has been pre defined
