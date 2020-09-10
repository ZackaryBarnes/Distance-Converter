# Distance converter using Tkinter
# Length of CVS receipt based on largest recorded account

import tkinter as tk

windowHeight = 250
windowWidth = 275

measurmentDict = {
    "inches":1,
    "feet":12,
    "yards":36,
    "CVS receipts":68,
    "miles":63360,
    "times around the earth":1577727360
    }

# Creating the window
root = tk.Tk()
root.title('Distance Converter')
root.geometry(("%dx%d" % (windowWidth,windowHeight)))
# <div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
root.iconbitmap(r'windowicon.ico')
root.resizable(0, 0)

# Labels
convertLabel = tk.Label(root, text="Convert:")
toLabel = tk.Label(root, text="To:")
resultLabel = tk.Label(root, text="Units = Units")
spacerLabelX = tk.Label(root, text="")

# List of options
options = [
    "inches",
    "feet",
    "yards",
    "CVS receipts",
    "miles",
    "times around the earth"
]

# Drop down menu 1
clicked1 = tk.StringVar()
clicked1.set(options[0])
dropDownMenu1 = tk.OptionMenu(root, clicked1, *options)

# Drop down menu 2
clicked2 = tk.StringVar()
clicked2.set(options[3])
dropDownMenu2 = tk.OptionMenu(root, clicked2, *options)

# Entry box
e1 = tk.Entry(root)

# Actual calculations
def convertUnits():
    try:
        howMany = int(e1.get())
    except ValueError:
        resultLabel.config(text="Invalid Input!")
    inUnit = clicked1.get()
    outUnit = clicked2.get()
    startingVal = howMany * measurmentDict[inUnit]
    endingVal = round((startingVal / measurmentDict[outUnit]), 2)
    mystring = ' '.join(map(str, (howMany, inUnit, "=", endingVal, outUnit)))
    resultLabel.config(text=(mystring))
    e1.delete(0, 'end')

# Calculate button
myButton = tk.Button(root, text="Calculate", padx=25, command=convertUnits)

# Packing widgets
convertLabel.pack()
e1.pack()
dropDownMenu1.pack()
toLabel.pack()
dropDownMenu2.pack()
spacerLabelX.pack()
myButton.pack()
resultLabel.pack()

# Main loop for tkinter window
root.mainloop()