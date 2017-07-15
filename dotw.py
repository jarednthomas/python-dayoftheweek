# init date at 0s
given_day   = 0
given_month = 0
given_year  = 0

# days of the week in base 7
day_of_week = {
	0:'sunday',
	1:'monday',
	2:'tuesday',
	3:'wednesday',
	4:'thursday',
	5:'friday',
	6:'saturday',
}

# month values
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
	2:28,
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

# century values
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

# promt user for mm/dd/ccyy
while given_month not in range(1,13):
	given_month = input("What month?(1-12) ")

while given_day not in range(1,length_month[given_month]+1):
	given_day = input("What day?  (1-31) ")

while given_year < 1750:
	given_year = input("What year? (ccyy) ")

print "\n" + " %s / %s / %s" % (given_month, given_day, given_year)


# value_day / reduce
value_day = given_day % 7
# value_mm is returned from dict reference
value_mm = value_month[given_month]


# value_cc for part of year
year = str(given_year)
cc = int(year[:2])
yy = int(year[2:])
value_cc = value_century[cc]

# value_yy using formula (yy + (yy div 4)) mod 7
yy_div4  = yy / 4
value_yy = (yy + yy_div4) % 7

# consider leap_mm and leap_yy
is_LeapYear = False
value_ly = 0
if given_month < 3:
	# print "is within range of leap months"
	if given_year % 4 == 0:
		# print "is divisible by four"
		if given_year % 100 == 0:
			# print "is divisible by 100"
			if given_year % 400 == 0:
				# print "is divisible by 400"
				# print "is leap year!"
				value_ly = -1
				is_LeapYear = True
			else:
				# print "is NOT divisibile by 400"
				# print "is NOT leap year"
				is_LeapYear = False
		else:
			# print "is NOT divisible by 100"
			# print "is leap year!"
			value_ly = -1
			is_LeapYear = True
	else:
		#print "is NOT leap year"
		is_LeapYear = False
else:
	# print "is NOT within range of leap months"
	# print "leap not need be considered"
	is_LeapYear = False

# value_year of using yy, cc and ly
value_year = (value_cc + value_yy + value_ly)

# total
total = 0
total += value_mm
total += value_day
total += value_year

# user side math
print " %s + %s + %s = %s" % (value_mm, value_day, value_year, total)

""" for debugging
print "total is %s after adding in day" % total
print "total is %s after adding in month" % total
print "total is %s after adding in cc" % total
print "total is %s after adding in yy" % total
print "total is %s after adding in ly" % total
"""

# final_total
final_total = total

if final_total > 6:
	final_total = final_total % 7

day = day_of_week[final_total]
print "\n" + "%s returns" % final_total
print "%s" % day
