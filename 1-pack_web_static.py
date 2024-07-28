"""generates a .tgz file form the contents of the
web_static folder"""
from fabric import Connection
from datetime import datetime


conn = Connection(
    host="symonmuchemi.tech",
    username="ubuntu"
)

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
filename = f"web_static_{timestamp}.tgz"

def do_pack():
    conn.run("mkdir -p versions/")
    compression = conn.run(f"tar -czvf {filename} web_static/*")
    move = conn.run(f"mv {filename} versions/")
    
    if compression.ok and move.ok:
        return f"versions/{filename}"
    
    return None
