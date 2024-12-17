name = input("Who are you? ")
age = int(input("\nHow old are you? "))

print(f"Hi, nice to meet you, {name}, your name data is {type(name)} and age is {type(age)}")
print("Your age is " + str(age) + " you are still young!\n")

if age < 10:
    print("You are a child")
elif age > 9 and age < 18:
    print("You are a teenager")
else:
    print("You are an adult")