def fib(n):
	if n < 0:
		raise Exception("please input a integer number bigger than 0")
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib(n - 1) + fib(n - 2)
'''
time: O(2^n)
space: O(n)
'''

def fib(n):
	if n < 0:
		raise Exception("please input a integer number bigger than 0")
	if n == 0:
		return 0
	if n == 1:
		return 1
	a, b = 0, 1
	for i in range(n - 1):
		b, a = a + b, b
	return b
'''
time: O(n)
space: O(1)
'''
## dynamic programming: tabulation (bottom up)
def fib(n):
	res = [0, 1]
	if n == 0:
		res[0]
	if n <= 2:
		return 1
	for i in range(2, n + 1):
		res.append(fib(i - 1) + fib(i - 2))
	return res[n]


## dynamic programming: memorization (top down)
def fib(n):
	res = {1:1, 2:1}
	if n <= 2:
		return 1
	if n in res:
		return res[n]
	else:
		res[n] = fib(n - 1) + fib(n - 2)
		return res[n]

'''
Recursion is just a function calling itself, it's not related to dynamic programming, like recursion vs iteration.
Coming to dynamic programming, most DP problems can be solved by top-down recursion or bottoms up approach (iterative) caching intermediate results a technique which is called 'memorization'
One major difference using these two methods to solve a problem is that in 'recursive' top down approach, you need not calculate all the sub-problems, but the bottoms-up approach you calculate all the sub-problems whether they are used in the final solution or not.
'''



