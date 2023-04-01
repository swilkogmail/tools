#!/usr/bin/env python3
x = [[[1,2], [3,4]], [[5,6],[7,8]]]

print(x)
print(x[0]) # prints the first value in the list [[1, 2], [3, 4]]
print(x[1]) # prints the second value in the list [[5, 6], [7, 8]]
print(x[0][0]) # prints the first value in the first nested list [1, 2]
print(x[1][1]) # prints the second value in the second nested list [7, 8]

def func(data): # [[1,2],[3,4]]
    res = data[0][0] # a list [1] so res = 1
    print(f"initial value of res is: {res}")
    for da in data: # [1, 2], [3, 4]
        print(f"da is: {da}")
        for d in da: # 1, 2, 3, 4
            print(f"d is: {d}")
            if res < d: # first: res = 1, d = 1 return false
                        # second: res = 1 d = 2 return true
                        # third: res = 2 d = 3 return true
                        # fourth: res = 3 d = 4 return true
                res = d # res = 1, res = 2, res = 3, res = 4
    return res # 

print(func(x[0])) # we call the function passing in [[1,2],[3,4]]
