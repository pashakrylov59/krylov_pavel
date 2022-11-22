import numpy as np

w = np.zeros((16)) # Веса связей

D = np.array([ # Входной вектор
    [0,1,1,0,
     1,0,0,1,
     1,0,0,1,
     0,1,1,0,],
    [0,0,1,0,
     0,0,1,0,
     0,0,1,0,
     0,0,1,0,],
    [0,1,0,0,
     0,1,0,0,
     0,1,0,0,
     0,1,0,0,],
])
Y0 = np.array([0,1,1]) # Выходной вектор

# Константы обучения
alfa = 0.2 # темп 
beta = -0.4 # торможение.

# Активационная функция 
sigma = lambda x: 1 if x > 0 else 0

# Тело нейрона
def f(x):
    s = beta + np.sum(x @ w)
    return sigma(s)

# Эпоха обучения
def train():
    global w
    _w = w.copy()
    for x, y in zip(D, Y0):
        w += alfa * (y - f(x)) * x
    return (w != _w).any()

# Обучение и тестирование
while train():
    print(w)
    
# Вывод
for x in D:
    print(x, f(x))
