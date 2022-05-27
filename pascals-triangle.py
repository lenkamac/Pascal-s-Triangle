def get_pascals_triangle_row(row_number: int) -> list:

    # row 0 is constantly 1
    if row_number == 0:
        return [1]
    else:
        n = [1]
        # recursive function
        m = get_pascals_triangle_row(row_number - 1)
        for i in range(len(m) - 1):
            n.append(m[i] + m[i + 1])
        n += [1]
    return n

print(get_pascals_triangle_row(6))