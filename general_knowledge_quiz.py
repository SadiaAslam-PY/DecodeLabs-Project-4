# Project 4
# The General Knowledge Quiz

# Initialise the score
score = 0

print("=" * 50)
print("       GENERAL KNOWLEDGE QUIZ")
print("=" * 50)
print("Answer the following 3 questions.")
print("Each correct answer gives you 1 point.")
print()

# Question 1
question1 = input("1. What is the capital of France? ")

# Sanitise user input
answer1 = question1.strip().lower()

if answer1 == "paris":
    score += 1
    print("Correct! You earned 1 point.")
else:
    print("Incorrect. The correct answer is Paris.")

print()

# Question 2
question2 = input("2. Which planet is known as the Red Planet? ")

# Sanitise user input
answer2 = question2.strip().lower()

if answer2 == "mars":
    score += 1
    print("Correct! You earned 1 point.")
else:
    print("Incorrect. The correct answer is Mars.")

print()

# Question 3
question3 = input("3. How many continents are there in the world? ")

# Sanitise user input
answer3 = question3.strip().lower()

if answer3 == "7" or answer3 == "seven":
    score += 1
    print("Correct! You earned 1 point.")
else:
    print("Incorrect. The correct answer is 7.")

print()

# Display final score
print("=" * 50)
print(f"FINAL SCORE: {score}/3")
print("=" * 50)

# Final performance message
if score == 3:
    print("Excellent! You answered all questions correctly.")
elif score == 2:
    print("Great job! You got most of the questions correct.")
elif score == 1:
    print("Good effort! Keep practising your general knowledge.")
else:
    print("Keep learning and try the quiz again!")

print("Thank you for playing!")