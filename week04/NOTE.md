## pandas学习总结

## 一、Pandas数据结构

1、import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

2、S1=pd.Series([‘a’,’b’,’c’]) series是一组数据与一组索引（行索引）组成的数据结构

3、S1=pd.Series([‘a’,’b’,’c’],index=(1,3,4)) 指定索引

4、S1=pd.Series({1:‘a’,2:’b’,3:’c’}) 用字典形式指定索引

5、S1.index() 返回索引

6、S1.values() 返回值

7、Df=pd.DataFrame([‘a’,’b’,’c’]) dataframe是一组数据与两组索引（行列索引）组成的数据结构

8、Df=pd.DataFrame([[a,A],[b,B],[c,C]],columns=[‘小写’,’大写’]，index=[‘一’,’二’,’三’])

Columms 为列索引，index为行索引

9、pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyspider 清华镜像

10、data={‘小写’:[‘a’,’b’,’c’],’大写’:[‘A’,’B’,’C’]} 传入字典

Df=Pd.DataFrame(data)

11、Df.index() df.columns()

二、读取数据

12、df=pd.read_excel(r’C:\user\...xlsx’,sheet_name=’sheet1’) 或

Pd.read_excel(r’C:\user\...xlsx’,sheet_name=0) 读取excel表

13、Pd.read_excel(r’C:\user\...xlsx’,index_col=0,header=0)

index_col指定行索引，header指定列索引

14、pd.read_excel(r’C:\user\...xlsx’,usecols=[0,1]) 导入指定列,不能有index_col和header

15、pd.read_tablel(r’C:\user\...txt’，sep=’ ’) 导入txt文件,sep指定分隔符是什么

16、df.head(2) 展示前两行，默认展示前5行

17、df.shape 显示数据几行几列，不包含行和列索引

18、http://df.info() 可查看表中数据的类型

19、df.describe() 可获得表中数值类型指端的分布值（和、平均值、方差等）

三、数据预处理

20、http://df.info() 可显示表中哪个数据为空

21、df.isnull() 方法可以判断哪个值是缺失值，如果缺失返回True，否则为False

22、df.dropna() 默认删除含缺失值的行

23、df.dropna(how=’all’) 删除全为空值的行，不全为空值的行不会删除

24、df.fillna(0) 用0填充所有空值

25、df.fillna({‘性别’:’男’,’年龄’:’30’}) 对性别列中空值填充男，年龄填充30

26、df.drop_duplicates() 默认对所有值进行重复值检查，保留第一行的值

27、df.drop_duplicates(subset=’性别’) 对性别列中重复值查询保留第一行

28、df.drop_duplicates(subset=[’性别’,’公司’]，keep=’last’) 对性别和公司两列查重

keep设置默认为first（保留第一个），可设置为last（保留最后一个） 或False(不部不保留)

29、df[‘ID’].dtype 查看ID列的数据类型

30、df[‘ID’].astype(‘float’) 将ID列的数据类型转换为float类型

31、数据类型：int、float、object、string、unicode、datetime

32、df[‘ID’][1] ID列的第二个数据

33、df.columns=[‘大写’,’小写’,’中文’] 为无索引表添加列索引

34、df.index=[1,2,3] 添加行索引

35、df.set_index(‘编号’) 指明要用的列作为行索列

36、df.rename(index={‘订单编号’:’新订单编号’,’客户姓名’:’新客户姓名’}) 对行索引进行重新命名

37、df.rename(columns={1:’一’,2:’二’}) 对列索引进行重新命名

38、df.reset_index() 默认将全部index转化为column

39、df.reset_index(level=0) 将0级索引转化为column

40、df.reset_index(drop=True) 删除原有索引

四、数据选择

41、df[[‘ID’,’姓名’]] 多个列名要装入list

42、df.iloc[[1,3],[2,4]] 用行列编号选择数据

43、df.iloc[1,1] 选取表中的第3行2列数据，第一行默认为列索引

44、df.iloc[:,0:4] #获取第1列到第4列的值

45、df.loc[‘一’] #loc用行名选取的行数据，格式是Series，但可以用列表形式访问

46、df.loc[‘一’][0] 或 df.loc[‘一’][‘序号’]

47、df.iloc[1]#iloc用行编号选取行数据

48、df.iloc[[1,3]]#多行编号选取行数据，要用list封装，不然变成行列选取

49、df.iloc[1:3]#选择第二行和第四行

50、df[df[‘年龄’]<45] #加判断条件返回符合条件的全部数据，不局限年龄列

51、df[(df[‘年龄’]<45)&(df[‘ID’]<4)] #判断多条件选择数据

52、df.iloc[[1,3],[2,4]] 相当于df.loc[[‘一’,’二’],[‘年龄’,’ID’]] #loc是名，iloc是编号

53、df[df[‘年龄’]<45][[‘年龄’,’ID’]]#先通过年龄条件选择行，再通过不同索引指定列

54、df.iloc[1:3,2:4]#切片索引

五、数值操作

