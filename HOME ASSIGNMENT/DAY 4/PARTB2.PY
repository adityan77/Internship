# o	If temp > 35, print "Too Hot"
# o	If 25–35, print "Normal Weather"
# o	If 15–24, print "Cool"
# o	Else, print "Too Cold"
temp=int(input("Enter The Tempreature:-"))
if temp>=35:
    print("Too Hot")
elif temp>=25 and temp<35:
    print("Normal Weather")
elif temp>=15 and temp<25:
    print("Cool")
else:
    print("Too Cool")
    