# Лаборатоная работа 1

## Проект – графический интерфейс для работы с LLM моделями 

### Плохие практики в "плохом" DockerFile:
#### 1. Использование последней версии образа huggingface/transformers-pytorch-gpu
**Плохая практика:** используется последняя версия (latest) образа huggingface/transformers-pytorch-gpu 
**Почему:** может привести к проблемам с совместимостью при установке определенных версий бибилиотек при последующем использовании.  
**Как исправлена:** использован фиксированный образ huggingface/transformers-pytorch-gpu  

#### 2. Происходит копирование всех файлов проекта
**Плохая практика:** копирование всех файлов благодаря команде ```COPY . /app```.  
**Почему:** увеличивается размер образа, а также возникает риск получения вредоносных файлов или файлов, которые пользователь не должен был увидеть.  
**Как исправлена:** указано что конкретно необходимо копировать - ```COPY app.py /app/app.py```.  

#### 3. В файлу requirements.txt отсутствуют версии бибилиотек
**Плохая практика:** в файле requirements.txt указаны только названия библиотек без версий.  
**Почему:** без указания версии библиотеки по умолчанию будет ставиться самая новая версия, поэтому возникает риск появления несовместимостей при установке бибилиотек.  
**Как исправлена:** указаны версии библиотек в requirements.txt.  

### Когда НЕ стоит использовать контейнеры

#### Монолитные архитектуры  
Монолитные системы, где все компоненты тесно связаны друг с другом, чаще всего лучше работают вне контейнерной среды. Разделение такой системы на отдельные микросервисы потребует много сил и времени, но выигрыш от использования контейнеров будет минимальным.    

#### Когда необходимо хранить данные  
Все файлы создаются внутри контейнера. Стоит заметить, что все данные, хранящиеся внутри контейнера, будут потеряны при его удалении. Поэтому если данных много и сам проект большой, то лучше отказаться от использования контейнеров.


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
