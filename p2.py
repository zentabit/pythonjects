# Calculate pi with Nilakanta series
def calc_pi(max_num):
	pi = 3
	for i in range(1, max_num):
		if i % 2 == 0:
			pi = pi - (4 / ((2 * i) * (2 * i + 1) * (2 * i + 2)))
		else:
			pi = pi + (4 / ((2 * i) * (2 * i + 1) * (2 * i + 2)))
	return pi


print("Pi would be {}".format(calc_pi(int(input("Max number: ")))))
