# EXAMPLE: connect_cluster_tls
"""Cluster connection example with TLS.
"""

# STEP_START connect_cluster_tls
import redis

r = redis.RedisCluster(
    host='redis-18141.c34428.eu-west-2-mz.ec2.cloud.rlrcp.com',
    port=18141,
    decode_responses=True,
    ssl=True,
    ssl_ca_certs="/Users/andrew.stark/Documents/Repos/forks/redis-py/doctests/redis_ca.pem",
    username="default",
    password="d8gzw2azTFVSh0tTPDsvuzc2BDC1dOQN",
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
