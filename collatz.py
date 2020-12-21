import matplotlib.pyplot as plt
import math

runs = 100 # The largest n value to be considered
stop_at_power_of_two = True # If true, termiminate the Collatz sequence when n is a power of 2.

lastSum = 0
results = []
averages = []
maxes = []

# Return True if n is a power of 2 (including 1)
def isPowerOfTwo(n):
    p = math.log(n, 2)
    return math.floor(p) == math.ceil(p)

# Given n, return the length of the Collatz sequence beginning at f(n)
# If stop_at_power_of_two is True, then we stop when n is a power of 2
# Otherwise, we stop when n is 1
def collatz(n, stop_at_power_of_two):
    if n == 1 or (stop_at_power_of_two and isPowerOfTwo(n)):
        return 1
    if n % 2 == 0:
        return 1 + collatz(n / 2, stop_at_power_of_two)
    else:
        return 1 + collatz(n * 3 + 1, stop_at_power_of_two)

def findAverage(lastSum, nextElement, numElements):
    return (lastSum + nextElement, (lastSum + nextElement) / numElements)

def findMax(lastMax, candidate):
    if lastMax < candidate:
        return candidate
    return lastMax

for s in range(1, runs + 1):
    c = collatz(s, stop_at_power_of_two)
    results.append(c)
    
    lastSum, average = findAverage(lastSum, c, len(results))
    averages.append(average)
    
    if len(maxes) == 0:
        maxes.append(results[0])
    else:
        lastMax = maxes[len(maxes) - 1]
        maxes.append(findMax(lastMax, c))
    if s % (runs / 20) == 0:
        print("%d / %d" % (s, runs))

plt.plot([r for r in range(1, runs + 1)], results)
plt.xlabel('Set Size')
plt.ylabel('Collatz Value')
plt.title('Results of Collatz Values')
plt.show()

plt.plot([r for r in range(1, runs + 1)], averages)
plt.xlabel('Set Size')
plt.ylabel('Average Collatz Value')
plt.title('Average Collatz Values')
plt.show()

plt.plot([r for r in range(1, runs + 1)], maxes)
plt.xlabel('Integer')
plt.ylabel('Max Collatz Value')
plt.title('Max Collatz Values')
plt.show()