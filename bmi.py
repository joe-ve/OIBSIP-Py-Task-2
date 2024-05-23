import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight < 10 or weight > 300:
            messagebox.showerror("Input Error", "Weight must be between 10 kg and 300 kg.")
            return
        
        if height < 0.5 or height > 3:
            messagebox.showerror("Input Error", "Height must be between 0.5 m and 3 m.")
            return
        
        bmi = weight / (height * height)
        
        if bmi < 18.5:
            category = "Underweight"
            message = "You are underweight. It's important to eat a nutritious diet."
        elif bmi >= 18.5 and bmi < 24.9:
            category = "Normal"
            message = "You have a normal weight. Keep up the good work!"
        elif bmi >= 25 and bmi < 29.9:
            category = "Overweight"
            message = "You are overweight. Consider a balanced diet and regular exercise."
        elif bmi >= 30 and bmi < 34.9:
            category = "Obesity (Class 1)"
            message = "You have obesity class 1. It's advisable to consult a healthcare provider."
        elif bmi >= 35 and bmi < 39.9:
            category = "Obesity (Class 2)"
            message = "You have obesity class 2. It's important to seek medical advice."
        else:
            category = "Obesity (Class 3)"
            message = "You have obesity class 3. Please consult a healthcare provider immediately."
        
        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}\n{message}")
        plot_bmi_chart(bmi)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

def plot_bmi_chart(bmi):
    categories = ['Underweight', 'Normal', 'Overweight', 'Obesity (Class 1)', 'Obesity (Class 2)', 'Obesity (Class 3)']
    values = [18.5, 24.9, 29.9, 34.9, 39.9, 45]
    
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.bar(categories, values, color=['blue', 'green', 'yellow', 'orange', 'red', 'purple'])
    ax.axhline(y=bmi, color='black', linestyle='--', linewidth=2)
    ax.set_ylabel('BMI Value')
    ax.set_title('BMI Categories')
    
    ax.set_xticklabels(categories, rotation=45, ha='right')
    
    fig.tight_layout()
    
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=5, column=0, columnspan=2, pady=10, sticky='nsew')

def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)

root = tk.Tk()
root.title("BMI Calculator")
root.configure(bg='#f0f0f0')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(5, weight=1)

weight_label = tk.Label(root, text="Weight (kg):", bg='#f0f0f0', fg='#333')
weight_label.grid(row=0, column=0, padx=10, pady=5, sticky='e')
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=5, sticky='w')

height_label = tk.Label(root, text="Height (m):", bg='#f0f0f0', fg='#333')
height_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

calculate_button = tk.Button(root, text="Calculate", command=calculate_bmi, bg='#4CAF50', fg='white')
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_fields, bg='#f44336', fg='white')
clear_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="", bg='#f0f0f0', fg='#333')
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()