# 分解模数n
def rsa_moder(n):
    base = 2
    while base < n:
        if n % base == 0:
            return base, n // base
        base += 1


# 求欧拉函数f(n)
def rsa_get_euler(prime1, prime2):
    return (prime1 - 1) * (prime2 - 1)


# 求私钥
def rsa_get_key(e, euler):
    k = 1
    while True:
        if (((euler * k) + 1) % e) == 0:
            return (euler * k + 1) // e
        k += 1


# 根据n,e计算d(或根据n,d计算e)
def get_rsa_e_d(n, e=None, d=None):
    if e is None and d is None:
        return

    arg = e
    if arg is None:
        arg = d

    primes = rsa_moder(n)
    p = primes[0]
    q = primes[1]

    d = rsa_get_key(arg, rsa_get_euler(p, q))

    return d


def test():
    str_fmt = 'n: {:<10} e: {:<10} d: {:<10}'

    # 解密
    n = 14666299
    d = 2101153
    e = get_rsa_e_d(n, None, d)
    print(str_fmt.format(n, e, d))

    n = 12748507
    e = 65537
    d = get_rsa_e_d(n, e, None)
    print(str_fmt.format(n, e, d))

    n = 0x36bc7d82d9e42084b4318a65ec92c204d5d40572b5f95bcd090884a1250bbaabdee3ab3b80c664ee34081580e12d819e46dbceb3d8baefec3dc102ad8aee9e0b0b4afa3ba186b3f435818ee96ddaeb0a17b28eeaea371a0da21b780d6cf20bc8ea9ad892003415bbdd4795125aa6dab598be332bee62ce9c2a0b9cfab7f9549
    e = 3
    d = get_rsa_e_d(n, e, None)
    print(str_fmt.format(n, e, d))



if __name__ == '__main__':
    test()