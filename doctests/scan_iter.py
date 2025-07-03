# EXAMPLE: scan_iter
# HIDE_START
"""
Code samples for scan iteration page:
    https://redis.io/docs/latest/develop/clients/redis-py/scaniter
"""
# HIDE_END

# STEP_START scan
import redis

r = redis.Redis(decode_responses=True)
# REMOVE_START
r.flushall()
# REMOVE_END

r.set("key:1", "a")
r.set("key:2", "b")
r.set("key:3", "c")
r.set("key:4", "d")
r.set("key:5", "e")

for key in r.scan_iter():
    print(f"Key: {key}, value: {r.get(key)}")
# >>> Key: key:1, value: a
# >>> Key: key:4, value: d
# >>> Key: key:3, value: c
# >>> Key: key:2, value: b
# >>> Key: key:5, value: e
# STEP_END

# STEP_START zscan
r.zadd("battles", mapping={
    "hastings": 1066,
    "agincourt": 1415,
    "trafalgar": 1805,
    "somme": 1916,
})

for item in r.zscan_iter("battles"):
    print(f"Key: {item[0]}, value: {int(item[1])}")
# >>> Key: hastings, value: 1066
# >>> Key: agincourt, value: 1415
# >>> Key: trafalgar, value: 1805
# >>> Key: somme, value: 1916
# STEP_END

# STEP_START hscan
r.hset("details", mapping={
    "name": "Mr Benn",
    "address": "52 Festive Road",
    "hobbies": "Cosplay"
})

for key in r.hscan_iter("details", no_values=True):
    print(f"Key: {key}, value: {r.hget("details", key)}")

# >>> Key: name, value: Mr Benn
# >>> Key: address, value: 52 Festive Road
# >>> Key: hobbies, value: Cosplay
# STEP_END
