from pymongo import MongoClient
import uuid
from flask import request, Flask, make_response, abort, jsonify
from flask_cors import CORS
from datetime import datetime, timezone
import hashlib

# 设置 MongoDB 连接 URI
uri = "mongodb://localhost:27017/"
client = MongoClient(uri)  # 创建 MongoClient 实例

# 选择数据库和集合
database = client["database"]
users_collection = database["users"]  # 用户集合
articles_collection = database["articles"]  # 文章集合

app = Flask(__name__)  # 创建 Flask 应用实例
CORS(app)  # 允许跨源请求

# 错误代码字典，存储各种错误的描述信息
ErrorCode = {
    '10000': 'Success',
    '10011': '该账号已被注册',  # 账号已存在
    '10012': '该账号尚未注册',  # 账号不存在
    '10013': '密码错误',  # 密码验证失败
    '10014': '身份校验未通过',  # 身份验证失败
    '10021': '操作失败',  # 操作未成功
    '10022': '无权限'  # 权限不足
}



def encryptText(text):
    return hashlib.md5(text).hexdigest

# 密码不明文直接存储，选择生成一个 token 来验证身份
def generateToken(email, password):
    hash1 = encryptText(password)
    hash2 = encryptText(email+hash1)
    return hash2

# 检查用户名是否已存在
def checkIfUserNameExist(email):
    return bool(users_collection.find_one({"email": email}))  # 查找用户

# 用户注册功能
def user_register(email, password, permissions="guest"):
    if checkIfUserNameExist(email):
        return (False, 10011)  # 用户名已存在
    
    # 生成用户 ID （自增）
    userId = str(len(list(users_collection.find())) + 10001)
    token = generateToken(email, encryptText(password))  # 生成 token

    # 创建用户数据
    insert_data = {
        "_id": userId,
        "email": email,
        "password": encryptText(password),  # 存储加密后的密码
        "token": token,
        "permissions": permissions  # 用户权限
    }

    # 插入用户数据到数据库
    users_collection.insert_one(insert_data)
    return (True, userId, email, token)  # 返回成功信息

# 用户登录功能
def user_login(email, password):
    user = users_collection.find_one({"email": email})  # 查找用户是否存在

    if not user:
        return (False, 10012)  # 用户未注册

    # 验证密码
    if user["password"] == encryptText(password):
        return (True, user["_id"], user["email"], user["token"])  # 登录成功
    else:
        return (False, 10013)  # 密码错误

# 一个管理员账号
def superuser():
    if not checkIfUserNameExist("admin@example.com"):
        user_register("admin@example.com", "L@shdOH*sa#aqncsp", "admin")  # 创建 admin 用户
    return user_login("admin@example.com", "L@shdOH*sa#aqncsp")  # 返回 admin 登录信息

# 添加文章功能
def article_insert(title, content, author, category, create_time):
    article_id = uuid.uuid4().hex  # 生成唯一的文章 ID

    # 创建文章数据
    insert_data = {
        "_id": article_id,
        "title": title,
        "content": content,
        "author": author,
        "category": category,
        "create_time": create_time
    }

    # 将文章数据插入到数据库
    articles_collection.insert_one(insert_data)
    return (True, article_id)  # 返回成功信息

# 获取所有文章
def articles_get_all():
    articles = list(articles_collection.find())  # 从数据库中查找所有文章
    return articles  # 返回文章列表

# 根据文章 ID 获取特定文章
def article_get_by_id(article_id):
    article = articles_collection.find_one({"_id": article_id})  # 根据 ID 查找文章
    return article  # 返回文章信息

# 根据类别获取文章
def articles_get_by_category(category):
    articles = list(articles_collection.find({"category": category}))  # 根据类别查找文章
    return articles  # 返回文章列表

# 根据标题获取文章
def articles_get_by_title(title):
    articles = list(articles_collection.find({"title": title}))  # 根据标题查找文章
    return articles  # 返回文章列表

# 根据文章 ID 删除特定文章
def article_delete_by_id(article_id):
    result = articles_collection.delete_one({"_id": article_id})  # 删除文章
    return result.deleted_count == 1  # 返回删除结果

# 根据文章 ID 更新特定文章
def article_update_by_id(article_id, title, content, category):
    result = articles_collection.update_one({"_id": article_id}, {"$set": {"title": title, "content": content, "category": category}})
    return result.modified_count == 1  # 返回更新结果

# 获取用户权限
def get_permission(token):
    user = users_collection.find_one({"token": token})  # 根据 token 查找用户
    if not user:
        return (False, 10014)  # 身份校验未通过
    return (True, user["permissions"])  # 返回用户权限

# 用户注册接口
# 传入 data: { email: str, password: str[, permissions: str] } 
# 成功则返回 { userid: str, email: str, token: str }
@app.route('/register', methods=['POST'])
def register():
    data = request.form.to_dict()  # 获取请求的 JSON 数据
    if not data or 'email' not in data or 'password' not in data:
        return make_response({"error": "Missing email or password"}, 400)  # 请求数据缺失，返回 400

    result = user_register(data["email"], data["password"], data.get("permissions", "guest"))  # 注册用户

    if result[0]:
        return make_response({"user_id": result[1], "email": result[2], "token": result[3]}, 201)  # 注册成功，返回 201
    else:
        return make_response({"error": ErrorCode[str(result[1])]}, 400)  # 注册失败，返回 400

