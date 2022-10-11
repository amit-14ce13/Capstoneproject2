import pandas as pd
import math
list3 = []
file = pd.read_table('amit',compression= 'gzip')
file.columns = ['date_time', 'post_event_list',  'post_product_list',
                                 'post_page_event', 'page_url', 'exclude_hit']
df2 = pd.DataFrame().assign(post_event_list = file["post_event_list"], post_product_list = file["post_product_list"])
df2 = df2.dropna()
print(len(df2))
list2 = df2["post_event_list"].str.split(",", n= -1, expand = False)
for i in list2:
    for event in range(len(i)):
        if i[event] == '20113':
             list3.append((','.join(i)))
#print(list3)
df3 = df2.loc[df2["post_event_list"].isin(list3)]
df3 = df3.reset_index(drop = True)
#print(df3["post_product_list"][1])
#print(df3)
df4 = df3["post_product_list"].str.split(",", n= -1, expand = True)
df4 = df4.stack()
df4 = df4.reset_index(drop = True)
df4 =df4.str.split(";|;;;", n= -1, expand = True)
nan_value = float("NaN")
df4.replace("", nan_value, inplace=True)
df4.dropna(how='all', axis=1, inplace = True)
df4.columns = range(df4.shape[1])

df6= df4.iloc[:,2]
df6= df6.str.split("|", n= -1, expand = True)
#print(df6)
df6a = df6.iloc[:,0].str.replace("=",'').astype(float)
df6b = df6.iloc[:,1].str.replace("=",'').astype(float)
df6c = df6.iloc[:,2].str.replace("=",'').astype(float)
df6=pd.concat([df6a,df6b,df6c],axis=1)
df6 = df6.fillna(0)
df6.columns = ["Event1",'Event2','Event3']
df6 = df6.astype(int)
df6.loc[df6["Event1"]== 201131, 'count'] = 1
df6.loc[df6["Event2"]== 201131, 'count'] = 1
df6.loc[df6["Event3"]== 201131, 'count'] = 1
df6 = df6.fillna(0)
#df6.to_csv('file3.csv')
#print("done sucessfully")

frames = [df4.iloc[:,[0,1]], df6.iloc[:,3]]
df7 = pd.concat(frames, axis= 1)
df7.columns = range(df7.shape[1])
df7.columns = ['Dealer_ID','AdID','Event Count1' ]

df8 = df7.groupby(['Dealer_ID','Ad_ID'], sort=False, as_index=False).sum()
#print(df8)
df8.to_csv('final file.csv')
Total1 = df8['Event Count1'].sum()
print(Total1)

