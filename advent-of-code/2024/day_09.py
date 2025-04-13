from pathlib import Path


def parse_data(data: str) -> dict[complex, str]:
    files = []
    free_spaces = []
    print(data)
    print(data[0::2])
    print(data[1::2])
    for digit in data[0::2]:
        files.append(int(digit))
    for digit in data[1::2]:
        free_spaces.append(int(digit))
    return files, free_spaces


def part_1(files, free_spaces) -> int:
    s = 0
    for digit in files:
        s += digit
    blocks = []
    for i in range(len(files)):
        blocks.extend([i for _ in range(files[i])])
        try:
            blocks.extend(["." for _ in range(free_spaces[i])])
        except:
            pass
    for i in range(s):
        if blocks[i] == ".":
            blocks[i] = len(files) - 1
            files[-1] -= 1
            if files[-1] == 0:
                files.pop()
    checksum = 0
    for i in range(s):
        checksum += i * blocks[i]
    return checksum


def part_2(files, free_spaces) -> int:
    s = 0
    for digit in files + free_spaces:
        s += digit
    print(s)
    blocks = []

    file_index = 0
    i = 0
    while True:
        # Add file
        blocks.extend([i for _ in range(files[i])])
        # Fill space
        space = free_spaces[i]
        good = False
        while not good:
            for j in reversed(range(len(files))):
                print(space, files[j], j)
                if files[j] <= space:
                    blocks.extend([j for _ in range(files[j])])
                    space = space - files[j]
                    del files[j]
                    break
            if space:
                
            blocks.extend([["."] for _ in range(space)])
            good = True
            print(blocks)
        i += 1

    blocks = []
    print(files)
    for i in range(len(files)):
        blocks.extend([i for _ in range(files[i])])
        try:
            blocks.extend(["." for _ in range(free_spaces[i])])
        except:
            pass
    for i, space in enumerate(free_spaces):
        print(i)
        print(files)
        for j in reversed(range(len(files))):
            print(files)
            if files[j] <= space:
                del files[j]
                break
            print(files)
    for i in range(s):
        if blocks[i] == ".":
            blocks[i] = len(files) - 1
            files[-1] -= 1
            if files[-1] == 0:
                files.pop()
    checksum = 0
    for i in range(s):
        checksum += i * blocks[i]
    return checksum


def main() -> None:
    data = Path("input").read_text(encoding="utf-8")
    files, free_spaces = parse_data(data)
    # print(f"Part 1: {part_1(files, free_spaces)}")
    print(f"Part 2: {part_2(files, free_spaces)}")


if __name__ == "__main__":
    main()
