# backend_fastapi
后端开发，使用python的fastapi



# 使用说明
* step1创建虚拟环境
  python -m venv venv
* step2激活虚拟环境
  source venv/bin/activate(或source venv/Scripts/activate)
* step3安装依赖
  pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
* step4启动服务
  python run.py

# 实用Tips
如果在运行过程中涉及任何对models的操作，或是在数据库发生变更，可能会出现循环报错。
* 解决办法：删除migrate文件夹下的models文件夹（不可以仅仅删除models文件夹中的文件）


  