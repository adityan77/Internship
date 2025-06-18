temp = float(input("Enter the temperature: "))

if temp > 35:
    print("Too Hot")
elif temp >= 25 and temp <= 35:
    print("Normal Weather")
elif temp>= 15 and temp < 25:
    print("Cool")
else:
    print("Too Cold")
