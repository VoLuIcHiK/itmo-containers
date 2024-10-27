# Используем актуальную версию базового образа
FROM huggingface/transformers-pytorch-gpu:4.46.0


# устанавливаем только нужные файлы
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt

# Устанавливаем зависимости с указанием версии
RUN pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app

# Запускаем без root прав
USER nobody
CMD ["python3", "./app.py"]
WORKDIR /notebooks