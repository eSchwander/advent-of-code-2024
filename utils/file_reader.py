def convert_file_to_2d_array(filename):
    array = []

    with open(filename, 'r') as f:
        for row in f.readlines():
            current_row = []
            for c in row.strip():
                current_row.append(c)
            array.append(current_row)

    return array
