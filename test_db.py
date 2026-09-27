from database import DatabaseClient

db = DatabaseClient()
if db.validate_connection():
    print("✅数据库连接成功")
else:
    print("❌数据库连接失败")
