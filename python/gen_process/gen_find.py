import pandas as pd
import argparse

parse = argparse.ArgumentParser(description="""
        找出在相同列出现过的基因，例如：基因XJY如果在A列、C列、F列均出现过，则输入文档中增加一条"XJY A   C   F    ";列之间的分割使用tab符。        
        """)
parse.add_argument("-name",help='用name作为名字，不用加后缀，如文件名是data.xlxs,则输入data.')
parse.add_argument("-type",default='xlsx',help='文件类型，默认是xlsx，支持xls,csv，tsv格式。')
args = parse.parse_args()

name = args.name
file_type = args.type

if file_type =="xlsx":
    file_name = name+'.xlsx'
    data = pd.read_excel(file_name)
if file_type =='xls':
    file_name = name+'.xls'
    data = pd.read_excel(file_name)
if file_type == 'csv':
    file_name = name+'.csv'
    data = pd.read_csv(file_name)
if file_type == 'tsv':
    file_name = name+'.tsv'
    data = pd.read_tsv(file_name)

row = len(data)
col = len(data.iloc[0,:])
result = ''
already = set()         #用来标记已经完成
tran ={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L'}
for i in range(row):
    for j in range(0,col):
        now = data.iat[i,j]
        print('now:',now)
        if now in already or str(now) == 'nan':
            continue

        tmp = now+'\t'
        count = 0
        for a in range(col):
            if now in data.iloc[:,a].values:
                tmp += (tran[a]+'\t')
                count += 1
                # print(tmp)
        if count>1:
            print(tmp)
            already.add(now)
            result+=(tmp+'\n')
with open(name+'_new.csv','w') as f:
    f.write(result)
