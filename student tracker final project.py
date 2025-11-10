import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# ----------------- Student Data -----------------
students = [
    {"name": "Reshma", "roll": 101, "section": "A", "telugu": 88, "hindi": 90, "science": 85, "maths": 92},
    {"name": "Chitti", "roll": 102, "section": "A", "telugu": 75, "hindi": 80, "science": 78, "maths": 70},
    {"name": "Govardhini", "roll": 103, "section": "B", "telugu": 65, "hindi": 60, "science": 68, "maths": 72},
    {"name": "Aparna", "roll": 104, "section": "B", "telugu": 45, "hindi": 50, "science": 55, "maths": 52},
    {"name": "Renuka", "roll": 105, "section": "C", "telugu": 35, "hindi": 40, "science": 42, "maths": 38}
]

teacher_credentials = {"username": "teacher", "password": "1234"}

# ----------------- Helper Functions -----------------
def get_feedback(mark):
    if mark >= 90:
        return "🌟 Excellent"
    elif mark >= 75:
        return "👍 Very Good"
    elif mark >= 60:
        return "🙂 Good"
    elif mark >= 40:
        return "⚠️ Needs Improvement"
    else:
        return "❌ Poor"

def star_rating(avg):
    stars = int(avg // 20)
    return "⭐" * stars + "☆" * (5 - stars)

def calculate_results(student):
    total = student["telugu"] + student["hindi"] + student["science"] + student["maths"]
    avg = total / 4
    if avg >= 90:
        grade = "A+"
        feedback = "Outstanding performance! Keep it up!"
    elif avg >= 75:
        grade = "A"
        feedback = "Very good work!"
    elif avg >= 60:
        grade = "B"
        feedback = "Good, can do even better."
    elif avg >= 40:
        grade = "C"
        feedback = "Needs improvement."
    else:
        grade = "F"
        feedback = "Fail — must work hard!"
    return total, avg, grade, feedback

# ----------------- Page Functions -----------------
def open_login_page():
    clear_window()
    title = tk.Label(window, text="LOGIN PORTAL", font=("Arial", 20, "bold"), bg="#4682B4", fg="white", pady=10)
    title.pack(fill="x", pady=(0, 20))

    tk.Button(window, text="👨‍🏫 Teacher Login", font=("Arial", 13, "bold"), bg="#5DADE2", fg="white",
              command=teacher_login_page, width=20).pack(pady=10)
    tk.Button(window, text="👩‍🎓 Student Login", font=("Arial", 13, "bold"), bg="#58D68D", fg="white",
              command=student_login_page, width=20).pack(pady=10)

def student_login_page():
    clear_window()
    tk.Label(window, text="Student Login", font=("Arial", 20, "bold"), bg="#4682B4", fg="white", pady=10).pack(fill="x")

    tk.Label(window, text="Name:", font=("Arial", 13, "bold"), bg="#F0F8FF").pack(pady=5)
    entry_name = tk.Entry(window, font=("Arial", 13))
    entry_name.pack(pady=5)

    tk.Label(window, text="Roll Number:", font=("Arial", 13, "bold"), bg="#F0F8FF").pack(pady=5)
    entry_roll = tk.Entry(window, font=("Arial", 13))
    entry_roll.pack(pady=5)

    def login_action():
        name = entry_name.get().strip().capitalize()
        roll = entry_roll.get().strip()
        if not roll.isdigit():
            messagebox.showerror("Error", "Roll number must be numeric.")
            return
        roll = int(roll)
        for s in students:
            if s["name"] == name and s["roll"] == roll:
                show_student_dashboard(s)
                return
        messagebox.showerror("Login Failed", "Invalid Name or Roll Number.")

    tk.Button(window, text="Login", font=("Arial", 13, "bold"), bg="#4682B4", fg="white",
              command=login_action).pack(pady=15)
    tk.Button(window, text="🔙 Back", font=("Arial", 12, "bold"), bg="#B0C4DE", command=open_login_page).pack()

def teacher_login_page():
    clear_window()
    tk.Label(window, text="Teacher Login", font=("Arial", 20, "bold"), bg="#4682B4", fg="white", pady=10).pack(fill="x")

    tk.Label(window, text="Username:", font=("Arial", 13, "bold"), bg="#F0F8FF").pack(pady=5)
    entry_user = tk.Entry(window, font=("Arial", 13))
    entry_user.pack(pady=5)

    tk.Label(window, text="Password:", font=("Arial", 13, "bold"), bg="#F0F8FF").pack(pady=5)
    entry_pass = tk.Entry(window, font=("Arial", 13), show="*")
    entry_pass.pack(pady=5)

    def teacher_login_action():
        user = entry_user.get()
        pw = entry_pass.get()
        if user == teacher_credentials["username"] and pw == teacher_credentials["password"]:
            show_teacher_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid Teacher Credentials.")

    tk.Button(window, text="Login", font=("Arial", 13, "bold"), bg="#4682B4", fg="white",
              command=teacher_login_action).pack(pady=15)
    tk.Button(window, text="🔙 Back", font=("Arial", 12, "bold"), bg="#B0C4DE", command=open_login_page).pack()

# ----------------- Dashboards -----------------
def show_student_dashboard(student):
    clear_window()

    total, avg, grade, overall_feedback = calculate_results(student)

    # Header
    header = tk.Label(window, text="STUDENT PERFORMANCE DASHBOARD", font=("Arial", 18, "bold"),
                      bg="#4682B4", fg="white", pady=10)
    header.pack(fill="x")

    info = f"Name: {student['name']}     Section: {student['section']}     Roll No: {student['roll']}"
    tk.Label(window, text=info, font=("Arial", 13, "bold"), bg="#D6EAF8").pack(fill="x", pady=(10, 5))

    # Table Header
    table_frame = tk.Frame(window, bg="#F0F8FF")
    table_frame.pack(pady=10)

    headers = ["Subject", "Marks", "Feedback"]
    for col, h in enumerate(headers):
        tk.Label(table_frame, text=h, font=("Arial", 13, "bold"), bg="#AED6F1", width=15, relief="ridge").grid(row=0, column=col)

    subjects = ["Telugu", "Hindi", "Science", "Maths"]
    marks = [student["telugu"], student["hindi"], student["science"], student["maths"]]

    for i, (sub, mark) in enumerate(zip(subjects, marks), start=1):
        tk.Label(table_frame, text=sub, font=("Arial", 12), bg="#EBF5FB", width=15, relief="ridge").grid(row=i, column=0)
        tk.Label(table_frame, text=mark, font=("Arial", 12), bg="#EBF5FB", width=15, relief="ridge").grid(row=i, column=1)
        tk.Label(table_frame, text=get_feedback(mark), font=("Arial", 12), bg="#EBF5FB", width=25, relief="ridge").grid(row=i, column=2)

    # Overall Performance
    performance = (
        f"\nTotal Marks: {total}\nAverage: {avg:.2f}\nGrade: {grade}\nRating: {star_rating(avg)}\nFeedback: {overall_feedback}"
    )
    tk.Label(window, text="Overall Performance", font=("Arial", 14, "bold"), bg="#D6EAF8").pack(fill="x", pady=(10, 0))
    tk.Label(window, text=performance, font=("Arial", 12), bg="#F0F8FF", justify="left").pack()

    # Graph at bottom
    subjects = ["Telugu", "Hindi", "Science", "Maths"]
    plt.clf()
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.bar(subjects, marks, color=["#3498DB", "#5DADE2", "#76D7C4", "#F7DC6F"])
    ax.set_ylim(0, 100)
    ax.set_ylabel("Marks")
    ax.set_title(f"{student['name']}'s Subject-wise Performance")
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

    tk.Button(window, text="🚪 Logout", font=("Arial", 12, "bold"), bg="#E74C3C", fg="white",
              command=open_login_page).pack(pady=10)

def show_teacher_dashboard():
    clear_window()
    tk.Label(window, text="TEACHER DASHBOARD", font=("Arial", 18, "bold"), bg="#4682B4", fg="white", pady=10).pack(fill="x")

    table_frame = tk.Frame(window, bg="#F0F8FF")
    table_frame.pack(pady=10)

    headers = ["Roll No", "Name", "Section", "Total", "Average", "Grade", "Rating"]
    for col, h in enumerate(headers):
        tk.Label(table_frame, text=h, font=("Arial", 13, "bold"), bg="#AED6F1", width=12, relief="ridge").grid(row=0, column=col)

    for i, s in enumerate(students, start=1):
        total, avg, grade, _ = calculate_results(s)
        data = [s["roll"], s["name"], s["section"], total, f"{avg:.2f}", grade, star_rating(avg)]
        for j, val in enumerate(data):
            tk.Label(table_frame, text=val, font=("Arial", 12), bg="#EBF5FB", width=12, relief="ridge").grid(row=i, column=j)

    tk.Button(window, text="🚪 Logout", font=("Arial", 12, "bold"),
              bg="#E74C3C", fg="white", command=open_login_page).pack(pady=10)

# ----------------- Utility -----------------
def clear_window():
    for widget in window.winfo_children():
        widget.destroy()
    window.config(bg="#F0F8FF")

# ----------------- Main Window -----------------
window = tk.Tk()
window.title("🎓 Student Assessment and Tracker")
window.geometry("950x650")
window.config(bg="#F0F8FF")

open_login_page()
window.mainloop()
