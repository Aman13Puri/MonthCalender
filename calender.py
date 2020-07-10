from calendar import monthcalendar
from tkinter import *
from datetime import date

calenderFont = 20

class CalenderMainFrame(Frame):
	def __init__(self,parent,year,month,date):
		Frame.__init__(self,parent)
		self["height"] = 500
		self["width"] = 500
		self["bg"] = 'black'
		self.frames = list()
		self.weekList = [monthcalendar(year, i) for i in range(1, 13)]
		header = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
		
		for i in range(len(header)):
			frame = DayFrame(self,header[i],0,"flat",'white')
			frame.place(x = i*(calenderFont+20), y = 0)
		for i in range(1,len(self.weekList[month-1])+1):
			for j in range(7):
				if(self.weekList[month-1][i-1][j] == 0):
					frame = DayFrame(self,str(self.weekList[month-1][i-1][j]),0,"flat",'black')
					frame.place(x = j*(calenderFont+20), y = i*(calenderFont+20))
				else:
					if(self.weekList[month-1][i-1][j] == date):
						frame = DayFrame(self,str(self.weekList[month-1][i-1][j]),2,"ridge",'white')
						frame.place(x = j*(calenderFont+20), y = i*(calenderFont+20))
					else:
						frame = DayFrame(self,str(self.weekList[month-1][i-1][j]),0,"flat",'white')
						frame.place(x = j*(calenderFont+20), y = i*(calenderFont+20))

class DayFrame(Frame):

	def __init__(self,parent,labText,border,relief,textColour):
		self.labText = labText
		Frame.__init__(self,parent)
		self["height"] = calenderFont+5
		self["width"] = 20
		self["border"] = border
		self["relief"] = relief
		pixel = PhotoImage(width=1, height=1)
		label = Label(self,text =labText,font=("Calibri", calenderFont-5),image=pixel, width= calenderFont+10, height=calenderFont+10, compound="c",bg = 'black', fg = textColour)
		label.pack()
	def __len__(self):
		return len(self.labText)



today = date.today()
year,month,date = str(today).split('-')
my_window = Tk()
my_window.geometry(str(calenderFont*15)+'x'+str(calenderFont*12))
my_window.configure(bg ="black")

myframe = CalenderMainFrame(my_window,int(year),int(month),int(date))
myframe.place(x=10,y=5) 
my_window.mainloop()