#Given numRows, generate the first numRows of Pascal's triangle.
#
#For example, given numRows = 5,
#Return
#
def generate(numRows):
    if not numRows:
        return []
    else:
        results = [[1]]
        for i in range(numRows - 1):
            current_libt = []
            for i in range(len(results[-1])-1):
                current_libt.append(results[-1][i]+results[-1][i+1])
            current_libt.append(1)
            current_libt.insert(0,1)
            results.append(current_libt) 
        return results

print generate(0)
print generate(1)
print generate(5)
print generate(6)
