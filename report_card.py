import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Grade Calculation
# -----------------------------
def calculate_grade(p):
    if p >= 90: return "A+"
    elif p >= 80: return "A"
    elif p >= 70: return "B"
    elif p >= 60: return "C"
    elif p >= 50: return "D"
    else: return "F"

# -----------------------------
# Generate Report
# -----------------------------
def generate_report():
    name, roll, course = name_var.get(), roll_var.get(), course_var.get()

    if not all([name, roll, course]):
        messagebox.showwarning("Missing Data", "Please fill all details.")
        return

    try:
        marks = [float(v.get()) for v in mark_vars]
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers for marks.")
        return

    if any(m < 0 or m > 100 for m in marks):
        messagebox.showerror("Error", "Marks must be between 0 and 100.")
        return

    total, percent = sum(marks), sum(marks)/len(marks)
    grade = calculate_grade(percent)

    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, f"Name: {name}\nRoll No: {roll}\nCourse: {course}\n")
    result_box.insert(tk.END, "----------------------\n")
    for s, m in zip(subjects, marks):
        result_box.insert(tk.END, f"{s}: {m}\n")
    result_box.insert(tk.END, f"----------------------\nTotal: {total}\nPercentage: {round(percent,2)}%\nGrade: {grade}")

    with open("report_cards.txt", "a") as f:
        f.write(f"{name}, {roll}, {course}, {round(percent,2)}%, {grade}\n")

    messagebox.showinfo("Done", "Report card saved successfully!")

# -----------------------------
# Clear All Fields
# -----------------------------
def clear_all():
    for v in [name_var, roll_var, course_var, *mark_vars]:
        v.set("")
    result_box.delete("1.0", tk.END)
    name_entry.focus()

# -----------------------------
# Move focus on Enter key
# -----------------------------
def focus_next(event):
    event.widget.tk_focusNext().focus()
    return "break"

# -----------------------------
# GUI Setup
# -----------------------------
root = tk.Tk()
root.title("Report Card Generator")
root.geometry("420x520")

tk.Label(root, text="Report Card Generator", font=("Arial", 16, "bold")).pack(pady=10)

# Basic Info Fields
fields = [("Name", tk.StringVar()), ("Roll No", tk.StringVar()), ("Course", tk.StringVar())]
for label, var in fields:
    tk.Label(root, text=label).pack()
    e = tk.Entry(root, textvariable=var, width=30)
    e.pack()
    e.bind("<Return>", focus_next)
name_var, roll_var, course_var = [v for _, v in fields]
name_entry = root.winfo_children()[2]  # first entry (Name)
name_entry.focus()

# Subject Marks
subjects = ["Python", "Data Visualization", "Descriptive Analysis", "NodeMCU", "Summer Training"]
tk.Label(root, text="\nEnter Marks (out of 100):", font=("Arial", 12, "bold")).pack()
mark_vars = []
for s in subjects:
    frame = tk.Frame(root)
    frame.pack()
    tk.Label(frame, text=s, width=18, anchor="e").pack(side="left")
    var = tk.StringVar()
    e = tk.Entry(frame, textvariable=var, width=10)
    e.pack(side="left")
    e.bind("<Return>", focus_next)
    mark_vars.append(var)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Generate", command=generate_report, bg="green", fg="white").pack(side="left", padx=5)
tk.Button(btn_frame, text="Clear", command=clear_all, bg="gray", fg="white").pack(side="left", padx=5)
tk.Button(btn_frame, text="Exit", command=root.destroy, bg="red", fg="white").pack(side="left", padx=5)

# Result Box
tk.Label(root, text="\nReport Output:", font=("Arial", 12, "bold")).pack()
result_box = tk.Text(root, width=48, height=10)
result_box.pack()

root.mainloop()
