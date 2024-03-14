def num_possible_orders(num_posts):
    total_possible_orders = 1
    for index in range(num_posts, 1, -1):
        total_possible_orders *= index
    return total_possible_orders
