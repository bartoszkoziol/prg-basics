<!--
(c) Janusz Stal
Krakow University of Economics
Department of Informatics
stalj@uek.krakow.pl
-->

# FUNCTIONS

## 1. Introduction

1. Functions are reusable blocks of code that perform a specific task. They allow you to break down complex problems into smaller, more manageable parts, and help in avoiding code repetition by enabling reuse of the same block of code with different inputs.

    Every function has a name. To execute the code inside a function, you "call" the function by using its name followed by parentheses, including any arguments required by the function. 

    For example, if you want to display information on the screen, you use the print() function, using its name and, in parentheses, the function's arguments, if any are required.

    ```python
    print('Hello World')
    ```

## 2. Built-in Functions

1. There are a number of built-in functions, ready to use, e.g. len(), print(), input() or type(). 

    <https://docs.python.org/3/library/functions.html>

    Using built-in Python functions, write a program that calculates and displays:

    * the largest number: 7,5,6,3,8,2
    * the smallest number: 4,7,2,3,9,8
    * length of the phrase: \"computer science\"
    * letter read from the keyboard
    * number representing the string \"20303\"
    * binary string representing decimal number 304
    * hexadecimal string representing decimal number 304
    * integer representing the Unicode code of the € sign
    * absolute value of -17

    ```python
    ###
    # Program for testing built-in functions
    #
    max_number = max(7,5,6,3,8,2)
    print('Max number of 7,5,6,3,8,2 is', max_number)

    min_number = min(4,7,2,3,9,8)
    print('Min number of 4,7,2,3,9,8 is', min_number)

    str_length = len("computer science")
    print('The number of characters in "computer science" is', str_length)

    ...
    ...
    ```

## 3. Using Modules

1. In addition to the built-in functions, you can use numerous functions available in ready-to-use modules. One example is the \'math\' module.

    <https://docs.python.org/3/library/math.html>

    Using functions and constants available in the \'math\' module, write a program that calculates and displays:

    * square root of 7
    * natural logarithm of 5
    * sine of 90 degrees

    ```python
    ###
    #
    #

    # To use the functions available in an external module,
    # you must include that module in your program.
    import math

    square_root = math.sqrt(7)
    print('A square root of 7 is', square_root)
    
    ...
    ...
    ```

1. Write a program that generates and displays a random number between 1 and 6, similar to rolling a dice. Use one of the functions from the **random** module to generate a random integer within a given range.

    ```python
    import random

    ...
    ...
    ```

## 4. Defining a Function

1. Watch the videos on defining a function:

    <https://youtu.be/89cGQjB5R4M?feature=shared>

    <https://youtu.be/NE97ylAnrz4?feature=shared>

1. A function is defined using the def keyword, followed by the function name, parentheses, and a colon. Inside the parentheses, you can specify parameters that the function can accept. The function's code block is indented.

    ```python
    def function_name(parameters):
        # Code block (function body)
        return result  # Optional: Returns a value
    ```

    Components of a Function:

    * **def**: Keyword used to define a function.
    * **function_name**: The name of the function. It should be descriptive of the task the function performs.
    * **parameters**: Optional inputs that the function accepts. They are defined inside the parentheses.
    * **Function Body**: Code block that contains the logic of the function. This code is executed whenever the function is called.
    * **return**: Optional statement that specifies the value to be returned by the function.

    Take a look at the function below that allows you to sum two numbers. The add function takes two parameters, a and b, and returns their sum. The returned value is stored in the variable sum_value and then printed.

    ```python
    def add(a, b):
        result = a + b
        return result

    sum_value = add(5, 3)
    print(sum_value)  # Output: 8
    ```

1. Define a function **triangle_area** that calculates and returns the area of ​​a triangle with sides a, b, and c. Use Heron's formula:

    <https://en.wikipedia.org/wiki/Heron%27s_formula>

    Write a program that calculates the area of ​​a triangle based on the lengths of the triangle's sides read from the keyboard. Use the defined function. Then calculate the area of ​​the triangle for the following dimensions of sides a, b, and c:

    * 3, 4, 5 (result is 6)
    * 5, 12, 13 (result is 30)
    * 7, 24, 25 (result is 84)

1. Define a function that calculates and returns the sum of the digits in a number. Then write a program that reads a number from the keyboard and displays the sum of its digits.

    ```python
    ###
    # Calculates the sum of the digits in a number
    #
    def digit_sum(number):
        ...
        ...
        return ...
    
    any_number = int(input('Enter integer number: '))
    result = digit_sum(...)
    print('The sum of the digits in the number ... is ...')
    ```

1. Define a function that calculates the final grade for a test based on the number of points obtained, according to the rules:

    * Less than 10 points, final grade: Fail
    * At least 10 points, final grade: Satisfactory
    * At least 14 points, final grade: Good
    * At least 18 points, final grade: Excellent

    ```python
    ###
    # Calculates the final grade for a test based
    # on the number of points obtained
    #
    def pts_to_grade(points):
        grade = ''
        if points >= 18:
            grade = 'Excellent'
        ...
        ...
        return grade

    test_result = 15
    final_grade = pts_to_grade(test_result)
    print('You scored ... points on the test. Your final grade is ...')
    ```


