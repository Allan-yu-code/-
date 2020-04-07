from redis import Redis, StrictRedis

# redis链接
redis_conn = Redis(host="127.0.0.1",port=6379,db=1)
# 如果设置了密码
# redis_conn = Redis(host="127.0.0.1",port=6379,db=1,password="123456")

"""字符串操作"""
# 添加一个字符串数据 set name xiaoming
# redis_conn.set("name","xiaoming")

# 添加一个临时数据, setex title 30 hello
# redis_conn.setex("title",30,"hello")

# 获取一个字符串
# name = redis_conn.get("name")
# print(name)
# print(name.decode())

# 删除key,因为del是一个关键词,所以在redis模块,凡是命令如果是一个关键词,全部改成单词的全拼
# redis_conn.delete("name")

# 哈希的操作
dict1 = {
    "liubei": 28,
    "guanyu": 20,
    "zhangfei": 14,
}
redis_conn.hmset("brother",dict1)


# 获取哈希里面的所有成员
dict_data = redis_conn.hgetall("brother")
print(dict_data) # {b'liubei': b'28', b'guanyu': b'20', b'zhangfei': b'14'}
for key,name in dict_data.items():
    print(key.decode(),name.decode())


age = dict_data.get("liubei".encode()).decode()
print(age) # 28