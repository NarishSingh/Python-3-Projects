import array as arr
from datetime import datetime as dt  # import only one thing from module

name = "Narish"

print('Hello world')
print(name)
print('Hello ' + name)
print(f"Hello {name}")
print('''He said "I don't know"''')  # lets you write with as many diff ' " as possible

myList = ["a", 1, "Long", 3.2]  # lists can put all types in a myList

print(myList)
# list.append("AYYYYY")
print(myList)

myTuple = ("a", 1, "Long", 3.2)  # tuples are like lists but are immutable
print(myTuple)

new_array = arr.array('i', [1, 2, 3])  # declaring an array type of integer
print(new_array[1])
new_array.append(4)
print(new_array)

# dictionaries = hashmaps, keys must be enclosed in ""
car = {
    "make": "ford",
    "model": "focus",
    "year": 2017
}
print(car)
print(car["model"])

car['color'] = "blue"  # adding new kv
print(car["color"])

# if else else if
num = -5
if num < 0:
    print("number is negative")
    num *= -1
elif num > 0:
    print("number is positive")
else:
    print("number is 0")

# while loops
nums = [1, 2, 3, 4, 5]
i = 0
while i < len(nums):
    print(nums[i])
    i += 1

print(sum(nums))

# for reach loop
for n in nums:
    print(n)

# for with iterator
for i in range(len(nums)):
    print(i)

for i in range(len(myList)):
    print(f"{i} - {myList[i]}")

for i in range(5):
    if i == 2:
        continue
    print(i)

for i in range(10):
    if i == 7:
        break
    print(i)


# function
def fibonacci(n: int) -> list:
    """
    Get first few nums of fibonacci seq
    :param n: {int} how many elements of sequence to print
    :return: {list} fibonacci sequence up until param
    """
    a = 0
    b = 1
    sequence = [0]
    while b <= n:
        sequence.append(b)
        c = a + b
        a = b
        b = c
    return sequence


print(fibonacci(100))

# date time class
print(dt.now())
