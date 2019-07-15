import xlrd     # Used for pulling in spreadsheet data
import tkinter  # Used for all the gui fun


# Reads in an entire excel spreadsheet using xlrd
def read_in_spreadsheet(path):
    spreadsheet = xlrd.open_workbook(path)
    return spreadsheet


# Function that is called whenever the "Go" button is pressed
def go_button_press():
    print("Button was pressed")
    return


# Where stuff actually starts
def main():
    print("Welcome to the Beer Style Review Program")

    # Make the window object and set it up
    window = tkinter.Tk()
    window.title('Beer Style Review')
    window.geometry('666x420')

    # Add a button to start the activity
    go_button = tkinter.Button(window, text='Go', width=25, command=go_button_press)
    go_button.pack()
    # Run the GUI
    window.mainloop()

    print("Reading in style data now from \"Cicerone Beer Study Guides.xlsx\"")

    # First, read in the spreadsheet
    # TODO: Let them specify the path to the spreadsheet?
    spreadsheet = read_in_spreadsheet('Cicerone Beer Study Guides.xlsx')

    return


# Stoopid python "main" scheme
if __name__ == "__main__":
    main()
