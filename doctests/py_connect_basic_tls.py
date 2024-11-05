# EXAMPLE: connect_basic_tls
"""Basic connection example with TLS.
"""

# STEP_START connect_basic_tls
import redis

r = redis.Redis(
    host='<host>',
    port=<port>,
    decode_responses=True,
    ssl=True,
    ssl_ca_certs="<path_to_redis_ca.pem_file>",
    username="default",
    password="<password>",
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
