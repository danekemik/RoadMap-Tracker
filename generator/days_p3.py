# -*- coding: utf-8 -*-
# ФАЗА 3: Инструменты (дни 79-100)

DAYS_P3 = [
    # ============ Блок 3.2: Docker ============
    {
        "id": 86, "phase": 2, "week": 18,
        "module": "Docker: основы",
        "title": "Docker: образы, контейнеры, Dockerfile",
        "goal": "Контейнеризировать приложение.",
        "points": [
            "docker run/ps/exec/logs",
            "Dockerfile: FROM, WORKDIR, COPY, RUN, CMD",
            ".dockerignore",
            "docker build, docker images"
        ],
        "resources": [
            {"type": "article", "title": "Habr: Docker для начинающих", "url": "https://habr.com/ru/search/?q=docker+для+начинающих+пособие", "lang": "ru"},
            {"type": "video", "title": "Docker с нуля (RU)", "url": "https://www.youtube.com/results?search_query=docker+с+нуля+русский+урок", "lang": "ru"}
        ],
        "tasks": [
            "Установите Docker",
            "Соберите Dockerfile для Python-приложения"
        ],
        "xp": 15
    },
    {
        "id": 87, "phase": 2, "week": 19,
        "module": "Docker: основы",
        "title": "Слои, кэш, размер образа",
        "goal": "Собирать оптимальные образы.",
        "points": [
            "Слои и кэширование сборки",
            "Порядок COPY/RUN влияет на кэш",
            "Минимизация размера: slim, alpine",
            "docker history, dive"
        ],
        "resources": [
            {"type": "article", "title": "Docker best practices (EN)", "url": "https://docs.docker.com/build/building/best-practices/", "lang": "en"},
            {"type": "article", "title": "Habr: уменьшение размера docker-образа", "url": "https://habr.com/ru/search/?q=уменьшение+размера+docker+образа+python", "lang": "ru"}
        ],
        "tasks": [
            "Соберите python:slim и посмотрите размер",
            "Оптимизируйте порядок инструкций"
        ],
        "xp": 10
    },
    {
        "id": 88, "phase": 2, "week": 19,
        "module": "Docker: compose",
        "title": "docker-compose: многоконтейнер",
        "goal": "Поднять app + БД + Redis одной командой.",
        "points": [
            "docker-compose.yml: services, ports, volumes",
            "Зависимости (depends_on), healthcheck",
            "env в compose",
            "Сети между контейнерами"
        ],
        "resources": [
            {"type": "article", "title": "Docker: Compose docs (RU)", "url": "https://docs.docker.com/get-started/compose/", "lang": "ru"},
            {"type": "article", "title": "Habr: docker-compose для разработки", "url": "https://habr.com/ru/search/?q=docker+compose+python+postgres", "lang": "ru"}
        ],
        "tasks": [
            "Соберите compose: app + postgres + redis",
            "Поднимите всё через docker compose up"
        ],
        "xp": 15
    },
    {
        "id": 89, "phase": 2, "week": 19,
        "module": "Docker: compose",
        "title": "Сети и volumes",
        "goal": "Управлять сетями и данными.",
        "points": [
            "Bridge/композ-сети, имена контейнеров",
            "Volumes: named vs bind",
            "Персистентность БД",
            "docker exec, docker logs"
        ],
        "resources": [
            {"type": "article", "title": "Docker: Volumes docs (EN)", "url": "https://docs.docker.com/engine/storage/volumes/", "lang": "en"},
            {"type": "article", "title": "Habr: volumes в docker", "url": "https://habr.com/ru/search/?q=docker+volumes+пособие", "lang": "ru"}
        ],
        "tasks": [
            "Сохраните данные Postgres в volume",
            "Подключитесь из app-контейнера по имени"
        ],
        "xp": 10
    },
    {
        "id": 90, "phase": 2, "week": 19,
        "module": "Docker: практика",
        "title": "Многоступенчатая сборка, запуск без root",
        "goal": "Безопасный продакшен-образ.",
        "points": [
            "Multi-stage: builder → runtime",
            "Не запускать от root (USER app)",
            "python:3.12-slim",
            "Миграции при старте"
        ],
        "resources": [
            {"type": "article", "title": "Docker best practices (EN)", "url": "https://docs.docker.com/build/building/best-practices/", "lang": "en"},
            {"type": "article", "title": "Habr: python в docker правильно", "url": "https://habr.com/ru/search/?q=docker+python+многоступенчатая+сборка", "lang": "ru"}
        ],
        "tasks": [
            "Соберите multi-stage образ",
            "Запустите контейнер от непривилегированного пользователя"
        ],
        "xp": 15
    },
    {
        "id": 91, "phase": 2, "week": 20,
        "module": "Docker: практика",
        "title": "Деплой проекта в Docker",
        "goal": "Собрать прод-контейнер и поднять весь стек одной командой.",
        "points": [
            "Прод-Dockerfile для учебного API",
            "compose для прода (app + nginx)",
            "Проверка одной командой",
            "Практика на учебном коде"
        ],
        "resources": [
            {"type": "article", "title": "Docker best practices (EN)", "url": "https://docs.docker.com/build/building/best-practices/", "lang": "en"}
        ],
        "tasks": [
            "Соберите прод-Dockerfile для учебного API",
            "Проверьте запуск всего стека одной командой"
        ],
        "xp": 20
    },
    # ============ Блок 3.3: Безопасность ============
    {
        "id": 92, "phase": 2, "week": 20,
        "module": "Безопасность: веб",
        "title": "OWASP Top 10 для API",
        "goal": "Знать главные уязвимости веба.",
        "points": [
            "Top 10: инъекции, ломаная аутентификация, XSS, IDOR, SSRF...",
            "Распознавать в своём коде",
            "Практические примеры",
            "Как защищаться"
        ],
        "resources": [
            {"type": "article", "title": "OWASP Top 10 (RU)", "url": "https://owasp.org/www-project-top-ten/", "lang": "en"},
            {"type": "video", "title": "OWASP Top 10 разбор (RU)", "url": "https://www.youtube.com/results?search_query=owasp+top+10+русский+разбор", "lang": "ru"}
        ],
        "tasks": [
            "Изучите список и отметьте 3 уязвимости в своём коде",
            "Исправьте хотя бы одну"
        ],
        "xp": 15
    },
    {
        "id": 93, "phase": 2, "week": 20,
        "module": "Безопасность: веб",
        "title": "XSS, CSRF, CORS на практике",
        "goal": "Защитить приложение от атак через браузер.",
        "points": [
            "XSS: хранимый/отражённый, экранирование",
            "CSRF: как работает и защиты",
            "CORS vs CSRF",
            "Заголовки: CSP, X-Frame-Options"
        ],
        "resources": [
            {"type": "article", "title": "Habr: XSS для начинающих", "url": "https://habr.com/ru/search/?q=XSS+атака+объяснение", "lang": "ru"},
            {"type": "article", "title": "Habr: CSRF атаки", "url": "https://habr.com/ru/search/?q=CSRF+атака+защита", "lang": "ru"}
        ],
        "tasks": [
            "Проверьте, экранируется ли вывод пользовательского контента",
            "Добавьте CSP-заголовки"
        ],
        "xp": 10
    },
    {
        "id": 94, "phase": 2, "week": 20,
        "module": "Безопасность: данные",
        "title": "Шифрование, секреты, .env",
        "goal": "Защитить данные и секреты.",
        "points": [
            "Симметричное/асимметричное шифрование (обзор)",
            "Хранение секретов: env, secret manager",
            "Никогда не коммитить ключи",
            ".gitignore для .env"
        ],
        "resources": [
            {"type": "article", "title": "Habr: шифрование простыми словами", "url": "https://habr.com/ru/search/?q=шифрование+простыми+словами", "lang": "ru"},
            {"type": "article", "title": "OWASP: secrets management (EN)", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html", "lang": "en"}
        ],
        "tasks": [
            "Проверьте git-историю на утечки секретов",
            "Вынесите все ключи в .env + .gitignore"
        ],
        "xp": 10
    },
    {
        "id": 95, "phase": 2, "week": 21,
        "module": "Безопасность: аудит",
        "title": "Аудит проекта: чек-лист",
        "goal": "Применить знания безопасности к учебному API.",
        "points": [
            "Чек-лист: пароли, JWT, права, инъекции, секреты",
            "Зависимости: pip-audit / dependabot",
            "Логирование подозрительных событий",
            "Исправление найденного"
        ],
        "resources": [
            {"type": "article", "title": "pip-audit: документация (EN)", "url": "https://pypi.org/project/pip-audit/", "lang": "en"},
            {"type": "article", "title": "Habr: аудит безопасности Python-приложения", "url": "https://habr.com/ru/search/?q=аудит+безопасности+python+приложения", "lang": "ru"}
        ],
        "tasks": [
            "Пройдите чек-лист аудита по учебному API",
            "Запустите pip-audit и исправьте критичные уязвимости"
        ],
        "xp": 15
    },
    # ============ Блок 3.4: Очереди и фоновые задачи ============
    {
        "id": 96, "phase": 2, "week": 21,
        "module": "Очереди: Celery",
        "title": "Celery: воркеры, задачи, брокер",
        "goal": "Уметь выносить тяжёлое в фон.",
        "points": [
            "Зачем очередь: тяжёлые задачи",
            "Celery + брокер (Redis/RabbitMQ)",
            "@app.task, .delay(), воркер",
            "Результаты задач"
        ],
        "resources": [
            {"type": "article", "title": "Celery: First Steps (EN)", "url": "https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html", "lang": "en"},
            {"type": "video", "title": "Celery для начинающих (RU)", "url": "https://www.youtube.com/results?search_query=celery+python+русский+урок", "lang": "ru"}
        ],
        "tasks": [
            "Настройте Celery с Redis",
            "Перенесите тяжёлую задачу в фоновый воркер"
        ],
        "xp": 15
    },
    {
        "id": 97, "phase": 2, "week": 21,
        "module": "Очереди: Celery",
        "title": "Periodic tasks, retry, FastAPI+Celery",
        "goal": "Расписания и надёжность задач.",
        "points": [
            "celery beat: расписание",
            "autoretry, max_retries",
            "Приоритеты и backoff",
            "Связка FastAPI + Celery"
        ],
        "resources": [
            {"type": "article", "title": "Celery: Beat docs (EN)", "url": "https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html", "lang": "en"},
            {"type": "article", "title": "Habr: celery beat расписание", "url": "https://habr.com/ru/search/?q=celery+beat+периодические+задачи", "lang": "ru"}
        ],
        "tasks": [
            "Настройте периодическую задачу (например, напоминание)",
            "Добавьте retry с экспоненциальным backoff"
        ],
        "xp": 15
    },
    {
        "id": 98, "phase": 2, "week": 21,
        "module": "Очереди: RabbitMQ",
        "title": "RabbitMQ: обзор, модели очередей",
        "goal": "Понять альтернативу Redis и плюсы брокеров.",
        "points": [
            "Что такое брокер сообщений",
            "Exchanges, queues, routing keys",
            "Паттерны: work queues, pub/sub, RPC",
            "Redis vs RabbitMQ: когда что"
        ],
        "resources": [
            {"type": "article", "title": "RabbitMQ: Tutorials (EN)", "url": "https://www.rabbitmq.com/tutorials", "lang": "en"},
            {"type": "video", "title": "RabbitMQ за 20 минут (RU)", "url": "https://www.youtube.com/results?search_query=rabbitmq+русский+обзор", "lang": "ru"}
        ],
        "tasks": [
            "Разберите модель exchange/queue",
            "Сравните Redis и RabbitMQ в конспекте"
        ],
        "xp": 10
    },
    {
        "id": 99, "phase": 2, "week": 22,
        "module": "Очереди: практика",
        "title": "Мини-проект 9: фоновая обработка",
        "goal": "Применить очередь в реальном сценарии.",
        "points": [
            "Выберите задачу: письма / генерация отчёта / резюме файлов",
            "Эндпоинт + задача + статус",
            "Статус задачи через Redis",
            "Оформление и README"
        ],
        "resources": [
            {"type": "article", "title": "FastAPI + Celery: туториал (RU)", "url": "https://habr.com/ru/search/?q=fastapi+celery+фоновые+задачи", "lang": "ru"}
        ],
        "projectOptions": [
            {"title": "Генератор PDF-отчётов", "desc": "POST → задача → готовый PDF со статусом; скачивание", "skills": "FastAPI, Celery, Redis", "complexity": "средне"},
            {"title": "Рассылка email-уведомлений", "desc": "Регистрация → фоновое письмо; очередь + retry", "skills": "FastAPI, Celery, SMTP", "complexity": "средне"},
            {"title": "Уменьшение/упаковка картинок", "desc": "Загрузка → фоновый ресайз и zip-архив; статус", "skills": "FastAPI, Celery, Pillow", "complexity": "средне"},
            {"title": "Парсер с фоновым сбором", "desc": "Эндпоинт запускает парсинг в фоне, результат в Redis", "skills": "FastAPI, Celery, httpx", "complexity": "средне"}
        ],
        "tasks": [
            "Выберите проект, реализуйте очередь",
            "Сделайте отображение статуса задачи"
        ],
        "xp": 25,
        "achievement": "Фоновые процессы"
    },
    {
        "id": 100, "phase": 2, "week": 22,
        "module": "Повторение",
        "title": "Чек-лист перед дипломом",
        "goal": "Закрепить инструменты и подготовиться к финалу.",
        "points": [
            "Тесты: покрытие проекта 60%+",
            "Docker: compose поднимается одной командой",
            "Безопасность: чек-лист пройден",
            "Очереди: хотя бы одна задача в фоне"
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: Testing (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/testing/", "lang": "ru"}
        ],
        "tasks": [
            "Пройдите все 4 пункта по своему Task Manager",
            "Запишите, что осталось доделать в дипломе"
        ],
        "xp": 15
    },
]