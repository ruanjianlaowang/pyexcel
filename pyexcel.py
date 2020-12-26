import pandas as pd

#欢迎添加老王微信（ruanjianlaowang）与关注【软件老王】公众号，有问题随时沟通！

if __name__ == '__main__':
    inputfile = '软件老王-source.xlsx'
    data = pd.read_excel(inputfile, engine='openpyxl')
    grp1 = data.groupby('待分类列')
    rcount = 1
    for name, group in grp1:
        print(group)
        name = name.replace('\n', '').replace('/', '')
        for i in range(len(group)):
            row = group.iloc[i].values  # 返回一个list
            cell = row[1]
            if cell is None:
                continue
            if not isinstance(cell, str):
                continue
            item = cell.strip('\n\r').split('\t')
            string = item[0]
            if string is None or len(string) == 0:
                continue
            else:
                print('这里获取group后明细值，软件老王可以单独处理，类别：' + name + '具体值：' + string)
