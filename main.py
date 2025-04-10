import numpy as np
import matplotlib.pyplot as plt



def f(x):
    return np.sin(x)



def simpson_3_8(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    # Применение формулы 3/8 Симпсона
    integral = 0
    for i in range(0, n, 3):
        integral += (3 * h / 8) * (y[i] + 3 * y[i + 1] + 3 * y[i + 2] + y[i + 3])

    return integral



def exact_integral(a, b):
    return -np.cos(b) + np.cos(a)



a = 0
b = np.pi
exact_value = exact_integral(a, b)


h_values = [np.pi / 6, np.pi / 12, np.pi / 24, np.pi / 48]
results = []

for h in h_values:
    n = int((b - a) / h)
    numerical_value = simpson_3_8(f, a, b, n)
    deviation = abs(numerical_value - exact_value)
    results.append((h, numerical_value, exact_value, deviation))

print("h\t\tĨ\t\tI\t\tОтклонение")
for row in results:
    print(f"{row[0]:.6f}\t{row[1]:.6f}\t{row[2]:.6f}\t{row[3]:.6f}")


h_list = [row[0] for row in results]
deviation_list = [row[3] for row in results]

plt.figure(figsize=(8, 6))
plt.plot(h_list, deviation_list, 'o-', label='Отклонение |I - Ĩ|')
plt.xlabel('Шаг h')
plt.ylabel('Отклонение |I - Ĩ|')
plt.title('Зависимость отклонения от шага h')
plt.grid(True)
plt.legend()
plt.show()