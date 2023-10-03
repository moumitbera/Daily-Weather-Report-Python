import requests
import smtplib
import os

# enviroment variables:
# Open weather map api key & password for gmail

OPENWM_EP = "https://api.openweathermap.org/data/2.8/onecall"
OPENWM_API_KEY = os.environ.get("OPENWM_API_KEY").strip('"')

# for gmail
USER_ID = "moumitcodecheck@gmail.com"
PASSWORD = os.environ.get("GMAIL_PASSWORD").strip('"')
MESSAGE = "Subject:Morning report\n\nGood morning Moumit,\n\n[MESSAGE]\n\nHave a wonderful day ahead!"
TO_MAIL = "contactmoumitbera@gmail.com"

# getting the weather status
PARAMETERS = {
    # pre programmed to DELHI, INDIA
    "lat": 28.7041,
    "lon": 77.1025,
    "exclude": "current,minutely,hourly",  # only get the daily weather forecast
    "appid": OPENWM_API_KEY,
}

response = requests.get(url=OPENWM_EP, params=PARAMETERS)
response.raise_for_status()
data = response.json()
day_forecast = data["daily"][0]
print(day_forecast)

weather_full = day_forecast["weather"][0]
weather_code = int(weather_full["id"])
desc = weather_full["description"]


weather_msg = ""


def get_weather_msg():
    global weather_msg
    if weather_code >= 200 and weather_code < 700:
        # thunderstorm to snow
        weather_msg = (
            f"It is expected to be a day of {desc}\nYou should carry an umbrella!"
        )
    elif weather_code >= 701 and weather_code < 800:
        weather_msg = f"It is expected to be a {desc}y day!"
    elif weather_code == 800:
        weather_msg = f"It's expected to be a clear day!"
    elif weather_code > 800 and weather_code < 900:
        weather_msg = f"It's expected to be a {desc} day!"


def send_mail():
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=USER_ID, password=PASSWORD)
        connection.sendmail(
            from_addr=USER_ID,
            to_addrs=TO_MAIL,
            msg=MESSAGE.replace("[MESSAGE]", weather_msg),
        )
        print("Sent")


get_weather_msg()
send_mail()
