
from tkinter import *
from tkinter import ttk
import requests

API_KEY = "d759291381f257c93bd757292a25cba6"  

def fetch_weather():
    city_name = com.get()
    if city_name == "Select City":
        return
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        weather_label1.config(text=data['weather'][0]['main'])
        descrip_label1.config(text=data['weather'][0]['description'])
        temp_label1.config(text=f"{data['main']['temp']}°C")
        pressure_label1.config(text=f"{data['main']['pressure']} hPa")
    else:
        weather_label1.config(text="N/A")
        descrip_label1.config(text="N/A")
        temp_label1.config(text="N/A")
        pressure_label1.config(text="N/A")

win = Tk()
win.title("Weather App GUI")
win.config(bg="blue")
win.geometry("500x700")

name_label = Label(win, text="Weather App", font=("Poppins", 40, "bold"), bg="blue", fg="white")
name_label.place(x=25, y=50, height=50, width=450)

list_name = [
    "Karachi", "Lahore", "Islamabad", "Rawalpindi", "Faisalabad",
    "Peshawar", "Quetta", "Multan", "Sialkot", "Hyderabad",
    "Gujranwala", "Bahawalpur", "Sargodha", "Sukkur", "Larkana",
    "Sheikhupura", "Jhang", "Gujrat", "Mardan", "Rahim Yar Khan",
    "Kasur", "Dera Ghazi Khan", "Okara", "Sahiwal", "Mirpur Khas",
    "Nawabshah", "Mingora", "Chiniot", "Kamoke", "Hafizabad",
    "Kohat", "Jacobabad", "Shikarpur", "Muzaffargarh", "Khanewal", "Kabirwala",
    "Gojra", "Bahawalnagar", "Abbottabad", "Mansehra", "Vehari",
    "Dera Ismail Khan", "Tando Adam", "Khuzdar", "Jhelum", "Gwadar"
]

com = ttk.Combobox(win, values=list_name, font=("Poppins", 20, 'bold'), state="readonly")
com.place(x=25, y=150, height=50, width=450)
com.set("Select City")

done_button = Button(win, text="Get Weather", font=("Poppins", 20, "bold"), bg="white", fg="blue", command=fetch_weather)
done_button.place(x=25, y=220, height=50, width=450)

weather_label = Label(win, text="Climate", font=("Poppins", 20, "bold"), bg="white", fg="blue")
weather_label.place(x=25, y=280, height=50, width=150)

weather_label1 = Label(win, text="N/A", font=("Poppins", 20, "bold"), bg="white", fg="blue")
weather_label1.place(x=250, y=280, height=50, width=150)

descrip_label = Label(win, text="Description", font=("Poppins", 20, "bold"), bg="white", fg="blue")
descrip_label.place(x=25, y=340, height=50, width=150)

descrip_label1 = Label(win, text="N/A", font=("Poppins", 20, "bold"), bg="white", fg="blue")
descrip_label1.place(x=250, y=340, height=50, width=150)

temp_label = Label(win, text="Temperature", font=("Poppins", 20, "bold"), bg="white", fg="blue")
temp_label.place(x=25, y=400, height=50, width=150)

temp_label1 = Label(win, text="N/A", font=("Poppins", 20, "bold"), bg="white", fg="blue")
temp_label1.place(x=250, y=400, height=50, width=150)

pressure_label = Label(win, text="Pressure", font=("Poppins", 20, "bold"), bg="white", fg="blue")
pressure_label.place(x=25, y=460, height=50, width=150)

pressure_label1 = Label(win, text="N/A", font=("Poppins", 20, "bold"), bg="white", fg="blue")
pressure_label1.place(x=250, y=460, height=50, width=150)

win.mainloop()
