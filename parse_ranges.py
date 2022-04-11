def parse_ranges(range):
    split_range = range.split(",")
    output = []
    for subrange in split_range:
        subrange_list = subrange.split("-")
        counter = int(subrange_list[0])
        high = int(subrange_list[1])
        while counter <= high:
            yield counter
            output.append(counter)
            counter += 1
    return output
