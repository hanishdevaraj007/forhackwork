import streamlit as st
import random

# Set the title of the app
st.title("Guess the Number Game!")

# Initialize session state variables
if 'number_to_guess' not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.previous_guesses = []

# Function to give feedback on how close the guess is
def give_feedback(guess, number_to_guess):
    if guess < number_to_guess:
        return "Your guess is too low!"
    elif guess > number_to_guess:
        return "Your guess is too high!"
    else:
        return "Congratulations! You've guessed the number!"

# Game instructions
st.write("I'm thinking of a number between 1 and 100.")
st.write("Try to guess it! After each guess, I'll tell you if your guess is too high or too low.")
st.write("Keep guessing until you get it right!")

# Input field for the user's guess
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Check if the user has submitted their guess
if st.button("Submit Guess"):
    # Store previous guesses
    st.session_state.previous_guesses.append(user_guess)
    
    # Get feedback for the current guess
    feedback = give_feedback(user_guess, st.session_state.number_to_guess)
    
    # Show feedback to the user
    st.write(feedback)
    
    # If the guess is correct, offer the option to play again
    if user_guess == st.session_state.number_to_guess:
        if st.button("Play Again"):
            st.session_state.number_to_guess = random.randint(1, 100)  # Reset with a new random number
            st.session_state.previous_guesses = []  # Reset previous guesses
            st.write("A new number has been chosen! Try again!")
    
    # Display previous guesses
    st.write(f"Your previous guesses: {st.session_state.previous_guesses}")