# EXAMPLE: connect_basic_tls_client_auth
"""Basic connection example with TLS and client authentication.
"""

# STEP_START connect_basic_tls_client_auth
import redis

r = redis.Redis(
    host='<host>',
    port=<port>,
    decode_responses=True,
    ssl=True,
    ssl_certfile="<path_to_redis-db-xxxxxxxx.crt_file>",
    ssl_keyfile="<path_to_redis-db-xxxxxxxx.key_file>",
    ssl_ca_certs="<path_to_redis_ca.pem_file>",
    ssl_cert_reqs="required",
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
