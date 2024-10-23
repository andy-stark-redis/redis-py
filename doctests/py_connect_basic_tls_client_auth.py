# EXAMPLE: connect_basic_tls_client_auth
"""Basic connection example with TLS and client authentication.
"""

# STEP_START connect_basic_tls_client_auth
import redis

r = redis.Redis(
    host='redis-14669.c338.eu-west-2-1.ec2.redns.redis-cloud.com',
    port=14669,
    decode_responses=True,
    ssl=True,
    ssl_certfile="/Users/andrew.stark/Documents/Repos/forks/redis-py/doctests/redis-db-12592910.crt",
    ssl_keyfile="/Users/andrew.stark/Documents/Repos/forks/redis-py/doctests/redis-db-12592910.key",
    ssl_ca_certs="/Users/andrew.stark/Documents/Repos/forks/redis-py/doctests/redis_ca.pem",
    ssl_cert_reqs="required",
    username="default",
    password="jj7hRGi1K22vop5IDFvAf8oyeeF98s4h",
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
