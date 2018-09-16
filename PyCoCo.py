import time
# Python 3.7

version = 1.0
#Begin distance____________________________
mm = 1 #The base measurement for distance conversion. Downward calculations will be based on dividing the greater number by the lesser number
cm = 10 #The measurement in MM (the base measurement.)
inch = 25.4
me = 1000
km = 1000000
ft = 304.8 
yd = 914.4
mi = 1609344
# Example downward calculation: feet > in (304.8 / 25.44 = 12) The final number is the converted unit, in this case inches.
# Verticle calculations are done the same way. Feet > yards (304.8 / 914.4 = 0.33333333333)
#End distance______________________________

#Begin material measurements_______________
ml = 1 #Base measurement
tsp =  4.92892
cl = 10
tbsp = 14.7867648
oz = 29.5735
cup = 236.588
li = 1000
gal = 3785.41178
#End material measurements_________________
def lb():
	print("_______________________________________________________________________________________________________________")
	print("")

def intro():
	lb()
	print("Welcome")
	print("v"+str(version))
	print("Type 'help' for a list of commands, type units for a list of units, type exit to quit.")

def main():	
	lb()
	UInput = input("What would you like to do: ")
	if UInput == "help":
		lb()
		print("'length' or 'l': do length measurement conversion")
		print("'volumetric' or 'volume' or 'v': do volumetric conversions")
		print("'Temperature' or 'temp' or 't': do temperature conversions")
		print("'help': Get help")
		print("'units': Print a list of units")
		print("'exit': quit the software or function")
		main()
	elif UInput == "units":
		lb()
		print("Millimeter, Centimeter, Meter, Kilometer, Inch, Foot, Yard, mile")
		print("Milliliter, Centiliter, Teaspoon, Tablespoon, Fluid ounce, cup, liter, gallon")
		main()
	elif UInput == "exit":
		return
	elif UInput == "length" or UInput == "l":
		lengthHandler()
	elif UInput == "volumetric" or UInput == "volume" or UInput == "v":
		volumeHandler()
	elif UInput == "temperature" or UInput == "temp" or UInput == "t":
		tempHandler()
	else:
		print("I'm sorry, I do not currently understand that argument.")
		main()

#Universal handler function
def measureParser(a,b,measure,MeasureLength): #Calculates the request and prints the final outcome
	a = a[:-MeasureLength]
	aVal = globals()[measure] * int(a)
	bVal = globals()[b]
	outcome = aVal / bVal
	print(a + measure + " in " + b + " is: " + str(outcome) + b)
	time.sleep(0.4)
	main()

#Length handling block start
def lengthCalc(a, b): #Takes in user input then passes it to the calculation function
	lb()
	if a.endswith("mm"):
		try:
			measureParser(a, b, "mm", 2)
		except:
			print("The target unit was not correct.")
			lengthHandler()
	elif a.endswith("cm"):
		try:
			measureParser(a, b, "cm", 2)
		except:
			print("The target unit was not correct.")
			lengthHandler()
	elif a.endswith("me"):
		try:
			measureParser(a, b, "me", 2)
		except:
			print("The target unit was not correct.")
			lengthHandler()
	elif a.endswith("km"):
		try:
			measureParser(a, b, "km", 2)
		except:
			print("The target unit was not correct.")
			lengthHandler()
	elif a.endswith("inch"): #unfortunately "in" is a reserved word
		try:
			measureParser(a, b, "in", 2)
		except:
			print("The target unit was not correct.")
			lengthHandler()
	elif a.endswith("ft"):
		try:
			measureParser(a, b, "ft", 2)
		except:
			print("The target unit was not correct.")
			lengthHandler()
	elif a.endswith("yd"):
		try:
			measureParser(a, b, "yd", 2)
		except:
			print("The target unit was not correct.")
			lengthHandler()
	elif a.endswith("mi"):
		try:
			measureParser(a, b, "mi", 2)
		except:
			print("The target unit was not correct.")
			lengthHandler()
	else:
		print("I'm sorry, I don't understand that measurement")
		main()


def lengthHandler(): #Presents the options available for length and asks for input, also accepts exit.
	lb()
	print('Viable measurements: mm, cm, m, km, inch, ft, yd, mi')
	print("Format queries as number then measure, eg: 50mm")
	firstInp = input("Measure to convert: ")
	if firstInp == "exit":
		return
	else:
		secondInp = input("Measure to convert TO (measurements only): ")
		if secondInp == "exit":
			return
		else:
			lengthCalc(firstInp, secondInp)
#Length handling block end

#Volume handling block begin
def volCalc(a,b):
	if a.endswith("ml"):
		try:
			measureParser(a,b,"ml",2)
		except:
			print("The target unit was not correct")
			volumeHandler()
	elif a.endswith("cl"):
		try:
			measureParser(a,b,"cl",2)
		except:
			print("The target unit was not correct")
			volumeHandler()
	elif a.endswith("tsp"):
		try:
			measureParser(a,b,"tsp",3)
		except:
			print("The target unit was not correct")
			volumeHandler()
	elif a.endswith("tbsp"):
		try:
			measureParser(a,b,"tbsp",4)
		except:
			print("The target unit was not correct")
			volumeHandler()
	elif a.endswith("oz"):
		try:
			measureParser(a,b,"oz",2)
		except:
			print("The target unit was not correct")
			volumeHandler()
	elif a.endswith("cup"):
		try:
			measureParser(a,b,"cup",3)
		except:
			print("The target unit was not correct")
			volumeHandler()
	elif a.endswith("li"):
		try:
			measureParser(a,b,"li",2)
		except:
			print("The target unit was not correct")
			volumeHandler()
	elif a.endswith("gal"):
		try:
			measureParser(a,b,"gal",3)
		except:
			print("The target unit was not correct")
			volumeHandler()
	else:
		print("I'm sorry, I don't understand that measurement.")
		main()


def volumeHandler(): #Presents the options available for volume and asks for input, also accepts exit.
	lb()
	print('Viable measurements: ml, cl, tsp, tbsp, oz, cup, li, gal')
	print("Format queries as number then measure, eg: 5ml")
	firstInp = input("Measure to convert: ")
	if firstInp == "exit":
		return
	else:
		secondInp = input("Measure to convert TO (measurements only): ")
		if secondInp == "exit":
			return
		else:
			volCalc(firstInp, secondInp)
#Volume handling block end



def tempCalc(type, c, f):
	valueC = int(c)
	valueF = int(f)
	if type == 1: #C to F
		temp = valueC * 1.8 + 32
		print(str(valueC) + "c in f is: " + str(temp) + "f")
		main()
	elif type == 2: #F to C
		stepdown = valueF - 32
		temp = stepdown / 1.8
		print(str(valueF) + "f in c is: " + str(temp) + "c")
		main()

def tempHandler():
	print("Lets convert some temps!")
	lb()
	print("1. Celsius to Fahrenheit")
	print("2. Fahrenheit to Celsius")
	print("Type exit to go back")
	lb()
	choice = input("What would you like to do: ")
	if choice == "1":
		celsiusInp = input("Input temperature: ")
		tempCalc(1, celsiusInp, "0")
	elif choice == "2":
		FahrenInp = input("Input temperature: ")
		tempCalc(2, "0", FahrenInp)
	elif choice == "exit":
		main()
	elif choice == "help":
		lb()
		print(">>>>>type the number of your selection to select your function, type exit to return to the main menu.<<<<<")
		lb()
		tempHandler()
	else:
		print("I do not undersand that input")
		tempHandler()
intro()
main()