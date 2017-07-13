#---------------------------------------------------------------------------------------------
# Description: Program plots the gaps between any given formalized list of primes
#
# Author: H.G. Arama
# Date: 06/17/2017
#---------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

# Derive y from given x value taken from

def getYFrom(x):
    y = [1]
    for i in range(0, (len(x) - 1)):
        if (i != len(x)):
            y.append(abs(x[i] - x[i + 1]))
        else:
            break;
    return y

# Given a file of primes formatted in columns this method will feed the
# primes line by line and parse them into a list in order to be 'formalized' for use in the file
def formalizeFile(file, endDigitLength):
    gap = ' '
    strGap = '{}'.format(gap * endDigitLength)
    file = file.replace(strGap, ',')

    if endDigitLength == 1:
        file = file.replace('\n', '')
        file = file.split(',')
        return file
    else:
        return formalizeFile(file, endDigitLength - 1)


file_of_primes = open('1000_primes', 'r')
file_of_primes = file_of_primes.read()

file_of_primes = file_of_primes.replace('      2', '2')

file_of_primes = formalizeFile(file_of_primes, 6)

for i in range(0, len(file_of_primes)):
    file_of_primes[i] = int(file_of_primes[i])

print(file_of_primes)

x = file_of_primes #list element
y = getYFrom(x)

plt.plot(x, y, 'ro')
plt.axis([0, 8000, 0, 50])
plt.show()