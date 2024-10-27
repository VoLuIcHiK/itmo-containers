# Используем актуальную версию базового образа
FROM huggingface/transformers-pytorch-gpu

# Копируем все файлы
COPY . /app

# Устанавливаем зависимости с указанием версии
RUN pip install -U pip
RUN pip install --no-cache-dir -r /app/requirements_bad.txt

WORKDIR /app

# Запускаем 
CMD ["python3", "./app.py"]