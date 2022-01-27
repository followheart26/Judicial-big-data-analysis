# Judicial-big-data-analysis
# 司法大数据分析说明文档

## 引言：

在数据时代下，软件产业的迅速发展可以为其他行业带来便利，在司法实践中，面临着文档录入繁琐，海量判决文书检索困难，文书阅读效率低等问题，而在计算机领域，借由NLP，OCR,深度学习等技术的发展，开发出适合司法实践的辅助工具，可以提高判决的效率与公平性，对于社会的发展带来了极大的便利。本项目正是秉持着这种宗旨进行开发。

 

## 目标：

\1.   用户可以在前端页面上选择选择年份以及案件数量，系统根据用户的选择自动爬取对应的数据集并保存到本地

\2.   用户可以在前端页面上传本地的文本或者直接输入案件信息，系统对文本内容进行自动化分词，通过文本命名实体、词性分析等方法获取基本信息可能对应的实体，并将其展示为可选 项形式

\3.   用户可以根据需要的基本信息如当事人等，点击对应的可选项，以此对基本信息进行标注 

\4.   用户可以点击保存按钮将案件和基本信息保存到本地，文件分别为：案件文本.txt、标 注.json

 

## Ui界面展示：

![图形用户界面, 文本, 应用程序  描述已自动生成](file:///C:/Users/hp/AppData/Local/Temp/msohtmlclip1/01/clip_image002.jpg)

## 功能及实现概述：

###  1.爬虫

![图示  描述已自动生成](file:///C:/Users/hp/AppData/Local/Temp/msohtmlclip1/01/clip_image004.jpg)

设置完成开始日期和结束日期后，程序将自动爬取该时间段内的内容（由于裁判文书网的反爬虫升级了，此功能无法使用，能力有限，抱歉）

 

### 2.上传案例

![img](file:///C:/Users/hp/AppData/Local/Temp/msohtmlclip1/01/clip_image006.jpg)

通过点击“上传案例文件”按钮，将会弹出窗口选择文件，文本内容将会回显在文本框中。也可以直接在文本框中输入文本内容。

![图形用户界面, 应用程序  描述已自动生成](file:///C:/Users/hp/AppData/Local/Temp/msohtmlclip1/01/clip_image008.jpg)![img](file:///C:/Users/hp/AppData/Local/Temp/msohtmlclip1/01/clip_image010.jpg)

 

### 3.清空案例文字

通过点击“清空案例文字”按钮，清除框内内容

![背景图案  低可信度描述已自动生成](file:///C:/Users/hp/AppData/Local/Temp/msohtmlclip1/01/clip_image012.jpg)

 

### 4.批量处理

通过点击“批量处理”按钮，选择文件夹路径，将对文件夹中所有文件进行自动标注处理

 ![图形用户界面, 应用程序  描述已自动生成](file:///C:/Users/hp/AppData/Local/Temp/msohtmlclip1/01/clip_image014.jpg) ![图形用户界面, 文本, 应用程序  描述已自动生成](file:///C:/Users/hp/AppData/Local/Temp/msohtmlclip1/01/clip_image016.jpg)

 

 

 

 

### 5.分析案例

通过点击“分析案例”按钮，程序将对文本框中的内容进行分析，从而更改下方选项内容。用户可以检查并选择其中的选项，当不存在多个当事人时，部分选项将不可选择。

![文本  描述已自动生成](file:///C:/Users/hp/AppData/Local/Temp/msohtmlclip1/01/clip_image018.jpg)

 

### 6.保存案件与标注

通过点击“保存案件与标注”按钮，用户可以选择存储路径，程序将读取上方选项中被选中的内容，生成.json文件，并读取文本框中内容生成.txt文件一起存储于选择的存储路径中，文件名会以“当事人+案由+案“的形式。（演示视频中有明明格式错误，此问题已经修复）

![图形用户界面, 应用程序  描述已自动生成](file:///C:/Users/hp/AppData/Local/Temp/msohtmlclip1/01/clip_image020.jpg) ![图片包含 图形用户界面  描述已自动生成](file:///C:/Users/hp/AppData/Local/Temp/msohtmlclip1/01/clip_image022.jpg)

 

 

 

 

 

 

 

## 源码解析

### 项目入口：

![图形用户界面, 文本  描述已自动生成](file:///C:/Users/hp/AppData/Local/Temp/msohtmlclip1/01/clip_image024.jpg)

### 各功能函数：

```
def findcase(self):
    # 爬虫程序，start，end为date对象，对该时间内的案件进行爬取
def upload(self):
    # 上传文件至指定路径
def cleartext(self):
    # 清除文本框内容
def save(self):
    # 将案件文本和标注分别保存为.txt和json文件
def batchprocess(self):
    # 对指定文件夹中的内容进行批量处理
def analyse(self):
    # 对案件文本进行分析，更改tab页中的选项
# 分析并更改当事人
def change_party(self,choices):
def analyse_party(self,text):
    # 返回list 排序 大小为4
# 分析并更改当事人1性别
def change_gender1(self, choices):
def analyse_gender1(self, text):
    # 返回list，大小为1，比如list[0]=“男”
# 分析并更改当事人2性别
def change_gender2(self, choices):
def analyse_gender2(self, text):
    # 返回list，大小为1，比如list[0]=“男” 若无返回空list
# 分析并更改案由
def change_cause(self, choices):
# 分析并更改相关法院
def change_court(self, choices):
def analyse_court(self, text):
    # 返回list 排序 大小为4
```

 
