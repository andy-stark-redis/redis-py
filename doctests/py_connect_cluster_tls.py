# EXAMPLE: connect_cluster_tls
"""Cluster connection example with TLS.
"""

# STEP_START connect_cluster_tls
import redis

r = redis.RedisCluster(
    host='<host>',
    port=<port>,
    decode_responses=True,
    ssl=True,
    ssl_ca_certs="<path_to_redis_ca.pem_file>",
    username="default",
    password="<password>",
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
