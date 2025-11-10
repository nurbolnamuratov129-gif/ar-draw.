import tkinter as tk

# Kalkulyator oynasi
root = tk.Tk()
root.title("Kalkulyator")

# Natija maydoni
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='ridge')
entry.grid(row=0, column=0, columnspan=4)

# Funksiya tugmalarni bosganda ishlaydi
def click(button_text):
    if button_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Xatolik")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Tugmalar ro'yxati
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Tugmalarni oynaga joylash
row_val = 1
col_val = 0
for button in buttons:
    action = lambda x=button: click(x)
    tk.Button(root, text=button, width=5, height=2, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
