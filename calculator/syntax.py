import re




#extract text into a list with number and operation seperated
#"2.5+3" ---> ["2.5","+","3"]
def extract(expression):
	countNumber=0
	countOperation=0
	newString=''
	tmpList = []

	for i in expression:
		if i == '+' or i == '%' or i == 'X' or i == '-':
			tmpList.append(newString)
			tmpList.append(i)
			newString =""
		else:
			newString += i

	if newString != "":
		tmpList.append(newString) #append the last string of the expression
	
	return tmpList 


#Expected order of element : Number, operation, number,operatio,...
#returns true if the oder is corrected else false
def validRow(checkList):

	print("Valid row: checklist: "+str(checkList))

	count = 1
	exitStatus = 0 #makes sure number is at the end

	for item in checkList:

		if count %2  != 0:
			if item != 'Number':
				return False
			exitStatus = 1
		else: 
			if item != 'Operation':
				return False
			exitStatus = 0

		count = count +1

	if exitStatus == 1:
		return True
	else: 
		return False



#in order to check the validity of the syntax the  whole list is converted to 
# ["2.5", "+","3"]---->into--->["Number","Operation","Number"]

def is_numeric_string(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def orderCheck(s):
	newList = []
	print("s list value: "+str(s))
	for tmp in s:
		if is_numeric_string(tmp.strip()):
			newList.append("Number")
		else:
			newList.append("Operation")

	return validRow(newList)


def syntaxCheck(s):
	s = extract(s)
	return orderCheck(s)


def add(a,b):
	return float(a)+float(b)


def subtract(a,b):
	return float(a)-float(b)

def multiply(a,b):
	return float(a) * float(b)

def divide(a,b):
	print("a: " + str(a) + "b: "+str(b))
	if b == '0':
		print("print Error!!")
		return "Error"
	else:
		return float(a)/float(b)



def leftElementIndex(stack,position):
	start = 0
	while position != -1 :
		if stack[position] != " ":
			return stack[position]
		position = position -1


def rightElementIndex(stack,position):
	end = len(stack)
	while position != end :
		if stack[position] != " ":
			return stack[position]
		position = position+1


def extractResult(tmpstack,operation):
	if operation in tmpstack:
		operationIndex = [n for n,x in enumerate(tmpstack) if x==operation]
		for x in operationIndex:
			left = leftElementIndex(tmpstack,x-1)
			right = rightElementIndex(tmpstack,x+1)
			if operation == "X":
				result = multiply(left, right)  
			elif operation == "+":
				result = add(left, right)  
			elif operation == "-":
				result = subtract(left, right)

			tmpstack[x-1] = result
			tmpstack[x]=" "
			tmpstack[x+1] =" " 
			print(str(tmpstack))


#output the values in the stack
def computeStackValues(stack,text):
	tmpstack = extract(text)   # all the operation will be done on copied stack
	divideByZero = False
	#compute divide
	if '%' in tmpstack:
		divideIndex = [n for n,x in enumerate(tmpstack) if x=='%']
		print("Index position in list: "+str(divideIndex)+" type: "+str(type(divideIndex)))
		for x in divideIndex:
			left = leftElementIndex(tmpstack,x-1)
			print("Left element: "+str(left))
			right = rightElementIndex(tmpstack,x+1)
			print("Right element: "+str(left))
			result = divide(left,right)
			if result != "Error" :
				tmpstack[x-1] = result
				tmpstack[x]=" "
				tmpstack[x+1] =" "

			else:
				divideByZero = True


	if divideByZero != True:
		extractResult(tmpstack,'X')
		extractResult(tmpstack,'+')
		extractResult(tmpstack,'-')
		result=tmpstack[0]

	
	stack.clear()
	stack.append(result)









def analyze(stack,text):

	if syntaxCheck(text) == False:
		print("Syntax Error!!")
		stack.clear()
		stack.append("Syntax Error")
	else:
		print("Syntax is okey!!!")
		computeStackValues(stack,text)
		
		#stack.clear()

