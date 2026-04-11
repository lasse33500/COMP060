def debug_print(debug_msg=None, **kwargs):
    if debug_msg:
        print(debug_msg)

    for key, value in kwargs.items():
        print(f"{key}: {value}")


def mergesort(array):
    debug_print(array=array)

    if len(array) <= 1:
        return array

    m = len(array) // 2
    debug_print(m=m)

    left = mergesort(array[:m])
    right = mergesort(array[m:])

    return merge(left, right)


def merge(left, right):
    merged = []

    debug_print("Merging...")
    debug_print(left=left)
    debug_print(right=right)

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(left)
    merged.extend(right)

    debug_print(merged=merged)

    return merged


if __name__ == "__main__":
    input_str = input("Enter numbers, separated by ',': ")
    input_list = input_str.split(",")

    value_list = []
    for x in input_list:
        value_list.append(int(x))

    debug_print(input_list=input_list)
    debug_print(value_list=value_list)

    sorted_list = mergesort(value_list)
    print(sorted_list)
