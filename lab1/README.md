# Лаборатоная работа 1

## Проект – графический интерфейс для работы с LLM моделями 

### Запуск

Плохая версия
```bash 
docker build -t baaad -f docker_bad.dockerfile .
docker run -p 1337:1337 --name baaad -it --rm --gpus=all -v models_cache:/app/models_cache baaad
```

Хорошая версия
```bash 
docker build -t good -f docker_good.dockerfile .
docker run -it --rm --gpus=all -p 1337:1337 --name good -v models_cache:/app/models_cache good
```

