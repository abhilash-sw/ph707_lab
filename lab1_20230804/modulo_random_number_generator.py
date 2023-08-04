#####################################################
# @Author: Abhilash Sarwade
# @Date:   2023-08-03 09:03:37 am
# @email: sarwade@ursc.gov.in
# @File Name: modulo_random_number_generator.py
# @Project: lab1_20230804
#
# @Last Modified time: 2023-08-04 12:58:50 pm
#####################################################

import numpy as np
import matplotlib.pyplot as plt

a = 10**8 + 1
c = 10**8 + 3
m = 10**2 + 7


def modulo_random_generator(x): 
    return np.mod(a*x + c, m)

N_samples = 1000
random_numbers = modulo_random_generator(np.arange(1, N_samples+1))

# Simulating coin toss experiment from generated random numbers
random_coin_toss = random_numbers % 2 == 0

random_coin_toss.astype('int')  # Converting from boolean to integer

nHeads = sum(random_coin_toss == 0)
nTails = sum(random_coin_toss == 1)

print('# Estimating Heads/Tails distribution from random numbers')
print(f'Number of heads = {nHeads}')
print(f'Number of tails = {nTails}')


# Physical coin toss experiment
phy_coin_toss = np.loadtxt('coin_toss_samples.txt')

nHeads_phy = sum(phy_coin_toss == 0)
nTails_phy = sum(phy_coin_toss == 1)

print('# Physical Heads/Tails distribution')
print(f'Number of heads = {nHeads_phy}')
print(f'Number of tails = {nTails_phy}')


# Statistical characteristics of generated random numbers
print('# Random Number Distribution Properties:')
print(f'Minimum Value: {random_numbers.min()}')
print(f'Maximum Value: {random_numbers.max()}')
print(f'Mean: {random_numbers.mean()}')
print(f'Standard Deviation: {random_numbers.std():.5f}')

# Expected statistical characteristics of ideal uniform discrete distribution
p = random_numbers.min()
q = random_numbers.max()
n = (q-p+1)

print(f'# Uniform Distribution (Discrete) Properties (between {p} and {q})')
print(f'Minimum Value: p = {p}')
print(f'Maximum Value: q = {q}')
print(f'Mean: (p+q)/2 = {(p+q)/2}')
print(f'Standard Deviation: sqrt((n^2 - 1)/12) = {np.sqrt((n**2 - 1)/12):.5f}')


## Uniform Distribution Histogram
bins = np.arange(random_numbers.min(), random_numbers.max()+2)
hst, bins = np.histogram(random_numbers, bins)

fig, ax = plt.subplots()
ax.bar(bins[:-1], hst, label='Observed Histogram')
xlims = ax.get_xlim()
ax.axhline(N_samples/n, xmin=(p-xlims[0]-1)/(xlims[1]-xlims[0]), xmax=(
    q-xlims[0]+1)/(xlims[1]-xlims[0]), ls='--', color='k', label='Uniform Dist.')

ax.set_ylim([0,15])
ax.legend()
ax.set_xlabel('Random Number',fontsize=26)
ax.set_ylabel('Frequency', fontsize=26)
fig.savefig('rand_distribution.pdf')

## Characteristic Function
def characteristic_func(t, X): 
    return np.mean(np.exp(t*X))

def th_characteristic_func(t, p, q): 
    return (np.exp(p*t) - np.exp((q+1)*t))/(q - p + 1)/(1 - np.exp(t))

t = np.logspace(-5, 0, 100)
calc_char = []
theo_char = []
for ti in t:
    calc_char.append(characteristic_func(ti, random_numbers))
    theo_char.append(th_characteristic_func(ti, p, q))

fig, ax = plt.subplots()
ax.loglog(t, calc_char, label='Calculated')
ax.loglog(t, theo_char, label='Theoretical')
ax.legend()

ax.set_xlabel('t',fontsize=26)
ax.set_title('Characteristic Function')
fig.savefig('characterstic_func.pdf')
