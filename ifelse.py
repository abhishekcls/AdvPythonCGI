age=int(input("Enter your age: "))
print(age)
print(type(age))
gen=input("Enter your gender: ")

#check whether the age is eligible to vote
if age>=18 and gen=='F':
    print("Eligible to Marry")
elif age>=21 and gen=='M':
    print("Eligible to Marry")
else:
    print("NOT eligible to Marry")

#check eligibility to marry