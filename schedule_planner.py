
import xlrd
import win32com.client
from tkinter import *

root = Tk()

def Get_Schedule():
    file_path = file_path_entry.get()
    name = name_entry.get()
    week = week_entry.get()
    roster = xlrd.open_workbook(file_path)
    sheet_name = "Week " + week
    worksheet = roster.sheet_by_name(sheet_name)
    outlook = win32com.client.Dispatch(
        "Outlook.Application").GetNamespace("MAPI")
    calendar = outlook.GetDefaultFolder(9)

    for row in range(worksheet.nrows):
        for col in range(worksheet.ncols):
            if worksheet.cell_value(row, col) == name:
                for x in range(2, 9):
                    d_date = worksheet.cell_value(2, x)
                    d_day = worksheet.cell_value(row, x)
                    appointment = calendar.Items.Add(1)
                    appointment.Start = d_date
                    appointment.AllDayEvent = True
                    appointment.Subject = d_day
                    appointment.Save()

    my_label = Label(root, text="Schedule updated to Calendar")
    my_label.pack()


root.title("Calendar work")
file_path_label = Label(text="File Path: ")
file_path_label.pack()
file_path_entry = Entry(width=50)
file_path_entry.pack()
file_path_entry.insert(0, "Day Clerk Roster 20-21.xlsx")
name_label = Label(text="Name:")
name_label.pack()
name_entry = Entry(width=10)
name_entry.pack()
week_label = Label(text="Week Number:")
week_label.pack()
week_entry = Entry(width=10)
week_entry.pack()
my_button = Button(text="Get schedule", command=Get_Schedule)
my_button.pack()

root.mainloop()
