## A Facebook Use Case

--

## Intersecting HLL

```python

class HyperLogLog(LogLog):
    # def add, size ...

    def intersect(self, other):
        """ A near constant time intersection of two HLLs"""
        new_hll = HyperLogLog()
        new_hll.__registers = [
            self.__registers[i] & other.__registers[i]
            for i in len(self.__registers)
        ]
        return new_hll
```

--

## If Facebook Had a Notion of a Clique...

... They may want to represent cliques as HLL.

- clique overlap analytics would be $O(n + m)$ algorithm
  (as opposed to $O(nm)$) {% fragment %}
- we can predict clique properties based on clique "distance" {% fragment %}
- we can increase interactivity of the overlap and property analytics via a
  combination of real-time and batch processes {% fragment %}

---

# Thank You

--

## References

- LogLog Algo: http://algo.inria.fr/flajolet/Publications/DuFl03-LNCS.pdf

- HyperLogLog Algo: http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf

- Highly Scalable Webpost: https://highlyscalable.wordpress.com/2012/05/01/probabilistic-structures-web-analytics-data-mining/

--

## More References

- Probabilistic Counting Analysis: http://arxiv.org/abs/0801.3552

- Google SuperLogLog: http://research.google.com/pubs/pub40671.html