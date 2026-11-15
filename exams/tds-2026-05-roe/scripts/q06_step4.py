def fnv1a32(s):
    h = 2166136261
    for byte in s.encode('utf-8'):
        h = (h * 16777619) ^ byte
    return h & 0xFFFFFFFF

cache_key = "body_version: version-from-the-trace source: cache uri: /api/v1/data"
hash_value = fnv1a32(cache_key)
print(f"fnv1a32: {hash_value:08x}")
