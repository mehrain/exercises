def verify_tsp(paths, dist, actual_path):
    for city in actual_path:
        sum_distance = paths[city][actual_path[0]]
        for i in range(len(actual_path) - 1):
            sum_distance += paths[actual_path[i]][actual_path[i + 1]]
    return sum_distance < dist