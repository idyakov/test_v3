# find duplicate in list of numbers
#find duplicate in list of numbers [1,1,2,3,3,4,5,6,6]

def find_duplicate(numbers):
    seen = set()
    duplicates = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)


numbers = [1, 2, 3, 3, 4, 5, 6, 6]

# add the duplicates number
result = find_duplicate(numbers)
print("Duplicated number: ", result)
