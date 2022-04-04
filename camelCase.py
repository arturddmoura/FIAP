#Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

#Examples

#"the-stealth-warrior" gets converted to "theStealthWarrior"
#"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

word = input("Please input the word: ")

temp = word.replace('-',' ')
temp = temp.replace("_", " ")
temp = temp.split()

res = temp[0] + ''.join(ele.title() for ele in temp[1:])

print(res)