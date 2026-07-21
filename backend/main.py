from http.server import BaseHTTPRequestHandler, HTTPServer
import json

profile = {
    "heroTitle": "关于我",
    "heroSubtitle": "项目、创意、灵感、心得、我的作品",
}


class Handler(BaseHTTPRequestHandler):
    # 处理 GET 请求
    def do_GET(self):
        # 根据请求路径返回不同的响应
        if self.path == "/api/profile":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            body = json.dumps(profile, ensure_ascii=False)
            self.wfile.write(body.encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()


print("后端已启动：http://localhost:8000/api/profile")
HTTPServer(("", 8000), Handler).serve_forever()
