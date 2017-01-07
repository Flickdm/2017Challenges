

def get_ranges(inputRange):
    if inputRange is None:
        return None

    start = inputRange[0]
    outList = []

    for i in range(1, len(inputRange)):

        # A boundry is denoted as a range greater than 1
        if inputRange[i] - inputRange[i-1] > 1:
            if start != inputRange[i-1]:
                outList.append("{}->{}".format(start, inputRange[i-1]))
            # update start
            start = inputRange[i]

        # End condition
        if (i == len(inputRange)-1):
            if start != inputRange[i]:
                outList.append("{}->{}".format(start, inputRange[i]))

    return outList
