# EXAMPLE: connect_cluster
"""Cluster connection example.
"""

# STEP_START connect_cluster
import redis

r = redis.RedisCluster(
    host='redis-13891.c34425.eu-west-2-mz.ec2.cloud.rlrcp.com',
    port=13891,
    decode_responses=True,
    username="default",
    password="wtpet4pI5EgyJHyldPwR7xM7GaZB0EcG"
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
