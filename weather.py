import tkinter as tk
from typing import final
import requests
import datetime
import time


def getWeather(canvas):
    apikey="b7eaa9824eefd6c987eb62b55aa2b446"
    city=textfield.get()
    api="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+apikey
    response=requests.get(api).json()
    conditions = response['weather'][0]['main']
    description= response['weather'][0]['description']
    lat= response['coord']['lat']
    long=response['coord']['lon']
    temperature=int(response['main']['temp']-273.15) #in celsius
    feels_like=int(response['main']['feels_like']-273.15)
    min_temp=int(response['main']['temp_min']-273.15)
    max_temp=int(response['main']['temp_max']-273.15)
    pressure=response['main']['pressure']
    humidity=response['main']['humidity']
    wind_speed=response['wind']['speed']
    wind_direc=response['wind']['deg']
    sunrise=time.strftime("%I:%M:%S",time.gmtime(response['sys']['sunrise']-21600))
    sunset=time.strftime("%I:%M:%S",time.gmtime(response['sys']['sunset']-21600))
    
     
    final_info=conditions+'\n'+str(temperature)+"°C"
    info2="\n"+"Max Temo:"+str(max_temp)+"\n"+"Min Temp: "+str(min_temp)
    info3="Pressure:"+str(pressure)+"\nHumidity:"+str(humidity)
    info4="Sunrise: "+sunrise+"\nSunset: "+sunset
    label1.config(text=final_info)
    label2.config(text=info2)
    label3.config(text=info3)
    label4.config(text=info4)

canvas= tk.Tk()
canvas.geometry("600x500")
canvas.title("The Weather App")

font=("poppins",15,"bold")
t=("poppins",35,"bold")

#get city name from the user
textfield=tk.Entry(canvas,font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>',getWeather)

label1=tk.Label(canvas,font=t)
label1.pack()
label2=tk.Label(canvas,font=font)
label2.pack(anchor='e')

label3=tk.Label(canvas,font=font)
label3.pack(anchor='e')

label4=tk.Label(canvas,font=font)
label4.pack(anchor='e')

canvas.mainloop()