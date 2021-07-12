# Workout Tracker
An application that uses natural language processing, Nutritionix API, and Sheety API to prompt for the user's
description of their exercise and adds it to a Google Sheet.

The code works live on [Repl.it](https://replit.com/@SaraStrasner/exercise-tracker).

# Feature Tasks
1. Create a "My Workouts" Google Sheet.
1. Get a Nutritionix API key.
1. Using the Nutritionix "Natural Language for Exercise" API Documentation, figure out how to print the exercise stats for a plain text input.
1. Setup Your Google Sheet with Sheety, enabling GET and POST requests.
1. Using the Sheety Documentation, write some code to use the Sheety API to generate a new row of data in your Google Sheet for each of the exercises that you get back from the Nutritionix API. The date and time columns should contain the current date and time from the Python datetime module.
1. Add either "Basic Authentication" or "Bearer Token" to your Sheety endpoint to secure it.  You can hardcode the token in your code for now while you test your code. Once you're sure it works, we can add it to the environment variables in the next step.
1. Configure your code to run on Repl.it and update your code to use environment variables for all sensitive data.