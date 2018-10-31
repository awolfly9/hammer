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
python setup.py sdist
```
* 上传打包后的文件到 pypi
```
twine upload dist/* 
```
* 具体参考网址[uploading-your-project-to-pypi](https://packaging.python.org/tutorials/distributing-packages/#uploading-your-project-to-pypi)


## django_bulk 使用说明

bulk_create 在原生 django 的 bulk_create 基础上，将 INSERT INTO 改为 INSERT IGNORE INTO
使用方法同 django bulk_create

bulk_insert 基于 datas 动态添加字段，这样只需要一个 model 就能够插入所有类型的数据。
目前可能还不稳定
使用方法
将 hammer.django_bulk 加入到 INSTALLED_APPS 然后使用同 bulk_create