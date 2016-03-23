# Matrix Algebra

"""
Matrix Dimensions
    1.1) 2x3
    1.2) 2x2
    1.3) 3x2
    1.4) 2x3
    1.5) 1x4
    1.6) 4x1
 """
    
"""
Vector Operations
"""
>>> u = np.array([6, 2, -3, 5])
>>> v = np.array([3, 5, -1, 4]
>>> u
array([ 6,  2, -3,  5])
>>> v
array([ 3,  5, -1,  4])

#2.1
>>> u+v
array([ 9,  7, -4,  9])

#2.2
>>> u - v
array([ 3, -3, -2,  1])

#2.3
>>> 6*u
array([ 36,  12, -18,  30])

#2.4
>>> u.dot(v)
51

#2.5
>>> np.linalg.norm(u)
8.6023252670426267
