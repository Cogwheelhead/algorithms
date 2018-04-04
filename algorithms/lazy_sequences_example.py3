from functools import partial
from itertools import count, islice, tee
from toolz import compose


def drop(n, sequence):
    return islice(sequence, n, None)

tail = partial(drop, 1)


def zip_with(with_func):
    return compose(partial(map, with_func), zip)


def primes():
    def erato_sieve(sequence):
        current_prime = next(sequence)  
        yield current_prime

        sieved = filter(lambda x: x % current_prime, sequence)
        yield from erato_sieve(sieved)

    return erato_sieve(count(2))


def fibs():
    yield 1
    yield 1
    
    fibs1, fibs2 = tee(fibs())
    yield from zip_with(sum)(fibs1, tail(fibs2))