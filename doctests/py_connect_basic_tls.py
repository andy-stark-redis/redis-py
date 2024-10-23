# EXAMPLE: connect_basic_tls
"""Basic connection example with TLS.
"""

# STEP_START connect_basic_tls
import redis

r = redis.Redis(
    host='redis-14669.c338.eu-west-2-1.ec2.redns.redis-cloud.com',
    port=14669,
    decode_responses=True,
    ssl=True,
    ssl_ca_certs="/Users/andrew.stark/Documents/Repos/forks/redis-py/doctests/redis_ca.pem",
    username="default",
    password="wtpet4pI5EgyJHyldPwR7xM7GaZB0EcG",
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
