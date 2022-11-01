import numpy as np
y = np.genfromtxt('C:/Users/pasha/xx.csv', delimiter=';', names=True) #импортируем данные из csv-файла в переменную y
np.savetxt('C:/Users/pasha/xx.txt', y) #экспортируем данные из переменной y в файл xx.xtx, так как при экспорте из файла csv мы не можем отобразить количество столбцов и количество элементов массива (путем различных манипуляций исправить это не удалось)
y = np.loadtxt('C:/Users/pasha/xx.txt') #импортируем данные из текстового файла обратно в переменную y
ylines = len(y) #вычисляем количество строк
ycolumns = int(y.size/len(y)) #вычисляем количество столбцов
x = np.eye(ylines,ycolumns) #создаем единичную матрицу с ylines строк и ycolumns столбцов
yx = y*x #перемножаем две матрицы
np.savetxt("yx.csv", yx, delimiter=",") #сохраняем перемноженные матрицы в CSV файл
