import redis
import re


with open("lorem") as lorem_file:
    lines = lorem_file.readlines()
    lorem = " ".join(lines)

word_list = re.split("\s", lorem)
redis_conn = redis.StrictRedis(host="localhost", port=6379, db=0)
redis_conn.flushdb()
word_set = set([])

for word in word_list:
    word = word.strip(".").strip(",").lower()
    redis_conn.pfadd("lorem", word)
    word_set.add(word)

actual_size = len(word_set)
print actual_size

print redis_conn.pfcount("lorem")