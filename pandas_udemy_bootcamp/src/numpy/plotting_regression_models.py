""" Visualization and plotting different regression models/equations """
import numpy as np
import matplotlib.pyplot as plt


plt.style.use("seaborn")

# Histogram
# creating 10,000 normally distributed numbers with mean 5 and std 2
y = np.random.normal(5, 2, 10000)
print(y)

plt.figure(figsize=(10, 6))
plt.hist(y, bins=100, label="Data")  # Histogram
plt.title("Frequency Distribution of y")
plt.vlines(np.mean(y), 0, 350, label="Mean")
plt.xlabel("y")
plt.ylabel("frequency")
plt.legend()
plt.show()

# sin plot
# creating evenly spaced numbers over a specified interval.
print(np.linspace(1, 10, 10))

# creating 1,000 evenly spaced numbers over the interval -10 to 10
x = np.linspace(-10, 10, 1000)
print(x)

y = 3 * x**3 - 2 * x**2 + 5*x - 5  # function over x
print(y)

y = np.sin(x)  # function over x
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# scatter plot
# creating 20 normally distributed numbers in (2,10) shape: mean 10 and std 2
np.random.seed(123)
m = np.random.normal(10, 2, 20).reshape(2, 10)
print(m)

a = m[0]  # array a is represents first row of m and contains 10 elements
print(a)

b = m[1]  # array b is represents second row of m and contains 10 elements
print(b)

plt.figure(figsize=(10, 6))  # scatter plot of a and b
plt.scatter(a, b)
plt.show()

# plotting regressions/ equations
reg1 = np.polyfit(a, b, 1)  # linear regression
print(reg1)  # function: b = 12.51 - 0.1599 * a

# creating x and y values for regression line
x = np.linspace(min(a), max(a), num=100)
y = np.polyval(reg1, x)

reg2 = np.polyfit(a, b, 2)  # quadratic regression
reg2  # function: b = 16.986 + 0.0535 * a**2 - 1.1738 * a

reg3 = np.polyfit(a, b, 3)  # cubic regression
reg3  # function: b = 92.25 - 0.1178 * a**3 + 3.267 * a**2 - 28.899 * a

plt.figure(figsize=(10, 6))
plt.scatter(a, b, label="Data")  # Data points

# linear regression
plt.plot(x, y, 'b--', label='linear')

# quadratic regression
plt.plot(x, np.polyval(reg2, x), 'm-.', label='quadratic')

# cubic regression
plt.plot(x, np.polyval(reg3, x), 'g.', label='cubic')

plt.legend()
plt.show()

# perfect regression, polynomial of degree 9 perfectly regresses 10 data points
reg_perfect = np.polyfit(a, b, len(a)-1)
print(reg_perfect)

plt.figure(figsize=(10, 6))
plt.scatter(a, b, label="Data")
plt.plot(x, np.polyval(reg_perfect, x), 'b--', label='perfect')
plt.legend()
plt.ylim(min(b)-0.5, max(b)+0.5)
plt.show()
