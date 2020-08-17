#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

content="<html> <head> </head> <body> Holberton School </body> </html>"

location=" location \/hbnb_static/ { alias /data/web_static/current/; }"

if ! which nginx > /dev/null 2>&1; then
    apt update && sudo apt-get install -y nginx
fi

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "$content" > /data/web_static/releases/test/index.html
mkdir -p /data/web_static/current
ln -sfn /data/web_static/current /data/web_static/releases/test/
chown -R ubuntu:ubuntu /data

sed -i "55 i\ $location" /etc/nginx/sites-available/default
# restart nginx
service nginx restart > /dev/null 2>&1
