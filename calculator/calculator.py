from tkinter import *

import syntax




stack = []

# for displaying output# 
#each time output display is destroyed and new screen is added
# variable is created global to destroy the old display
displayLabel = None  # declearing 


def getValue(root,value):

	if value == "=":
		syntax.analyze(stack,getText())
	elif value == 'AC':
		stack.clear()
	else: 
		#print("This is the value: "+ str(value))
		stack.append(str(value))

	printOutputdisplay(root)


def getText():
	str1 = ""
	status=0
	count = len(stack)
	#print("Value of count: "+str(count))
	while (status != count):
		str1 += str(stack[status])
		status = status + 1

	return str1


def printOutputdisplay(root):
	global displayLabel

	if displayLabel is not None:
		displayLabel.destroy()
	x = getText()
	#print("Text: " + str(x))
	displayLabel = Label(root, text=str(x), font=("Helvetica", 30), borderwidth=3, relief="raised")
	displayLabel.grid(row=0, columnspan=5, padx=20, pady=20)  

def printNumber(root, value, row, column):
	mybutton = Button(root, text=str(value), font=("Helvetica", 24), padx=30, pady=30, command=lambda m=value: getValue(root, m))
	mybutton.grid(row=row, column=column)


def printRest(root, row, column):
    printNumber(root, "0", row + 1, 0)  # print 0
    printNumber(root, ".", row + 1, 1)  # print .
    printNumber(root, "=", row + 1, 2)  # print =

    printNumber(root, "X", row - 2, column + 1)  
    printNumber(root, "-", row - 1, column + 1)  
    printNumber(root, "+", row, column + 1) 
    printNumber(root, "%", row + 1, column + 1)  
    printNumber(root, "AC", row - 2, column + 2)





def printBorad(root):

	printOutputdisplay(root)

	row = 4
	for x in range(9):
		if x % 3  == 0 :
			row = row + 1
			column = 0
		printNumber(root,str(9-x),row,column)
		column = column + 1
	printRest(root,row,column)



if __name__ == "__main__":
	root = Tk()
	root.title("Calculator")
	root.geometry("500x500")

	printBorad(root)

	root.mainloop()