55、df[‘年龄’].replace(100,33)#对年龄列中的100替换成33

56、df.replace(np.NaN,0)#相当于fillna(),其中np.NaN是python中缺省值的表示方式

57、df.replace([A,B],C)#多对一替换，A、B替换成C

58、df.replace({‘A’:’a’,‘B’:’b’,‘C’:’c’})#多对多替换

59、df.sort_values(by=['申请单编号'],ascending=False)#申请单编号列降序排列，Ture升序排列（默认）

60、df.sort_values(by=['申请单编号'],na_position=’first’)#申请单编号列升序排列，缺失值排在第一位

默认缺失值在最后一位last

61、df.sort_values(by=['col1',’col2’],ascending=[False,True])#多列排序

62、df[‘销量’].rank(method=’first’)#销量排名（不是排序），method有first\min\max\average

63、df.drop([‘销量’,’ID’],axis=1)#删除列,直接是列名

64、df.drop(df.columns[[4,5]],axis=1)#删除列,是编号

65、df.drop(colums=[‘销量’,’ID’])#此种方式删除列，可以不写axis=1

66、df.drop([‘a’,’b’],axis=0)#删除行,直接是列名

67、df.drop(df.index[[4,5]],axis=0)#删除行,是编号

68、df.drop(index=[‘a’,’b’])#此种方式删除行，可以不写axis=0

69、df[‘ID’].value_counts()#对ID列中数据出现的次数进行统计

70、df[‘ID’].value_counts(normalize=Ture,sort=False)#对ID列中数据出现的次数占比进行统计，并降序排序

71、df[‘ID’].unique()#获取列的唯一值

72、df[‘年龄’].isin([‘a’,11])#查看这列中是否包含a或11

73、pd.cut(df[‘ID’],bins=[0,3,6,10])#用bins指明切分区间

74、pd.qcut(df[‘ID’],3)#ID列切分成3个部分，每部分数据个数尽量一致

75、df.insert(2,’商品’,[‘书’,’笔’,’计算器’])#插入第三列

76、df[’商品’]=[‘书’,’笔’,’计算器’])#插新列，在表的最后面

77、df.T行列互换

78、df.tack()#把表格型数据转化成树形数据

79、df.set_index([‘ID’,’姓名’]).stack().reset_index()#宽表转换成长表，先将共同列设置成行索引，再对其他列

进行转化成树形数据，再重置行索引

80、df.melt(id_vars=[‘ID’,’姓名’],var_name=’year’,value_name=’sale’)#id_var参数指明宽表转换成长表时保持不

变的列，var_name参数表示原来的列索引转化为行索引对应的列名，value_name表示新索引对应值的列名

81、df[‘C1’].apply(lambda x:x+1)#相当于map(),只是需要和lambda配合

82、df.applymap(lambda x:x+1),对表中的所有数据执行相同函数运算

六、数据运算

83、df[‘ID’]+Df[‘ID’]#可进行加减乘除

84、df[‘ID’]>Df[‘ID’]#可进行> < == !=等比较运算

85、df.count()#统计每列的非空值的个数

86、df.count(axis=1)#统计每行的非空值的个数

87、df[‘ID’].count()#统计指定列的非空值的个数

88、df.sum(axis=1)#每列/行求和结果

89、df.mean(axis=1)#每列/行求均值

90、df.max(axis=1)#每列/行求最大值

91、df.min(axis=1)#每列/行求最小值

92、df.median(axis=1)#每列/行求中间值

93、df.mode(axis=1)#每列/行中出现最多的值

94、df.var(axis=1)#每列/行求方差

95、df.std(axis=1)#每列/行求标准差

96、df.quantile(0.25)#求1/4分位数，可以0.5、0.75等分位数

97、df.corr()#求整个DataFrame表中的相关性

七、时间序列

98、from datetime import datetime

99、datatime.now()#返回现在的时间年月日时分秒

100、datatime.now().year#返回年，可以.month\.day

101、datatime.now().weekday()-1#返回周几

102、datatime.now().isocalendar()#返回周数

103、 （2018，41，7）#2018年的第41周第7天

104、datatime.now().date()#只返回年月日

105、datatime.now().time()#只返回时间

106、datatime.now().strftime(‘%Y-%m-%d %H:%M:%S’)#返回2020-03-13 09:09:12

107、from dateutil.parer import parse

108、 parse(str_time)#将字符串的时间转化成为时间格式

109、pd.Datetimeindex([‘2020-02-03’,2020-03-05’])#设置时间索引

110、data[‘2018’]#获取2018年的数据

111、data[‘2018-01’]#获取2018年1月的数据

112、data[‘2018-01-05’:‘2018-01-15’]#获取这个时段的数据

113、非时间索引的表格处理

114、df[df[‘成交时间’]==datetime(2018,08,05)]

115、df[df[‘成交时间’]>datetime(2018,08,05)]

116、df[(df[‘成交时间’]>datetime(2018,08,05))&(df[‘成交时间’] <datetime(2018,08,15))]

