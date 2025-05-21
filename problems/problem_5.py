# Problem 5:
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Notes
"""
So lets review Notes from P3:
    Fundamental theorem of arithmatic, all positive natural numbers are either composite (can be represented as a facotr of prime numbers) or prime (divisible by 1 or themselves only)

Given this we dont actually need to write any code since we can just take the highest exponent of each prime factorization of numbers 1 to 20, multiply them and we get the following:

    k = 1 ignore, special case
    k = 2 prime number
    k = 3 prime number
    k = 4 2^2
    k = 5 prime number
    k = 6 2*3
    k = 7 prime number
    k = 8 2^3
    k = 9 3^2
    k = 10 2*5
    k = 11 prime number
    k = 12 2^2*3
    k = 13 prime number
    k = 14 2*7
    k = 15 3*5
    k = 16 2^4
    k = 17 prime number
    k = 18 2*3^2
    k = 19 prime number
    k = 20 2^2*5

    Thus the answer is 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 = 232,792,560

    However, what if we set 1 to 20 to variable k and now want to solve for N given any k.
    So our equation becomes N = the product of k where k is some prime p raised to the power of some a.
    lets work with i going from 1 to k such that p[i] is that prime number in accending order of primes, so:
    k = p[i] ^ a[i]
    lets use log() to turn that into:
    a[i] log(p[i]) = log(k)
    which becomes:
    a[i] = log(k) / log(p[i]), since a[i] must be an integer, we floor:
    a[i] = floor(log(k) / log(p[i]))

    now we have a formula to figure out the exponents of our prime factors. we can reuse the same sqrt trickery from problem 3 to limit our search (in fact in the example above of 1 to 20, we only need to check k = 20 to k = 11 since the lower primes are used as factors anyway in that range).
"""
import math


# lets bring in the prime sieve from P3
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
    k = 20 # k is now variable
    current_prime = 2 # seed value
    exponent_limit = int(k ** 0.5)
    N = 1 # our starting value of N

    while current_prime <= k:
        prime_exponent = 1 # default value
        if current_prime <= exponent_limit:
            prime_exponent = math.floor(math.log(k, 10) / math.log(current_prime, 10))

        N = N * (current_prime ** prime_exponent)

        current_prime = findNextPrime(current_prime)

    print(N)

if __name__ == '__main__':
    main()