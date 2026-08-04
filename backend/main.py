from fastapi import FastAPI

# BaseModel 是 Pydantic 提供的一个基类，用于定义数据模型和验证数据
from pydantic import BaseModel

# CORSMiddleware 是 FastAPI 提供的一个中间件，用于处理跨域请求
from fastapi.middleware.cors import CORSMiddleware

# 创建 FastAPI 应用实例
app = FastAPI()

# 添加 CORS 中间件，允许来自指定来源的请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 允许所有来源的请求
    allow_methods=["GET", "POST"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有请求头
)

# 定义一个简单的配置文件，包含关于我们的信息
profiles = {
    "heroTitle": "关于我",
    "heroSubtitle": "项目，创意，灵感，心得，我的作品",
    "featuredWork": {
        "kicker": "作品",
        "title": "文字实验室",
        "copy": "拼音和情绪，挖掘中文里的细节",
        "linkLabel": "打开作品",
    },
    "identity": {
        "motto": "已识乾坤大，尤怜草木青",
        "learning": "零到全栈",
    },
}


# 定义一个 Pydantic 模型，用于解析请求体中的数据
class AnalysisRequest(BaseModel):
    text: str


# 定义一个 POST 请求的路由，接收文本数据并返回分析结果
@app.post("/api/analyze")
def analyze(req: AnalysisRequest):
    # 这里可以添加对 req.text 的分析逻辑
    return {
        "text": req.text,
        "score": 0.5,
        "label": "偏平静",
        "pinyin": "（模块 6 再说）",
    }


# 定义一个 GET 请求的路由，返回配置文件中的信息
@app.get("/api/profile")
def get_profile():
    return profiles
