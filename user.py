import streamlit as st
import random

st.title("Guess the Number Game!")

if 'num2guess' not in st.session_state:
    st.session_state.num2guess = random.randint(1, 100)
    st.session_state.previous_guesses = []

def give_feedback(guess, num2guess):
    if guess < num2guess:
        return "Your guess is too low!"
    elif guess > num2guess:
        return "Your guess is too high!"
    else:
        return "Congratulations! You've guessed the number!"

st.write("I'm thinking of a number between 1 and 100.")
st.write("Try to guess it! After each guess, I'll tell you if your guess is too high or too low.")
st.write("Keep guessing until you get it right!")

user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)


if st.button("Submit Guess"):
    
    st.session_state.previous_guesses.append(user_guess)
    
    feedback = give_feedback(user_guess, st.session_state.num2guess)
    
    st.write(feedback)
    
    if user_guess == st.session_state.num2guess:
        if st.button("Play Again"):
            st.session_state.num2guess = random.randint(1, 100) 
            st.session_state.previous_guesses = []  
            st.write("A new number has been chosen! Try again!")
    
    st.write(f"Your previous guesses: {st.session_state.previous_guesses}")