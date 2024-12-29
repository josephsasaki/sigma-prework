
def find_max_and_min(array):
    # Arbitrarily assume min and max are first two elements.
    min, max = array[0], array[1]
    # Iterate through list and update min and max if necessary.
    for x in array:
        min = x if x < min else min
        max = x if x > max else max
    #  Print results
    return [min, max]


print(find_max_and_min([2, 4, 1, 0, 2, -1]))
print(find_max_and_min([20, 50, 12, 6, 14, 8]))
print(find_max_and_min([100, -100]))
