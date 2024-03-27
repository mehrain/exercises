def get_num_guesses(length):
    return sum(26 ** i for i in range(1, length + 1))