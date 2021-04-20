import numpy as np

myTuple = ('abc', np.arange(1, 8, 2), 2.5)
#hàm arange truyền vào 2 tham số (x, y) thì sẽ nhận được mảng bắt đầu từ x > y
#hàm arange truyền vào 3 tham số (x, y, z) thì x là start, y là end và z là step.
print(myTuple[1])