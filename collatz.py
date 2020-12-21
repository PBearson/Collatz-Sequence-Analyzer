import matplotlib.pyplot as plt

runs = 1000000 # Change this to whatever you want

lastSum = 0
results = []
averages = []
maxes = []

def collatz(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + collatz(n / 2)
    else:
        return 1 + collatz(n * 3 + 1)

def findAverage(lastSum, nextElement, numElements):
    return (lastSum + nextElement, (lastSum + nextElement) / numElements)

def findMax(lastMax, candidate):
    if lastMax < candidate:
        return candidate
    return lastMax

for s in range(1, runs + 1):
    c = collatz(s)
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