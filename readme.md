### README: Student Grade Calculator

#### Overview
The **Student Grade Calculator** is a Python script designed to calculate the percentage and grade of a student based on their scores in four subjects: Maths, English, Physics, and Chemistry. It ensures accurate grading and validates user inputs for correctness.

---

#### Features
1. **Input Validation**:
   - Ensures all scores are valid integers.
   - Verifies scores fall within the range of 0 to 100.

2. **Percentage Calculation**:
   - Calculates the total score and determines the percentage.

3. **Grade Assignment**:
   - Grades are assigned based on the percentage:
     - **A1**: 90% and above
     - **B2**: 70% - 89%
     - **C4**: 60% - 69%
     - **C6**: 50% - 59%
     - **F (Fail)**: Below 50%

4. **Personalized Messages**:
   - Displays personalized messages using the student's name.

---

#### Requirements
- Python 3.x must be installed on your system.

---

#### How to Use
1. **Clone or Download the Script**:
   - Save the script in a `.py` file, e.g., `grade_calculator.py`.

2. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is saved.
   - Run the script using:
     ```bash
     python grade_calculator.py
     ```

3. **Enter Inputs**:
   - Enter the student's name.
   - Input scores for Maths, English, Physics, and Chemistry when prompted.

4. **View Results**:
   - The script will display the total score, percentage, and grade.

---

#### Example Output
##### Valid Input:
```plaintext
Enter your name: Akinyemi Taiwo
Welcome AKINYEMI TAIWO, let's calculate your percentage score!
Enter your Maths score: 85
Enter your English score: 90
Enter your Physics score: 70
Enter your Chemistry score: 75

Your total score is 320/400.
And your percentage is 80.00%.

Congratulations, AKINYEMI TAIWO! You achieved grade B2!
```

##### Invalid Input:
```plaintext
Enter your name: Akinyemi Taiwo
Welcome AKINYEMI TAIWO, let's calculate your percentage score!
Enter your Maths score: 110
Enter your English score: 90
Enter your Physics score: 70
Enter your Chemistry score: 75
Error: All scores must be between 0 and 100.
```

---

#### Code Explanation
1. **Input Handling**:
   - Accepts student name and scores for four subjects.
   - Validates input to ensure correctness.

2. **Score and Percentage Calculation**:
   - Computes the total score and percentage using the formula:
     ```
     percentage = (total_score / 400) * 100
     ```

3. **Grade Assignment**:
   - Uses conditional statements to assign grades based on percentage ranges.

4. **Output Formatting**:
   - Results are displayed with meaningful and personalized messages.

---

#### Customization
- Add more subjects by including additional input prompts and updating the total score calculation.
- Modify the grade boundaries to match different grading systems.
- Improve the script by saving the results to a file or database for record-keeping.

---

#### Notes
- The program ensures robust error handling for invalid inputs.
- All outputs are user-friendly and formatted for clarity.

Enjoy using the **Student Grade Calculator**! 🎉