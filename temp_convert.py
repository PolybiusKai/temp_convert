import sys
from pyfiglet import figlet_format


# Menu instructions
def instructions():
	print(figlet_format("My Temp"))
	print(figlet_format("Converter"))
	x = """
=>	Please select an option below:
	
[#] celsius    => Convert Celsius to Fehrenheit
[#] fehrenheit => Convert Fehrenheit to Celsius
[#] help       => Help Menu
[#] exit       => Exit Program
"""
	print(x)


def celsius_convert(c):
	#Converts Celsius to Fahrenheit
	f = (c * 1.8) + 32
	return print(f'\nThe converted Temperature is {f}°F.', file=sys.stderr)
	


def fahrenheit_convert(f):
	#Convert Fehrenheit to Celsius
	c = (f - 32) * .5556
	return print(f'\nThe converted Temperature is {c}°C.', file=sys.stderr)


def main():
	command = ''
	instructions()
	while True:
		command = input(" >> ")

		if command == 'celsius':
			c = int(input("What is the temperature in °C? >> "))
			celsius_convert(c)
			print('\n => Please Select Another Option\n ')
		elif command == 'fehrenheit':
			f = int(input("What is the temperature in °F? >> "))
			fahrenheit_convert(f)
			print('\n => Please Select Another Option\n ')
		elif command == 'help':
			instructions()
		elif command == 'exit':
			sys.exit('Goodbye')
		else:
			if command == '':
				print('Type something in!')
			elif command[0] == 'c' and command != "celsius":
				print('Did you mean "celsius" ?')
			elif command[0] == 'f' and command != 'fehrenheit':
				print('Did you mean "fehrenheit" ?')
			elif command[0] == 'h' and command != "help":
				print('Did you mean "help" ?')
			elif command[0] == 'e' and command != "exit":
				print('Did you mean "exit" ?')
			else:
				print(f'{command} is not a valid command, type "help" for help menu.')


if __name__ == '__main__':
	main()

