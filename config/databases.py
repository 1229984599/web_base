# 数据库管理
# 是否忽略sql语句错误 （错误后继续执行代码）
IGNORE_SQL_FALSE = False
USER = 'root'   # 用户名
PASSWORD = 'admin'  # 密码
HOST = 'localhost'  # 主机地址
PORT = '3306'       # 端口号
DATABASE = 'fisher_book'    # 数据库名称
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
