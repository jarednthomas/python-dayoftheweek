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
while given_month < 1:
	given_month = input("What month?(1-12) ")

while given_day < 1:
	given_day = input("What day?  (1-31) ")

while given_year < 1:
	given_year = input("What year? (ccyy) ")

print ""
# calc value of day / reduce
value_day = given_day % 7

# ---- value of month is returned with dict
value_mm = value_month[given_month]

# calc value of cc using dict
year = str(given_year)
cc = int(year[:2])
yy = int(year[2:])
value_cc = value_century[cc]

# calc value of yy using formula (yy + (yy div 4)) mod 7
yy_div4  = yy / 4
value_yy = (yy + yy_div4) % 7

# consider leap_mm and leap_yy
value_ly = 0

if given_month < 3:
	print "is within range of leap months"
	if given_year % 4 == 0:
		print "is divisible by four"
		if given_year % 100 == 0:
			print "is divisible by 100"
			if given_year % 400 == 0:
				print "is divisible by 400"
				print "is leap year!"
				value_ly = -1
			else:
				print "is not divisibile by 400"
				print "is not leap year"
		else:
			print "is not divisible by 100"
			print "is leap year!"
			value_ly = -1
	else:
		print "is NOT leap year"
else:
	print "is NOT within range of leap months"
	print "leap not need be considered"

# calc total
print ""
total = 0
total += value_day
print "total is %s after adding in day" % total
total += value_mm
print "total is %s after adding in month" % total
total += value_cc
print "total is %s after adding in cc" % total
total += value_yy
print "total is %s after adding in yy" % total
total += value_ly
print "total is %s after adding in ly" % total
print ""

# final_total
final_total = total

if final_total > 6:
	final_total = final_total % 7

day = day_of_week[final_total]
print "%s returns" % final_total
print "%s" % day
