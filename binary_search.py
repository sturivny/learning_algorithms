search_data = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def binary_search(data, item_to_find):
    iterations = 0

    start = 0
    end = len(data)
    position = -1

    while start <= end:
        iterations += 1
        print(f'Iteration: {iterations}')
        middle = int((start + end)/2)

        if data[middle] == item_to_find:
            position = middle
            return position

        if item_to_find < data[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return position


if __name__ == '__main__':
    pos = binary_search(search_data, 3)
    print(pos)
