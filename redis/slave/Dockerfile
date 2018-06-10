FROM redis

ADD redis.conf /redis-config/redis.conf

ENTRYPOINT ["/usr/local/bin/redis-server", "/redis-config/redis.conf"]