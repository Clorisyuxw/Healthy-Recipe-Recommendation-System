import streamlit as st

def main():
    st.title('user information')

    # input name
    name = st.text_input('Please input your name:')

    #choose allergenic ingredients

    aller_ingredient = st.multiselect(
        'allergenic source:',
        options=['egg', 'fish', 'nuts', 'tomato', 'potato'],
        default=[]
    )

    # calorie

    calorie_limit = st.number_input(
        'Select calorie limit(<= 500):',
        min_value=1,)
    if st.button('submit'):
        if not name.strip():
            st.error('Please select a name!')
        else:
            user_info = f'{name},{aller_ingredient},{calorie_limit}'
            with open('user_information.txt', 'w') as infile:
                infile.write(user_info)

            st.success('Your information has been submitted successfully!')

main()