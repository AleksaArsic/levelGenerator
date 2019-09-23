import sys

w, h = 32, 30

if __name__ == "__main__":

    level = [[0 for _ in range(w)] for _ in range(h)]

    n = int(input("Enter number of platforms: "))

    platforms = [0 for _ in range(n * 3)]

    for i in range(0, len(platforms), 3):
        platforms[i], platforms[i + 1], platforms[i + 2] = map(int, input("Enter (x, y, len) for platform number {} : ".format(i // 3)).split())
    
    print(platforms)

    for i in range(0, len(platforms) - 2, 3):
        x, y, length = platforms[i], platforms[i + 1], platforms[i + 2]
        for j in range(x, x + length):
            level[y - 1][j - 1] = 1

    print()
    for array in level:
        print(array)

    file = open('levelMap.h', "w")

    file.write("const u8 level_map[] = \n{")

    for array in level:
        file.write("\n\t")
        file.write(', '.join(str(x) for x in array))
        file.write(',')

    file.write("\n};")