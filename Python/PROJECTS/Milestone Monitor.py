import tkinter as tk
import datetime
import os

# Path to the icon image (optional)
icon_path = "images/cgev.ico"

# Create the main window
root = tk.Tk()
root.title("Milestone Monitor")
root.configure(bg="#d8f3dc")
root.geometry("1900x300")

# Set icon (only if file exists)
if os.path.exists(icon_path):
    try:
        root.iconbitmap(icon_path)
    except Exception as e:
        print("Icon could not be set:", e)

# Get today's date
today = datetime.date.today()
# Get the ordinal day of the year (1–366)
day_of_year = today.timetuple().tm_yday

# Progress stages colors
progress_stages = ["#b7efc5", "#6ede8a", "#25a244", "#1a7431", "#04471c"]

# Month names
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# List to hold buttons
buttons = []


# Function to change the color of a button
def change_button_color(event):
    """Change button background color based on progress stages"""
    button = event.widget
    bg_color = button.cget("background")

    for index, item in enumerate(progress_stages):
        if bg_color == item and index < 4:
            button.configure(bg=progress_stages[index + 1])
            break
    else:
        # If color not in progress_stages, set to first stage
        button.configure(bg=progress_stages[0])


# Function to create a row of buttons for a week
def create_row(week):
    for i in range(1, 8):  # 7 days per week
        color_button = tk.Button(root, background="#ffffff", width=2, height=1)
        color_button.bind("<Button-1>", change_button_color)
        color_button.grid(row=i, column=week, padx=2, pady=2)
        buttons.append(color_button)


# Function to save button colors
def save_buttons():
    with open("buttons_data.txt", "w") as file:
        for button in buttons:
            bg_color = button.cget("background")
            file.write(bg_color + "\n")
    root.destroy()


# Function to load button colors
def load_buttons():
    colors = []
    try:
        with open("buttons_data.txt", "r") as file:
            for line in file:
                colors.append(line.strip())
    except FileNotFoundError:
        pass
    return colors


# Variable to track edit mode
edit = False


# Function to toggle edit mode
def button_edit_on_off():
    global edit
    button_index = 0
    if not edit:
        for b in buttons:
            if button_index + 1 == day_of_year:  # fix: +1 for correct day
                bg_color = b.cget("background")
                if bg_color not in progress_stages:
                    b.configure(bg="#252422")
            else:
                b.configure(state="disabled")
                b.unbind("<Button-1>")
            button_index += 1
        edit = True
    else:
        for b in buttons:
            b.configure(state="normal")
            b.bind("<Button-1>", change_button_color)
        edit = False


# --- GUI Construction ---

# Display month labels (once, not inside create_row)
for i in range(12):
    month = tk.Label(root, text=months[i], font=("Helvetica", 10), bg="#d8f3dc")
    month.grid(row=0, column=(1 + i) * 4, padx=2, pady=2)

# Create rows of buttons (52 weeks)
for i in range(1, 53):
    create_row(i)

# Load existing button colors from file
existing_colors = load_buttons()
for button, color in zip(buttons, existing_colors):
    button.configure(bg=color)

# Start in edit mode for today
button_edit_on_off()

# Display labels for progress stages
label_less = tk.Label(root, text="Less", font=("Helvetica", 12), bg="#d8f3dc")
label_less.grid(row=10, column=0, padx=2, pady=2)

for index, stage_color in enumerate(progress_stages):
    example_color = tk.Button(root, state="disabled",
                              background=stage_color, width=2, height=1)
    example_color.grid(row=10, column=index + 1, padx=2, pady=2)

# Button to toggle edit mode
edit_button = tk.Button(root, command=button_edit_on_off,
                        text="Edit", background="#f07167")
edit_button.grid(row=9, column=53, padx=6, pady=2)

# Button to exit and save
exit_button = tk.Button(root, command=save_buttons,
                        text="Exit and save", background="#f07167")
exit_button.grid(row=9, column=54, padx=6, pady=2)

# Run the application
root.mainloop()
