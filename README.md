# Campus-website-study-room
1、安装python3.7
window参考：https://www.cnblogs.com/telwanggs/p/10043142.html
2、安装mysql 5.7
window安装参考：https://www.cnblogs.com/7q4w1e/p/9989129.html
安装完成进入mysql，执行下面命令创建数据库并授权：
CREATE DATABASE zixishi DEFAULT CHARACTER SET utf8 collate utf8_general_ci;
CREATE USER 'zixishi '@'%' IDENTIFIED BY '123456';
GRANT ALL PRIVILEGES ON zixishi.* TO 'zixishi '@'%' WITH GRANT OPTION; 
ALTER USER 'zixishi '@'%' IDENTIFIED BY '123456' PASSWORD EXPIRE NEVER; 
ALTER USER 'zixishi '@'%' IDENTIFIED WITH mysql_native_password BY '123456';
FLUSH PRIVILEGES;
用cmd进入项目目录，登陆数据库，导入数据：
use zixishi
source zixishi.sql
3、安装python相关的包
打开cmd，进入项目目录，执行下面命令
pip  install -r  requirements.txt -i  https://pypi.tuna.tsinghua.edu.cn/simple
安装完成之后输入
pip list 






代码修改settings文件的数据库配置，修改成自己的数据库ip和端口，密码等等。

创建数据库：
CREATE DATABASE IF NOT EXISTS zixishi DEFAULT CHARSET utf8mb4;

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'zixishi',
        'USER': 'zixishi',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", 'charset': 'utf8', },
    }
}


运行项目:
打开navicat工具执行导入数据库文件zixishi.sql


启动文件
python manage.py runserver 127.0.0.1:8000

4、访问
浏览器打开：http://127.0.0.1:8000，可以注册用户
登陆管理用户：admin/123456
普通用户：张三/123456  李四/123456  陈五/123456
