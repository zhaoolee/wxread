# wxread
微信读书刷时长


- 微信读书有一个鼓励机制, 一周阅读5小时可兑换10书币，每周日晚清空一周的总读书时长，没兑换的时长不计入下一周(1书币 == 1块钱)
- 作为一个经常加班的程序猿, 一周刷5个小时, 有点困难, 所以只好请一些自动化测试工具来帮忙(刷时长真是一个古老而有效的技能), 花了一天的时间,终于完成了~
## 最终效果
> ![](https://upload-images.jianshu.io/upload_images/3203841-acc68cc85a404bb8.gif?imageMogr2/auto-orient/strip)
> ![](https://upload-images.jianshu.io/upload_images/3203841-493c8c03e260c906.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> ![](https://upload-images.jianshu.io/upload_images/3203841-77a37d77be0fde06.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 第一步: 安装网易mumu, 通过应用中心安装微信读书
- 网页mumu下载地址: http://mumu.163.com/
>  ![](https://upload-images.jianshu.io/upload_images/3203841-06caef43a99b43b1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
-  在网易mumu模拟器内安装微信读书
> ![](https://upload-images.jianshu.io/upload_images/3203841-726604661574a2f3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 第二步:下载安装python环境
> 下载地址: https://www.python.org/downloads/
> ![](https://upload-images.jianshu.io/upload_images/3203841-c0034f0f89408263.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 通过python自带的pip安装依赖包`uiautomator`
```
pip install uiautomator
```
## 第三步: 获取adb, 将adb连接到mumu所在的`127.0.0.1:7555`
> - adb相当于mumu的驱动, 我找到了一个无需安装的版本, 解压即用,adb压缩包里的文件如下图(文末提供了下载的链接)
> ![](https://upload-images.jianshu.io/upload_images/3203841-c14eddb53272c2ee.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> - 测试: 启动mumu, 右键cmd.exe, 以管理员身份启动, 在终端内输入`adb connect 127.0.0.1:7555`, adb即可成功连接到mumu(注意: 这里一定要先启动mumu, 再输入`adb connect 127.0.0.1:7555`,否则adb无法连接成功)
> ![](https://upload-images.jianshu.io/upload_images/3203841-de547d14d092b68b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 第四步: 启动脚本, 刷时长
- 为了方便, 我把脚本`wx_read_auto.py`放到了adb的目录下
> ![](https://upload-images.jianshu.io/upload_images/3203841-8a7bbbbb6edbaa67.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 打开mumu内的微信读书的某一页, 启动脚本
> ![](https://upload-images.jianshu.io/upload_images/3203841-acb1d32977afd824.gif?imageMogr2/auto-orient/strip)

