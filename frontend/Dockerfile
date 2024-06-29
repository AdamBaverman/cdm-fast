# Используем Node.js в качестве базового образа
FROM node:14

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем весь проект
COPY . .

# Открываем порт, на котором будет работать наше приложение
EXPOSE 3000

# Команда для запуска приложения
CMD ["npm", "start"]
