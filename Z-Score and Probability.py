def findx():
    z = float(input("Z = "))
    mean = float(input("Mean = "))
    sigma = float(input("St. Dist = "))

    solve = mean + (z * sigma)

    print(f"\nX = {solve}\n")
    init()


def findz():
    x = float(input("X = "))
    mean = float(input("Mean = "))
    sigma = float(input("St. Dist = "))

    solve = (x - mean) / sigma

    print(f"\nZ = {solve}\n")
    init()


def init():
    ans = input("Solve for: (x,z) ")

    if ans.lower() == "x":
        findx()
    elif ans.lower() == "z":
        findz()
    else:
        print("I don't understand")
        init()


init()
