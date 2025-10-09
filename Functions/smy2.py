def greater_than_average(numbers):
    average = sum(numbers) / len(numbers)
    result = []
    for num in numbers:
        if num > average:
            result.append(num)
    return result

print(greater_than_average([1, 2, 3, 4, 5, 6]))



