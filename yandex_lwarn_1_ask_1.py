data = list(map(str, input().split(' -> ')))
for _ in range(int(input())):
    index = data.index(input())
    if index == len(data) - 1:
        print(f'{data[index - 1]} -> {data[index]}')
    elif index == 0:
        print(f'{data[index]} -> {data[index + 1]}')
    else:
        print(f'{data[index - 1]} -> {data[index]} -> {data[index + 1]}')