import requests
import json
import datetime
from tkinter import *
import tkinter.messagebox as mb
from labels import MyLabel
from pygame import mixer
from PIL import ImageTk, Image

# Initialise sound mixer from PyGame
mixer.init()

# Setting sound variables
SNOW = "./sounds/snow_fade.mp3"
RAIN = "./sounds/rain_fade.mp3"
SUNNY = "./sounds/sunny_fade.mp3"
CLOUDY = "./sounds/cloudy_fade2.mp3"
THUNDER = "./sounds/thunder_fade.mp3"
WIND = "./sounds/wind_fade.mp3"


# Initialise main window
root = Tk()
root.title("Weatheready")
root.geometry("720x543")
root.resizable(0, 0)
root.configure(bg="black")


# Weather API variables
API_KEY = # insert API key from Open Weather Map.org
LONG = # insert long here
LAT = # insert lat here
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

# Weather API parameters
weather_params = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "exclude": "minutely",
    "units": "metric"
}


# Setting StringVar variables
time_now = StringVar()
time_next = StringVar()
weather_description_now = StringVar()
weather_description_next = StringVar()
chance_rain_now = StringVar()
chance_rain_next = StringVar()
temp_now = StringVar()
temp_next = StringVar()
feels_like_now = StringVar()
feels_like_next = StringVar()
wind_speed_now = StringVar()
wind_speed_next = StringVar()


def GetWeather():
    '''Getting weather API data as json'''
    try:
        response = requests.get(OWM_ENDPOINT, params=weather_params)
        response.raise_for_status()
        weather_data = response.json()

        with open("weather.json", "w") as f:
            json.dump(weather_data, f)

        with open("weather.json", "r") as f:
            data = json.load(f)

        '''Setting fields'''
        time_now_epoch = data["current"]["dt"]
        time_now.set(datetime.datetime.fromtimestamp(time_now_epoch).strftime('%H:%M'))

        time_next_epoch = data["hourly"][1]["dt"]
        time_next.set(datetime.datetime.fromtimestamp(time_next_epoch).strftime('%H:%M'))

        weather_description_now.set(data["current"]["weather"][0]["description"])
        weather_description_next.set(data["hourly"][1]["weather"][0]["description"])

        chance_rain_now.set(data["hourly"][0]["pop"])
        chance_rain_next.set(data["hourly"][1]["pop"])

        temp_now.set(data["current"]["temp"])
        temp_next.set(data["hourly"][1]["temp"])

        feels_like_now.set(data["current"]["feels_like"])
        feels_like_next.set(data["hourly"][1]["feels_like"])

        wind_now_pre = data["current"]["wind_speed"] * 2.237
        wind_now_temp = f"{wind_now_pre:.2f}mph"
        wind_speed_now.set(wind_now_temp)

        wind_next_pre = data["hourly"][1]["wind_speed"] * 2.237
        wind_next_temp = f"{wind_next_pre:.2f}mph"
        wind_speed_next.set(wind_next_temp)

    except:
        mb.showerror(title="Error!", message="Unable to retrieve weather.")


# Acquire weather data to send to Tkinter widgets
GetWeather()


# Title field
Label(root, text="WEATHEREADY", fg="#219ebc", bg="black", font=("Helvetica", 40), justify="center").grid(column=0, row=0, columnspan=5)

# Time fields
Label(root, text="Time next hour:", width=14, anchor="e", fg="silver", bg="black").grid(column=0, row=1)
time_now_data = MyLabel(root, time_now).grid(column=1, row=1)

spacer = Label(root, width=5, bg="black").grid(column=2, row = 1)

time_next_label = Label(root, text="Time next hour:", width=14, anchor="e", fg="silver", bg="black").grid(column=3, row=1)
time_next_data = MyLabel(root, time_next).grid(column=4, row=1)

# Weather description fields
description_now_label = Label(root, text="Weather State:", width=14, anchor="e", fg="silver", bg="black").grid(column=0,row=2)
description_now_data = MyLabel(root, weather_description_now).grid(column=1, row=2)

description_next_label = Label(root, text="Weather State:", width=14, anchor="e", fg="silver", bg="black").grid(column=3,row=2)
description_next_data = MyLabel(root, weather_description_next).grid(column=4, row=2)

# Chance of rain fields
rain_now_label = Label(root, text="Chance of rain % :", width=14, anchor="e", fg="silver", bg="black").grid(column=0,row=3)
rain_now_data = MyLabel(root, chance_rain_now).grid(column=1, row=3)

rain_next_label = Label(root, text="Chance of rain % :", width=14, anchor="e", fg="silver", bg="black").grid(column=3,row=3)
rain_next_data = MyLabel(root, chance_rain_next).grid(column=4, row=3)

# Temperature Fields
temp_now_label = Label(root, text="Temperature °C :", width=14, anchor="e", fg="silver", bg="black").grid(column=0,row=4)
temp_now_data = MyLabel(root, temp_now).grid(column=1, row=4)

