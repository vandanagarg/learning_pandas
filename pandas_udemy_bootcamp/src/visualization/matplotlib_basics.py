""" Visualization with Matplotlib """
import matplotlib.pyplot as plt
import random


l1 = [1, 3, 5, 7, 9]

plt.plot(l1)
plt.show()

# default x axis values, y axis is l1
plt.plot(range(5), l1)  # same as above
plt.show()
plt.plot(range(5, 10), l1)  # customized x axis range
plt.show()

# scatter plot
plt.scatter(x=range(5), y=l1)
plt.show()
""" Here x and y should be of same size else we get error
plt.scatter(x=range(7), y=l1)
plt.show() """

# histograms
random.seed(123)
# creates 10000 normal distributed numbers with standard deviation of 5
speed_ny = [random.normalvariate(55, 5) for i in range(10000)]
print(len(speed_ny))
speed_bo = [random.normalvariate(60, 8) for i in range(10000)]

# creating a histogram of list speed with 100 bins
plt.hist(speed_ny, bins=100)
plt.show()

# additional features

plt.style.use("seaborn")  # change style to seaborn
plt.figure(figsize=(12, 6))  # change the size of graph
# Histogram of NY Data
plt.hist(speed_ny, bins=100, label="New York Data", alpha=0.5, color="red")
# alpha = 1 no transperancy, 0.5 - partially transparent
# Histogram of Boston Data
plt.hist(speed_bo, bins=100, label="Boston Data", alpha=0.5, color="blue")
plt.title("Measured Car Speed (Speed Limit 50 mph)", fontsize=15)  # set title
plt.xlabel("Speed")  # label x-axis
plt.ylabel("Occurences")  # label y-axis
# vertical line at NY mean
plt.vlines(sum(speed_ny)/len(speed_ny), 0, 400, color="red",
           linestyle="--", label="Mean New York")
# vertical line at Boston mean
plt.vlines(sum(speed_bo)/len(speed_bo), 0, 400, color="blue",
           linestyle="-.", label="Mean Boston")
plt.axis((30, 90, 0, 400))  # set range of axis
plt.xticks(range(30, 91, 5))  # set ticks of x-axis
plt.yticks(range(0, 401, 50))  # set ticks of y-axis
plt.grid(True)  # enable/disable grid
plt.legend(loc="centre right", fontsize=13)  # includes legend/ show labels
plt.show()
