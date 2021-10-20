def ways(data, k):
    if k==0:
        return 1

    s = len(data) -k
    if data[s] == '0':
        return 0
    result = ways(data, k-1)
    if k>=2 and int(data[s:s+2])<=26:
        result+= ways(data, k-2)
    return result

def num_ways(data):
    return ways(data, len(data))

def main():
    data = input("Enter all numbers")
    print("Ways:", num_ways(data))

main()



