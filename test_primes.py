from app import primes


def test_primes():
    gen = primes()

    expected = [
        1,
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
    ]

    for i in range(len(expected)):
        p = gen.get_prime(i)
        e = expected[i]

        assert p == e
