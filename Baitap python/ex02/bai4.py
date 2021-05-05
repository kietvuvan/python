str=input()
def return_max(str):
    return max(str, key=str.count)
print(return_max(str))