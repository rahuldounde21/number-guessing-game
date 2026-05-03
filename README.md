# 🎯 Number Guessing Game

A fun, beginner-friendly command-line game built with pure Python.
The computer secretly picks a number — your job is to guess it with as few tries as possible!

---

## 📋 Description

Number Guessing Game is a terminal-based game where the computer randomly
selects a number between 1 and 100. After every guess you receive a hint
("Too high" or "Too low") to help you zero in on the answer. At the end,
your attempt count is shown along with a fun performance rating.
The game then asks if you want to play again — all without restarting the program.

---

## ✨ Features

- 🎲 **Random number** — A new secret number (1–100) is chosen every round
- 📉 **"Too low" hint** — Your guess is below the secret number
- 📈 **"Too high" hint** — Your guess is above the secret number
- 🎉 **Correct guess** — Celebration message with your attempt count
- 🌟 **Performance rating** — Fun feedback based on how many tries you used
- 🛡️ **Input validation** — Letters, symbols, and blank entries are handled gracefully
- ⚠️  **Range check** — Warns if guess is outside 1–100 without wasting an attempt
- 🔄 **Play again** — Instantly starts a fresh round without restarting the program

---

## ▶️ How to Run

**Step 1 — Check that Python is installed**

Open your terminal (Command Prompt on Windows, Terminal on Mac/Linux) and run:
```
python --version
```
You should see `Python 3.x.x`. If not, download Python from https://python.org.

**Step 2 — Save the file**

Download or copy `guessing_game.py` into any folder, for example your Desktop.

**Step 3 — Navigate to that folder**

```
cd Desktop
```

**Step 4 — Run the game**

```
python guessing_game.py
```

**Step 5 — Play!**

- Read the hint after each guess.
- Type a new number and press **Enter**.
- Keep going until you find the secret number.
- When asked "Play again?", type `yes` or `no`.

---

## 💻 Example Output

```
========================================
     🎯  NUMBER GUESSING GAME  🎯
========================================
  I'm thinking of a number between
  1 and 100. Can you guess it?
========================================

  🎲 A new number has been chosen. Good luck!

  👉 Enter your guess: hello
  ⚠  Invalid input! Please enter a whole number.

  👉 Enter your guess: 50
  📈 Too high! Try a lower number.

  👉 Enter your guess: 25
  📉 Too low!  Try a higher number.

  👉 Enter your guess: 37
  📉 Too low!  Try a higher number.

  👉 Enter your guess: 43
  📈 Too high! Try a lower number.

  👉 Enter your guess: 40
  ────────────────────────────────────
  🎉 Correct! The number was 40.
  🏁 You guessed it in 5 attempt(s).
  👏 Great job — very few tries!
  ────────────────────────────────────

  🔄 Play again? (yes / no): no

  Thanks for playing! See you next time. 👋
```

---

## 🛠️ Technologies Used

Only Python 3 built-ins — nothing to install with pip:

| Concept         | Where it's used                                           |
|-----------------|-----------------------------------------------------------|
| `import random` | Generates the secret number with `randint(1, 100)`        |
| `functions`     | Each responsibility lives in its own named function       |
| `while` loop    | Keeps guessing / play-again loops running                 |
| `if-elif-else`  | Decides which hint to show and whether guess is correct   |
| `try-except`    | Catches non-numeric input without crashing                |
| `input/print`   | All player interaction and feedback                       |
| `variables`     | Stores secret number, attempts count, and answers         |
| `f-strings`     | Clean, readable output formatting                         |
| Constants       | `MIN_NUMBER` / `MAX_NUMBER` make the range easy to change |

---

## 🚀 Bonus — Improvements to Try

Here are **3 beginner-friendly upgrades** to challenge yourself:

---

**1. 🎚️ Difficulty Levels**

Before each round, ask the player to choose a difficulty that changes the range:

```python
def choose_difficulty():
    print("Choose difficulty:")
    print("  1. Easy   (1 – 50)")
    print("  2. Medium (1 – 100)")
    print("  3. Hard   (1 – 200)")
    choice = input("Enter 1, 2, or 3: ").strip()
    if choice == "1":
        return 1, 50
    elif choice == "3":
        return 1, 200
    else:
        return 1, 100   # Default to Medium
```

---

**2. ⏱️ Limited Attempts**

Give the player a fixed number of chances (e.g. 7). If they run out, reveal the answer:

```python
MAX_ATTEMPTS = 7

while attempts < MAX_ATTEMPTS:
    guess = get_guess()
    attempts += 1
    remaining = MAX_ATTEMPTS - attempts
    print(f"  Attempts remaining: {remaining}")
    if give_hint(guess, secret_number):
        print("🎉 You win!")
        break
else:
    print(f"💀 Out of attempts! The number was {secret_number}.")
```

---

**3. 🏆 Score System**

Track a running score across rounds. Award more points for fewer attempts:

```python
total_score = 0

# After each win:
bonus = max(0, 100 - (attempts - 1) * 10)
total_score += bonus
print(f"  ⭐ Points this round : {bonus}")
print(f"  🏆 Total score so far: {total_score}")
```

Fewer guesses = more points. Try to beat your own high score!

---

## 👤 Author

Built as a beginner Python learning project.
Experiment freely — change the range, add features, and make it your own!
