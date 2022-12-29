def min(array :list):

    val = int(array.__getitem__(0))

    for x in array:
        x = int(x)
        if x < val:
            val = x

    return f"output => {val}"

def max(array=None):

    val = int(array.__getitem__(0))

    for x in array:
        x = int(x)
        if x > val:
            val = x

    return f"output => {val}"


def rata2(array):

    _len = len(array)
    _sum = sum(array)

    return f"output => {float(_sum / _len)}"