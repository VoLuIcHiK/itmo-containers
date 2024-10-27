# Лаборатоная работа 1

## Проект – графический интерфейс для работы с LLM моделями 

### Запуск

Плохая версия
```bash 
docker build -t baaad -f docker_bad.dockerfile .
docker run -p 1337:1337 --name baaad -it --rm --gpus=all baaad
```

Хорошая версия
```bash 
docker build -t good -f docker_good.dockerfile .
docker run -p 1337:1337 --name good -it --rm --gpus=all good
```

