import matplotlib.pyplot as plt

X = [-1,1,2,4,6,7]
Y = [-1,2,3,3,5,8]
X_bar = sum(X) / len(X)
Y_bar = sum(Y) / len(Y)
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
# plt.plot(X, R, color='black')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()