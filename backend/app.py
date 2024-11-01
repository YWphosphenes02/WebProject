#pip install Flask-Login 处理用户登录
#pip install Flask pymongo markdown 处理 Markdown 文本、MongoDB 数据库、Flask 应用
#pip install Werkzeug 处理密码哈希


from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import markdown
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS




app = Flask(__name__)
CORS(app)  # 允许所有来源的跨域请求
app.secret_key = 'dev_secret_key' # 由于是比赛项目，所以这里的密钥是随便设置的，请不要在生产环境中使用此密钥
login_manager = LoginManager()
login_manager.init_app(app)

# 连接到 MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['wikiDB']
users_collection = db['users']  # 用户集合
collection = db['wikis']  # Wiki集合

# 用户类
class User(UserMixin):
    def __init__(self, id, admin=False):
        self.id = id
        self.admin = admin

@login_manager.user_loader
def load_user(user_id):
    user_data = users_collection.find_one({"_id": ObjectId(user_id)})
    if user_data:
        return User(user_id, user_data.get('admin', False))
    return None

# 注册路由
@app.route('/api/register', methods=['POST'])
def api_register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    if users_collection.find_one({"username": email}):
        return jsonify({"error": "Email already exists."}), 400
    
    hashed_password = generate_password_hash(password)
    users_collection.insert_one({"username": email, "password": hashed_password, "admin": False})
    return jsonify({"message": "Registration successful."}), 201


# 登录路由
@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    user_data = users_collection.find_one({"username": email})
    if user_data and check_password_hash(user_data['password'], password):
        user = User(str(user_data['_id']), user_data.get('admin', False))
        login_user(user)
        return jsonify({"message": "Login successful."}), 200
    return jsonify({"error": "Invalid credentials."}), 401

# 登出路由
@app.route('/api/logout', methods=['POST'])
@login_required
def api_logout():
    logout_user()
    return jsonify({"message": "Logout successful."}), 200


# 首页，渲染查询页面
@app.route('/')
def index():
    return render_template('index.html')

# 创建新的 Wiki 信息
def create_wiki(title, content):
    new_wiki = {
        "title": title,
        "content": content,
        "createdAt": datetime.now()
    }
    result = collection.insert_one(new_wiki)
    return str(result.inserted_id)

# 获取所有 Wiki 信息
def get_wikis():
    wikis = list(collection.find())
    for wiki in wikis:
        wiki['_id'] = str(wiki['_id'])
        wiki['content_html'] = markdown.markdown(wiki['content'])
    return wikis

# 根据 ID 获取 Wiki 信息
def get_wiki_by_id(wiki_id):
    wiki = collection.find_one({"_id": ObjectId(wiki_id)})
    if wiki:
        wiki['_id'] = str(wiki['_id'])
        wiki['content_html'] = markdown.markdown(wiki['content'])
        return wiki
    return None

# 更新 Wiki 信息
def update_wiki(wiki_id, title, content):
    result = collection.update_one(
        {"_id": ObjectId(wiki_id)},
        {"$set": {"title": title, "content": content, "updatedAt": datetime.now()}}
    )
    return result.modified_count > 0

# 删除 Wiki 信息
def delete_wiki(wiki_id):
    result = collection.delete_one({"_id": ObjectId(wiki_id)})
    return result.deleted_count > 0

# 根据关键词查询 Wiki
def search_wiki(keyword):
    keyword = keyword.strip()
    if not keyword:
        return []
    
    wikis = list(collection.find({
        "$or": [
            {"title": {"$regex": keyword, "$options": "i"}},
            {"content": {"$regex": keyword, "$options": "i"}}
        ]
    }))
    
    for wiki in wikis:
        wiki['_id'] = str(wiki['_id'])
        wiki['content_html'] = markdown.markdown(wiki['content'])
    return wikis

# API 路由
@app.route('/api/wiki', methods=['GET'])
def api_get_wikis():
    return jsonify(get_wikis()), 200

@app.route('/api/wiki/<id>', methods=['GET'])
def api_get_wiki(id):
    wiki = get_wiki_by_id(id)
    if wiki:
        return jsonify(wiki), 200
    return jsonify({"error": "Wiki not found"}), 404

@app.route('/api/wiki/search', methods=['GET'])
def api_search_wiki():
    keyword = request.args.get('keyword', '')
    results = search_wiki(keyword)
    return jsonify(results), 200

@app.route('/api/wiki', methods=['POST'])
@login_required
def api_create_wiki():
    if not current_user.admin:  # 仅允许管理员进行创建
        return jsonify({"error": "Unauthorized"}), 403
    title = request.json.get('title')
    content = request.json.get('content')
    new_id = create_wiki(title, content)
    return jsonify({"id": new_id}), 201

@app.route('/api/wiki/<id>', methods=['PUT'])
@login_required
def api_update_wiki(id):
    if not current_user.admin:  # 仅允许管理员进行更新
        return jsonify({"error": "Unauthorized"}), 403
    title = request.json.get('title')
    content = request.json.get('content')
    result = update_wiki(id, title, content)
    if result:
        return jsonify({"message": "Wiki updated"}), 200
    return jsonify({"error": "Wiki not found"}), 404

@app.route('/api/wiki/<id>', methods=['DELETE'])
@login_required
def api_delete_wiki(id):
    if not current_user.admin:  # 仅允许管理员进行删除
        return jsonify({"error": "Unauthorized"}), 403
    result = delete_wiki(id)
    if result:
        return jsonify({"message": "Wiki deleted"}), 200
    return jsonify({"error": "Wiki not found"}), 404

# 启动应用
if __name__ == "__main__":
    app.run(port=5000)


