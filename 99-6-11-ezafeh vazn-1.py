w= int(input(" Enter your weight:"))
h= float(input(" Enter your height:"))
g=h**2

print(g)
BMI=w/g
print(BMI)
if BMI<18.5:
    print("You are underweight")
if 18.5<BMI<25:
    print("You are normal")
if 25<BMI<30:
    print("You are overweight ")
if BMI>30:
    print("You are obese:")
        
print("End weight program")
