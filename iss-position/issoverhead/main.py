import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "Enter you e-mail"
MY_PASSWORD = "Enter your password"
MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude


# Check if my position is within +5 or -5 degrees of the ISS position.
def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude < MY_LONG:
        return True


# Check if it is night
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


# Send a E-mail if the iss is close to me and it is at night
while True:
    time.sleep(60)
    if is_close() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look up \n\nThe Iss is above you in the sky."
        )
