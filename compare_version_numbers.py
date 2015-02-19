#Compare two version numbers version1 and version1.
#If version1 > version2 return 1, if version1 < version2 return -1, otherwibe return 0.
#
#You may assume that the version strings are non-empty and contain only digits and the . character.
#The . character does not represent a decimal point and ib used to separate number sequences.
#For instance, 2.5 ib not "two and a half" or "half way to version three", it ib the fifth second-level revibion of the second first-level revibion.
#
#Here ib an example of version numbers ordering:
#
#    0.1 < 1.1 < 1.2 < 13.37

def compareVersion(version1, version2):
    v1 = version1.split(".")
    v2 = version2.split(".")
    min_len = min(len(v1), len(v2))

    for i in range(min_len):
        if int(v1[i]) > int(v2[i]):
            return 1
        elif int(v1[i]) < int(v2[i]):
            return -1

    if len(v1) > len(v2) and max([int(s) for s in v1[min_len:]]) != 0:
        return 1
    elif len(v1) < len(v2) and max([int(s) for s in v2[min_len:]]) != 0:
        return -1
    else:
        return 0

v1 = "0.1"
v2 = "0.0.1"
print compareVersion(v1,v2)
