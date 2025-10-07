"""
To install Tkinter use:
    sudo apt-get install python3-tk
    
Use packs format in the tkinter code.
"""
import tkinter as tk
import sqlite3
import database as db
import auxilary_info as aux

def Window():
    window = tk.Tk()
    window.geometry("700x500")
    window.configure(bg="lightblue")
    window.title("Wanderly - Tourist Recommender System")

    city_variable = tk.StringVar()
    dark_mode = [False]

    label = tk.Label(window, text="Hello Traveller!\nPlease enter your tourist destination : ",
                     bg="lightblue", font=("Courier", 20))
    label.pack(pady=20)

    name_entry = tk.Entry(window, textvariable=city_variable, font=('Courier', 20))
    name_entry.pack(pady=10)

    
    def GetInput():
        inp_var = city_variable.get().strip()
        print(f"User entered: {inp_var}")
        textbox.delete("1.0", tk.END)

        if not inp_var:
            textbox.insert(tk.END, "Please enter a city name.\n")
            return

        if inp_var == "./help":
            textbox.insert(tk.END, f"{aux.help_text}")
            return

        result = db.findCity(inp_var)

        if result is not None:
            name, pin, dist, landmarks = result
            landmarks = landmarks.replace(",", "\n")
            textbox.insert(tk.END, f"Name: {name}\nPIN: {pin}\nDistance from Tuticorin:\n{dist}\nAttractions:\n{landmarks}")
        else:
            textbox.insert(tk.END, f"Error: '{inp_var}' not found in database.\nPlease check the spelling or try another city.")

    button = tk.Button(window, text="Find About My Trip", bg='grey', fg='black',
                       command=GetInput, font=("Courier", 14))
    button.pack(pady=10) 

    
    textbox_frame = tk.Frame(window)
    textbox_frame.pack(pady=10)

    scrollbar = tk.Scrollbar(textbox_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    textbox = tk.Text(textbox_frame, height=10, width=50, font=("Courier", 16), yscrollcommand=scrollbar.set)
    textbox.pack(side=tk.LEFT)
    scrollbar.config(command=textbox.yview)

    # Dark mode toggle
    def toggle_dark_mode():
        if not dark_mode[0]:
            window.configure(bg="#2d2d2d")
            label.configure(bg="#2d2d2d", fg="white")
            name_entry.configure(bg="#1e1e1e", fg="white", insertbackground="white")
            button.configure(bg="#444444", fg="white", activebackground="#555555")
            dark_button.configure(bg="#444444", fg="white", activebackground="#555555")
            textbox.configure(bg="#1e1e1e", fg="white", insertbackground="white")
            dark_mode[0] = True
            dark_button.configure(text="Light Mode")
        else:
            window.configure(bg="lightblue")
            label.configure(bg="lightblue", fg="black")
            name_entry.configure(bg="white", fg="black", insertbackground="black")
            button.configure(bg="grey", fg="black", activebackground="white")
            dark_button.configure(bg="grey", fg="black", activebackground="white")
            textbox.configure(bg="white", fg="black", insertbackground="black")
            dark_mode[0] = False
            dark_button.configure(text="Dark Mode")

    dark_button = tk.Button(window, text="Dark Mode", font=("Courier", 12),
                            command=toggle_dark_mode)
    dark_button.pack(pady=5)

    window.mainloop()

