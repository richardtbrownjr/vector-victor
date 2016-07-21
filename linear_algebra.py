from math import sqrt

class ShapeError(Exception):
    pass

def compare_shapes(*args):
    if len(set([shape(arg) for arg in args])) == 1:
        return shape
    #else:
    #if shape(a) != shape(b):
    #    raise ShapeError

def shape(vector):
    return (len(vector),)

def vector_add(a, b):
    vectorsum =[]
    if shape(a) == shape(b):
        return [a[index] + b[index] for index, value in enumerate(a)]
    else:
        raise ShapeError
        # assert shape([1]) == (1,)
        # assert shape(m) == (2,)
        # assert shape(v) == (3,)
    #assert vector_add(x, y) == [1, 5, 4]
    # for index, value in enumerate(a):
    #     vectorsum.append(a[index] + b[index])
    # return vectorsum


def vector_sub(a, b):
    vectorsub =[]
    if shape(a) != shape(b):
        raise ShapeError
    else:
        return [a[index] - b[index] for index, value in enumerate(a)]

            #return [a[index] - b[index] for index, value in enumerate(a)]

def vector_sum(*args):
    if len(set([shape(arg) for arg in args])) == 1:
        return [sum(args) for args in zip(*args)]
    else:
        raise ShapeError

def dot(*args):
    #compare_shapes(a, b)
    if len(set([shape(arg) for arg in args])) == 1:
        return sum([(args) * (args) for args, args in zip(args, args)])
    else:
        raise ShapeError

def vector_multiply(a, b):
    return [x * b for x in (a)]

def vector_mean(*args):
    #vector_mean(m, n) == [4, 2]
    return([v/len([x for x in args]) for v in vector_sum(*[x for x in args])])


def magnitude(b):
    return sqrt(sum([a**2 for a in b]))


#def compare_shapes(*args):
    #shapes - [shape(item) for item in args]
    #first_shape = shapes[0]
    #some_shapes =[first_shape == shape for shape in shapes]
    #return all(same_shapes)
#def comare_shapes(*args):
#    return len(set[shape(item) for item in args])) == 1
