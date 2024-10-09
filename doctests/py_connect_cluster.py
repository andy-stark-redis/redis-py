# EXAMPLE: connect_cluster
"""Cluster connection example.
"""

# STEP_START connect_cluster
import redis

r = redis.RedisCluster(
    host='localhost',
    port=6379,
    decode_responses=True,
    username="yourUsername",
    password="yourPassword",
)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
# >>> bar
# STEP_END

# REMOVE_START
assert success
assert result == "bar"
# REMOVE_END
