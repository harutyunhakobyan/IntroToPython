text = input()

print("The given string: " + text)
print("The USA/usa count is: ", text.count('USA') + text.count('usa'))
text_new = text.replace('usa','USA')
print("The new string: ", text_new.replace('USA','Armenia'))