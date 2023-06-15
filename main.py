from datetime import datetime
if __name__ == '__main__':
    n = 999
    binn = [i for i in bin(n)[2:]]
    count = 0
    while binn[0] != "0":
        count += 1
        if binn[-1] == "1":
            binn[-1] = "0"
        else:
            binn.pop(-1)
    print(count)
    print(datetime.now())
