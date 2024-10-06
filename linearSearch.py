pos = -1

def search(list, n):
    i= 0
    while i<len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i +=1
    return False

list = [3,6,9,8,7,2]
n= 7

if search(list, n):
    print(f"Found at {pos+1}")
else:
    print("Not found")