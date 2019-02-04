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
def line_break():
	print("_______________________________________________________________________________________________________________")
	print("")

def app_introduction():
	line_break()
	print("Welcome")
	print("v"+str(version))
	print("Type 'help' for a list of commands, type units for a list of units, type exit to quit.")

def app_main():	
	line_break()
	user_input = input("What would you like to do: ")
	if user_input == "help":
		line_break()
		print("'length' or 'l': do length measurement conversion")
		print("'volumetric' or 'volume' or 'v': do volumetric conversions")
		print("'Temperature' or 'temp' or 't': do temperature conversions")
		print("'help': Get help")
		print("'units': Print a list of units")
		print("'exit': quit the software or function")
		app_main()
	elif user_input == "units":
		line_break()
		print("Millimeter, Centimeter, Meter, Kilometer, Inch, Foot, Yard, mile")
		print("Milliliter, Centiliter, Teaspoon, Tablespoon, Fluid ounce, cup, liter, gallon")
		app_main()
	elif user_input == "exit":
		return
	elif user_input == "length" or user_input == "l":
		length_handler()
	elif user_input == "volumetric" or user_input == "volume" or user_input == "v":
		volume_handler()
	elif user_input == "temperature" or user_input == "temp" or user_input == "t":
		temperature_handler()
	else:
		print("I'm sorry, I do not currently understand that argument.")
		app_main()

#Universal handler function
def measure_parser(a,b,measure,measure_length): #Calculates the request and prints the final outcome
	a = a[:-measure_length]
	aVal = globals()[measure] * int(a)
	bVal = globals()[b]
	outcome = aVal / bVal
	print(a + measure + " in " + b + " is: " + str(outcome) + b)
	time.sleep(0.4)
	app_main()

#Length handling block start
def length_calculator(a, b): #Takes in user input then passes it to the calculation function
	line_break()
	if a.endswith("mm"):
		try:
			measure_parser(a, b, "mm", 2)
		except:
			print("The target unit was not correct.")
			length_handler()
	elif a.endswith("cm"):
		try:
			measure_parser(a, b, "cm", 2)
		except:
			print("The target unit was not correct.")
			length_handler()
	elif a.endswith("me"):
		try:
			measure_parser(a, b, "me", 2)
		except:
			print("The target unit was not correct.")
			length_handler()
	elif a.endswith("km"):
		try:
			measure_parser(a, b, "km", 2)
		except:
			print("The target unit was not correct.")
			length_handler()
	elif a.endswith("inch"): #unfortunately "in" is a reserved word
		try:
			measure_parser(a, b, "in", 2)
		except:
			print("The target unit was not correct.")
			length_handler()
	elif a.endswith("ft"):
		try:
			measure_parser(a, b, "ft", 2)
		except:
			print("The target unit was not correct.")
			length_handler()
	elif a.endswith("yd"):
		try:
			measure_parser(a, b, "yd", 2)
		except:
			print("The target unit was not correct.")
			length_handler()
	elif a.endswith("mi"):
		try:
			measure_parser(a, b, "mi", 2)
		except:
			print("The target unit was not correct.")
			length_handler()
	else:
		print("I'm sorry, I don't understand that measurement")
		app_main()


def length_handler(): #Presents the options available for length and asks for input, also accepts exit.
	line_break()
	print('Viable measurements: mm, cm, m, km, inch, ft, yd, mi')
	print("Format queries as number then measure, eg: 50mm")
	first_input = input("Measure to convert: ")
	if first_input == "exit":
		return
	else:
		second_input = input("Measure to convert TO (measurements only): ")
		if second_input == "exit":
			return
		else:
			length_calculator(first_input, second_input)
#Length handling block end

#Volume handling block begin
def volume_calculator(a,b):
	if a.endswith("ml"):
		try:
			measure_parser(a,b,"ml",2)
		except:
			print("The target unit was not correct")
			volume_handler()
	elif a.endswith("cl"):
		try:
			measure_parser(a,b,"cl",2)
		except:
			print("The target unit was not correct")
			volume_handler()
	elif a.endswith("tsp"):
		try:
			measure_parser(a,b,"tsp",3)
		except:
			print("The target unit was not correct")
			volume_handler()
	elif a.endswith("tbsp"):
		try:
			measure_parser(a,b,"tbsp",4)
		except:
			print("The target unit was not correct")
			volume_handler()
	elif a.endswith("oz"):
		try:
			measure_parser(a,b,"oz",2)
		except:
			print("The target unit was not correct")
			volume_handler()
	elif a.endswith("cup"):
		try:
			measure_parser(a,b,"cup",3)
		except:
			print("The target unit was not correct")
			volume_handler()
	elif a.endswith("li"):
		try:
			measure_parser(a,b,"li",2)
		except:
			print("The target unit was not correct")
			volume_handler()
	elif a.endswith("gal"):
		try:
			measure_parser(a,b,"gal",3)
		except:
			print("The target unit was not correct")
			volume_handler()
	else:
		print("I'm sorry, I don't understand that measurement.")
		app_main()


def volume_handler(): #Presents the options available for volume and asks for input, also accepts exit.
	line_break()
	print('Viable measurements: ml, cl, tsp, tbsp, oz, cup, li, gal')
	print("Format queries as number then measure, eg: 5ml")
	first_input = input("Measure to convert: ")
	if first_input == "exit":
		return
	else:
		second_input = input("Measure to convert TO (measurements only): ")
		if second_input == "exit":
			return
		else:
			volume_calculator(first_input, second_input)
#Volume handling block end



def tempCalc(type, c, f):
	valueC = int(c)
	valueF = int(f)
	if type == 1: #C to F
		temp = valueC * 1.8 + 32
		print(str(valueC) + "c in f is: " + str(temp) + "f")
		app_main()
	elif type == 2: #F to C
		stepdown = valueF - 32
		temp = stepdown / 1.8
		print(str(valueF) + "f in c is: " + str(temp) + "c")
		app_main()

def temperature_handler():
	print("Lets convert some temps!")
	line_break()
	print("1. Celsius to Fahrenheit")
	print("2. Fahrenheit to Celsius")
	print("Type exit to go back")
	line_break()
	choice = input("What would you like to do: ")
	if choice == "1":
		celsius_input = input("Input temperature: ")
		tempCalc(1, celsius_input, "0")
	elif choice == "2":
		fahrenheit_input = input("Input temperature: ")
		tempCalc(2, "0", fahrenheit_input)
	elif choice == "exit":
		app_main()
	elif choice == "help":
		line_break()
		print(">>>>>type the number of your selection to select your function, type exit to return to the main menu.<<<<<")
		line_break()
		temperature_handler()
	else:
		print("I do not undersand that input")
		temperature_handler()
app_introduction()
app_main()