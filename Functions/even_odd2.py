def count_even_odd(numbers):
    count_even = 0
    count_odd = 0
    for num in numbers:
        if num % 2 !=0:
            count_odd += 1
        else:
            count_even += 1
    return count_odd , count_even
    

print(count_even_odd([1, 2, 3, 4, 5, 6]))