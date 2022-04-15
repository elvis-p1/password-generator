import secrets
import tkinter as tk

# function to generate a password
def generatePass(hasLower, hasUpper, hasSpecial, hasNum, passLength):
    """Generate a password
    :param hasLower: True if the password should contain lowercase letters, False if not
    :param hasUpper: True if the password should contain uppercase letters, False if not
    :param hasSpecial: True if the password should contain special characters/symbols
    :param hasNum: True if the password should contain numbers, False otherwise
    :param passLength: The length of the password to be generated, as a string
    :return: The generated password, which is a string
    #
    """
    
    lower_chars = list('abcdefghijklmnopqrstuvwxyz')
    upper_chars = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    special_chars = list('!@#$%^&*-_')
    num_chars = list('0123456789')

    # Creating the alphabet based on what the user chose
    alphabet = []
    if hasLower:
        for i in lower_chars:
            alphabet.append(i)
    if hasUpper:
        for i in upper_chars:
            alphabet.append(i)
    if hasSpecial:
        for i in special_chars:
            alphabet.append(i)
    if hasNum:
        for i in num_chars:
            alphabet.append(i)
    while True:
        lower_flag = False
        upper_flag = False
        num_flag = False
        special_flag = False

        password = ''.join(secrets.choice(alphabet) for i in range(passLength))
        for c in password:
            if not lower_flag and c.islower():
                lower_flag = True
            elif not upper_flag and c.isupper():
                upper_flag = True    
            elif not num_flag and c.isdigit():
                num_flag = True
            elif not special_flag and c in special_chars:
                special_flag = True

        # Check if the password matches user requirements
        if lower_flag == hasLower and upper_flag == hasUpper and num_flag == hasNum and special_flag == hasSpecial:
            break

    return password

# the GUI
root = tk.Tk()
root.title('Password Generator')
root.geometry('650x500')

label = tk.Label(root, text="Password Generator", font=("Calibri", 36))
label.pack()

# Variables to store checkbox states
lowerCBvar = tk.BooleanVar()
upperCBvar = tk.BooleanVar()
specialCBvar = tk.BooleanVar()
numCBvar = tk.BooleanVar()

# Checkbox widgets
lowerCB = tk.Checkbutton(root, text="Include lower case letters", font=("Calibri", 16), variable=lowerCBvar)
lowerCB.select()
lowerCB.pack()
upperCB = tk.Checkbutton(root, text="Include upper case letters", font=("Calibri", 16), variable=upperCBvar)
upperCB.select()
upperCB.pack()
specialCB = tk.Checkbutton(root, text="Include special characters e.g. !@#$%^&*-_", font=("Calibri", 16), variable=specialCBvar)
specialCB.pack()
numCB = tk.Checkbutton(root, text="Include numbers", font=("Calibri", 16), variable=numCBvar)
numCB.pack()

lengthLabel = tk.Label(root, text="Length of password", font=("Calibri", 12))
lengthLabel.pack()
lengthEntry = tk.Entry(root, width=8, textvariable=tk.StringVar(root, value="16"))
lengthEntry.pack()

passLabel = tk.Label(root,text="\nPassword appears below", font=("Calibri",14))
passLabel.pack()
passwordEntry = tk.Entry(root,width=40, font=("Calibri", 14))
passwordEntry.pack()

# Function to put the generated password on the entry area in the GUI
# Displays coressponding error messages for invalid input
def generate(hasLower, hasUpper, hasSpecial, hasNum, passLength, entry):
    if not (hasLower or hasUpper or hasSpecial or hasNum):
        errorLabel.config(text="Check at least one box!")
    elif not passLength.isnumeric():
        errorLabel.config(text="Please enter a valid number for the length")
    elif int(passLength) <= 0:
        errorLabel.config(text="Invalid length (should be higher than 0)")
    else:
        errorLabel.config(text="")
        entry.delete(0, "end")
        entry.insert(0, generatePass(hasLower,hasUpper, hasSpecial, hasNum, int(passLength)))

# Function to select and copy the generated password
def copyPassword():
    passwordEntry.selection_range(0, "end")
    passwordEntry.event_generate("<<Copy>>")

copyButton = tk.Button(root, text="Copy password", font=("Calibri", 14), command=copyPassword)

# If right clicking in the password entry, allows for cut, copy and paste functions
rcMenu = tk.Menu(root, tearoff=0)
rcMenu.add_command(label="Cut", command=lambda: passwordEntry.event_generate("<<Cut>>"))
rcMenu.add_command(label="Copy", command=lambda: passwordEntry.event_generate("<<Copy>>"))

# Right click menu pops up when done in the password entry area, copy/cut function
def rcPopup(event):
    try:
        rcMenu.tk_popup(event.x_root, event.y_root)
    finally:
        rcMenu.grab_release()

passwordEntry.bind("<Button-3>", rcPopup)

generateButton = tk.Button(root, text="Generate password", font=("Calibri",14), command=lambda: generate(lowerCBvar.get(), upperCBvar.get(), specialCBvar.get(), numCBvar.get(), lengthEntry.get(), passwordEntry))
generateButton.pack()
copyButton.pack()
errorLabel = tk.Label(root, text="", fg="#FF3346", font=("Calibri",14))
errorLabel.pack()

root.mainloop()
