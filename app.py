import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from recipes import get_recipes_by_ingredients

def main():
    st.markdown(
        """
        <style>
        .main {
            background-color: #f0f2f6;
            padding: 10px;
            border-radius: 10px;
        }
        .title {
            font-size: 2.5em;
            font-weight: bold;
            color: #4A4A4A;
            text-align: center;
        }
        .subheader {
            font-size: 1.5em;
            font-weight: bold;
            color: #4A4A4A;
        }
        .section {
            margin-top: 20px;
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<div class="title">Welcome to Recipe and Nutrition Recommendation System</div>', unsafe_allow_html=True)

    user_info = load_user_information()
    if not user_info:
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("Enter your user information:")
        user_info = get_user_information()
        if user_info:
            save_user_information(user_info)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        name, aller_ingredient = user_info
        st.markdown(f'<div class="subheader">Hello, {name}!</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="section">Your allergenic ingredients: <b>{", ".join(aller_ingredient)}</b></div>', unsafe_allow_html=True)

    fridge_ingredients = load_fridge_ingredients()
    if not fridge_ingredients:
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("Input ingredients into your fridge:")
        fridge_ingredients = get_ingredients()
        if fridge_ingredients:
            save_fridge_ingredients(fridge_ingredients)
        st.markdown('</div>', unsafe_allow_html=True)

    if user_info and fridge_ingredients:
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("Ingredients loaded from your fridge:")
        st.markdown(f"<b>{', '.join(fridge_ingredients)}</b>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        recipes = get_recipes_by_ingredients(fridge_ingredients)
        st.markdown(f'<div class="section">Found <b>{len(recipes)}</b> recipes</div>', unsafe_allow_html=True)

        if recipes:
            filtered_recipes = [
                recipe for recipe in recipes
                if not any(ingredient.lower() in [ai.lower() for ai in aller_ingredient] for ingredient in recipe['ingredients'])
            ]
            st.markdown(f'<div class="section">Filtered down to <b>{len(filtered_recipes)}</b> recipes</div>', unsafe_allow_html=True)
            if filtered_recipes:
                st.markdown('<div class="section">', unsafe_allow_html=True)
                recipe_options = st.multiselect('Select Recipes:', filtered_recipes, format_func=lambda x: x['name'])
                st.markdown('</div>', unsafe_allow_html=True)

                if recipe_options:
                    st.markdown('<div class="section">', unsafe_allow_html=True)
                    show_recipe_details(recipe_options)
                    st.markdown('</div>', unsafe_allow_html=True)
                    st.markdown('<div class="section">', unsafe_allow_html=True)
                    show_nutrition_info(recipe_options)
                    st.markdown('</div>', unsafe_allow_html=True)
                    st.markdown('<div class="section">', unsafe_allow_html=True)
                    generate_diet_suggestions(recipe_options)
                    st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="section">No matching recipes found after filtering allergens.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="section">No matching recipes found.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="section">Please complete the initial setup by providing user information and ingredients.</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

def load_user_information():
    try:
        with open('user_information.txt', 'r') as file:
            user_info = file.read().split(',')
            name = user_info[0].strip()
            aller_ingredient = eval(user_info[1])
            return name, aller_ingredient
    except FileNotFoundError:
        return None

def get_user_information():
    name = st.text_input('Please input your name:')
    aller_ingredient = st.multiselect(
        'allergenic source:',
        options=['egg', 'fish', 'nuts', 'tomato', 'potato'],
        default=[]
    )
    if st.button('Submit User Information'):
        if not name.strip():
            st.error('Please input a name!')
        else:
            return name, aller_ingredient
    return None

def save_user_information(user_info):
    with open('user_information.txt', 'w') as file:
        file.write(f'{user_info[0]},{user_info[1]}')

def load_fridge_ingredients():
    try:
        with open('fridge_ingredients.txt', 'r') as file:
            ingredients = file.read().split(',')
            return [ingredient.strip().lower() for ingredient in ingredients if ingredient.strip()]
    except FileNotFoundError:
        return []

def get_ingredients():
    ingredients_input = st.text_input('Please input ingredients, separated by commas (e.g., milk, eggs, sugar):')
    if st.button('Submit Ingredients'):
        if ingredients_input:
            ingredients = [ingredient.strip().lower() for ingredient in ingredients_input.split(',')]
            return ingredients
        else:
            st.error('Please input some ingredients before submitting.')
    return None

def save_fridge_ingredients(ingredients):
    with open('fridge_ingredients.txt', 'w') as file:
        file.write(', '.join(ingredients))

def show_recipe_details(selected_recipes):
    st.subheader("Recipe Details")
    for recipe in selected_recipes:
        st.markdown(f"<div class='subheader'>{recipe['name']}</div>", unsafe_allow_html=True)
        if 'image' in recipe:
            st.image(recipe['image'], caption=recipe['name'], width=300)  # 显示图片
        st.write("Ingredients:")
        st.markdown(f"<ul><li>{'</li><li>'.join(recipe['ingredients'])}</li></ul>", unsafe_allow_html=True)
        st.write("Cooking Instructions:")
        instructions = recipe['instructions'].replace("\n", "<br>")
        st.markdown(f"""<p>{instructions}</p>""", unsafe_allow_html=True)

def show_nutrition_info(selected_recipes):
    st.subheader("Nutrition Information")
    total_nutrition = pd.DataFrame([{
        "Calories": recipe.get('calories', 0),
        "Protein (g)": recipe['nutrition'].get('protein', 0),
        "Carbs (g)": recipe['nutrition'].get('carbs', 0)
    } for recipe in selected_recipes]).sum()

    st.write("Total Nutrition from selected recipes:")
    st.dataframe(total_nutrition)

    if not total_nutrition.empty:
        # 绘制饼图
        fig, ax = plt.subplots()
        ax.pie([total_nutrition['Protein (g)'], total_nutrition['Carbs (g)']], labels=['Protein', 'Carbs'], autopct='%1.1f%%')
        st.pyplot(fig)

def generate_diet_suggestions(selected_recipes):
    st.subheader("Dietary Suggestions")
    total_calories = sum(recipe['calories'] for recipe in selected_recipes)
    total_protein = sum(recipe['nutrition'].get('protein', 0) for recipe in selected_recipes)
    total_carbs = sum(recipe['nutrition'].get('carbs', 0) for recipe in selected_recipes)
    total_vitamins = set()
    for recipe in selected_recipes:
        vitamins = recipe['nutrition'].get('vitamins', "").split(", ")
        total_vitamins.update(vitamins)

    if total_calories < 500:
        st.markdown("**Suggestion**: Your meal contains less than 500 calories. Consider consuming more energy.")
    elif total_calories > 700:
        st.markdown("**Suggestion**: Your meal contains more than 700 calories. Consider consuming less energy.")

    if total_carbs < total_protein or total_carbs < total_protein * 2:
        st.markdown("**Suggestion**: Your carbohydrate intake is low. Consider consuming more carbohydrates.")
    if total_protein < total_carbs or total_protein < total_carbs / 2:
        st.markdown("**Suggestion**: Your protein intake is low. Consider consuming more protein.")

    required_vitamins = {"Vitamin A", "Vitamin B", "Vitamin C"}
    missing_vitamins = required_vitamins - total_vitamins
    if missing_vitamins:
        st.markdown(f"**Suggestion**: You need to intake the following vitamins: {', '.join(missing_vitamins)}")

if __name__ == "__main__":
    main()
