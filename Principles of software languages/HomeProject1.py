
def is_prime(num):
    """
    Cheking if given number is a prime number.

    :param num: Any number
    :return: True or False if given number is prime number.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

#-----------------------------------------------------------------------------------------------
def factorSum(number):
    """
    Canculating the sum of uniqe prime numbers in recieved input

    :param number: Any input number.
    :return: The sum of prime numbers not including the repeat ones.
    """
    if number <= 1:
        print("Please enter a number greater than 1.")
        return

    primes = set()
    divisor = 2

    while number > 1:
        if number % divisor == 0 and is_prime(divisor):
            primes.add(divisor)
            number //= divisor
        else:
            divisor += 1

    print(f"Sum of unique prime numbers: {sum(primes)}")

input_number = int(input("Enter a number greater than 1: "))
factorSum(input_number)

#-----------------------------------------------------------------------------------------------

def interceptPoint(line1, line2):
    """
    Canculating if 2 given lines have an interception point.

    :param line1: Two numners that representm X and Y of first line
    :param line2: Two numners that representm X and Y of second line
    :return: Interception point of 2 lines.
    """
    a1, b1 = line1
    a2, b2 = line2

    if a1 == a2:
        return None

    x_intersection = (b2 - b1) / (a1 - a2)
    y_intersection = a1 * x_intersection + b1

    return (x_intersection, y_intersection)

line1 = (3, 11)
line2 = (5, 1)

result = interceptPoint(line1, line2)

if result:
    print(f"Intersection point: {result}")
else:
    print("Lines are parallel, no intersection point.")

#--------------------------------------------------------------------------------------------
def printNumbers(a, b, c):
    """
    Recursive function to print numbers in order exept 1 given number
    :param a: Starting point number
    :param b: End point number
    :param c: The number u want to exclude
    :return: None
    """
    if a > b:
        return
    if a != c:
        print(a, end=" ")
    printNumbers(a + 1, b, c)

a = 1
b = 10
c = 5

printNumbers(a, b, c)

#--------------------------------------------------------------------------------------------

def listProduct(A, B):
    """
    Creating a new list that duplicates numbers from a given list.

    :param A: List of numbers to duplicate.
    :param B: List of times u want to duplicate param A.
    :return: New list that duplicates A list by B times in any given index.
    """
    result = []
    for a, b in zip(A, B):
        result.extend([a] * b)
    return result

A = [0, 2, 3, 4]
B = [2, 5, 1, 3]
result_list = listProduct(A, B)
print(result_list)

#-------------------------------------------------------------------------------------------
def analyze(text):
    """
    Function to calculate amount of numbers that are greater than 85 in a given string.

    :param text: String that includes floating numbers and separated by comma.
    :return: Amount of numbers greater than 85.
    """
    numbers_str = text.split(',')
    numbers = [float(num) for num in numbers_str]
    count = sum(1 for num in numbers if num > 85)
    return count

text = "45,65,70.4 ,82.6,20.1,90.8,76.1,67.1,79.9,85.1"
result = analyze(text)
print(f"Number of outstanding students: {result}")
