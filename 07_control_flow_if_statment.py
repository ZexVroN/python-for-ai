# IF-ELSE
name = "Deni Septiawan"
if name == "Deni Septiawan":
    print("Hallo Captain")
else:
    print("Who are u bruh!")

# IF-ELIF-ELSE
age = 26
if age >= 17:
    print("LFG!")
elif age >= 16:
    print("Cant bruh sorry")
else:
    print("Nahhhh bruh go enjoy your milk!")

# == AND OR NOT ==

# Both must be True
age_check = 20
has_license = True
if age_check >= 17 and has_license:
    print("You can drive!")

# At least one must be True
if weekend or holiday:
    print("No work today!")

# Reverse the condition
if not raining:
    print("Let's go outside!")

has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Enjoy the movie!")
    else:
        print("Need adult supervision")
else:
    print("Buy a ticket first")
