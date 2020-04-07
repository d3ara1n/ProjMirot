# ProjMirot
基于[mirai](https://github.com/mamoe/mirai)和[python-mirai](https://github.com/NatriumLab/python-mirai)的私有机器人.

## 部署(git)
```bash
git clone https://github.com/ac682/ProjMirot.git
cd ProjMirot
pip install -r requirements.txt
```

## 配置
运行前需要先在`config.py`同名文件夹创建一个`env.py`文件用于传入一些外部参数。
```python
# 机器人自己的qq
_SELF_QQ_ = 'QQ_ID_FOR_YOUR_BOT'
# 没啥用， 以后会修复
_MASTERS_QQ_LIST_ = [10001]
# mirai-api-http 插件提供的授权码
_MIRAI_AUTHKEY_ = 'MIRAI_API_HTTP_AUTH_KEY'
# mirai-api-http 对接口， 如果开启ws则需要在末尾加上'/ws'
_MIRAI_ENDPOINT_ = 'MIRAI_API_HTTP_URL'
```
## 运行(python3)
```bash
python index.py
```

## 二次开发
翻一翻源码就大概知道该怎么追加功能。

## 许可(MIT)
没有技术含量的东西只要不嫌弃, 随便怎么用.