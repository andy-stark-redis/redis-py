# EXAMPLE: connect_cluster_tls_client_auth
"""Basic connection example with TLS and client authentication.
"""

# STEP_START connect_cluster_tls_client_auth
import redis

r = redis.RedisCluster(
    host='redis-15313.c34461.eu-west-2-mz.ec2.cloud.rlrcp.com',
    port=15313,
    decode_responses=True,
    ssl=True,
    ssl_certfile="/Users/andrew.stark/Documents/Repos/forks/redis-py/doctests/redis-db-12605866.crt",
    ssl_keyfile="/Users/andrew.stark/Documents/Repos/forks/redis-py/doctests/redis-db-12605866.key",
    ssl_ca_certs="/Users/andrew.stark/Documents/Repos/forks/redis-py/doctests/redis_ca.pem",
    ssl_cert_reqs="required",
    username="default",
    password="MrlnkBuSZqO0s0vicIkLnqJXetbSTCan",
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
