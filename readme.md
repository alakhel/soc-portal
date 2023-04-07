## Update your server:
```
sudo apt-get update
sudo apt-get upgrade
```

## Install Nginx:
```
sudo apt-get install nginx
```

## Install MySQL:
```
sudo apt-get install mysql-server
```

## Secure your MySQL installation (follow the prompts):
```
sudo mysql_secure_installation
```

## Install PHP and required PHP extensions:
```
sudo apt-get install php8.1 php8.1-fpm php8.1-mysql php8.1-zip
```

## If the step upthere didn't work, execute these following commands:
```
sudo apt update && sudo apt install -y software-properties-common 
sudo add-apt-repository ppa:ondrej/php 
sudo apt update
```

## Install Node.js and npm (install curl if not installed) :
```
curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt-get install -y nodejs
```

## Clone or copy your Laravel project to the server (install git if not installed):
```
# If using Git, for example:
sudo git clone https://github.com/alakhel/soc-portal /var/www/html/soc-portal
```

## Configure Nginx:
```
sudo cp /var/www/html/soc-portal/laravel-backend.conf /etc/nginx/sites-available/laravel-backend
sudo cp /var/www/html/soc-portal/vue-frontend.conf /etc/nginx/sites-available/vue-frontend
```

### Create a symbolic link to the sites-enabled directory:
```
sudo ln -s /etc/nginx/sites-available/laravel-backend /etc/nginx/sites-enabled/laravel-backend
sudo ln -s /etc/nginx/sites-available/vue-frontend /etc/nginx/sites-enabled/vue-frontend
sudo rm /etc/nginx/sites-enabled/default
```
### Copy frontend et renomer Backend
```
sudo cp -r /var/www/html/soc-portal /var/www/html/laravel-backend
sudo cp -r /var/www/html/soc-portal/frontend-vue /var/www/html/frontend-vue
```
### Test the Nginx configuration:
```
sudo nginx -t
```

### Reload Nginx:
```
sudo systemctl reload nginx
```

## Configure MySQL:
### Log in to MySQL:
```
sudo mysql -u root -p
```

Create a database and user for your Laravel project:
```
CREATE DATABASE soc;
CREATE USER 'laravel'@'localhost' IDENTIFIED BY 'P@ssw0rd';
GRANT ALL PRIVILEGES ON soc.* TO 'laravel'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

## Configure your Laravel project:
Copy .env.example to .env and update the necessary values (e.g., database credentials).
```
cd /var/www/html/laravel-backend
cp .env.example .env
```

## Install the Composer dependencies:
```
composer install
```

### Generate an application key:
```
php artisan key:generate
```

### Run any necessary migrations:
```
php artisan migrate
```
## Install npm dependencies for the Vue frontend:
```
cd /var/www/html/frontend-vue
npm install
```

### Build the Vue frontend:
```
sudo sed -i "s|baseURL: 'http://127.0.0.1:8000/api'|// baseURL: 'http://127.0.0.1:8000/api'|" /var/www/html/frontend-vue/src/services/index.js
sudo sed -i "s|// baseURL: 'http://64.226.68.181/api'|baseURL: 'http://64.226.68.181/api'|" /var/www/html/frontend-vue/src/services/index.js

npm run build
```

### Update permissions for the storage directory:
```
sudo chown -R www-data:www-data /var/www/html/laravel-backend/storage
sudo chmod -R 755 /var/www/html/laravel-backend/storage
```

## Restart Nginx and PHP-FPM:
```
sudo systemctl restart nginx
sudo systemctl restart php8.1-fpm
```
