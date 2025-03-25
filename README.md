# Weather App GUI
 
This Weather App is built using Python's Tkinter for the graphical user interface and OpenWeatherMap API to fetch real-time weather updates for selected cities.

Features

Select a city from the dropdown menu

Fetch real-time weather data including:

Climate

Description

Temperature (in Celsius)

Pressure (in hPa)

User-friendly GUI with a modern look

Prerequisites

Ensure you have Python installed on your system. You can check this by running:

python --version

If Python is not installed, download and install it from python.org.

Installation

Clone or download the repository.

Install required dependencies:

pip install requests

Tkinter is included by default with Python, so no separate installation is needed.

How to Run the App

Navigate to the project directory.

Run the script:

python temp.py

API Key Setup

This application requires an API key from OpenWeatherMap. Replace API_KEY in temp.py with your own key:

API_KEY = "your_api_key_here"

You can obtain an API key by signing up at OpenWeatherMap.

Cities Included

The dropdown menu contains a list of major cities in Pakistan, such as:

Karachi

Lahore

Islamabad

Rawalpindi

Faisalabad

Peshawar

Quetta

And many more...

Troubleshooting

ModuleNotFoundError: No module named 'requests'

If you encounter this error, install the requests module:

pip install requests

Unable to Fetch Weather Data

Ensure your internet connection is active and that your API key is correct.

License

This project is open-source and free to use.

