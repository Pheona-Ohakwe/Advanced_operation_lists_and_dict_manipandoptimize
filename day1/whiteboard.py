# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized 
# (known as Upper Camel Case, also often referred to as Pascal case). 
# The next words should be always capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
# "lets_go_team" gets converted to "letsGoTeam"




def solution(string):
    new_string = ""
    capitalize = False
    for char in string:
        if char == "-"or char =="_":
            capitalize = True
        else:
            if capitalize == True:
                new_string += char.upper()
                capitalize = False
            else:
                new_string += char  
    return new_string
           
        



