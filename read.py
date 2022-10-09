import pandas as pd
#list1 = []
list3 =[]
file = pd.read_table('amit',compression= 'gzip')
#print('read file')
file.columns = ['date_time', 'post_event_list',  'post_product_list',
                                 'post_page_event', 'page_url', 'exclude_hit']
#print(file.head())
#print(file["post_event_list"])
df2 = pd.DataFrame().assign(post_event_list = file["post_event_list"], post_product_list = file["post_product_list"])
df2 = df2.dropna()
#df3 = df2.head()
#print(df2["post_event_list"][0])
#print(df3)
list2 = df2["post_event_list"].str.split(",", n= -1, expand = False)
#print(type(list2))
#for lst in list2:
    #list1.append(lst.split(","))
#print(list1)
#print(type(list1[0]))
#print(list1[0])
#print((list1[0][1]))
#print(list1)
for i in list2:
    for event in range(len(i)):
        if i[event] == '20113':
             list3.append((','.join(i)))
#print(list3)
df3 = df2.loc[df2["post_event_list"].isin(list3)]
df3 = df3.reset_index(drop = True)
#print(df3["post_product_list"][0])
#print(df3)
df4 = df3["post_product_list"].str.split(",", n= -1, expand = True)
df4 = df4.stack()
df4 = df4.reset_index(drop = True)
df5 = df4.iloc[100000:150000]
df5 =df5.str.split(";|;;;", n= -1, expand = True)
nan_value = float("NaN")
df5.replace("", nan_value, inplace=True)
#print(df4)
df5.dropna(how='all', axis=1, inplace = True)
#print(df4)
df5.columns = range(df5.shape[1])

print(df5)
df6= df5.iloc[:,2]
df6= df6.str.split("|", n= -1, expand = True)
print(df6)
frames = [df5.iloc[:,[0,1]], df6.iloc[:,[0,1]]]
df7 = pd.concat(frames, axis= 1)
#print(df7)
df7.columns = range(df7.shape[1])
df7.columns = ['Dealer_ID','Header_ID','Event Count1', 'Event count2']
print(df7)
result = df7.dtypes
#print(result)





