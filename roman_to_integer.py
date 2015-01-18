#Given a roman numeral, convert it to an integer.
#
#Input is guaranteed to be within the range from 1 to 3999.

def romanToInt(s):
    if not s:
        return 0
    
    digits = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
    }

    sum = 0
    for i,c in enumerate(s):
        if c not in digits.keys():
            return 0
        elif c in ["I","X","C"] and i + 1 < len(s) and digits[c] < digits[s[i+1]]:
            sum += -1 * digits[c]
        else:
            sum += digits[c]

    return sum

print romanToInt("IV")
print romanToInt("MDCCCLXXX")
print romanToInt("VIII")
print romanToInt("MMMCCCXXXIII")
