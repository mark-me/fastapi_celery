import redis

redis_cli = redis.Redis(
    host='localhost',
    port=6379,
    charset="utf-8",
    decode_responses=True
    )
connection = redis_cli.ping()

print(connection)