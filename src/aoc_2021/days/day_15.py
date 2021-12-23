from aoc_2021.utils import get_input, pretty_print_solutions

import numpy as np
from heapq import heappush, heappop


def preprocess_input_data(input_data):
    matrix = []
    for line in input_data.splitlines():
        matrix.append([int(x) for x in line])
    return np.matrix(matrix)


def get_new_matrix(matrix):
    matrices = []
    for i in range(5):
        row = []
        for j in range(5):
            tmp_matrix = np.matrix(matrix)
            for _ in range(i+j):
                tmp_matrix += 1
                tmp_matrix[tmp_matrix == 10] = 1
            row.append(tmp_matrix)
        matrices.append(np.hstack(row))
    return np.vstack(matrices)


def get_neighbors(node, max_width, max_height):
    neighbors = []

    for (i, j) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        coord_0, coord_1 = node[0]+i, node[1]+j
        if (0 <= coord_0 < max_height) and (0 <= coord_1 < max_width):
            neighbors.append((coord_0, coord_1))

    return neighbors


def fast_dijkstra(matrix, initial_node, end_node):
    max_width, max_height = map(int, matrix.shape)

    heap = [(0, initial_node)]

    distances = {}
    distances[initial_node] = 0

    current_node = initial_node
    while heap:
        _, current_node = heappop(heap)

        if current_node == end_node:
            break

        for neighbor in get_neighbors(current_node, max_width, max_height):
            tmp_distance = matrix[neighbor] + distances[current_node]
            if neighbor in distances:
                distances[neighbor] = min(distances[neighbor], tmp_distance)
            else:
                distances[neighbor] = tmp_distance
                heappush(heap, (distances[neighbor], neighbor))
    return distances[end_node]


if __name__ == '__main__':
    first_matrix = preprocess_input_data(
        get_input('https://adventofcode.com/2021/day/15/input')
    )

    second_matrix = get_new_matrix(first_matrix)

    solution_first_part = fast_dijkstra(
        matrix=first_matrix,
        initial_node=(0, 0),
        end_node=(first_matrix.shape[0]-1, first_matrix.shape[1]-1)
    )
    solution_second_part = fast_dijkstra(
        matrix=second_matrix,
        initial_node=(0, 0),
        end_node=(second_matrix.shape[0]-1, second_matrix.shape[1]-1)
    )

    pretty_print_solutions(solution_first_part, solution_second_part, 15)
