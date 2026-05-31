# Healthy-Recipe-Recommendation-System# Healthy Recipe Recommendation System

## Overview

The Healthy Recipe Recommendation System is a Python-based web application developed using Streamlit. The application recommends recipes based on ingredients available in a user's fridge while considering dietary preferences and food allergies.

The system also provides nutritional analysis and personalised dietary suggestions to help users make informed food choices and reduce food waste.

---

## Features

### Ingredient-Based Recipe Recommendation

* Input available ingredients from the user's fridge
* Match ingredients with recipes stored in the database
* Recommend suitable recipes based on available ingredients

### Allergy-Aware Filtering

* Allow users to select allergenic ingredients
* Automatically exclude recipes containing allergens

### Nutrition Analysis

* Display nutritional information for selected recipes
* Calculate calories, protein, and carbohydrate intake
* Generate visual nutrition charts

### Personalised Dietary Suggestions

* Provide recommendations based on nutritional balance
* Identify potential vitamin deficiencies
* Suggest improvements for a healthier diet

### Interactive User Interface

* Built using Streamlit
* User-friendly and easy to navigate
* Supports personalised user input and recipe selection

---

## Technologies Used

* Python
* Streamlit
* Pandas
* Matplotlib

---

## Project Structure

```text
app.py                        # Main Streamlit application
recipes.py                    # Recipe database and matching logic
user_information.py           # User profile and allergy input
Input_ingredients.py          # Ingredient input module

picture/
├── braised_pork_belly.jpg
├── cucumber_salad.jpg
├── fish_flavored_eggplant.jpg
├── kung_pao_chicken.jpg
├── oyster_sauce_lettuce.jpg
└── stir_fried_tofu.jpg
```

---

## Skills Demonstrated

* Python Programming
* Data Processing
* Data Visualisation
* User Interface Development
* Recommendation System Design
* Problem Solving
* Software Development

---

## Running the Application

```bash
streamlit run app.py
```

---

## Future Improvements

* Expand the recipe database
* Add more dietary preference options
* Integrate external nutrition APIs
* Improve recommendation accuracy using machine learning techniques
* Deploy the application as a public web application

---
## Application Preview

### Home Page

![Home Page](screenshots/home_page.png)

### Nutrition Analysis

![Nutrition Analysis](screenshots/nutrition_analysis.png)

## Contributors

* Xiaowen Yu

---

## Academic Context

This project was completed as part of the Master of Applied Data Science programme at the University of Canterbury.
