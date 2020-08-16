## 学习总结
本周学习的内容主要是python的一些 高级语法，对比前端而言，就像是 ES6、ES NEXT

### python的高级特性

generator 生成器
iterator 迭代器
collection 集合
pack/unpack 打包/解包
decorator 装饰器
context manager 上下文管理器

### python语言的一些高阶用法主要有以下几个特性：

generators生成器用法
collections包常见用法
itertools包常见用法
packing/unpacking封包/解包特性
Decorators装饰器
Context Managers上下文管理期
以上几个特性我会针对应用场景，使用注意事项，应用举例几个维度分别进行讲解，如果有同学对某个特性特别熟悉则可以直接跳过。

###generators生成器用法
generator一般用来产生序列类型的值得对象，一般都可以在for循环中迭代，也可以通过next方法调用，生成器可以通过yield关键字产生。

#### 生成器的作用：

减少内存占用
比如：利用迭代器的使用方式打开文件
```python
with open("/path/to/file") as f:
    for line in f:   # 这个地方迭代文件
        print(line)
```
提高运行效率

延迟运行，仅当需要运行的地方才开始执行

如下例子：
```python
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Print all the numbers of the Fibonacci sequence that are lower than 1000
for i in fibonacci_generator():
    if i > 1000:
        break
    print(i)
# 输出结果

0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
```
在python中可以使用生成器表达式去迭代一个对象，生成器表达式和列表最大的差别就在于是否一次性将结果计算完成，举例如下：
```python
a = (x * x for x in range(100))

# a is a generator object
print(type(a))

# Sum all the numbers of the generator
print(sum(a))

# There are no elements left in the generator
print(sum(a))
# 输出结果如下：

<class 'generator'>
328350
0
```
### collections包常见用法
collections包是标准库的一个模块，主要目的是用来扩展容器相关的数据类型，
我们可以通过dir查看collections包有哪些模块：
```python
>>> import collections
>>> dir(collections)
['Callable', 'Container', 'Counter', 'Hashable', 'ItemsView', 'Iterable', 'Iterator', 'KeysView', 'Mapping', 'MappingView', 'MutableMapping', 'MutableSequence', 'MutableSet', 'OrderedDict', 'Sequence', 'Set', 'Sized', 'ValuesView', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_abcoll', '_chain', '_class_template', '_eq', '_field_template', '_get_ident', '_heapq', '_imap', '_iskeyword', '_itemgetter', '_repeat', '_repr_template', '_starmap', '_sys', 'defaultdict', 'deque', 'namedtuple']
```
我们以Counter为例：
```
from collections import Counter

a = Counter('blue')
b = Counter('yellow')

print(a)
print(b)
print((a + b).most_common(3))
输出结果如下：

Counter({'u': 1, 'e': 1, 'l': 1, 'b': 1})
Counter({'l': 2, 'y': 1, 'e': 1, 'o': 1, 'w': 1})
[('l', 3), ('e', 2), ('y', 1)]
```
另外defaultdict也是常用的一个模块，defaultdict是dict的子类，允许我们通过工厂方法来动态创建不存在的属性，举例如下：
```python
from collections import defaultdict

my_dict = defaultdict(lambda: 'Default Value')
my_dict['a'] = 42

print(my_dict['a'])
print(my_dict['b'])
# 运行结果如下：

42
Default Value
```
在工作中经常用defaultdict来构造一颗树形数据结构来满足常规需求，实例如下：
```python
from collections import defaultdict
import json

def tree():
    """
    Factory that creates a defaultdict that also uses this factory
    """
    return defaultdict(tree)

root = tree()
root['Page']['Python']['defaultdict']['Title'] = 'Using defaultdict'
root['Page']['Python']['defaultdict']['Subtitle'] = 'Create a tree'
root['Page']['Java'] = None

print(json.dumps(root, indent=4))
# 运行结果如下：

{
    "Page": {
        "Python": {
            "defaultdict": {
                "Subtitle": "Create a tree",
                "Title": "Using defaultdict"
            }
        },
        "Java": null
    }
}
```
### itertools包常见用法
itertools包也是标准库的一个模块，常见的用法是用来扩展迭代器的使用，高效的执行迭代

