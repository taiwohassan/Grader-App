# Get the user's name and convert it to uppercase
name = input("Enter your name: ").strip().upper()

print(f"Welcome {name}, let's calculate your percentage score!")

# Input scores for each subject with validation
try:
    maths = int(input("Enter your Maths score: "))
    english = int(input("Enter your English score: "))
    physics = int(input("Enter your Physics score: "))
    chemistry = int(input("Enter your Chemistry score: "))

    # Ensure all scores are within the valid range
    if any(score < 0 or score > 100 for score in [maths, english, physics, chemistry]):
        print("Error: All scores must be between 0 and 100.")
    else:
        # Calculate total and percentage score
        total_score = maths + english + physics + chemistry
        percentage = (total_score / 400) * 100

        print(f"\nYour total score is {total_score}/400.")
        print(f"And your percentage is {percentage:.2f}%.\n")

        # Assign grades based on percentage
        if percentage >= 90:
            grade = "A1"
        elif 70 <= percentage < 90:
            grade = "B2"
        elif 60 <= percentage < 70:
            grade = "C4"
        elif 50 <= percentage < 60:
            grade = "C6"
        else:
            grade = "F (Fail)"

        print(f"Congratulations, {name}! You achieved grade {grade}!")
except ValueError:
    print("Error: Please enter valid integer scores.")