# 用户登录接口
# 传入 data: { email: str, password: str} 
# 成功则返回 { userid: str, email: str, token: str }
@app.route('/login', methods=['POST'])
def login():
    data = request.form.to_dict()  # 获取请求的 JSON 数据
    if not data or 'email' not in data or 'password' not in data:
        return make_response({"error": "Missing email or password"}, 400)  # 请求数据缺失，返回 400

    result = user_login(data["email"], data["password"])  # 登录用户

    if result[0]:
        return make_response({"user_id": result[1], "email": result[2], "token": result[3]}, 200)  # 登录成功，返回 200
    else:
        return make_response({"error": ErrorCode[str(result[1])]}, 401)  # 登录失败，返回 401

# 修改文章接口
# 传入 data: { id: str, title: str, content: str, category: str } 
# 成功则返回 { content: str }
@app.route('/update', methods=['POST'])
def update():
    token = request.cookies.get("token")  # 获取用户的 token
    permission = get_permission(token)  # 获取用户权限

    if not permission[0]:
        return make_response({"error": ErrorCode[str(permission[1])]}, 403)  # 身份校验未通过，返回 403

    if permission[1] == 'guest':
        return make_response({"error": ErrorCode['10022']}, 403)  # 权限不足，返回 403

    data = request.form.to_dict()  # 获取请求的 JSON 数据
    if not data or 'id' not in data or 'title' not in data or 'content' not in data or 'category' not in data:
        return make_response({"error": "Missing article data"}, 400)  # 请求数据缺失，返回 400

    result = article_update_by_id(data["id"], data["title"], data["content"], data["category"])  # 更新文章

    if result:
        return make_response(data["content"], 200)  # 更新成功，返回 200
    else:
        return make_response({"error": ErrorCode['10021']}, 400)  # 更新失败，返回 400

# 删除文章接口
# 传入 data: { id: str } 
# 成功则返回 { success }
@app.route('/delete', methods=['POST'])
def delete():
    token = request.cookies.get("token")  # 获取用户的 token
    permission = get_permission(token)  # 获取用户权限

    if not permission[0]:
        return make_response({"error": ErrorCode[str(permission[1])]}, 403)  # 身份校验未通过，返回 403

    if permission[1] != 'admin':
        return make_response({"error": ErrorCode['10022']}, 403)  # 权限不足，返回 403

    data = request.form.to_dict()  # 获取请求的 JSON 数据
    if not data or 'id' not in data:
        return make_response({"error": "Missing article ID"}, 400)  # 请求数据缺失，返回 400

    result = article_delete_by_id(data["id"])  # 删除文章

    if result:
        return make_response({"message": "success"}, 200)  # 删除成功，返回 200
    else:
        return make_response({"error": ErrorCode['10021']}, 400)  # 删除失败，返回 400

# 添加文章接口
# 传入 data: { title: str, content: str, author: str, category: str, create_time: str } 
# 成功则返回 { article_id: str }
@app.route('/insert', methods=['POST'])
def insert():
    token = request.cookies.get("token")  # 获取用户的 token
    permission = get_permission(token)  # 获取用户权限

    if not permission[0]:
        return make_response({"error": ErrorCode[str(permission[1])]}, 403)  # 身份校验未通过，返回 403

    if permission[1] != 'admin':
        return make_response({"error": ErrorCode['10022']}, 403)  # 权限不足，返回 403

    data = request.form.to_dict()  # 获取请求的 JSON 数据
    if not data or 'title' not in data or 'content' not in data or 'author' not in data or 'category' not in data or 'create_time' not in data:
        return make_response({"error": "Missing article data"}, 400)  # 请求数据缺失，返回 400

    result = article_insert(data["title"], data["content"], data["author"], data["category"], data["create_time"])  # 插入文章

    if result[0]:
        return make_response({"article_id": result[1]}, 201)  # 插入成功，返回 201
    else:
        return make_response({"error": ErrorCode['10021']}, 400)  # 插入失败，返回 400

# 获取所有文章接口 
# todo: 实现分页、清洗数据只留下 id 和标题，其他的不用返回
# 成功则返回 { articles }
@app.route('/get_all_articles', methods=['GET'])
def get_all_articles():
    articles = articles_get_all()  # 获取所有文章
    return make_response(articles, 200)  # 返回文章列表，状态码 200

# 根据 ID 获取文章接口
@app.route('/get_article_by_id', methods=['GET'])
def get_article_by_id():
    article_id = request.args.get("id")  # 从查询参数获取文章 ID
    if not article_id:
        return make_response({"error": "Missing article ID"}, 400)  # 请求数据缺失，返回 400

    article = article_get_by_id(article_id)  # 获取文章
    if article:
        return make_response(article, 200)  # 文章存在，返回 200
    else:
        return make_response({"error": "Article not found"}, 404)  # 文章不存在，返回 404

@app.route('/get_article_by_title', methods=['GET'])
def get_article_by_title():
    title = request.args.get("title")
    if not title:
        return make_response({"error": "Missing title"}, 400)
    
    article = articles_get_by_title(title)
    return make_response(article, 200)

# 根据类别获取文章接口
@app.route('/get_articles_by_category', methods=['GET'])
def get_articles_by_category():
    category = request.args.get("category")  # 从查询参数获取类别
    if not category:
        return make_response({"error": "Missing category"}, 400)  # 请求数据缺失，返回 400

    articles = articles_get_by_category(category)  # 获取该类别的文章
    return make_response(articles, 200)  # 返回文章列表，状态码 200

if __name__ == "__main__":
    app.run()

    
