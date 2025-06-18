def calculate_bmi(weight, height):   
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        category = "Normal"
    elif bmi >= 25 and bmi < 30:
        category = "Overweight"
    else:  # bmi >= 30
        category = "Obese"
    return round(bmi, 2), category

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi, category = calculate_bmi(weight, height)

print(f"BMI: {bmi}")
print(f"Category: {category}")
