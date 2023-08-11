#####################################################
# @Author: Abhilash Sarwade
# @Date:   2023-08-11 08:42:56 am
# @email: sarwade@ursc.gov.in
# @File Name: monte_carlo_annulus_circumference.py
# @Project: lab2_20230811
#
# @Last Modified time: 2023-08-11 10:00:14 am
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


# Function to estimate area of a circle using Monte Carlo 
def monte_carlo_area_estimate_circle(radius, num_points):
    num_points_inside = 0
    x = seed_x
    y = seed_y
    for i in range(1, num_points+1):
        x = modulo_random_generator(x)
        random_normalized_x = x/m
        random_x = 2*radius*random_normalized_x - radius

        y = modulo_random_generator(y)
        random_normalized_y = y/m
        random_y = 2*radius*random_normalized_y - radius

        distance = np.sqrt(random_x**2 + random_y**2)
        if distance <= radius:
            num_points_inside += 1

    estimated_area = (num_points_inside / num_points) * (2*radius)**2
    return estimated_area


# Calculating area of an annulus
outer_radius = 5
inner_radius = 4.9
delta_radius = outer_radius - inner_radius
num_points = 10000

estimated_outer_circle_area = monte_carlo_area_estimate_circle(outer_radius,num_points)
estimated_inner_circle_area = monte_carlo_area_estimate_circle(inner_radius,num_points)

estimated_annulus_area = estimated_outer_circle_area - estimated_inner_circle_area

estimated_value_2pi = estimated_annulus_area / (delta_radius * outer_radius)

# Display estimated areas
print(f"Estimated Outer Circle Area: {estimated_outer_circle_area}")
print(f"Estimated Inner Circle Area: {estimated_inner_circle_area}")

print(f"Estimated Annulus Area: {estimated_annulus_area}")

print(f"Estimated Value of 2*pi: {estimated_value_2pi}")

# Calculating value of 2*pi for different delta_radius
outer_radius = 5
delta_radii = np.logspace(0,-4,100)

values_2pi = []

for dr in delta_radii:
    inner_radius = outer_radius - dr
    estimated_outer_circle_area = monte_carlo_area_estimate_circle(outer_radius, num_points)
    estimated_inner_circle_area = monte_carlo_area_estimate_circle(inner_radius, num_points)

    estimated_annulus_area = estimated_outer_circle_area - estimated_inner_circle_area

    estimated_value_2pi = estimated_annulus_area / (dr * outer_radius)
    values_2pi.append(estimated_value_2pi)



#plotting

def monte_carlo_area_estimate_circle_me(radius, num_points):
    num_points_inside = 0
    x = seed_x
    y = seed_y

    rx = []
    ry = []
    for i in range(1, num_points+1):
        x = modulo_random_generator(x)
        random_normalized_x = x/m
        random_x = 2*radius*random_normalized_x - radius
        rx.append(random_x)

        y = modulo_random_generator(y)
        random_normalized_y = y/m
        random_y = 2*radius*random_normalized_y - radius
        ry.append(random_y)

        distance = np.sqrt(random_x**2 + random_y**2)
        if distance <= radius:
            num_points_inside += 1

    estimated_area = (num_points_inside / num_points) * (2*radius)**2
    return estimated_area, rx, ry

outer_radius = 5
inner_radius = 4.5

ee, rx, ry = monte_carlo_area_estimate_circle_me(outer_radius,10000)

rx = np.array(rx)
ry = np.array(ry)


rx_i = rx[(rx**2 + ry**2) <= inner_radius**2]
ry_i = ry[(rx**2 + ry**2) <= inner_radius**2]

rx_o = rx[(rx**2 + ry**2) <= outer_radius**2]
ry_o = ry[(rx**2 + ry**2) <= outer_radius**2]

fig, ax = plt.subplots()

# fig.set_size_inches(8,8)
ax.set_aspect(1)
ax.scatter(rx, ry,alpha=0.3)
ax.scatter(rx_o, ry_o,color='r')
ax.scatter(rx_i, ry_i)


ax.axhline(y=0, color='black', lw=2)
ax.axvline(x=0, color='black', lw=2)

ax.set_xlim([-1.2*outer_radius, 1.2*outer_radius])
ax.set_ylim([-1.2*outer_radius, 1.2*outer_radius])

ax.set_xlabel('x', fontsize=22)
ax.set_ylabel('y', fontsize=22)

circle_art1 = plt.Circle((0, 0), outer_radius, fill=False, lw=2)
circle_art2 = plt.Circle((0, 0), inner_radius, fill=False, lw=2)

ax.add_artist(circle_art1)
ax.add_artist(circle_art2)

fig.savefig('scatter_distribution_annulus.pdf')
