import pandas as pd

df = pd.DataFrame(data)
# 1. SELECT * FROM data;
df
 
	
# 2. SELECT * FROM data LIMIT 10;
df.head(10)
 
	
# 3. SELECT id FROM data;  //id 是 data 表的特定一列	
df['id']
	
# 4. SELECT COUNT(id) FROM data;
df['id'].shape[0]
 
	
# 5. SELECT * FROM data WHERE id<1000 AND age>30;
df[(df['id'] < 1000) & (df['age'] > 30)]
 
	
# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
df.groupby('id').order_id.nunique()
 
	
# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
pd.merge(table1, table2, on='id', how='inner')
 
	
# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
pd.concat([table1, table2]).drop_duplicates()
 
	
# 9. DELETE FROM table1 WHERE id=10;
index = df[df['id'] == 10].index
df.drop(index, inplace=True)
 
	
# 10. ALTER TABLE table1 DROP COLUMN column_name;
#axis=0跨行，axis=1跨列
df.drop(['column_name'], axis=1)