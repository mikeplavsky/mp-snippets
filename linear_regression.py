import numpy as np

x = np.matrix([[1,2],[3,4]]);
y = np.matrix('1;2');

w = np.linalg.solve(
    x.T.dot(x),x.T.dot(y))

x1 = np.matrix('3,4')
x1.dot(w)
