# encoding:utf-8
import threading
import time
import _thread

# 装饰器的使用
# def have_arg(arg):
#     def func(pre_func):
#         def func_inner():
#             if arg == 'good':
#                 print("出去玩")
#             if arg == "bad":
#                 print("不出去玩")
#             return pre_func()
#
#         return func_inner
#
#     return func
#
#
# @have_arg('good')
# def func1():
#     print('天气非常好')
#
#
# @have_arg('bad')
# def func2():
#     print("天气不好")
#
#
# func1()
# func2()

#
# def runner(thread_name, delay):
#     """多线程(方法一)"""
#     count = 0
#     while count < 5:
#         print(thread_name + " 线程开始")
#         print("%s:%s" % (thread_name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
#
#         time.sleep(delay)
#         count += 1
#         print("{}:{}".format(thread_name, str(count)))
#
#
# try:
#     _thread.start_new_thread(runner, ("thread_1", 2))
#     _thread.start_new_thread(runner, ("thread_2", 3))
# except:
#     print("线程创建失败")
#
# while True:
#     pass

# class MyThread(threading.Thread):
#     """多线程（方法二）"""
#
#     def __init__(self, thread_name, time_delay, thread_count):
#         threading.Thread.__init__(self)
#         self.thread_name = thread_name
#         self.time_delay = time_delay
#         self.thread_count = thread_count
#
#     def run(self):
#         print(self.thread_name + " 线程开始")
#         runner(self.thread_name, self.time_delay, self.thread_count)
#         print(self.thread_name + " 线程结束")
#
#
# def runner(thread_name, delay, count):
#     while count:
#         time.sleep(delay)
#         # print("%s:%s" % (thread_name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
#         print("%s:%s" % (thread_name, time.ctime(time.time())))
#         count -= 1
#
#
# thread1 = MyThread("thread_1", 4, 5)
# thread2 = MyThread("thread_2", 2, 5)
#
# # 开启线程
# thread1.start()
# thread2.start()
# print("退出主线程")

# 字典中的常用方法测试
# 字典反转
dic = {"name": "chenqiong", "age": 18, "univ": "anli", "sex": "man"}
dic3 = dict([(v, k) for k, v in dic.items()])
print(dic3)
# dic1 = {"name": "wangzedong", "age": 18, "univ": "anli"}
# # 遍历字典key，value
# for key, value in dic.items():
#     print("{}:{}".format(key, value))
# dic['name'] = "dongze"
# print("name:" + dic['name'])
# # 删除字典给定键 key 所对应的值
# P = dic.pop('age')
# print(P)
# # 重新给age赋值
# dic["age"] = 18
# print(dic)
# # 以列表返回一个字典所有的键
# lis = dic1.keys()
# print(lis)
# # 返回值格式:dict_keys(['name', 'age', 'univ'])
# lis = list(dic1.keys())
# print(lis)
# # 返回值格式:['name', 'age', 'univ']
# # 两个字典，dic1,dic2 合并成为一个字典，并把dic2中缺少的键赋值为默认值null
# dic1 = {"name": "wangzedong", "age": 18, "univ": "anli"}
# dic2 = {'name': "wang"}
# for i in lis:
#     dic2.setdefault(i, "null")
# print(dic2)
# # 删除字典中的指定元素
# del dic2['age']
# print(dic2)
# # 删除字典内的随机一个键，一般是最后一个
# dic2.popitem()
# print(dic2)
# # 删除字典内所有元素
# dic2.clear()
# print(dic2)

# # 元组
# tuple1 = ("s", "m")
# # 遍历数组
# for i in tuple1:
#     print(str(i), end=' ')
# # 换行
# print()
# # 打印第1个元组元素
# print(tuple1[0])
# # 查看元组长度
# print(len(tuple1))
# # 输出元组的最大值
# print(max(tuple1))
# # 输出元组的最小值
# print(min(tuple1))
# # 输出元组中的1出现的次数
# print(tuple1.count("s"))
# # 输出元组中的1的索引
# print(tuple1.index("s"))  # 返回的是第一次出现的位置
# lis = [1, 2]
# tuple2 = (lis, "d", "f")
# print(tuple2)
# print(id(tuple2))
# lis.append(3)
# print(lis)
# print(tuple2)
# print(id(tuple2))
# list 的用法
# lis = [1, 2, 3, 4]
