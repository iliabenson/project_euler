# Problem 4:
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 X 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Notes
"""
Since multiplication is recipricole and larger numbers produce larger products I start at 999 X 999 and only need to decrement one side at a time until I find a palindrone that is greater then 900009 since that is the lower limit of the largest palindrone product.

900009 / 999 = ~900 which will be my lower bound for left number
"""

def isPalindrome(n):
    if str(n) == "".join(reversed(str(n))):
        return True

    return False

def main():
    left = right = 999
    max = 0

    for left in range(999, 899, -1):
        for right in range(999, 99, -1):
            product = left * right
            if isPalindrome(product):
                if product > max:
                    max = product

    print(max)

if __name__ == '__main__':
    main()