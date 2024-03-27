import matplotlib.pyplot as plt

DIGIT_WIDTH = 2

digit_endpoints = {
    2: [
        [[-1, 2], [1, 2], [1, 0], [-1, 0], [-1, -2], [1, -2]]
    ],
    3: [
        [[-1, 2], [1, 2], [1, 0], [-1, 0]], [[1, 0], [1, -2], [-1, -2]]
    ],
    4: [
        [[-1, 2], [-1, 0], [1, 0]], [[1, 2], [1, -2]]
    ],
    7: [
        [[-1, 1.5], [-1, 2], [1, 2], [1, -2]]
    ]
}


def get_coordinates_from_endpoints(endpoints_paths: list[list[list[int]]], resolution_per_unit=20, offset=[0, 0]):

    coordinates = []
    for endpoint_path in endpoints_paths:
        for i in range(len(endpoint_path)-1):

            start = [endpoint_path[i][0] + offset[0],
                     endpoint_path[i][1] + offset[1]]
            end = [endpoint_path[i+1][0] + offset[0],
                   endpoint_path[i+1][1] + offset[1]]

            print(start, end)

            delta_x = end[0] - start[0]
            delta_y = end[1] - start[1]

            print(delta_x, delta_y)

            n_steps = int(((delta_x**2+delta_y**2)**0.5)*resolution_per_unit)

            for j in range(n_steps):
                coordinates.append(
                    [start[0]+(delta_x*j/n_steps), start[1]+(delta_y*j/n_steps)])

        coordinates.append(end)

    return coordinates


def gen_coordinates_from_digits(digits: list[int], spacing=1):

    total_width = len(digits)*DIGIT_WIDTH + spacing*(len(digits)-1)

    offsets = []
    for i in range(len(digits)):
        x = (-total_width/2) + (i+0.5)*(total_width/len(digits))
        offsets.append([x, 0])

    print(offsets)

    coordinates = []
    for i in range(len(digits)):
        coordinates.extend(
            get_coordinates_from_endpoints(digit_endpoints[digits[i]], offset=offsets[i]))

    return coordinates


if __name__ == '__main__':

    coordinates = gen_coordinates_from_digits([3, 4])
    plt.scatter([x[0] for x in coordinates], [x[1] for x in coordinates])
    plt.show()
