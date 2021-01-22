i = 0
numbers = []

def funkcja(x, i, y):
    while i < x:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + y
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


# print("The numbers: ")
#
# for num in numbers:
#     print(num)

funkcja(6, 0, 2)