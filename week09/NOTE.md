## 学习笔记

## 
```
import pymysql
 
pymysql.install_as_MySQLdb()
```
改成
```
import MySQLdb
```

根据官网所述，Django框架中使用mysqlclent需要版本在1.3.13或者更高版本。
而使用pip install pymysql目前最高只能下载0.9.3版本。
真的气，网上也没找到升级pymysqlclient版本的方法。
所以只能采取不需要依赖第三方库的mysqldb进行替换。

















