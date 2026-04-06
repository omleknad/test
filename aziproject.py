
import streamlit as st


st.snow()
st.title("Welcome to my Hangman Game: MONTHSARY EDITION <3")
st.write("love, your matty <3")
st.image("https://i.postimg.cc/Kv77W0rc/bcc0582f-c8ea-4d88-983e-469cea2c396d.jpg", width=1000)
st.sidebar.title("About This Game")
st.sidebar.info("The rules are that you just need to guess the word through entering one letter at a time and you have 10 guesses for each word! If you guess the word correctly then you will get a message relating to the word you guessed hehe. I hope you enjoy the game!")
st.sidebar.image("https://i.postimg.cc/9M4tNVJZ/0a4fbfde-d3db-43b9-b193-48ea6b2846d3.jpg", width=1000)

# Dictionary of words and their messages
words = {
    "motivating": "you always motivate me to do better and you are da best cheerleader ever ><",
    "lovely": "you are so beautiful i can never take my eyes off you <33",
    "thoughtful": "i always feel your efforts and you are always thinking of me and i appreciate it hehe",
    "caring": "i love that you are always making sure im healthy and getting enough rest ",
    "hardworking": "i love how hardworking you are and it really inspires me to always do better ><",
    "supportive": "whenever i feel like i am having a tough time you are always there to support me and keep me going ",
    "optimistic": "you are always the ray of sunlight that keeps me positive and help me think more positively hehe",
    "cute": "you are sososososo cute i wanna keep squishing your cheeks my rabbit ><",
    "creative": "i love how creative you are from the gifts that you make and from the drawings and even builds in any game we play together <33",
    "sweet": "having a pleasant taste or being kind and gentle",
    "fashionista": "a person who is very interested in fashion and follows the latest trends"
}

def hangman():
    # Initialize session state variables
    if 'i' not in st.session_state:
        st.session_state.i = 0
    if 'num_guesses' not in st.session_state:
        st.session_state.num_guesses = 10
    if 'guessed_letters' not in st.session_state:
        st.session_state.guessed_letters = set()

    i = st.session_state.i
    num_guesses = st.session_state.num_guesses
    guessed_letters = st.session_state.guessed_letters

    word_keys = list(words.keys())
    total_words = len(word_keys)
    if i >= total_words:
        st.write("You've completed all words! 🎉")
        st.balloons()   
        st.progress(1.0, text="All words completed!")
        return

    # Progress bar for words completed
    st.progress(i / total_words, text=f"Words completed: {i} / {total_words}")
    st.write("Welcome to Hangman!")
    st.write("Guess the word!")
    word = word_keys[i]
    # Display the word with guessed letters (always visible)
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    st.write(display_word.strip())
    st.write(f"You have {num_guesses} guesses left.")
    st.write(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

    # Only process guess if not already won/lost
    if all(letter in guessed_letters for letter in word):
        st.write(f"Congratulations! You guessed the word: '{word}'!")
        st.success(f"Reward Message <3: {words[word]}")
        st.balloons()
        if st.button("Next word"):
            st.session_state.i += 1
            st.session_state.num_guesses = 10
            st.session_state.guessed_letters = set()
            st.rerun()
        return
    elif num_guesses == 0:
        st.write(f"Game over! The word was '{word}'.")
        if st.button("Try again?"):
            st.session_state.num_guesses = 10
            st.session_state.guessed_letters = set()
            st.rerun()
        elif st.button("Next word"):
            st.session_state.i += 1
            st.session_state.num_guesses = 10
            st.session_state.guessed_letters = set()
            st.rerun()
        return

    # Guess input outside form, only process on button click
    guess_key = f"guess_{i}_{num_guesses}"
    guess = st.text_input("Enter a letter:", key=guess_key)
    guess_button = st.button("Guess", key=f"guess_button_{i}_{num_guesses}")

    if guess_button and guess:
        guess = guess.lower()
        if guess in guessed_letters:
            st.write(f"You already guessed '{guess}'. Try a different letter.")
        elif guess in word:
            guessed_letters.add(guess)
            st.session_state.guessed_letters = guessed_letters
            st.write(f"Good guess! '{guess}' is in the word.")
        else:
            guessed_letters.add(guess)
            st.session_state.num_guesses -= 1
            st.write(f"Wrong guess. '{guess}' is not in the word.")
            

hangman()



