project = "cake"
difficulty = 1
ingredients = ["flour", "butter", "sugar", "eggs", "cocoa powder", "baking powder"]
print("apple" in ingredients)
print("butter" in ingredients)
print(("eggs" in ingredients) or ("margarine" in ingredients))
print(("eggs" in ingredients) and ("margarine" in ingredients))
flour,butter,sugar,eggs,cocoa_powder,baking_powder = [175, 175, 100, 2, 1, 0.5]
print("flour - ",flour)
print("butter - ",butter)
print("sugar - ",sugar)
print("eggs - ",eggs)
print("cocoa_powder - ",cocoa_powder)
print("baking_powder - ",baking_powder)

a = 15
b = 8
c = 2
print(5*a**2 - a*b + a%2 -a/5)

print(b**3 + 3*a*b - 10*c)

number = int(input("Enter the number: "))
if (number % 2) == 0:
    print(number, "is even")
else:
    print(number, "is odd")