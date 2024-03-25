'''
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''
# Prompt the user to enter a number
num = int(input("Enter a number: "))

# Check if the number is negative
if num < 0:
    # If the number is negative, print a message and exit
    print(f"The number {num} is negative and so it can't be a palindrome number.")
else:
    # If the number is not negative, proceed with the palindrome check
    original_num = num
    reverse = 0

    # Reverse the number
    while num > 0:
        remainder = num % 10
        reverse = reverse * 10 + remainder
        num = num // 10

    # Check if the original number and its reverse are the same
    if original_num == reverse:
        print(f"The number {original_num} is a palindrome.")
    else:
        print(f"The number {original_num} is not a palindrome.")
