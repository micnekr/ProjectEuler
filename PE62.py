if __name__ == '__main__':
    maxNum = 10 ** 12

    cubes = []

    i = 1
    while True:
        cube = i ** 3
        if cube >= maxNum:
            break
        cubes.append([cube, "".join(sorted(str(cube)))])
        i += 1
    print(cubes)

    cubesSorted = {}

    for cube, sortedCube in cubes:
        if sortedCube in cubesSorted:
            cubesSorted[sortedCube].append(cube)
        else:
            cubesSorted[sortedCube] = [cube]
    print(cubesSorted)

    for sortedCubeKey in cubesSorted:
        if len(cubesSorted[sortedCubeKey]) == 5:
            print(cubesSorted[sortedCubeKey])
