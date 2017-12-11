import os
import sys


def cls():
	os.system('cls' if os.name == 'nt' else 'clear')


def convert(cidr):
	cidr = int(cidr)
	binary_temp = ""
	parted = []
	n = 8
	int_parted = []

	for i in range(0, 32):
		if i < cidr:
			binary_temp += '1'
		else:
			binary_temp += '0'

	for i in range(0, len(binary_temp), n):
		parted.append(binary_temp[i:i + n])

	for byte in parted:
		int_parted.append(int(byte, 2))
	final = map(str, int_parted)
	return '.'.join(final)


def ipcidr(ip, cidr):
	octets = ip.split('.')
	for n in range(0, len(octets)):
		octets[n] = bin(int(octets[n]))

	cidr = int(cidr)
	binary_temp = ""
	parted = []
	n = 8

	for i in range(0, 32):
		if i < cidr:
			binary_temp += '1'
		else:
			binary_temp += '0'

	for i in range(0, len(binary_temp), n):
		parted.append(binary_temp[i:i + n])

	print(octets)
	print(parted)
	# Fixa detta, ta reda på hur man gör bitwise and på cidr + varje oktett av IPn
	print(bin(octets[0]) & bin(parted[0]))


def menu():
	print('-' * 50)
	print("Network tools by some dood")
	print('-' * 50)

	print('What do you want to do today?\n')
	print('1. Convert CIDR to subnet mask.')
	print('2. Analyse an IP + CIDR.')
	print('3. Exit')
	try:
		choice = int(input('Choose an instruction: '))
		if choice is 1:
			print(convert(input("CIDR notation: ")))
			input()
			cls()
		elif choice is 2:
			ipcidr(input('IP to analyse: '), input('CIDR notation: '))
		elif choice is 3:
			sys.exit(0)
	except ValueError:
		print("Try again.")
		cls()


while True:
	menu()
