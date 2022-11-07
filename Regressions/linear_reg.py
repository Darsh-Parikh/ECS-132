import matplotlib.pyplot as plt

X = [72,50,81,74,94,86,59,83,65,33,88,81]
Y = [84,63,77,78,90,75,49,79,77,52,74,90]
X_bar = sum(X) / len(X)
Y_bar = sum(Y) / len(Y)
#   X_bar = 89.667      Y_bar = 498.78
Beta_1 = 0.0
Beta_0 = 0.0
denominator = 0.0
for i in range(len(X)):
    Beta_1 += (X[i] - X_bar)*(Y[i] - Y_bar)
    denominator += (X[i] - X_bar) ** 2
Beta_1 /= denominator
Beta_0 = Y_bar - (Beta_1 * X_bar)
print(f"y = {Beta_0} + {Beta_1}x")
R = list(map(lambda a: (Beta_0 + (a * Beta_1)), X))

plt.scatter(x=X, y=Y)
plt.plot(X, R, color='black')
plt.xlabel("Midterm")
plt.ylabel("Final")
plt.show()