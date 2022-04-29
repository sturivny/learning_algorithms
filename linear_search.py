search_data = [2, 6, 1, 6, 4, 8, 6, 4, 7, 9, 5, 3]


def linear_search(data, item_to_find):
    iterations = 0
    for position in range(len(data)):
        iterations += 1
        if data[position] == item_to_find:
            print(f'Iterations: {iterations}')
            print(f'Position: {position}')
            return position
    return


if __name__ == '__main__':
    linear_search(search_data, 3)
