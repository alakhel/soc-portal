# Use the official PHP image with Apache
FROM php:7.4-apache

# Copy the contents of the Laravel project to the image
COPY . /var/www/html/

# Set the working directory to the root of the Laravel project
WORKDIR /var/www/html/

# Install dependencies for Laravel and the Vue frontend
RUN apt-get update && apt-get install -y \
    npm \
    libzip-dev \
    && docker-php-ext-install zip \
    && rm -rf /var/lib/apt/lists/*

# Install the necessary PHP extensions for Laravel
RUN docker-php-ext-install pdo_mysql

# Install the npm dependencies for the Vue frontend
WORKDIR /var/www/html/frontend-vue
RUN npm install

# Build the Vue frontend
RUN npm run build

# Set the working directory back to the root of the Laravel project
WORKDIR /var/www/html/

# Configure Apache document root to point to the Laravel public directory
RUN sed -i 's!/var/www/html!/var/www/html/public!g' /etc/apache2/sites-available/000-default.conf
