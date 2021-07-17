#  贪心算法中的assign cookie问题


def minPrize(num, scores):
    if num == 0:
        return 0

    res = [1] * num
    index = scores.index(min(scores))
    for i in range(0, num - 1):
        if scores[(index + i + 1) % num] > scores[(index + i) % num]:
            res[(index + i + 1) % num] = res[(index + i) % num] + 1

    for i in range(0, num - 1):
        if scores[(index - i - 1) % num] > scores[(index - i) % num]:
            res[(index - i - 1) % num] = max(res[(index - i - 1) % num], res[(index - i) % num] + 1)

    return sum(res)


if __name__ == "__main__":
    num = int(input())
    score_temp = input().split()
    score = [int(i) for i in score_temp]

    result = minPrize(num, score)
    print(result)
