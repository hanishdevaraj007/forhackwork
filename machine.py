import streamlit as st

st.title("Computer Guesses the Number (Binary Search)")

if 'lower_bound' not in st.session_state:
    st.session_state.lower_bound = 1  
    st.session_state.upper_bound = 100  
    st.session_state.guess = (st.session_state.lower_bound + st.session_state.upper_bound) // 2


def update_computer_guess(feedback):
    if feedback == "Too low":
        st.session_state.lower_bound = st.session_state.guess + 1
    elif feedback == "Too high":
        st.session_state.upper_bound = st.session_state.guess - 1
    elif feedback == "Correct":
        st.write(f"Yay! I guessed your number: {st.session_state.guess}!")
        return True
    
    st.session_state.guess = (st.session_state.lower_bound + st.session_state.upper_bound) // 2
    return False


st.write(f"Think of a number between {st.session_state.lower_bound} and {st.session_state.upper_bound}.")
st.write("The computer will try to guess your number using binary search.")
st.write("After each guess, please tell the computer if the guess is 'Too low', 'Too high', or 'Correct'.")

st.write(f"My guess is: {st.session_state.guess}")

feedback = st.radio("Is my guess:", ("Too low", "Too high", "Correct"))

if st.button("Submit Feedback"):
    
    game_over = update_computer_guess(feedback)

    if game_over:
        st.write("I guessed it! You can continue or think of a new number.")
    else:
        st.write("Let me try again with a new guess!")


st.write(f"Current range: {st.session_state.lower_bound} - {st.session_state.upper_bound}")