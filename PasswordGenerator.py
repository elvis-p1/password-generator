import random
import tkinter as tk

# function to generate a password
def generatePass(hasLower, hasUpper, hasSpecial, hasNum, minLen, maxLen):
    """Generate a password
    :param hasLower: True if the password should contain lowercase letters, False if not
    :param hasUpper: True if the password should contain uppercase letters, False if not
    :param hasSpecial: True if the password should contain special characters/symbols
    :param hasNum: True if the password should contain numbers, False otherwise
    :param minLen: Minimum length of the generated password
    :param maxLen: Maximum length of the generated password
    :return: A string that meets the given requirements
    #
    """
    chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*-_')

    output = []
    aNumber = False
    aBigLetter = False
    aSmallLetter = False
    aSpecChar = False
    
    filteredChars = chars
    # removing characters that can be in the password based on what boxes are checked
    if not hasLower:
        filteredChars = [i for i in filteredChars if i not in 'abcdefghijklmnopqrstuvwxyz']
    if not hasUpper:
        filteredChars = [i for i in filteredChars if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    if not hasNum:
        filteredChars = [i for i in filteredChars if not i.isnumeric()]
    if not hasSpecial:
        filteredChars = [i for i in filteredChars if i not in '!@#$%^&*_-<>.']
    
    if hasLower:
        output.append(chars[random.randint(0,25)])
    if hasUpper:
        output.append(chars[random.randint(26,51)])
    if hasNum:
        output.append(chars[random.randint(52,61)])
    if hasSpecial:
        output.append(chars[random.randint(62,len(chars)-1)])

    for i in range(random.randint(minLen-len(output), maxLen-len(output))):
        output.append(filteredChars[random.randint(0,len(filteredChars)-1)])
    
    random.shuffle(output)
    return ''.join(output)

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

minLabel = tk.Label(root, text="Minimum number of characters", font=("Calibri", 12))
minLabel.pack()
minEntry = tk.Entry(root, width=8, textvariable=tk.StringVar(root, value="8"))
minEntry.pack()

maxLabel = tk.Label(root, text="Maximum number of characters", font=("Calibri", 12))
maxLabel.pack()
maxEntry = tk.Entry(root, width=8, textvariable=tk.StringVar(root, value="16"))
maxEntry.pack()

passLabel = tk.Label(root,text="\nPassword appears below", font=("Calibri",14))
passLabel.pack()
passwordEntry = tk.Entry(root,width=40, font=("Calibri", 14))
passwordEntry.pack()

def generate(hasLower, hasUpper, hasSpecial, hasNum, minLen, maxLen, entry):
    # Function to put the generated password on the entry area in the GUI
    # Displays coressponding error messages for invalid input
    if not (hasLower or hasUpper or hasSpecial or hasNum):
        errorLabel.config(text="Check at least one box!")
    elif not (minLen.isnumeric() and maxLen.isnumeric()):
        errorLabel.config(text="Please enter a valid number for the minimum/maximum values")
    elif(int(minLen) > int(maxLen)):
        errorLabel.config(text="Max # of characters should be greater than the minimum number")
    elif(int(minLen) == 0 or int(maxLen) == 0):
        errorLabel.config(text="Minimum and maximum number of characters cannot be 0")
    else:
        errorLabel.config(text="")
        entry.delete(0, "end")
        entry.insert(0, generatePass(hasLower,hasUpper, hasSpecial, hasNum, int(minLen), int(maxLen)))

generateButton = tk.Button(root, text="Generate password", font=("Calibri",14), command=lambda: generate(lowerCBvar.get(), upperCBvar.get(), specialCBvar.get(), numCBvar.get(), minEntry.get(), maxEntry.get(), passwordEntry))
generateButton.pack()
errorLabel = tk.Label(root, text="", fg="#FF3346", font=("Calibri",14))
errorLabel.pack()
root.mainloop()
