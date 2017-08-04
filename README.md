# 造的锤子工具

### sqlhelper
* 支持多线程
* 连接池
* 友好的插入数据接口
* 友好的查询数据接口

### kill_port
* 清理端口占用

## TODO
* 造更多的锤子



## 上传到 pypi 步骤
* 更改代码
* 输入命令打包
```
python setup.py sdict
```
* 上传打包后的文件到 pypi
```
twine upload dist/* 
```
* 具体参考网址[uploading-your-project-to-pypi](https://packaging.python.org/tutorials/distributing-packages/#uploading-your-project-to-pypi)
