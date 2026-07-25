from fastapi import FastAPI

# BaseModel 是 Pydantic 提供的一个基类，用于定义数据模型和验证数据
from pydantic import BaseModel

# 创建 FastAPI 应用实例
app = FastAPI()

# 定义一个简单的配置文件，包含关于我们的信息
profiles = {
    "heroTitle": "关于我们",
    "heroSubtitle": "项目、创意、灵感、心得、我们的作品",
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
