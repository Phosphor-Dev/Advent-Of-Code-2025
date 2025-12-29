def getData(filename):
    with open (filename, "r") as file:
        data_list = [line.rstrip('\n') for line in file]
    return data_list


def main():
    path = r"Day 1\input.txt"
    turns = getData(path)

    counter = 0
    dialPos =  50
    for turn in turns:
        magnitude = int(turn[1:]) % 100
        if turn[0] == "L":
            dialPos -= magnitude
        if turn[0] == "R":
            dialPos += magnitude
        if dialPos < 0:
            dialPos =  100-(-dialPos)
        if dialPos > 99:
            dialPos =  dialPos - 100
        if dialPos == 0:
            counter += 1
    return counter

print(main())

