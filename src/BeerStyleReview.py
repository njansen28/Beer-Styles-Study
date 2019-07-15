import xlrd                     # Used for pulling in spreadsheet data
from tkinter import filedialog  # Used for file dialog stuff
from tkinter import *           # Used for all the other gui stuff


# After a file is chosen, read it in and setup the config screen
def file_button_press():
    window.filename = filedialog.askopenfilename(initialdir=".", title="Select file",
                                                 filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
    print(window.filename)
    file_label.config(text=window.filename)

    spreadsheet = xlrd.open_workbook(window.filename)

    num_sheets = spreadsheet.nsheets
    for i in range(0, num_sheets):

        quiz_categories.append(spreadsheet.sheet_by_index(i).name)
        subcategories = spreadsheet
    window.geometry("")
    print(quiz_categories)


# Where stuff actually starts

print("Welcome to the Beer Style Review Program")

# Define window/frames
window = Tk()
top_frame = Frame(window)
frame = Frame(window)
bottom_frame = Frame(window)

quiz_categories = list()

# Make the window object and set it up
window.title('Beer Style Review')
window.geometry('666x50')

# Add a frame to the window
frame.pack(fill=X)
top_frame.pack()
bottom_frame.pack(side=BOTTOM, fill=X)

# Add a button to choose the input file
file_button = Button(frame, text='Choose Source File', width=25, command=file_button_press)
file_button.pack(side=RIGHT)

# Label to display chosen file
file_label = Label(frame, text="No File Chosen Yet")
file_label.pack(side=RIGHT, expand=YES, fill=X)

# Add a button to start the activity
# go_button = Button(bottom_frame, text='Go', width=25, command=go_button_press)
# go_button.pack(side=RIGHT)

# Run the GUI
window.mainloop()
