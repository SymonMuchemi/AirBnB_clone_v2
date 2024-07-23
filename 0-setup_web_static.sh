#!/usr/bin/env bash
# Install Nginx if it is not already installed
if ! dpkg -l | grep -q nginx; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create a symbolic link
if sudo [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership of /data to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data

# Update Nginx configuration
sudo tee /etc/nginx/sites-available/default > /dev/null <<EOL
server {
    listen 80;
    server_name localhost;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html;
    }
}
EOL

# Restart Nginx
sudo service nginx restart
