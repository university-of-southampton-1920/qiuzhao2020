# 残酷刷题

每天完成leetcode的一道题，每天截止是英国时间20：00。持续时间：2020/02/03 - 秋招结束

## 如何加入

微信号添加：hjyyizi。然后我会拉你进群

## T人规则 or 发红包规则

连续三天不打卡（从执行代码那一刻开始），T人&发红包。准确来说是第三天过20：00之后，仍然没有完成三天前的任何一道题。

举个例子：

```python
# 在24号晚上过了20：00后开始运行脚本
if 小黑22号没有刷 & 23号没有刷 & 24号20点过后仍然没有刷过22，23，24号的任何一道题：
	小黑被T or 发红包
else:
  小黑侥幸活过来
```

T人 || 发红包的脚本你可以在github仓库中：[https://github.com/university-of-southampton-1920/qiuzhao2020/blob/master/judge.py](https://github.com/university-of-southampton-1920/qiuzhao2020/blob/master/judge.py)。找到

**发红包规则**

红包金额 = 群里面的人数*2。红包的类型是普通红包，不能是拼手气红包。

每天20：00过后，服务器运行`judge.py`脚本，该脚本拉取github上的代码，并统计每个人的提交情况。

## 代码提交

完成题目的代码需要提交到leetcode的同时也需要提交到github仓库上，方便统计。

github仓库：[https://github.com/university-of-southampton-1920/qiuzhao2020](https://github.com/university-of-southampton-1920/qiuzhao2020)

**文件命名规范：leetcode id + leetcode题号。**

举个例子：

这是我leetcode的专属链接：[https://leetcode.com/biss/](https://leetcode.com/biss/)

假如我完成了题号为**1**的leetcode题目，名字叫Two Sum。

那么你当天提交的文件名是(biss是链接最后一个词，它是你leetcode的唯一id，1是题号)：

* biss_1.py(如果你是用python写的话，biss是我的leetcode id，1是这个题的题号)
* biss_1.cpp(如果你是用cpp写的话)
* ...

**如何提交到github上**

假如你电脑上没有该github仓库：

```shell
git clone https://github.com/JyiHUO/2020_qiuzhao.git
```

加入有github仓库了，你需要更新该仓库：

```shell
git pull
```

接着，找到当天日期的文件夹（假如是2020_01_27）：

```shell
cd qiuzhao2020/2020_01_27
```

将你的代码添加到该文件夹里面(使用ls命令来查看你的代码是否在该文件夹里面)：

```python
ls
biss-test_1.cpp biss_1.cpp
```

返回到父目录中，使用以下代码更新仓库，并推送到服务器：

```shell
git add -A
git commit -m "leetcode_id + 题号"
git push origin master
```

## 复活规则

被T之后7天完成7道题目，并且这7道题目没有出现在之前布置的题目中，并且题目的难度的平均值要在medium之上。比如说easy，medium，medium，medium，medium，hard，hard

## 群规

* 每天20：00过后在群里面布置明天的题号
* 不许私自删除被人提交的代码（在历史记录可以追查的喔）。发现必踢
* 可以补交之前没有完成的题目
* 群暂时限定20人

## 视频讲解

* [leetcode368(biss)](https://www.bilibili.com/video/av86351318/)
* [leetcode39(biss)](https://www.bilibili.com/video/av86616360/)
* [leetcode40(biss)](https://www.bilibili.com/video/av86817804)
* [leetcode77(biss)](https://www.bilibili.com/video/av87023917/)
* [leetcode1319(biss)](https://www.bilibili.com/video/av87240025/)
* [leetcode377(biss)](https://www.bilibili.com/video/av87240049/)
* [leetcode1286(biss)](https://www.bilibili.com/video/av87459206/)
* [leetcode1345(biss)](https://www.bilibili.com/video/av87699671/)
* [leetcode1267(biss)](https://www.bilibili.com/video/av88125905)
* [leetcode910(biss)](https://www.bilibili.com/video/av88125889)
* [leetcode959(biss)](https://www.bilibili.com/video/av88965869/)
* [leetcode765(biss)](https://www.bilibili.com/video/av89198166/)
* [leetcode130(biss)](https://www.bilibili.com/video/av89555280/)
* [leetcode128(biss)](https://www.bilibili.com/video/av89559140/)
* [leetcode947(biss)](https://www.bilibili.com/video/av89559185/)
* [leetcode552(biss)](https://www.bilibili.com/video/av97481634/)