通过dir方法来查看itertools都有哪些模块
```python
>>> import itertools
>>> dir(itertools)
['__doc__', '__file__', '__name__', '__package__', 'chain', 'combinations', 'combinations_with_replacement', 'compress', 'count', 'cycle', 'dropwhile', 'groupby', 'ifilter', 'ifilterfalse', 'imap', 'islice', 'izip', 'izip_longest', 'permutations', 'product', 'repeat', 'starmap', 'takewhile', 'tee']
```
我们以permutations举例如下：
```python
from itertools import permutations

for p in permutations([1,2,3]):
    print(p)
# 输出结果：

(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)
combinations示例如下：

from itertools import combinations

for c in combinations([1, 2, 3, 4], 2):
    print(c)
# 输出结果：

(1, 2)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
(3, 4)
```
另外chain模块也是常用模块之一
chain使用示例：
```python
from itertools import chain

for c in chain(range(3), range(12, 15)):
    print(c)
输出结果如下：

0
1
2
12
13
14
```
另外itertools工具包里还有很多常见的用法

### packing/unpacking特性
在函数参数里使用*args，**kwargs都很常见，但是以下的几种用法你们有试过吗？
```python
a, *b, c = [2, 7, 5, 6, 3, 4, 1]
print(a)
print(b)
print(c)
以上代码输出：

2
[7, 5, 6, 3, 4]
1
```
```python
def repeat(count, name):
    for i in range(count):
        print(name)

print("Call function repeat using a list of arguments:")
args = [4, "cats"]
repeat(*args)

print("Call function repeat using a dictionary of keyword arguments:")
args2 = {'count': 4, 'name': 'cats'}
repeat(**args2)
# 运行结果如下：

Call function repeat using a list of arguments:
cats
cats
cats
cats
Call function repeat using a dictionary of keyword arguments:
cats
cats
cats
cats
```
最后再回归到函数参数的例子上：
```python
def f(*args, **kwargs):
    print("Arguments: ", args)
    print("Keyword arguments: ", kwargs)

f(3, 4, 9, foo=42, bar=7)
```
以上代码输出：
```python
Arguments:  (3, 4, 9)
Keyword arguments:  {'bar': 7, 'foo': 42}
```
### Decorators装饰器
装饰器这个语法糖相信使用flask或者bottle的同学应该都不陌生，使用django的也应该经常会遇到，但是大家有没有去想过这个语法糖的应用场景呢？我简单整理了下，大概有以下几种装饰器：

缓存装饰器

权限验证装饰器

计时装饰器

日志装饰器

路由装饰器

异常处理装饰器

错误重试装饰器

拿缓存装饰器举例：
```python
def cache(function):
    cached_values = {}  # Contains already computed values
    def wrapping_function(*args):
        if args not in cached_values:
            # Call the function only if we haven't already done it for those parameters
            cached_values[args] = function(*args)
        return cached_values[args]
    return wrapping_function

@cache
def fibonacci(n):
    print('calling fibonacci(%d)' % n)
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(n) for n in range(1, 9)])
# 以上代码输出：

calling fibonacci(1)
calling fibonacci(2)
calling fibonacci(0)
calling fibonacci(3)
calling fibonacci(4)
calling fibonacci(5)
calling fibonacci(6)
calling fibonacci(7)
calling fibonacci(8)
[1, 1, 2, 3, 5, 8, 13, 21]
```
在python3中有一个包叫做lrucache，就是用的装饰器的语法糖进行实现。

lrucache的简单实用如下：
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    print('calling fibonacci(%d)' % n)
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(n) for n in range(1, 9)])
# 运行结果：

calling fibonacci(1)
calling fibonacci(2)
calling fibonacci(0)
calling fibonacci(3)
calling fibonacci(4)
calling fibonacci(5)
calling fibonacci(6)
calling fibonacci(7)
calling fibonacci(8)
[1, 1, 2, 3, 5, 8, 13, 21]
```
### Context Managers上下文管理期
最后我们再看python中的上下文管理器，这个语法糖在资源管理上有很常见的使用场景，比如上文中我用with open("file") as的用法，使用了with后就不用担心文件不会关闭了，在处理socket编程的时候也可以用。这个语法糖其实也不难就是两个魔术方法的实现，__enter__ 和 __exit__，一个控制入口，一个控制出口。

常规的使用with来统计一段代码运行时间的例子：
```python
from time import time


class Timer():
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time()
        return None  # could return anything, to be used like this: with Timer("Message") as value:

    def __exit__(self, type, value, traceback):
        elapsed_time = (time() - self.start) * 1000
        print(self.message.format(elapsed_time))


with Timer("Elapsed time to compute some prime numbers: {}ms"):
    primes = []
    for x in range(2, 500):
        if not any(x % p == 0 for p in primes):
            primes.append(x)
    print("Primes: {}".format(primes))
# 输出结果：

Primes: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
Elapsed time to compute some prime numbers: 1.055002212524414ms
```