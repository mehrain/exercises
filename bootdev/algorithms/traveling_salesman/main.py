def tsp(cities, paths, dist):
    city_combinations = permutations(cities)
    for city_combination in city_combinations:
        total_distance = 0
        for i in range(len(city_combination) - 1):
            current_city = city_combination[i]
            next_city = city_combination[i + 1]
            total_distance += paths[current_city][next_city]
        if total_distance < dist:
            return True
    return False


# don't touch below this line


def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res