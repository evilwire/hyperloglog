## What is HyperLogLog?

HyperLogLog is an algorithm to estimate the *cardinality*
of multisets, i.e. the number of *unique* elements in
collection. Authors: Flajolet, Fusy, Ganouet, Meunier.

---

## What is the big deal with cardinality?

### How about:

```python
def naivesize(myset):
    """ gets the size of my set"""
    myset.foldLeft(lambda aggr, x: aggr + 1, 0)
```

### Problem

Multisets & double counting, e.g., {1, 2, 5, 1, 3, 5}.
Expect 4, but &nbsp; `naivesize` &nbsp; tells me 6.

---

## What does it take to size multisets?

For *exact* size: $O(n)$ for space, and $O(n\log(n))$ for time,
where $n$ is the cardinality.

---

### Q: Can we sacrifice accuracy for speed and space?

<p class="fragment">Yes, via probabilistic algorithms like HyperLogLog</p>
