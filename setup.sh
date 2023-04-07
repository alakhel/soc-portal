#!/bin/bash

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install nginx
sudo apt-get install mysql-server
#sudo mysql_secure_installation
sudo apt update && sudo apt install -y software-properties-common 
sudo add-apt-repository ppa:ondrej/php 
sudo apt update
sudo apt-get install php8.1 php8.1-fpm php8.1-mysql php8.1-zip
sudo apt install curl
curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo apt install git
sudo apt install npm
sudo git clone https://github.com/alakhel/soc-portal /var/www/html/soc-portal
sudo cp /var/www/html/soc-portal/laravel-backend.conf /etc/nginx/sites-available/laravel-backend
sudo cp /var/www/html/soc-portal/vue-frontend.conf /etc/nginx/sites-available/vue-frontend
sudo ln -s /etc/nginx/sites-available/laravel-backend /etc/nginx/sites-enabled/laravel-backend
sudo ln -s /etc/nginx/sites-available/vue-frontend /etc/nginx/sites-enabled/vue-frontend
sudo cp -r /var/www/html/soc-portal /var/www/html/laravel-backend
sudo cp -r /var/www/html/soc-portal/frontend-vue /var/www/html/frontend-vue
cd /var/www/html/laravel-backend
cp .env.example .env
composer install
php artisan key:generate
php artisan migrate
cd /var/www/html/frontend-vue
sudo npm install
sudo sed -i "s|baseURL: 'http://127.0.0.1:8000/api'|// baseURL: 'http://127.0.0.1:8000/api'|" /var/www/html/frontend-vue/src/services/index.js
sudo sed -i "s|// baseURL: 'http://64.226.68.181/api'|baseURL: 'http://64.226.68.181/api'|" /var/www/html/frontend-vue/src/services/index.js
sudo npm run build
sudo chown -R www-data:www-data /var/www/html/laravel-backend/storage
sudo chmod -R 755 /var/www/html/laravel-backend/storage
sudo nginx -t
sudo systemctl restart nginx