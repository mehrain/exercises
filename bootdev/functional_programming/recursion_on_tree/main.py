def list_files(current_node, current_path=""):
    file_paths = []
    for node, children in current_node.items():
        if children is None:
            file_paths.append(current_path + "/" + node)
        else:
            file_paths.extend(list_files(children, current_path + "/" + node))
    return file_paths
