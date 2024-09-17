import tkinter as tk
from tkinter import messagebox

def calculate_age(current_year, birth_year):
    return current_year - birth_year

def calculate_age_in_days(age):
    return age * 365

def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_days_with_leap_years(current_year, birth_year):
    age = calculate_age(current_year, birth_year)
    leap_years = sum(1 for year in range(birth_year, current_year + 1) if leap_year(year))
    days = (age * 365) + leap_years
    return age, days

def calculate():
    try:
        current_year = int(entry_current_year.get())
        birth_year = int(entry_birth_year.get())

        if birth_year > current_year:
            messagebox.showerror("Error", "The birth year is greater than the current year.")
            return
        age = calculate_age(current_year, birth_year)
        days_without_leap_years = calculate_age_in_days(age)
        age_with_leap_years, days_with_leap_years = calculate_days_with_leap_years(current_year, birth_year)

        output_display.delete(1.0, tk.END)
        output_display.insert(tk.END, f"Your age is: {age} years\n")
        output_display.insert(tk.END, f"Age in days (without leap years): {days_without_leap_years} days\n")
        output_display.insert(tk.END, f"Age in days (with leap years): {days_with_leap_years} days\n")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

root = tk.Tk()
root.title("Age Calculator")

label_current_year = tk.Label(root, text="Current year:")
label_current_year.grid(row=0, column=0, padx=10, pady=10)

entry_current_year = tk.Entry(root)
entry_current_year.grid(row=0, column=1, padx=10, pady=10)

label_birth_year = tk.Label(root, text="Birth year:")
label_birth_year.grid(row=1, column=0, padx=10, pady=10)

entry_birth_year = tk.Entry(root)
entry_birth_year.grid(row=1, column=1, padx=10, pady=10)

btn_calculate = tk.Button(root, text="Calculate", command=calculate)
btn_calculate.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

output_display = tk.Text(root, height=6, width=40)
output_display.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
