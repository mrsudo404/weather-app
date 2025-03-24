from tkinter import *
from tkinter import ttk
import requests
city_name = "Karachi"
api_key = "d759291381f257c93bd757292a25cba6"  # Replace with your actual API key

# Corrected API request URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
response = requests.get(url)
data = response.json()



win = Tk()
win.title("Weather App GUI")
win.config(bg= "blue")
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
    "Kohat", "Jacobabad", "Shikarpur", "Muzaffargarh", "Khanewal","Kabirwala",
    "Gojra", "Bahawalnagar", "Abbottabad", "Mansehra", "Vehari",
    "Dera Ismail Khan", "Tando Adam", "Khuzdar", "Jhelum", "Gwadar"
]
com = ttk.Combobox(win, text = "Weather App", values=list_name, font=("Poppins", 30, 'bold'), state="readonly")
com.place(x=25, y=150, height=50, width=450)

com.set("Select City")
# com.bind("<<ComboboxSelected>>", lambda event: print(f"You selected: {com.get()}"))
done_button = Button(win, text="Done", font=("Poppins", 20, "bold"), bg="white", fg="blue", command=lambda: print(f"You selected: {com.get()}"))
done_button.place(x=25, y=220, height=50, width=450)

Weather_label = Label(win, text="Climate", font=("Poppins", 20, "bold"),  bg="white", fg="blue")
Weather_label.place(x=25, y=280, height=50, width=150)

Weather_label1 = Label(win, text="Weather", font=("Poppins", 20, "bold"),  bg="white", fg="blue")
Weather_label1.place(x=250, y=280, height=50, width=150)

Descrip_label = Label(win, text="Description", font=("Poppins", 20, "bold"),  bg="white", fg="blue")
Descrip_label.place(x=25, y=340, height=50, width=150)  # Adjusted y for proper spacing

Descrip_label1 = Label(win, text="Description", font=("Poppins", 20, "bold"),  bg="white", fg="blue")
Descrip_label1.place(x=250, y=340, height=50, width=150)  # Adjusted y for proper spacing


Temp_label = Label(win, text="Temperature", font=("Poppins", 20, "bold"),  bg="white", fg="blue")
Temp_label.place(x=25, y=400, height=50, width=150)  # Adjusted y for proper spacing

Temp_label1 = Label(win, text="Temperature", font=("Poppins", 20, "bold"),  bg="white", fg="blue")
Temp_label1.place(x=250, y=400, height=50, width=150)  # Adjusted y for proper spacing

Pressure_label = Label(win, text="Pressure", font=("Poppins", 20, "bold"), bg="white", fg="blue")
Pressure_label.place(x=25, y=460, height=50, width=150)  # Adjusted y for proper spacing

Pressure_label1 = Label(win, text="Pressure", font=("Poppins", 20, "bold"),  bg="white", fg="blue")
Pressure_label1.place(x=250, y=460, height=50, width=150)  # Adjusted y for proper spacing

win.mainloop()