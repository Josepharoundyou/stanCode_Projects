"""
File: weather_master.py
Name: Joseph
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100


def main():
	"""
	To compute the average, highest, lowest,
	cold days among the inputs
	"""
	print('stanCode \"Weather Master 4.0\"')
	data1 = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	if data1 != EXIT:
		highest = data1
		lowest = data1
		times = 1
		summary = data1
		cold = 0
		cold = cold_day(data1, cold)
		# while loop
		while True:
			data1 = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			# Stop the program.
			if data1 == EXIT:
				print('Highest Temperature = ' + str(highest))
				print('Lowest Temperature = ' + str(lowest))
				print('Average = ' + str(summary/times))
				print(str(cold)+' cold day(s)')
				break
			highest = highest_temp(data1, highest)
			lowest = lowest_temp(data1, lowest)
			summary = average_temp_amount(data1, summary)
			times = average_temp_numbers(times)
			cold = cold_day(data1, cold)
	else:
		# Stop the program.
		print('No Temperatures were entered. ')


def highest_temp(data1, highest):
	"""
	To decide the highest temperature
	among user inputs
	:param data1: int, the input number to be compared.
	:param highest: int, the highest number for now.
	"""
	if data1 > highest:
		highest = data1
	return highest


def lowest_temp(data1, lowest):
	"""
	To decide the lowest temperature
	among user inputs.
	:param data1: int, the input number to be compared.
	:param lowest: int, the lowest number for now.
	"""
	if lowest > data1:
		lowest = data1
	return lowest


def average_temp_numbers(times):
	"""
	To count how many temperatures
	were typed.
	:param times: int, how many temperatures has been inputted.
	"""
	times += 1
	return times


def average_temp_amount(data1, summary):
	"""
	To sum up the total temperature.
	:param data1: int, the input number to be compared.
	:param summary: int, the sum up amount.
	"""
	summary += data1
	return summary


def cold_day(data1, cold):
	"""
	To decide how many cold
	days has been input.
	:param data1: int, the input number to be compared.
	:param cold: int, the numbers of cold day(s) to be added.
	"""
	if data1 < 16:
		cold += 1
	return cold


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == "__main__":
	main()
