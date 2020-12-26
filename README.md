### 1.场景描述

因[文本相似性热度统计(python版)](https://www.cnblogs.com/ruanjianlaowang/p/12320273.html)需求中要根据故障类型进行分组统计，需要对excel进行分组后再分词统计，简单记录下，有需要的朋友可以直接拿走，不客气！

### 2.解决方案

采用pandas包首先进行分组，然后获取具体明细再进行分词处理（分词处理这里就不展开了），只介绍下python下excel分组，然后对具体明细进行处理。

#### 2.1 完整代码

```
import pandas as pd

if __name__ == '__main__':
    inputfile = '软件老王-source.xlsx'
    data = pd.read_excel(inputfile,engine='openpyxl')
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
                print('这里获取group后明细值，软件老王可以单独处理，类别：' +name + '具体值：' + string)

```

#### 2.2 执行效果

```
 待分类列      原因
0  软件老王1  主机不能加电
1  软件老王1  有时不能加电
2  软件老王1    开机加电
这里获取group后明细值，软件老王可以单独处理，类别：软件老王1具体值：主机不能加电
这里获取group后明细值，软件老王可以单独处理，类别：软件老王1具体值：有时不能加电
这里获取group后明细值，软件老王可以单独处理，类别：软件老王1具体值：开机加电
    待分类列       原因
3  软件老王2  自检报错或死机
4  软件老王2    机器噪音大
这里获取group后明细值，软件老王可以单独处理，类别：软件老王2具体值：自检报错或死机
这里获取group后明细值，软件老王可以单独处理，类别：软件老王2具体值：机器噪音大
    待分类列    原因
5  软件老王3  噪音问题
这里获取group后明细值，软件老王可以单独处理，类别：软件老王3具体值：噪音问题
```

#### 2.3 软件老王-source.xlsx

| 待分类列  | 原因           |
| --------- | -------------- |
| 软件老王1 | 主机不能加电   |
| 软件老王1 | 有时不能加电   |
| 软件老王1 | 开机加电       |
| 软件老王2 | 自检报错或死机 |
| 软件老王2 | 机器噪音大     |
| 软件老王3 | 噪音问题       |

**更多信息请关注公众号：「软件老王」**，关注不迷路，软件老王和他的IT朋友们，分享一些他们的技术见解和生活故事。

![hb](images\hb.png)

