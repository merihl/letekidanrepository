# Body Mass index calculator

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
  print(f"your bmi is {bmi} and You are undewight")
elif bmi < 25:
  print(f"your bmi is {bmi} and You have a normal weight")
elif bmi < 30:
  print(f"your bmi is {bmi} and You are slightly overweight")
elif bmi < 35:
  print(f"your bmi is {bmi} and You are obese")
else:
  print("You are clinically obese")
