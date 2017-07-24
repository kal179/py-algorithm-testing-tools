from tools.testalgorithms import TestFunction

# The bubble_sort is slow because it is written in hurry dont mind just focus on tests
def bubble_sort(li):
    for i in range(len(li)):
	    for v in range(len(li) - 1):
		    if (li[v] > li[v + 1]):
			    tmp = li[v]
			    li[v] = li[v + 1]
			    li[v + 1] = tmp
    return li 

tests = [[[4, 3, 2, 1]], [[21, 4, 23, 43, 23, 435, 234, 45, 234, 45, 76, 689, 1132343, 465, 7, 34, 7, 4, 2]],
		 [[12, 46755, 23435, 1, 4, 2, 89, 2, 54, 100, 100, 1000, 10000]], [[100000, 10000, 1000, 100, 10, 1, 0]] ]

# Note: I have put the list inside an outer list because the list should be treated as an argument
# If you don't do so you'll end up having UnboundLocalError because the function won't work

res = [[1, 2, 3, 4], [2, 4, 4, 7, 7, 21, 23, 23, 34, 43, 45, 45, 76, 234, 234, 435, 465, 689, 1132343],
		[1, 2, 2, 4, 12, 54, 89, 100, 100, 1000, 10000, 23435, 46755], [0, 1, 10, 100, 1000, 10000, 100000]]

test_the_bub_sort = TestFunction(tests, bubble_sort, res, False)
print("Testing Bubble Sort(with details disabled):")
test_the_bub_sort.test()
