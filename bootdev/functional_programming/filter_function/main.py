def remove_invalid_lines(document):
    return '\n'.join(filter(lambda line: not line.startswith('-'), document.split('\n')))

'''
I understand that the above solution is the most efficient way to solve the problem, but I wanted to try a different approach.
I find the below approach more pleasing to the eye. It is also more readable and easier to understand.

def remove_invalid_lines(document):
    lines = document.split('\n')
    valid_lines = []

    for line in lines:
        if not line.startswith('-'):
            valid_lines.append(line)

    return '\n'.join(valid_lines)

'''