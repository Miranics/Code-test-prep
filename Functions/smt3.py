def count_pos_sum_neg(numbers):
    count_pos = 0
    sum_neg = 0

    for num in numbers:
        if num > 0:
            count_pos += 1
        elif num < 0:
            sum_neg += num

    return count_pos, sum_neg



print(count_pos_sum_neg([1, -2, 3, 4, -5]))
