# Number Guessing Game (Python)

This is a simple Python-based number guessing game where the computer randomly selects a number between 1 and 100, and the player tries to guess it within a limited number of attempts. The number of attempts depends on the difficulty level chosen at the beginning of the game.

---

## Project Link
Project link here:
https://roadmap.sh/projects/number-guessing-game


---

## Description

The game begins by asking the user to select a difficulty level. Each level provides a different number of chances:

Easy: 10 attempts

Medium: 5 attempts

Hard: 3 attempts


After selecting a level, the player begins guessing numbers. The program gives hints such as whether the correct number is higher or lower than the player’s guess. The game also tracks how long the player takes to finish and how many attempts they use.

If the player guesses correctly within the allowed attempts, the game displays a success message along with the time taken. If not, it reveals the correct answer at the end.


---

## How to Run the Game

1. Download or clone the project:
git clone [https://github.com/arjuncodelab/python-project]
2. Navigate to the project folder:
cd Beginner/Guessing Game

3. Run the script using Python:
python guessing_game.py


---

## Features

- Three difficulty levels with different attempt limits
- Hints provided after every incorrect guess
- Tracks number of attempts used
- Displays time taken to complete the game
- Handles invalid inputs (non-numeric entries or values outside 1–100)

---

## Example Game Flow

Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter Your Choice: easy
Great! You have selected the easy difficulty level.
You have 10 chances.

Enter Your Guess: 50
Incorrect! The number is smaller than 50. Try again.


---

## Requirements

Python 3.x
(No external libraries are required.)

---

## About This Project

This is one of my early beginner-level Python projects. I will continue updating this repository with new projects as I learn more.
