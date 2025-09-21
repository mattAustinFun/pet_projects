def  diff_intervals_list(intervals:int, start_from:int,end_with:int) ->list[int]:
    """
    return a list of integers for all values between two input integers.
    Length of list based on input
    """
    diff = end_with - start_from
    diff_list = [start_from]
    for interval in range(intervals-1):
        start_from += diff/intervals
        diff_list.append(int(round(start_from)))
    diff_list.append(end_with)
    return diff_list