1. Define a function that returns the full name of a day of the week based on its number.

    ```python
    ###
    # Function that returns the full name of a day of the week
    # based on its number
    #
    def day_name(day_number):
        result = ''
        if day_number == 1:
            result = 'Monday'
        elif day_number == 2:
            ...
        ...
        ...
        return result

    # Function usage
    print('The name of day 5 in the week is', day_name(5))
    print('The name of day 3 in the week is', day_name(3))
    print('The name of day 7 in the week is', day_name(7))
    ```

1. The ICAO (International Civil Aviation Organization) phonetic alphabet is used internationally for spelling out letters in radio communication. The icao.py program contains a function that returns the corresponding word for a given letter. Complete the program to spell out a name entered from the keyboard.

## 5. Dividing Program Code into Modules

1. Familiarise yourself with dividing a program code into modules:

    <https://www.w3schools.com/python/python_modules.asp>

    <https://docs.python.org/3/tutorial/modules.html>

1. The converters.py file defines two functions for converting length units (cm-->m and m-->cm). The test_converters.py file uses these functions to convert values.

    Define the following functions in the converters.py file that allow you to:

    * convert centimeters to inches
    * convert feet and inches to centimeters

    YThen complete the main program to test the added functions.

1. In the module mykeyboard.py, define a function read_number() that returns an integer number entered from the keyboard. The function should print a text prompting user to enter data \'Enter a number: \'. Then, use the function to read two numbers from the keyboard. To test the function, use the \_\_name\_\_ variable. Display the sum of two entered numbers. Sample result:

    Enter a number: 34\
    Enter a number: 7\
    34 + 7 = 41

## 7. Practice Makes Perfect

1. In the module mymath.py, define the function generate_number() that creates and returns random integer number in the range of \<1,9\>. Then create a main program, in which, first import modules mymath.py and mykeyboard.py, you created earlier. The program is a simple guessing game. The user enters a one-digit number from the keyboard. The computer then generates a random one-digit number. If the numbers match, the user wins the game. Sample result:

    Enter a number: 7\
    Computer number: 7\
    You won the game!!

1. Each month of a calendar year can be expressed by its name or by a number that indicates the position of the month in year. In a separate module, define a function month(n) that returns a month name based on the month number (values from 1 to 12). Then, create a program to display the name of the month 7. Import the module with the created function. Sample result:

    Enter month number: 9\
    The name of month 9 is September

1. Create a program that calculates how many times the given letter appears in any text. Then create a program and check how many times the letter 'e' appears in the text below. In a separate module, define a function for making calculations. Sample result:

    You never get a second chance to make a first impression\
    The number of letter \'e\': 7

1. In a separate module, define a function that checks if the number is within the range \<x, y\>. The function returns a boolean value. Then, create a program and use the function you defined. Sample result:

    A number: 7\
    Number 7 in the range \<2,15\>: yes

1. Define an anonymous function that returns True when the first number is greater than the second one. Otherwise returns False. Use a conditional operator. Then, check the function for pairs of numbers:

    34, 25 and 19,23.

1. Define an anonymous function that returns True when a number is even or False otherwise.

