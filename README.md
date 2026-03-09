# Student Report Card Generator (GUI)

A simple, user-friendly desktop application built with Python and Tkinter to generate digital report cards. The system calculates totals, percentages, and letter grades based on student marks across multiple subjects.

---

## 📄 Overview

The **Student Report Card Generator** is a tool designed for teachers and educational administrators to quickly generate a summary of a student's academic performance. It takes student details and marks for five core subjects, then instantly computes the final result in a clear, formatted display.

## 🚀 Key Features

* **Intuitive Data Entry:** Form-based input for student name, roll number, and course.
* **Automatic Grade Calculation:** Features a built-in logic to assign letter grades (A+ to F) based on the calculated percentage.
* **Dynamic Calculations:** Automatically computes the total marks and the overall percentage.
* **Input Validation:** * Checks for missing data before generating results.
* Validates that marks are numeric and stay within the 0–100 range.


* **Keyboard Navigation:** Supports the `Enter` key to move focus between input fields for faster data entry.
* **Instant Result Preview:** Displays the final report card within a scrollable text area for easy review.

## 🛠️ Technology Stack

* **Language:** Python 3.x
* **GUI Framework:** `tkinter`
* **Internal Logic:** Custom algorithms for grading and arithmetic operations.

## ⚙️ Logic & Grading Scale

The system uses the following grading criteria:

* **90% - 100%**: A+
* **80% - 89%**: A
* **70% - 79%**: B
* **60% - 69%**: C
* **50% - 59%**: D
* **Below 50%**: F (Fail)

## 🖥️ Subjects Included

1. Python
2. Data Visualization
3. Descriptive Analysis
4. NodeMCU (IoT)
5. Summer Training

## 🔧 Installation & Usage

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/report-card-generator.git

```


2. **Run the application:**
```bash
python report_card.py

```


3. **Generate a Report:**
* Enter student details.
* Enter marks (out of 100) for all five subjects.
* Click **Generate** to see the results.
* Click **Clear** to reset the form for the next student.



## 📈 Future Enhancements

* **Export to PDF:** Ability to save the generated report card as a PDF file.
* **Database Integration:** Save student results to an SQLite database for long-term record keeping.
* **Custom Subjects:** Allow users to add or remove subjects dynamically.
* **Theme Support:** Add dark mode or custom color schemes to the UI.
