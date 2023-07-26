# Weather Project

The Weather Project is a web application built using Python, Django, and Bootstrap that allows users to add cities and view the weather information for the added cities. This README.md file provides an overview of the project, its features, and how to set it up.

## Features

- Users can add cities of their choice to the application.
- The application fetches weather data for the added cities from the OpenWeatherMap API.
- Weather information displayed includes temperature, description, and weather icon.
- The project uses Django for the backend, Python for server-side logic, and Bootstrap for the frontend.

## Prerequisites

Before running the Weather Project, ensure you have the following installed:

- Python
- Django
- Requests library (to make API calls)

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/amankumar1222/weather_project.git
   cd weather_project
   ```

2. Install the required packages using `pip`:

   ```bash
   pip install django requests
   ```

3. Get an API key from [OpenWeatherMap](https://openweathermap.org/appid) and replace `'AddYourKey'` in `views.py` with your API key.

## Running the Application

1. Apply the initial migrations:

   ```bash
   python manage.py migrate
   ```

2. Start the development server:

   ```bash
   python manage.py runserver
   ```

3. Open your web browser and go to `http://localhost:8000/weather/` to access the application.

## Usage

1. On the homepage, you will see a list of cities that have been added.
2. To add a new city, type the city name in the input field and click the "Add City" button.
3. The weather information for the added cities will be displayed, including temperature, description, and weather icon.

## Contribution

If you want to contribute to the Weather Project, feel free to submit pull requests or open issues in the repository.

## Author 
Name -: Aman kumar

## Acknowledgments

- The Weather Project uses the [OpenWeatherMap API](https://openweathermap.org/) to fetch weather data for cities.

