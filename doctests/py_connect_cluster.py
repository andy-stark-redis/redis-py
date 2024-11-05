# EXAMPLE: connect_cluster
"""Cluster connection example.
"""

# STEP_START connect_cluster
import redis

r = redis.RedisCluster(
    host='<host>',
    port=<port>,
    decode_responses=True,
    username="default",
    password="<password>"
)
# REMOVE_START
r.delete('foo')
# REMOVE_END

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
