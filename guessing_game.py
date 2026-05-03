# ============================================================
#  Number Guessing Game — A beginner-friendly CLI game
#  The computer picks a number (1–100). Can you guess it?
# ============================================================

import random  # Only external module used — part of Python's standard library


# ── Constants ─────────────────────────────────────────────────
MIN_NUMBER = 1
MAX_NUMBER = 100


# ── Helper Functions ──────────────────────────────────────────

def show_banner():
    """Print the welcome banner at the start."""
    print("\n" + "=" * 40)
    print("     🎯  NUMBER GUESSING GAME  🎯")
    print("=" * 40)
    print(f"  I'm thinking of a number between")
    print(f"  {MIN_NUMBER} and {MAX_NUMBER}. Can you guess it?")
    print("=" * 40 + "\n")


def get_guess():
    """
    Ask the player to enter a guess.
    Keeps asking until a valid whole number is entered.
    Returns the valid integer guess.
    """
    while True:
        try:
            # Strip whitespace, then try converting to int
            guess = int(input("  👉 Enter your guess: ").strip())
            return guess
        except ValueError:
            # Runs when user types letters, symbols, or leaves it blank
            print("  ⚠  Invalid input! Please enter a whole number.\n")


def give_hint(guess, secret):
    """
    Compare the guess to the secret number and print a hint.
    Returns True if the guess is correct, False otherwise.
    """
    if guess < MIN_NUMBER or guess > MAX_NUMBER:
        # Guess is valid as a number but out of the allowed range
        print(f"  ⚠  Please guess between {MIN_NUMBER} and {MAX_NUMBER}!\n")
        return False
    elif guess < secret:
        print("  📉 Too low!  Try a higher number.\n")
        return False
    elif guess > secret:
        print("  📈 Too high! Try a lower number.\n")
        return False
    else:
        # Guess is exactly right
        return True


def ask_play_again():
    """
    Ask the player if they want to play another round.
    Returns True for yes, False for no.
    Keeps asking until a clear yes/no answer is given.
    """
    while True:
        answer = input("  🔄 Play again? (yes / no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        else:
            print("  ⚠  Please type 'yes' or 'no'.\n")


# ── Core Game Function ────────────────────────────────────────

def play_game():
    """
    Run one full round of the guessing game.
    - Picks a random secret number.
    - Loops until the player guesses correctly.
    - Shows the number of attempts at the end.
    """
    # Pick a new random number for this round
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)

    # Reset attempts counter for each fresh game
    attempts = 0

    print("\n  🎲 A new number has been chosen. Good luck!\n")

    # Keep looping until the player guesses correctly
    while True:
        guess = get_guess()
        attempts += 1          # Count every valid guess

        correct = give_hint(guess, secret_number)

        if correct:
            # Player found the number — celebrate and summarise
            print("  " + "─" * 36)
            print(f"  🎉 Correct! The number was {secret_number}.")
            print(f"  🏁 You guessed it in {attempts} attempt(s).")

            # Fun rating based on how many tries it took
            if attempts == 1:
                print("  🌟 Incredible — first try!")
            elif attempts <= 5:
                print("  👏 Great job — very few tries!")
            elif attempts <= 10:
                print("  🙂 Good effort!")
            else:
                print("  💪 You got there — keep practising!")

            print("  " + "─" * 36 + "\n")
            break   # Exit the guessing loop


# ── Main Program ──────────────────────────────────────────────

def main():
    """
    Entry point of the game.
    Shows the banner, then loops rounds until the player quits.
    """
    show_banner()

    # Keep playing as long as the player wants
    while True:
        play_game()

        if ask_play_again():
            print("\n  ✅ Starting a new game...\n")
        else:
            print("\n  Thanks for playing! See you next time. 👋\n")
            break   # Exit the play-again loop


# ── Entry Point Guard ─────────────────────────────────────────

# Runs only when this file is executed directly,
# not when imported as a module in another script.
if __name__ == "__main__":
    main()
