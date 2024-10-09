# EXAMPLE: connect_basic_tls_client_auth
"""Basic connection example with TLS and client authentication.
"""

# STEP_START connect_basic_tls_client_auth
import redis

r = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True,
    ssl=True,
    ssl_certfile="./redis_user.crt",
    ssl_keyfile="./redis_user_private.key",
    ssl_ca_certs="./redis_ca.pem",
    ssl_cert_reqs="required",
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
