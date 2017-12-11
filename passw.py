def hack(n):
	return (80**int(n))/(10**9)

pass_n = input("How many characters in your password? ")
time = hack(pass_n)
print('It would take ' + str(int(time)) + ' seconds, or ' + str(int(time/60)) + ' minutes, or ' + str(int(time/60/60)) + ' hours to brute-force your password.')

if time > (10**9):
	print('This is ' + str(int(time/31536000000)) + ' thousand years.')

input("Enter to exit...")

