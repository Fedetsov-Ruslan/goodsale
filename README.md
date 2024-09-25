## Сервис по чтению данных из файла и анализу в elasticsearch 
 - создан docker-compose файл, в котором запускается и сам сервис, и elasticsearch и postgesql
 - Заполнены поля category_lvl_1, category_lvl_2, category_lvl_3, category_remaining 

## Запуск
 - Создаем файл .env и копируем в него переменные из .env.example выставляем параметры БД под свои

 - Для запуска в Docker-compose:
    - выполняем команду  "docker build -t script_sale ." для сборки контейнера скрипта
    - запускаем командой "docker-compose up --build" 
    - ждем пока все отработает

 - Для запуска на локальном компьютере:
    - Создаем БД с таблицой и заданными параметрами внесенными в .env
    - Устанавливаем зависимости из requiriments.txt
    - Меняем на DB_HOST=localhost и раскоментировать # ELASTIC_HOST=localhost и закоментировать ELASTIC_HOST=elasticsearch
    - запускаем docker-compose с elasticsearch (если такого отдельного файла нет, можно запусть мой docker-compose, закоментировав два других сервиса)
    - запускаем script.py


## результаты
| uuid                                   | similar_sku                                                                                                              |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| 1c7e1db7-997b-4701-a7bf-697e6110103d   | {ef89237f-e988-4306-8335-06cb01269bab,ee9a3976-9299-4d8f-bfd4-3207c5a194ac,e1d9de1e-67f7-4d17-9da1-086884e636ec,4182fc5e-435e-4656-b880-861f5bfea7c0,da366606-50ae-4a10-a45b-23a6cb736c6e} |

| 052abc93-87a4-4d52-b120-ec7a7f31e043   | {148e7edf-5ad2-4c9f-b54d-d371fc7ccd87,fd2c635e-1ea1-4677-9103-01f45600e2d6,3c7b427d-8712-4002-8bfe-87e0a6c22dc0,     33a98136-44b6-426f-89b2-ab6f8fef7579,81f6336f-7398-4143-b046-45d4269713a5} |
               |

| product_title                                                                     | similar_title                                                                               |
|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Смартфон Samsung Galaxy S22 8/128 ГБ, Dual: nano SIM + eSIM, Белый фантом         | Смартфон Samsung Galaxy S22 8/128 ГБ, Dual: nano SIM + eSIM, лавандовый                       |
| Смартфон Samsung Galaxy S22 8/128 ГБ, Dual: nano SIM + eSIM, Белый фантом         | Смартфон Samsung Galaxy S22 8/256 ГБ, Dual: nano SIM + eSIM, зеленый                         |
| Смартфон Samsung Galaxy S22 8/128 ГБ, Dual: nano SIM + eSIM, Белый фантом         | Смартфон Samsung Galaxy S22+ 8/256 ГБ, Dual: nano SIM + eSIM, черный фантом                   |
| Смартфон Samsung Galaxy S22 8/128 ГБ, Dual: nano SIM + eSIM, Белый фантом         | Смартфон Samsung Galaxy S22 Ultra 8/128 ГБ, Dual: nano SIM + eSIM, бургунди                  |
| Смартфон Samsung Galaxy S22 8/128 ГБ, Dual: nano SIM + eSIM, Белый фантом         | Смартфон Samsung Galaxy S22 8/128 ГБ, Dual: nano SIM + eSIM, розовый                         |
| Радиоприемник SVEN SRP-535 черный                                                  | Радиоприемник SVEN SRP-535 черный                                                           |
| Радиоприемник SVEN SRP-535 черный                                                  | Комплект 5 шт, Колонка портативная SONNEN B306, 12 Вт, Bluetooth, FM-тюнер, microSD, MP3-плеер, черная, 513479 |
| Радиоприемник SVEN SRP-535 черный                                                  | Беспроводные наушники Bluetooth со светящимися кошачьими ушами STN-28 черные                |
| Радиоприемник SVEN SRP-535 черный                                                  | Телефон DIGMA VOX FS240 RU, 2 SIM, серый                                                  |
| Радиоприемник SVEN SRP-535 черный                                                  | Смартфон Samsung Galaxy A32 6/128 ГБ, Dual nano SIM, синий                                 |
