def is_zigzag(numbers):
    result = []
    for i in range(len(numbers)-2):
        a = numbers[i]
        b = numbers[i+1]
        c = numbers[i+2]
        if (a < b > c) or (a > b < c):
            result.append(1)
        else:
            result.append(0)
    return result        
      
        

print(is_zigzag([1, 2, 1, 3, 4])) 



