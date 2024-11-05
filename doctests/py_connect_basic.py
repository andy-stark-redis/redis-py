# EXAMPLE: connect_basic
"""Basic connection example.
"""

# STEP_START connect_basic
import redis

r = redis.Redis(
    host='<host>',
    port=<port>,
    decode_responses=True,
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
