## The LogLog Algorithm

--

### Some Math

$[0, 1)$ and binary sequences ($\\{0, 1\\}^\infty$) {% fragment %}

Random hash functions: &nbsp; $f: \mathcal{S} \rightarrow [0, 1)$ {% fragment %}

Practicalities: finite binary sequences and pseudo-random hash functions {% fragment %}

--

### Data Structure

```python
# number of registers, B is a small number
NUM_REG = 2 ** B

class LogLog(object):

    # __register is some number of bits
    __registers = [bits(SIZE) for i in 0..NUM_REG]
```

--

### Add

Given our pseudo-random hash function &nbsp; `random_hash`:

```python
class LogLog(object):
    __registers = [bits(SIZE) for i in 0..NUM_REG]

    def add(self, item):
        # hash the object and OR it with register
        hash = random_hash(item)
        index = hash[0:B].toInt
        self.__registers[index] = self.__registers[index] | hash[B:]
```

--

### Cardinality

```python
class LogLog(object):
    __register = [bits(SIZE) for i in 0..NUM_REG]

    # def add(self, other): ...

    def size(self):
        size = 0.0
        for register in self.__registers:
            # count the number of consecutive 1's
            exp = first_zero(register) - 1
            size += floor(2 ** exp)
        return BIAS * size / 2 ** B
```

--

## Why does it work?

If $N$ is the true cardinality of a multiset $S$, then
the length &nbsp;$n$&nbsp; of the sequences of 1's is an
estimator for &nbsp; $\log_2(N)$ &nbsp; (with an additive bias of
about 1.33)

More mathematically: {% fragment %}

$\lim_{N \rightarrow \infty} \frac{1}{N} \mathbb{E}(2^n) = 1 + o(1) + \delta_N$
where $|\delta_N| < 10^{-6}$. {% fragment %}

http://algo.inria.fr/flajolet/Publications/DuFl03-LNCS.pdf

--

## What are the benefits?

- If you have a set of size $N$, you only need $\log_2(\log_2(N))$ bits (hence the
  name "LogLog") {% fragment %}
- Still linear time to calculate size {% fragment %}
- Error is about $1.3/\sqrt{m}$ where $m$ is the number of registers used {% fragment %}
- Can actually take unions/intersections without losing accuracy {% fragment %}

--

## Why does it *not* &nbsp; work?

1. The variance is too large, i.e. you can't be confident about your
solution. {% fragment %}

2. The error is too large: For 0.1% error on a set of size 4 billion,
you need about 3.3MB of compute space {% fragment %}
