"""In a list of weekdays days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], 
which slicing operation would return ['Wed', 'Fri', 'Sun']?"""

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print(days[2:7:2])
print(days[2::2])

"""
Given a list of months months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], 
how would you slice it to get the last quarter of the year in reverse order?
"""
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
print(months[-1:-4:-1])


"""
In a list of prime numbers primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
which slicing operation would return every third prime number starting from the second one?
"""
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(primes[1::3])