import re
import json
import random


def check_password_strength(password):
    """Check the strength of a given password."""
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Calculate the score based on criteria met
    score = sum([has_upper, has_lower, has_digit, has_special])
    strength = {
        4: "Strong",
        3: "Good",
        2: "Moderate",
        1: "Weak",
        0: "Very Weak"
    }
    return strength.get(score, "Very Weak")

def recommended(): # Open a word list and select 3 random words to make up a password
    with open('words.json') as file:
        data = json.load(file)

    words = list(data.keys())
    selected_words = random.sample(words, 3)
    output = []
    output.extend(selected_words)

    # Add 3 random numbers to the password
    for _ in range(3):
        randnum = random.randint(0, 9)
        output.extend(str(randnum))

    # Add a random symbol to the password
    symbols = "~!@#$%^&*.:;"
    symbol = random.choice(symbols)
    output.extend(symbol)

    print(''.join(output))


def main():
    """Main function to enforce password length and check strength."""
    min_length = 8  # Minimum password length requirement

    while True:
        user_password = input(f"Enter a password (minimum {min_length} characters): ")
        if len(user_password) < min_length:
            print(f"Password must be at least {min_length} characters long. Please try again.")
        else:
            break

    strength = check_password_strength(user_password)
    print(f"The password '{user_password}' is {strength}.")

    if strength not in ["Strong", "Good"]: # If the pw is moderate or worse
        print("Here is a recommended password:", end=" ")
        recommended()


if __name__ == "__main__":
    main()