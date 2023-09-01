import matplotlib.pyplot as plt
import numpy as np

# x = [1, 2, 3, 4, 5, 6]
# y = [2, 3.3, 2, 2.5, 4.5, 3.8]
# plt.plot(x, y)
# plt.show()

# python list vs numpy array

# #line
# x = np.array([1, 2, 3, 4, 5, 6])
# y = np.array([2, 3.3, 2, 2.5, 4.5, 3.8])
# plt.plot(x, y)
# plt.show()

# bar chart

# plt.bar(["Blue", "Red"], [2, 5])
# plt.show()

# # Drawing a histogram
# nums = [1, 1, 2, 3, 3, 3, 3, 3, 4, 5, 6, 6, 6, 7, 8, 8, 9,
#         10, 12, 12, 12, 12, 14, 18]
# _ = plt.hist(nums , color="red")
# _ = plt.xlabel('mehvat x')
# _ = plt.ylabel('Frequency')
# plt.show()

# Drawing a scatter plot

# plt.scatter([1,8,45],[35,83,96])
# # Adding a title
# plt.title("My Graph")
# plt.xlabel("tedad gheibat")
# plt.ylabel("معدل")
# plt.show()

# # Adding a legend
# plt.plot([1, 2, 3], label="blue", color="blue")  # add the label parameter here
# plt.plot([3, 2, 1], label="red", color="red")  # add the label parameter here
# plt.legend()  # to embed the legend
# plt.show()

# linear regression degree 1

# create data
x = np.array([1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9])
y = np.array([13, 14, 17, 12, 23, 24, 25, 25, 24,
              28, 32, 33])

# create basic scatterplot
plt.scatter(x, y)
# obtain m (slope) and b(intercept) of linear regression line
m, b = np.polyfit(x, y, 1)
print(m, b)
# # to see the function that can represents data
# f = np.poly1d(m, a)

# add linear regression line to scatterplot
plt.plot(x, m * x + b)
plt.show()