117、cha=datatime(2018,5,21,19,50)-datatime(2018,5,18,17,50)

118、 cha.days#返回天的时间差

119、 cha.seconds#返回秒的时间差

120、 cha.seconds/3600#返回小时的时间差

121、datatime(2018,5,21,19,50)+timedelta(days=1)#往后移一天

122、datatime(2018,5,21,19,50)+timedelta(seconds=20)#往后移20秒

123、datatime(2018,5,21,19,50)-timedelta(days=1)#往前移一天

八、数据透视表

124、df.groupby(‘客户分类’).count()#客户分类后求数运算

125、df.groupby(‘客户分类’).sum()#客户分类后求和运算

126、df.groupby(‘客户分类’,’区域分类’).sum()#多列分类后求和运算

127、df.groupby(‘客户分类’,’区域分类’)[‘ID’].sum()#多列分类后ID求和运算

128、df[‘ID’]#DataFrame取出一列就是Series类型

129、df.groupby(df[‘ID’]).sum（） 相当于 df.groupby(‘ID’).sum（）

130、df.groupby(‘客户分类’).aggregate([‘sum’,’count’]# aggregate可实现多种汇总方式

131、df.groupby(‘客户分类’).aggregate({‘ID’：‘count’,’销量’： ‘sum’})

132、# aggregate可针对不同列做不同的汇总运算

133、df.groupby(‘客户分类’).sum().reset_index()#分组汇总后再重置索引，变为标准DataFrame

134、pd.pivot_table(data,values,index,columms,aggfunc,fill_value,margins,dropna,margins_name)

135、数据透视表，data:数据表df,values:值，index:行索引，columns:列索引，aggfunc:values的计算类型，fill_value:对空值的填充方式；margins:是否有合计列；margins_name:合计列的列名

136、pd.pivot_table(df,values=[’ID’,‘销量’],index=’客户分类’,columms=‘区域’,aggfunc={‘ID’：‘count’,’销量’：‘sum’}),fill_value=0,margins=Ture,dropna=None,margins_name=’总计’)

九、多表格拼接

137、pd.merge(df1,df2)#默认自动寻找两个表中的公共列进行拼接

138、pd.merge(df1,df2,on=“学号“)#on来指定连接列，连接列要是公共列

139、pd.merge(df1,df2,on=[‘学号’,’姓名’]#on来指定连接列，连接列要是公共列

140、pd.merge(df1,df2,left_on=‘学号’right_on=’编号’) #由公共列，但类名不同时用左右键指定

141、pd.merge(df1,df2,left_index=‘学号’right_index=’编号’)#两表公共列都是索引列时

142、pd.merge(df1,df2,left_index=‘学号’right_on=’编号’)#公共列一个时索引列一个时普通列

143、pd.merge(df1,df2,on=’学号’,how=’inner’)#返回公共列中对应的公共值拼接（内连接）

144、pd.merge(df1,df2,on=’学号’,how=’left’)#返回公共列中对应的左表值（左连接）

145、pd.merge(df1,df2,on=’学号’,how=’right’)#返回公共列中对应的右表值（右连接）

146、pd.merge(df1,df2,on=’学号’,how=’outer’)#返回公共列中对应的所有值（外连接）

147、pd.concat([df1,df2])#两个结构相同的表纵向连接，保留原索引值

148、pd.concat([df1,df2]，ignore_index=True)#两个结构相同的表纵向连接，重新设置索引值

149、pd.concat([df1,df2]，ignore_index=True).drop_duplicates()#拼接后去掉重复值

十、导出文件

150、df.to_excel(excel_writer=r’C:\users\zhoulifu\Desktop\测试.xlsx’)#导出文件格式.xlsx用to_excel方法，通过excel_writer参数来实现

151、df.to_excel(excel_writer=r’C:\users\zhoulifu\Desktop\测试.xlsx’,sheet_name=’文档’)

152、df.to_excel(excel_writer=r’C:\users\zhoulifu\Desktop\测试.xlsx’,sheet_name=’文档’，index=False)#导出是去掉索引

153、df.to_excel(excel_writer=r’C:\users\zhoulifu\Desktop\测试.xlsx’,sheet_name=’文档’，index=False,columns=[‘ID’,’销量’,‘姓名’])#设置导出的列

154、df.to_excel(excel_writer=r’C:\users\zhoulifu\Desktop\测试.xlsx’,sheet_name=’文档’，index=False,columns=[‘ID’,’销量’,‘姓名’],encoding=’utf-8’)#设置导出的列

155、df.to_excel(excel_writer=r’C:\users\zhoulifu\Desktop\测试.xlsx’,sheet_name=’文档’，index=False,columns=[‘ID’,’销量’,‘姓名’],encoding=’utf-8’,na_rep=0)#缺失值填充

156、writer=pd.ExcelWriter(excelpath,engine=’xlsxwirter’)#导出多个文件至一个文件的多个sheet

157、df1.to_excel(writer,sheet_name=‘表一’)

158、df2.to_excel(writer,sheet_name=’表二’)

159、writer.save()






