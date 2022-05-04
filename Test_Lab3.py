import Lab3

print("Test_Lab3")

def test_REQ_1():
    result_assend = []
    result_decend = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 15, 89, 99]
    test_arr_up = [11, 12, 15, 22, 25, 34, 64, 89, 90, 99]
    test_arr_down = [99, 90, 89, 64, 34, 25, 22, 15, 12, 11]

    result_assend = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    result_decend = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert(result_assend == test_arr_up)
    assert(result_decend == test_arr_down)

def test_REQ_2():
    result = []
    input_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert(result == 1)

def test_REQ_3():
    result = []
    input_arr = [1, 2, 3]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert(result == -1)

def test_REQ_4():
    result = []
    input_arr = []

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert(result == 0)

def test_REQ_5():
    result = []
    input_arr = [12.6, 12.7, 1, 4]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert(result == 3)