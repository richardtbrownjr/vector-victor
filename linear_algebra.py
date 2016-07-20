class ShapeError(Exception):
    pass

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
def vector_sum(vectors):
    pass


#def compare_shapes(*args):
    #shapes - [shape(item) for item in args]
    #first_shape = shapes[0]
    #some_shapes =[first_shape == shape for shape in shapes]
    #return all(same_shapes)
#def comare_shapes(*args):
#    return len(set[shape(item) for item in args])) == 1
