#алгоритм хоара

def sort(array):

    if len(array) <= 1:
        return array

    elem = array[0]

    left = [i for i in array if i<elem]
    center = [i for i in array if i == elem]
    right = [i for i in array if i > elem]

    return sort(left) + sort(center) + sort(right)


print(sort(array=[5,9,4,6,2,1]))