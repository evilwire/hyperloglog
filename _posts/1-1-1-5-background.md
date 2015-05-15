## The HyperLogLog Algorithm

--

## Some More Math

*Harmonic average* of $n_1, n_2,\dots,n_k$ is

$\frac{k}{\frac{1}{n_1} + \cdots + \frac{1}{n_k}}$

For example, the harmonic average of 2, 2, 2 is 2,
and harmonic average of 1, 2, 3 is $18/11 \approx 1.636$ {% fragment %}

--

## HyperLogLog Algorithm

```python

class HyperLogLog(LogLog):
    # Everything else the same as LogLog except...

    # When sizing, use harmonic average instead
    def size(self):
        sizes = []
        for register in self.__registers:
            # count the number of consecutive 1's
            exp = first_zero(register) - 1
            sizes.push(floor(2 ** exp))

        return HLL_BIAS * harmonic_mean(sizes)
```

--

## Why does HLL work better?

LogLog's average puts too much weight on large values; solved
by using harmonic means.

--

## What are the benefits?

- LogLog computation space {% fragment %}
- Linear algorithm {% fragment %}
- Much smaller variance: 96% confident that error is within
  $1.04/\sqrt{4m}$ {% fragment %}

--

## How about some benchmarks?

Setup: Redis HLL, input: Lorem Ipsum

```python
import redis

SET = set([])
REDIS_CLIENT = redis.StrictRedis(host="localhost",
                                 port=6379,
                                 db=0)
with open("lorem") as lorem_file:
    LOREM = lorem_file.read()

for word in LOREM.split(" "):
    SET.push(word)
    REDIS_CLIENT.pfadd("lorem", word)

actual_size, hll_size = len(SET), REDIS_CLIENT.pfcount("lorem")

print actual_size, hll_size
print "Error: %s%" % (100 * actual_size - hll_size) / actual_size
```

