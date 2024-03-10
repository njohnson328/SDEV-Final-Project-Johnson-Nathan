# SDEV140 Final Projet
# 02/25/24
# Make a GUI weatehr application

# pseudo code
# display temperature
# display precipitation
# display condition
# display location

# making the program a GUI
from tkinter import *


def search():
    pass

# app title
app = Tk()
app.title("Nate's weather app")
app.geometry('700x350')

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text='Search weather', width=12, command=search)
search_btn.pack()
# location label
location_lbl = Label(app, text='Location', font=('bold',20))
location_lbl.pack()
# image label
image = Label(app, bitmap='')
image.pack()
# temperature label
temp_lbl = Label(app, text='temperature')
temp_lbl.pack()
# weather label
weather_lbl = Label(app, text='weather')
weather_lbl.pack()
