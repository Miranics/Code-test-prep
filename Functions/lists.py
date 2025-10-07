def count_odd(numbers):
    count = 0
    for num in numbers:
        if num % 2 != 0:
            count += 1
    return count

print(count_odd([3, 4 ,7, 10, 15]))        
   


