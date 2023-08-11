#####################################################
# @Author: Abhilash Sarwade
# @Date:   2023-08-10 06:41:06 pm
# @email: sarwade@ursc.gov.in
# @File Name: monte_carlo_pi_calculation.py
# @Project: lab2_20230811
#
# @Last Modified time: 2023-08-11 08:49:17 am
#####################################################

import numpy as np
import matplotlib.pyplot as plt

# Random Number Generator Parameters (Taken from Numerical Recipes)
a = 1664525
c = 1013904223
m = 2**32
seed_x = 0
seed_y = 10

# Random Number Generator Function
def modulo_random_generator(x):
    return np.mod(a*x + c, m)


# Estimating Value of Pi
total_points = 10000
x = seed_x
y = seed_y

random_x_array = []  # All generated random x values
random_y_array = []  # All generated random y values

random_x_array_circ = []  # Random x values inside the circle
random_y_array_circ = []  # Random y values inside the circle

n_points_inside_circle = 0  # Counter for points inside the circle
pi_estimates = []  # List of pi estimates

for i in range(1,total_points+1):
    x = modulo_random_generator(x)
    random_normalized_x = x/m
    random_x = 2*random_normalized_x - 1
    random_x_array.append(random_x)

    y = modulo_random_generator(y)
    random_normalized_y = y/m
    random_y = 2*random_normalized_y - 1
    random_y_array.append(random_y)

    distance = random_x**2 + random_y**2
    if distance <=1:
        random_x_array_circ.append(random_x)
        random_y_array_circ.append(random_y)

        n_points_inside_circle += 1

    tmp_pi_estimate = 4 * n_points_inside_circle / i
    pi_estimates.append(tmp_pi_estimate)

    if i%1000==0:
        print(f"Estimated value of pi after {i} iterations: {tmp_pi_estimate:.6f}")

# random_x_array = np.array(random_x_array)
# random_y_array = np.array(random_y_array)

# random_x_array_circ = np.array(random_x_array_circ)
# random_y_array_circ = np.array(random_y_array_circ)

# pi_estimates = np.array(pi_estimates)


# Plotting
fig, ax = plt.subplots()

# fig.set_size_inches(8,8)
ax.set_aspect(1)
ax.scatter(random_x_array,random_y_array)
ax.scatter(random_x_array_circ,random_y_array_circ)

ax.axhline(y=0, color='black',lw=2)
ax.axvline(x=0, color='black',lw=2)

ax.set_xlim([-1.1,1.1])
ax.set_ylim([-1.1,1.1])

ax.set_xlabel('x',fontsize=22)
ax.set_ylabel('y', fontsize=22)

circle_art = plt.Circle((0,0),1,fill=False,lw=2)

ax.add_artist(circle_art)

fig.savefig('scatter_distribution.pdf')

fig, ax = plt.subplots()
ax.plot(range(1, total_points + 1), pi_estimates)
ax.axhline(y=np.pi, color='r',
            linestyle='--', label=r'True $\pi$ Value')
ax.set_xlabel('Number of Iterations',fontsize=22)
ax.set_ylabel(r'Estimated $\pi$ Value', fontsize=22)
# ax.set_title('Evolution of Pi Estimation')
ax.legend()

fig.savefig('pi_value_estimate.pdf')
