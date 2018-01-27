#!/usr/bin/env python3
"""
dotw.py
~~~~~~~
Python function that returns the day of the week in the Gregorian Calendar given the Month, Day, and Year
Credit: https://blog.artofmemory.com/how-to-calculate-the-day-of-the-week-4203.html
"""

def calc_dotw(given_month=0,given_day=0,given_year=1749):
	""" Function that returns the day of the week given (mm,dd,ccyy) """
	day_of_week = {
		0:'sunday',
		1:'monday',
		2:'tuesday',
		3:'wednesday',
		4:'thursday',
		5:'friday',
		6:'saturday',
	}
	value_month = {
		1:0,
		2:3,
		3:3,
		4:6,
		5:1,
		6:4,
		7:6,
		8:2,
		9:5,
		10:0,
		11:3,
		12:5,
	}
	length_month = {
		1:31,
		2:29,
		3:31,
		4:30,
		5:31,
		6:30,
		7:31,
		8:31,
		9:30,
		10:31,
		11:30,
		12:31,
	}
	value_century = {
		17:4,
		18:2,
		19:0,
		20:6,
		21:4,
		22:2,
		23:0,
		24:6,
	}
	
	while given_month not in range(1,13):
		given_month = int(input("What month?(1-12): "))
	while given_day not in range(1,(length_month[given_month]+1)):
		given_day = int(input("What day?  (1-31): "))
	while given_year < 1750:
		given_year = int(input("What year? (ccyy): "))

	value_day = given_day % 7
	value_mm = value_month[given_month]
	value_cc = value_century[int(str(given_year)[:2])]
	value_yy = (int(str(given_year)[2:]) + (int(str(given_year)[2:]) // 4)) % 7

	is_LeapYear = False
	value_ly = 0
	if given_month < 3:
		if given_year % 4 == 0:
			if given_year % 100 == 0:
				if given_year % 400 == 0:
					value_ly = -1
					is_LeapYear = True
				else:
					is_LeapYear = False
			else:
				value_ly = -1
				is_LeapYear = True
		else:
			is_LeapYear = False
	else:
		is_LeapYear = False

	value_year = (value_cc + value_yy + value_ly)
	total = value_mm + value_day + value_year

	if total > 6:
		total = total % 7
	day = day_of_week[total]
	return day

if __name__=="__main__":
	print("\n{}\n".format(calc_dotw(1,29,1993)))
