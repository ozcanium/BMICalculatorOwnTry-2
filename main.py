from tkinter import *

window = Tk()
window.title("BMI Calculator 2")
window.minsize(300,  300)
window.config(padx=40, pady=40 )

custom_font = ("Arial", 12, "italic")

height_label = Label(text="Please Enter Your Height", font=custom_font)
height_label.pack()
height_entry = Entry()
height_entry.pack()

weight_label = Label(text="Please Enter Your Weight", font=custom_font)
weight_label.pack()
weight_entry = Entry()
weight_entry.pack()

result_label = Label(text="", font=custom_font)
result_label.pack()

def bmi_calculate():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        result = weight / ((height * 0.01) ** 2)
        result_text = f"Your BMI is calculated as: {round(result)}"

        if result <= 18.5:
            result_text += "\nYou are weak. You need to gain a little more weight for your health."
        elif 18.5 <= result < 24.9:
            result_text += "\nIt's pretty normal. You need to maintain your weight."
        elif 25 <= result < 29.9:
            result_text += "\nIt's pretty normal. You need to maintain your weight."
        elif 30 <= result < 34.5:
            result_text += "\nYou are obese. Lose weight for your health, my friend."

        result_label.config(text=result_text)

    except ValueError:
        result_label.config(text="Please enter valid numerical values for height and weight.")

button = Button(text="Calculate", command=bmi_calculate, font=custom_font)
button.pack()

window.mainloop()

