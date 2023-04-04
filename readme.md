change api link
vim frontend-vue/src/services/index.js 
cd frontend-vue
npm run build
cd ..
cp .env.example .env
docker-compose up -d --build
