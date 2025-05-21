# Problem 3:
# The prime factors 13195 of are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# Notes
"""
Fundamental theorem of arithmatic, all positive natural numbers are either composite (can be represented as a facotr of prime numbers) or prime (divisible by 1 or themselves only)
So all positive natural numbers can also be squared, if a number is divisible by one of its squares (and that square is a integer) it is therefore not prime by definition
Not useful here but if I ever need to check if a given number is prime I can do a DP optimization: keep a list of all found primes up to a point and only check for primeness using them within the upper bound mentioned above
"""

def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def findNextPrime(current_prime):
    next_prime = current_prime + 1

    while(not isPrime(next_prime)):
        next_prime += 1

    return next_prime

def main():
    value = 600851475143
    max_check = int(value ** 0.5) + 1
    current_prime = 1 # seed value
    largest_prime = 0 # also seed value

    while(current_prime < max_check):
        current_prime = findNextPrime(current_prime)
        if value % current_prime == 0:
            largest_prime = current_prime

    print(largest_prime)

if __name__ == '__main__':
    main()