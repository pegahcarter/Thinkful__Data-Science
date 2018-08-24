'''
Project Euler

Now that you’ve learned a little bit about algorithms and written some really simple but essential code,
it’s time to put those skills to the test. There is one resource above all that helps data scientists
and other engineers practice their mathematical programming skills: Project Euler.

Project Euler is a fantastic set of mathematical programming problems.
Use the skills we’ve discussed here to find efficient solutions to the first 10 problems.
Once you’ve found your own solutions look around the web for others’ Python solutions to see other ways
people have approached these problems.

It’s a good idea to come back to Project Euler and continue to work through these problems.
They are a really great way to sharpen your mathematical programming.

1. Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
'''
result = sum([i for i in range(1000) if (i % 3 == 0 or i % 5 == 0)])
'''
2. Even Fibonacci Numbers
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms
'''
def is_even(x):
	if x % 2 == 0:
		return True

def under_limit(x):
	if x < 4000000:
		return True

nums = (1, 2)
total = 2

while True:
	a = sum(nums)
	b = nums[1] + a
	if under_limit(a) and under_limit(b):
		if is_even(a):
			total += a
		if is_even(b):
			total += b
	elif under_limit(a) and is_even(a):
		total += a
	else:
		break

	nums = (a, b)
'''
3.
What is the largest prime factor of the number 600851475143?
'''
def find_prime(num):
	prime_factor = 1
	x = 2
	while x < num / x:
		if num % x == 0:
			prime_factor = x
			num /= x
		else:
			x += 1

	if prime_factor < num:
		prime_factor = num

	return prime_factor

find_prime(600851475143)
'''
4.
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
palindrome = 1
for x in range(100, 999):
	for y in range(x, 999):
		product = str(x * y)
		if product[0] == product[len(product) - 1] and product[1] == product[len(product) - 2]:
			if int(product) > palindrome:
				if len(product) == 5:
					palindrome = int(product)
				elif product[2] == product[3]:
					palindrome = int(product)

print(palindrome)
'''
5.
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
x = 2520
while True:
	for num in range(2, 21):
		i = num
		if x % num != 0:
			x += 10
			break

	if i == 20:
		print(x)
		break
'''
6.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
import numpy as np
nums = list(range(1,101))
sum_squares = np.dot(nums, nums)
square_sums = np.square(sum(nums))
print(str(square_sums - sum_squares))
'''
7.
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''
def is_prime(num):
	if num % 5 == 0:
		return False
	for x in range(3, int(num**0.5) + 1):
		if num % x == 0:
			return False
	return True

prime_count = 6
x = 15

while prime_count < 10001:
	x += 2
	if is_prime(x):
		prime_count += 1

print(x)
'''
8.
The four adjacent digits in the 1,000 digit number below that have the greatest product are 9 * 9 * 8 * 9 = 5832
Find the 13 adjacent digits in the 1000-digit number that have the greatest product.  What is the value of this product?
'''
large_number = [
'73167176531330624919225119674426574742355349194934',
'96983520312774506326239578318016984801869478851843',
'85861560789112949495459501737958331952853208805511',
'12540698747158523863050715693290963295227443043557',
'66896648950445244523161731856403098711121722383113',
'62229893423380308135336276614282806444486645238749',
'30358907296290491560440772390713810515859307960866',
'70172427121883998797908792274921901699720888093776',
'65727333001053367881220235421809751254540594752243',
'52584907711670556013604839586446706324415722155397',
'53697817977846174064955149290862569321978468622482',
'83972241375657056057490261407972968652414535100474',
'82166370484403199890008895243450658541227588666881',
'16427171479924442928230863465674813919123162824586',
'17866458359124566529476545682848912883142607690042',
'24219022671055626321111109370544217506941658960408',
'07198403850962455444362981230987879927244284909188',
'84580156166097919133875499200524063689912560717606',
'05886116467109405077541002256983155200055935729725',
'71636269561882670428252483600823257530420752963450']
import numpy as np
large_number = ''.join(large_number)

max_product = []
for x in range(1,5):
	nums = list(map(int, [large_number[x:x+14]]))
	print(len(nums))
	if 0 in nums:
		continue
print(max_product)
'''
9.
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
for a in range(1,1001):
	for b in range(a+1, 1001):
		c = 1000 - a - b
		if c < a or c < b:
			break
		if a**2 + b**2 == c**2:
			print(a * b * c)
'''
10.
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''
total = 17
for i in range(11, 2000001, 2):
	if is_prime(i):
		total += i

print(total)