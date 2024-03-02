def change_bullet_style(document):
    changed_lines = map(convert_line, document.split("\n"))
    joined_lines = "\n".join(list(changed_lines))
    return joined_lines




def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