temp_next_label = Label(root, text="Temperature °C :", width=14, anchor="e", fg="silver", bg="black").grid(column=3,row=4)
temp_next_data = MyLabel(root, temp_next).grid(column=4, row=4)

# Feels now temperate fields
feels_now_label = Label(root, text="Feels Like °C :", width=14, anchor="e", fg="silver", bg="black").grid(column=0,row=5)
feels_now_data = MyLabel(root, feels_like_now).grid(column=1, row=5)

feels_next_label = Label(root, text="Feels Like °C :", width=14, anchor="e", fg="silver", bg="black").grid(column=3,row=5)
feels_next_data = MyLabel(root, feels_like_next).grid(column=4, row=5)

# Wind speed fields
wind_now_label = Label(root, text="Wind Speed:", width=14, anchor="e", fg="silver", bg="black").grid(column=0,row=5)
wind_now_data = MyLabel(root, wind_speed_now).grid(column=1, row=5)

wind_next_label = Label(root, text="Wind Speed:", width=14, anchor="e", fg="silver", bg="black").grid(column=3,row=5)
wind_next_data = MyLabel(root, wind_speed_next).grid(column=4, row=5)

# Refresh weather data and get new joke
refresh_button = Button(root, text="REFRESH", font=("Helvetiva", 18), bg="grey", width=16, command=lambda:[GetWeather(), GetJoke()]).grid(pady=5, column=1, row=6)

# Set text widget
texty = Text(root, wrap=WORD, width=40, height=40, bg="black", fg="silver", font=("French Script MT", 20), border=0)
texty.place(height=252, width=327, x=374, y=275)


def play(sound):
    ''' Play sound based on weather ID'''
    mixer.music.load(sound)
    mixer.music.play()


def SoundCheck():
    '''Open json to gauge weather ID'''
    try:
        with open("weather.json", "r") as f:
            data = json.load(f)

            # Weather IDs for now and next hours
            id_now = data["current"]["weather"][0]["id"]
            id_next = data["hourly"][1]["weather"][0]["id"]

            # Variable for setting image based on weather ID
            global image_holder

            # Play sounds based on weather ID and set image variable
            if id_now >= 200 and id_now <= 232:
                sound = THUNDER
                play(sound)
                image_holder = "thunder1"
            elif id_next >= 200 and id_next <= 232:
                sound = THUNDER
                play(sound)
                image_holder = "thunder1"
            elif id_now >= 300 and id_now <= 531:
                sound = RAIN
                play(sound)
                image_holder = "rain1"
            elif id_next >= 300 and id_next <= 531:
                sound = RAIN
                play(sound)
                image_holder = "rain1"
            elif id_now >= 600 and id_now <= 622:
                sound = SNOW
                play(sound)
                image_holder = "snow1"
            elif id_next >= 600 and id_next <= 622:
                sound = SNOW
                play(sound)
                image_holder = "snow1"
            elif id_now > 799 and id_now < 801:
                sound = SUNNY
                play(sound)
                image_holder = "sun1"
            elif id_now >= 801 and id_now <= 804:
                sound = CLOUDY
                play(sound)
                image_holder = "cloud1"
            elif id_next >= 801 and id_next <= 804:
                sound = CLOUDY
                play(sound)
                image_holder = "cloud1"

            # Convert wind speed to MPH and gauge whether wind sound is played
            wind_speed_now = data["current"]["wind_speed"] * 2.237
            wind_speed_next = data["hourly"][1]["wind_speed"] * 2.237

            # If wind speed is high enough play wind sound after weather sound
            if wind_speed_now > 20 or wind_speed_next > 20:
                mixer.music.queue(wind)

    except:
        mb.showerror(title="Error!", message="Well something has gone wrong there!")


def GetJoke():
    '''Get joke api and send to text widget'''
    try:
        response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
        response.raise_for_status()
        joke_json = response.json()
        joke = joke_json["joke"]
        texty.delete("1.0", END)
        texty.insert(INSERT, joke)
    except:
        mb.showerror(title="Error!", message="Unable to retrieve joke")


# Get Joke
GetJoke()

# Run sounds
SoundCheck()


# Open image based on image_holder variable and weather ID
img = Image.open(f"./images/{image_holder}.jpg")
resized_image = img.resize((350, 250))
new_image = ImageTk.PhotoImage(resized_image)

# Create canvas and place image
canvas = Canvas(root)
canvas.place(x=12, y=280, width=350, height=250)
canvas.create_image(0,0,anchor="nw", image=new_image)


# Finalizing the window
root.update()
root.mainloop()


# Copyright attributions:
# Jingle bell sound by CGEffex - freesound.org
# Chimes by organicmanpl - freesound.org
# Seagull on beach by Squashy555 - freesound.org
# Rain Thunder by Nimlos - freesound.org
# Bug Rain drop by Macdaddyno1 - freesound.org
# Wind by Hope Sounds - freesound.org