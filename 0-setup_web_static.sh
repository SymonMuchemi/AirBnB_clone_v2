#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

# update packages
apt update -y

# install nginx if not installed
apt install nginx -v

# create data folder
mkdir -p /data/

# create web_static folder
mkdir -p /data/web_static/

# create releases folder
mkdir -p /data/web_static/releases

# create shared folder
mkdir -p /data/web_static/shared

# create test folder
mkdir -p /data/web_static/releases/test

# create fake file
echo "Web static dummy file" > /data/web_static/releases/test/index.html

# create symbolic link and delete it if it already exists
ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership of /data/ directory to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/web_static/
sudo chmod -R 755 /data/web_static/

printf %s "
server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /etc/nginx/html;
        index index.html index.htm;

        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
        error_page 404 /404.html;
        location /404 {
            root /usr/share/nginx/html;
            internal;
        }

        location /hbnb_static {
		alias /data/web_static/current/;
		autoindex on;
	}
}
" > /etc/nginx/sites-available/default

# restart nginx for changes to be applied
systemctl restart nginx.service