1. The credit card number consists of 16 digits. In a separate module, define a function f(card_number) that masks the card number. The function returns a character string in which only the first two and the last four digits of the card number are visible. The remaining digits of the card number are replaced with an asterisk. Then, create a program that masks some credit card digits. Import the module with the created function. Finally, display the credit card number. Sample result:

    f(\"5290312400019022\") returns \"52\*\*\*\*\*\*\*\*\*\*9022\"

1. The binary numerical system uses two symbols to represent a number: 0 and 1. Define a function f(binary_number) that returns True if the given string of digits is a valid binary number, or False otherwise. Sample result:

    f(\"101101\") returns True\
    f(\"1311a10100\") returns False

1. The vending machine accepts 1, 2 and 5 PLN coins. Define a function f(amount_to_pay) that returns the minimum number of coins that can be used to pay for the purchased product. Sample result:

    f(23) returns 6\
    f(8) returns 3\
    f(2) returns 1\
    f(0) returns 0

1. Create a function f(number, even) that computes the sum of the digits of a number. When the value of the even parameter is True, the function returns the sum of the even digits. When the value of the even parameter is False, the function returns the sum of the odd digits. Sample result:

    f(3124,True) returns 6\
    f(3124,False) returns 4\
    f(20576,False) returns 12\
    f(20576,True) returns 8\
    f(13115,True) returns 0

1. Define the function f(x,y) that returns the number of negative even numbers in the range \<x,y\>. Sample result:

    f(-7,8) returns 3\
    f(-1,11) returns 0

1. Define the function f(n1,n2,n3), which returns True if at least one of the numbers n1,n2,n3 is negative or False otherwise. Sample result:

    f(11,6,-4) returns True\
    f(5,4,14) returns False

1. Define a function f(n) that returns a string of n asterisks, separated by a slash sign. Sample result:

    f(4) returns \"\*/\*/\*/\*\"\
    f(1) returns \"\*\"

1. Define the function f(n), which returns numbers from 1 to n as a string. Sample result:

    f(11) returns \"1234567891011\"\
    f(4) returns \"1234\"

1. Two numbers and an operator are given. Define a function f(number1,number2,operator) that returns the result of an arithmetic operation. The available operators are +,-,\*,%,\*\*. Sample result:

    f(2,3, \"+\") returns 5\
    f(2,3, \"%\") returns 2\
    f(2,3, \"\*\*\") returns 8\
    f(2,3, \"\*\") returns 6\
    f(2,3, \"-\") returns -1

1. A device in a door registers people entering and leaving a room.The + sign means a person entering a room and the -- sign a person leaving a room. Define the function f(detector) that returns True if at least 3 people were in the room at the same time, or False otherwise. Sample result:

    f(\"+-+++-+\-\--\") returns True\
    f(\"+-+-+-+-\") returns False\
    f(\"+-++-+\--\") returns False\
    f(\"+-++-++-+\-\--\") returns True

1. Define the function f(n), which returns the n-th value of the Fibonacci sequence. The sequence is defined as follows: the first value of the sequence is 0, the second value is 1. Each subsequent value is the sum of the previous two. Sample result:

    f(5) returns 3\
    f(9) returns 21

1. A palindrome is an expression that sounds the same when read backwards. Define a function f(palindrome) that returns True if the expression is a palindrome or False otherwise. Sample result:

    f(\"radar\") returns True\
    f(\"12-11-21\") returns True\
    f(\"book\") returns False

1. A sentence is an ordered group of words separated by spaces. Define a function f(sentence) that returns a sentence with spaces removed. Sample result:

    f(\"integrated development environment\") returns
    \"integrateddevelopmentenvironment\"\
    f(\"A programming language is a system of notation for writing
    computer programs\") returns
    \"Aprogramminglanguageisasystemofnotationforwritingcomputerprograms\"

1. Define a function f(number) that returns the sum of repeated digits in a number. Sample result:

    f(1027) returns 0\
    f(230335) returns 9\
    f(513553007) returns 21

1. Define the function f(n) that returns the n-th prime number. A prime number is a natural number greater than 1, divisible by 1 and that number. Sample result:

    f(1) returns 2\
    f(5) returns 11

1. Define the function f(number1,number2,number3), which returns the difference between the largest and smallest numbers. Sample result:

    f(7,4,9) returns 5\
    f(2,12,8) returns 10

1. A text contains any number of words. Define a function f(name) that returns the acronym (first letters of all words). Sample result:

    f(\"Internet of Things\") returns \"IoT\"\
    f(\"For Your Information\") returns \"FYI\"\
    f(\"Python\") returns \"P\"

1. A valid password should consist of at least six different characters. Define a function f(password) that returns True if the password is correct or False otherwise. Sample result:

    f(\"ax15\") returns False\
    f(\"book123\") returns False\
    f(\"A2water3\") returns True\
    f(\"qwerty\") returns True\
    f(\"\") returns False

1. An expression contains operators for adding and subtracting single-digit numbers. Define a function f(expression) that returns the value of the expression. Sample result:

    f(\"2+3\") returns 5\
    f(\"3+8+1\") returns 12\
    f(\"2+3-4+5-0\") returns 6

1. Define the function f(x,y), which returns the sum of numbers in the range \<x,y\> that are completely divisible by 2 and 3 and not divisible by 4. Sample result:

    f(1,20) returns 24\
    f(10,30) returns 48

1. Define a function f(text) that returns the given text with all characters separated by \"-\" (minus sign). Example:

    f(\"Univesity\") returns \"U-n-i-v-e-r-s-i-t-y\"\
    f(\"UE\") returns \"U-E\"\
    f(\"x\") returns \"x\"\
    f(\"\") returns \"\"

1. Products are marked with a special code consisting of 3 digits and afourth control digit. The forth digit is determined by calculating the remainder of dividing the sum of the first three digits by 7. Define a function f(product_code) that returns True if the product code is correct or False otherwise. Sample result:

    f(\"1082\") returns True\
    f(\"2035\") returns True\
    f(\"1114\") returns False\
    f(\"7071\") returns False

1. The sequence of digits contains the number of points rolled with a dice. Define a function f(dice) that returns a number specifying the number of dice rolled the most times in a row. Sample result:

    f(\"5233165554211\") returns 5\
    f(\"2133\") returns 3

1. The following function calculates the factorial recursively. Try to analyse the function. Do you understand how it works? Then, write a program and use the function to calculate the factorial value for n = 5.

    def factorial(n):\
    \
    \# 0! = 1, 1! = 1\
    if n==0 or n==1:\
    return 1\
    \
    \# n! = n \* (n-1)!\
    if n \> 1:\
    return n \* factorial(n-1)

1. Define a function sum(n) that for the given natural number n calculates the sum of all natural numbers between 1 and n. Apply recursion. Then, create a program that calculates the sum of natural numbers in the range \<1,10\>.

1. Define a function power(x, n) that calculates x^n^. Apply recursion. Then, calculate 5^3^.

    Tip: x^n^ = x \* x^n-1^
