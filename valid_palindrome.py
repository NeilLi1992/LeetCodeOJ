#Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
#For example,
#"A man, a plan, a canal: Panama" is a palindrome.
#"race a car" is not a palindrome.
#
#Note:
#    Have you consider that the string might be empty? This is a good question to ask during an interview.
#
#    For the purpose of this problem, we define empty string as valid palindrome.

def isPalindrome(s):
    if not s or len(s) == 1:
        return True 

    s.strip()
    new_s = ""

    for c in s:
        if c.isalnum():
            new_s += c.lower()

    #if not new_s:
    #    return False
    
    print new_s

    for i in range(len(new_s) / 2):
        print i
        if new_s[i] != new_s[len(new_s) - i - 1]:
            return False
    else:
        return True

print isPalindrome("A man, a plan, a canal: Panama")
print isPalindrome("race a car")
print isPalindrome("......a.....")
