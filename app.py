import cherrypy
from cherrypy.lib.static import serve_file

class App:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def upload(self, file):
        filepath = r"C:\Users\Administrator\demos\admin\static" + f"\{file.filename}"
        with open(filepath, "wb") as f:
            f.write(file.file.read())
        
        return {
            "errno": 0,
            "data": {
            "url": f"http://127.0.0.1:9090/api/static/{file.filename}", 
            # 使用wangEditor5上传图片需要返回完整URL路径
            }
        }
    
    @cherrypy.expose
    def music(self):
        fp = open("./bgm.mp3", "rb")
        return fp.read()
    
    @cherrypy.expose
    def download(self):
        # path 需要是绝对路径
        path = r"C:\Users\Administrator\demos\admin\bgm.mp3"
        return serve_file(path, "audio/mpeg", "attachment")


cherrypy.config.update({"server.socket_port": 9091, "server.socket_host": "0.0.0.0"})

# conf = {
#     "/static": {
#     "tools.staticdir.on": True,
#     "tools.staticdir.dir": r"C:\Users\Administrator\demos\admin\static"
#     }
    
    
# }

cherrypy.quickstart(App(), "/api")