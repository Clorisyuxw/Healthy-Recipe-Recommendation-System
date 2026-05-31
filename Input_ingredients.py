import streamlit as st
from recipes import get_known_ingredients

# Load the list of known ingredients from recipes.py
known_ingredients = get_known_ingredients()

def main():
    st.title('Ingredient input')

    # Input multiple ingredients separated by commas
    ingredients_input = st.text_input('Please input ingredients, separated by commas (e.g., milk, eggs, sugar):')

    if st.button('Submit'):
        if ingredients_input:
            ingredients = [ingredient.strip().lower() for ingredient in ingredients_input.split(',')]
            unknown_ingredients = [ingredient for ingredient in ingredients if ingredient not in known_ingredients]
            if unknown_ingredients:
                st.error(f'These ingredients are not recognized. Please make sure the words are spelled correctly: {", ".join(unknown_ingredients)}')
            else:
                # Write all recognized ingredients to a single line in the file, separated by commas
                with open('fridge_ingredients.txt', 'a') as file:
                    file.write(', '.join(ingredients) + '\n')
                st.success('Your ingredients have been added successfully!')
                # Optionally display current ingredients from the file
                try:
                    with open('fridge_ingredients.txt', 'r') as file:
                        stored_ingredients = file.readlines()
                    st.text_area('Current ingredients in your fridge:', ''.join(stored_ingredients), height=250)
                except FileNotFoundError:
                    st.text_area('Current ingredients in your fridge:', 'No ingredients added yet.', height=250)
        else:
            st.error('Please input some ingredients before submitting.')

main()