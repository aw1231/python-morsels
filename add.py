def add(*args):
    result = []
    inputcount = len(args)
    externalcounter = 0
    internalcounter = 0
    place = 1
    while place-1 != inputcount:
        while externalcounter != len(args[place-1]):
            a = args[place-1][externalcounter]
            while len(result) != len(args[place-1]):
                result.append([0]*len(a))
            while internalcounter != len(a):
                b = a[internalcounter]
                result[externalcounter][internalcounter] = result[externalcounter][internalcounter] + args[place-1][externalcounter][internalcounter]
                internalcounter = internalcounter + 1
            externalcounter = externalcounter + 1
            internalcounter = 0
        externalcounter = 0
        place = place + 1
    return result
