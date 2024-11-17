import streamlit as st

# Set the title of the app
st.title("Computer Guesses the Number (Binary Search)")

# Initialize session state variables
if 'lower_bound' not in st.session_state:
    st.session_state.lower_bound = 1  # Starting lower bound
    st.session_state.upper_bound = 100  # Starting upper bound
    st.session_state.guess = (st.session_state.lower_bound + st.session_state.upper_bound) // 2

# Function to update the computer's guess using binary search
def update_computer_guess(feedback):
    if feedback == "Too low":
        st.session_state.lower_bound = st.session_state.guess + 1
    elif feedback == "Too high":
        st.session_state.upper_bound = st.session_state.guess - 1
    elif feedback == "Correct":
        st.write(f"Yay! I guessed your number: {st.session_state.guess}!")
        return True
    # Update guess based on new bounds (binary search)
    st.session_state.guess = (st.session_state.lower_bound + st.session_state.upper_bound) // 2
    return False

# Display instructions
st.write(f"Think of a number between {st.session_state.lower_bound} and {st.session_state.upper_bound}.")
st.write("The computer will try to guess your number using binary search.")
st.write("After each guess, please tell the computer if the guess is 'Too low', 'Too high', or 'Correct'.")

# Display the computer's guess
st.write(f"My guess is: {st.session_state.guess}")

# Feedback input
feedback = st.radio("Is my guess:", ("Too low", "Too high", "Correct"))

# Handle the user's feedback
if st.button("Submit Feedback"):
    # Update the computer's guess based on user feedback
    game_over = update_computer_guess(feedback)

    if game_over:
        st.write("I guessed it! You can continue or think of a new number.")
    else:
        st.write("Let me try again with a new guess!")

# Display current guess range
st.write(f"Current range: {st.session_state.lower_bound} - {st.session_state.upper_bound}")