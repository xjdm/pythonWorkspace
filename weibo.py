import redis

pool=redis.ConnectionPool(host='192.168.31.100',port=6379,db=0)
r = redis.StrictRedis(connection_pool=pool)

pipe = r.pipeline()
pipe_size = 100000

len = 0
key_list = []
print (r.pipeline())
keys = r.keys("*cm*")
sum_cm_count=0
for key in keys:
    print (key,end='')
    print ("的长度",end='')
    print (r.llen(key))
    sum_cm_count = sum_cm_count + 1
print(sum_cm_count)
