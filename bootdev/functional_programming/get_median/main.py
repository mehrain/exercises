def get_median_font_size(font_sizes):
    sorted_sizes = sorted(font_sizes)
    mid = len(sorted_sizes) // 2
    if not sorted_sizes:
        return None
    elif len(sorted_sizes) % 2 == 1:
        return sorted_sizes[mid]
    else:
        return (sorted_sizes[mid - 1] + sorted_sizes[mid]) / 2