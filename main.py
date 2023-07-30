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

#пузырьковый алгоритм сортировки
def bubble_method(array_bubble, count: int = 0):
    n = len(array_bubble)
    for r in range(n - 1):
        for i in range(n - 1):
            if array_bubble[i]>array_bubble[i + 1]:
                count += 1
                array_bubble[i],array_bubble[i + 1] = array_bubble[i+1], array_bubble[i]

    return array_bubble, count


print(bubble_method([5,7,4,3,8,2]))