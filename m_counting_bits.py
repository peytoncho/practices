def counting_bits(num):
    res = []
    count = rest = 2
    for i in range(0, num+1):
        if i==0 or i==1:
            res.append(i)
        else:
            res.append(res[i-count] + 1)
            rest -= 1
            if rest == 0:
                count = rest = count * 2

    return res


def counting_bits_dp(num):

    # f(n) = f(n/2) + 1
    # f(n) = f(n/2)

    res = [0 for _ in range(num+1)]
    for i in range(1, num+1):
        if i & 0x01:
            res[i] = res[i//2] + 1
        else:
            res[i] = res[i//2]
    return res


test_n = [2,3,5,10]
for n in test_n:
    # print(counting_bits(n))
    print(counting_bits_dp(n))

