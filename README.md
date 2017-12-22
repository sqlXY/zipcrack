# ZipCrack
### zip暴力破解程序
用来练手的小程序，以前写过的很多脚本都没有被保存下来，非常遗憾。
支持多线程，默认为10线程。
支持Python2。

### 用法
> `-z` 传入一个zip文件
`-d` 传入一个字典
`-t` 设置线程数(默认为10)

### 示例
> python zipcrack.py -z E:/test.zip -d E:/dic.txt

或者
> python zipcrack.py -z E:/test.zip -d E:/dic.txt -t 50