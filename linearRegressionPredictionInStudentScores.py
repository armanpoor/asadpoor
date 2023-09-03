# data set link in uci:
# https://archive.ics.uci.edu/dataset/320/student+performance

import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn.linear_model import LinearRegression

data = pd.read_csv("student-mat.csv", sep=";")
print(data)

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

x = np.array(data.drop([predict], axis='columns'))
y = np.array(data[predict])
print("x=", x, "\n", "y=", y, "\n")

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.1)
my_model = LinearRegression().fit(x_train, y_train)

accuracy = my_model.score(x_test, y_test)
print(accuracy)
print("Coefficient:", my_model.coef_)
print("Intercept:", my_model.intercept_)

results = my_model.predict(x_test)

for each_result in range(len(results)):
    print(results[each_result], x_test[each_result], y_test[each_result])
