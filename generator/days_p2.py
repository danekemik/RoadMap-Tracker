# -*- coding: utf-8 -*-
# ФАЗА 2: FastAPI (дни 50-78)

DAYS_P2 = [
    # ============ Блок 2.0: API-дизайн ============
    {
        "id": 50, "phase": 2, "week": 10,
        "module": "API-дизайн: основы",
        "title": "REST, ресурсы, статусы, версионирование",
        "goal": "Проектировать чистое API до написания кода — это отличает хорошего backend-разработчика.",
        "points": [
            "Ресурсы и коллекции: /users, /users/{id}",
            "HTTP-методы и их смысл: GET/POST/PUT/PATCH/DELETE",
            "Правильные статус-коды: 2xx, 4xx, 5xx",
            "Версионирование: /api/v1, заголовки",
            "Плюрализация и именование эндпоинтов"
        ],
        "resources": [
            {"type": "article", "title": "Microsoft REST API guidelines (EN)", "url": "https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design", "lang": "en"},
            {"type": "video", "title": "Проектирование REST API (RU)", "url": "https://www.youtube.com/results?search_query=проектирование+rest+api+с+нуля+русский", "lang": "ru"}
        ],
        "tasks": [
            "Спроектируйте API для блога: список ресурсов, методов и статусов",
            "Обоснуйте выбор методов и кодов ответов"
        ],
        "xp": 10
    },
    {
        "id": 51, "phase": 2, "week": 10,
        "module": "API-дизайн: основы",
        "title": "OpenAPI/Swagger и документация",
        "goal": "Грамотно описывать контракты API, чтобы с ними могли работать фронт и коллеги.",
        "points": [
            "OpenAPI 3: схема, paths, components",
            "Автодокументация FastAPI: /docs, /redoc, openapi.json",
            "Описание схем ответов и ошибок",
            "Стандартная структура ошибки: {detail, code}",
            "Пагинация и фильтры в API"
        ],
        "resources": [
            {"type": "article", "title": "OpenAPI Specification (EN)", "url": "https://swagger.io/specification/", "lang": "en"},
            {"type": "article", "title": "FastAPI: дополнительные возможности (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/extra-models/", "lang": "ru"}
        ],
        "tasks": [
            "Опишите схему ответа и ошибки для POST /users",
            "Настройте теги и описание в /docs"
        ],
        "xp": 10
    },
    # ============ Блок 2.1: Ядро FastAPI ============
    {
        "id": 50, "phase": 2, "week": 10,
        "module": "FastAPI: старт",
        "title": "FastAPI: ASGI, uvicorn, /docs",
        "goal": "Развернуть FastAPI и увидеть автодокументацию.",
        "points": [
            "Установка fastapi + uvicorn",
            "Первый endpoint: @app.get, @app.post",
            "ASGI vs WSGI — почему FastAPI быстрый",
            "Автодокументация /docs (Swagger) и /redoc"
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: официальный туториал (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/", "lang": "ru"},
            {"type": "video", "title": "FastAPI с нуля на русском", "url": "https://www.youtube.com/results?search_query=fastapi+с+нуля+русский+урок", "lang": "ru"}
        ],
        "tasks": [
            "Создайте приложение с GET /health и POST /echo",
            "Откройте /docs и потренируйтесь"
        ],
        "xp": 10
    },
    {
        "id": 51, "phase": 2, "week": 10,
        "module": "FastAPI: параметры",
        "title": "Path, Query, Body параметры",
        "goal": "Освоить все способы передачи данных.",
        "points": [
            "Path: /users/{user_id} с валидацией",
            "Query: ?page=2&limit=10, дефолты, Enum",
            "Body: Pydantic-модель",
            "Приоритет параметров в FastAPI"
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: Path Parameters (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/path-params/", "lang": "ru"},
            {"type": "article", "title": "FastAPI: Query Parameters (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/query-params/", "lang": "ru"}
        ],
        "tasks": [
            "Создайте endpoint с path, query и body параметрами",
            "Добавьте Enum и ограничения (gt, le)"
        ],
        "xp": 10
    },
    {
        "id": 52, "phase": 2, "week": 10,
        "module": "FastAPI: Pydantic",
        "title": "Pydantic v2, response_model",
        "goal": "Строгие схемы запросов и ответов.",
        "points": [
            "BaseModel, Field(min_length, gt, pattern)",
            "Вложенные модели и списки",
            "@field_validator, @model_validator",
            "response_model: сериализация, скрытие пароля"
        ],
        "resources": [
            {"type": "article", "title": "Pydantic v2: поля и валидаторы", "url": "https://docs.pydantic.dev/latest/concepts/fields/", "lang": "en"},
            {"type": "article", "title": "FastAPI: response_model (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/response-model/", "lang": "ru"}
        ],
        "tasks": [
            "Опишите UserCreate (name, email, password) с валидацией",
            "Сделайте response_model без пароля"
        ],
        "xp": 15
    },
    {
        "id": 53, "phase": 2, "week": 11,
        "module": "FastAPI: структура",
        "title": "Depends и структура проекта",
        "goal": "Организовать проект и внедрять зависимости.",
        "points": [
            "APIRouter: prefix, tags",
            "Depends: инъекция зависимостей",
            "Зависимости с параметрами",
            "Структура: app/main.py, routers/, schemas/, core/"
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: Dependencies (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/dependencies/", "lang": "ru"},
            {"type": "article", "title": "FastAPI: структура больших приложений (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/bigger-applications/", "lang": "ru"}
        ],
        "tasks": [
            "Реструктурируйте проект: роутеры + общая зависимость",
            "Напишите зависимость get_db-заглушку"
        ],
        "xp": 15
    },
    {
        "id": 54, "phase": 2, "week": 11,
        "module": "FastAPI: БД",
        "title": "Интеграция SQLAlchemy + FastAPI",
        "goal": "Подключить БД к FastAPI.",
        "points": [
            "engine, sessionmaker, get_db",
            "CRUD эндпоинты поверх ORM",
            "Транзакции и rollback",
            "Создание таблиц vs Alembic"
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: SQL Databases (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/sql-databases/", "lang": "ru"},
            {"type": "article", "title": "SQLAlchemy: работа с сессиями", "url": "https://docs.sqlalchemy.org/en/20/orm/session_basics.html", "lang": "en"}
        ],
        "tasks": [
            "Соберите CRUD для модели User через SQLAlchemy",
            "Настройте get_db с закрытием сессии"
        ],
        "xp": 20
    },
    {
        "id": 55, "phase": 2, "week": 11,
        "module": "FastAPI: БД",
        "title": "Отношения и пагинация",
        "goal": "Возвращать связанные данные и пагинировать.",
        "points": [
            "Связи User→Post, сериализация",
            "Пагинация: limit/offset и cursor-based",
            "Фильтрация и сортировка",
            "Ответы с метаданными (total, page)"
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: Pydantic + SQLAlchemy отношения", "url": "https://fastapi.tiangolo.com/ru/tutorial/sql-databases/", "lang": "ru"},
            {"type": "article", "title": "Habr: пагинация в REST API", "url": "https://habr.com/ru/search/?q=пагинация+REST+API", "lang": "ru"}
        ],
        "tasks": [
            "Добавьте связь User→Post, endpoint /users/{id}/posts",
            "Реализуйте limit/offset пагинацию с total"
        ],
        "xp": 15
    },
    {
        "id": 56, "phase": 2, "week": 11,
        "module": "FastAPI: ошибки",
        "title": "Обработка ошибок, HTTPException",
        "goal": "Возвращать корректные ошибки API.",
        "points": [
            "HTTPException с деталями",
            "Кастомные exception handlers (404, 500, validation)",
            "Единый формат ошибок (code, message)",
            "Логирование при пробросе"
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: Handling Errors (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/handling-errors/", "lang": "ru"},
            {"type": "article", "title": "Google API: дизайн ошибок (RU-перевод есть в статьях Habr)", "url": "https://habr.com/ru/search/?q=формат+ошибок+REST+API", "lang": "ru"}
        ],
        "tasks": [
            "Добавьте обработчик 404 с JSON-ответом",
            "Напишите обработчик ValidationError с деталями"
        ],
        "xp": 10
    },
    {
        "id": 57, "phase": 2, "week": 12,
        "module": "FastAPI: middleware",
        "title": "Middleware и CORS",
        "goal": "Настроить CORS и писать middleware.",
        "points": [
            "Что такое CORS и preflight OPTIONS",
            "CORSMiddleware: origins, methods, headers",
            "Свой middleware (логирование, X-Request-Id)",
            "Порядок выполнения middleware"
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: CORS (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/cors/", "lang": "ru"},
            {"type": "article", "title": "MDN (RU): CORS", "url": "https://developer.mozilla.org/ru/docs/Web/HTTP/CORS", "lang": "ru"}
        ],
        "tasks": [
            "Настройте CORS для localhost:3000",
            "Напишите middleware с X-Request-Id"
        ],
        "xp": 10
    },
    {
        "id": 58, "phase": 2, "week": 12,
        "module": "FastAPI: безопасность",
        "title": "Хэширование паролей (bcrypt)",
        "goal": "Хранить пароли правильно.",
        "points": [
            "Почему нельзя хранить пароли открыто и в MD5",
            "bcrypt/argon2: соль, стоимость",
            "pwdlib/bcrypt в FastAPI",
            "Валидация силы пароля"
        ],
        "resources": [
            {"type": "article", "title": "Habr: хэширование паролей правильно", "url": "https://habr.com/ru/search/?q=хэширование+паролей+bcrypt", "lang": "ru"},
            {"type": "article", "title": "OWASP: хранение паролей (EN)", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html", "lang": "en"}
        ],
        "tasks": [
            "Напишите hash_password/verify_password на bcrypt",
            "Интегрируйте в регистрацию"
        ],
        "xp": 10
    },
    {
        "id": 59, "phase": 2, "week": 12,
        "module": "FastAPI: безопасность",
        "title": "JWT + OAuth2",
        "goal": "Реализовать аутентификацию через JWT.",
        "points": [
            "JWT: header.payload.signature, HS256",
            "OAuth2PasswordBearer",
            "Создание токена, срок жизни (exp)",
            "get_current_user: декодирование"
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: OAuth2 с JWT (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/security/oauth2-jwt/", "lang": "ru"},
            {"type": "video", "title": "JWT простыми словами (RU)", "url": "https://www.youtube.com/results?search_query=jwt+что+это+русский", "lang": "ru"}
        ],
        "tasks": [
            "Реализуйте /auth/login → access token",
            "Защитите /me зависимостью get_current_user"
        ],
        "xp": 20
    },
    {
        "id": 60, "phase": 2, "week": 12,
        "module": "FastAPI: безопасность",
        "title": "Refresh-токены и logout",
        "goal": "Полный цикл жизни токенов.",
        "points": [
            "Зачем refresh: короткий access + долгий refresh",
            "Хранение refresh: httpOnly cookie vs БД",
            "Обновление токена, revoke при logout",
            "httpOnly, secure, sameSite"
        ],
        "resources": [
            {"type": "article", "title": "Habr: refresh-токены правильно", "url": "https://habr.com/ru/search/?q=refresh+токены+jwt", "lang": "ru"},
            {"type": "article", "title": "Auth0: Refresh Tokens (EN)", "url": "https://auth0.com/learn/refresh-tokens", "lang": "en"}
        ],
        "tasks": [
            "Добавьте refresh-токен и /auth/refresh",
            "Реализуйте logout с инвалидацией"
        ],
        "xp": 20
    },
    {
        "id": 61, "phase": 2, "week": 12,
        "module": "FastAPI: безопасность",
        "title": "RBAC: роли и права",
        "goal": "Контролировать доступ по ролям.",
        "points": [
            "User.role: user/admin/moderator",
            "Зависимость require_role",
            "Права владельца ресурса",
            "401 vs 403 на практике"
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: зависимости с проверками ролей", "url": "https://fastapi.tiangolo.com/ru/tutorial/security/", "lang": "ru"},
            {"type": "article", "title": "Habr: RBAC в веб-приложениях", "url": "https://habr.com/ru/search/?q=RBAC+роли+доступ", "lang": "ru"}
        ],
        "tasks": [
            "Добавьте роли и защитите админ-эндпоинт",
            "Реализуйте проверку владельца ресурса"
        ],
        "xp": 15
    },
    # ============ Блок 2.2: Мини-проект 7 ============
    {
        "id": 62, "phase": 2, "week": 13,
        "module": "FastAPI: мини-проект 7",
        "title": "Task Manager API (часть 1): проектирование",
        "goal": "Спроектировать REST API и схему БД.",
        "points": [
            "Выберите предметную область проекта",
            "Схема БД: 3+ таблицы, связи",
            "Список эндпоинтов и статусы",
            "Структура проекта"
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: структура больших приложений (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/bigger-applications/", "lang": "ru"}
        ],
        "projectOptions": [
            {"title": "Task Manager", "desc": "Users + Tasks (статус, приоритет, дедлайн). Auth + CRUD + фильтры", "skills": "FastAPI, JWT, SQLAlchemy", "complexity": "средне"},
            {"title": "Менеджер заметок", "desc": "Users + Notes + Tags (M:N). Поиск, теги, пагинация", "skills": "FastAPI, M:N", "complexity": "средне"},
            {"title": "Трекер привычек", "desc": "Users + Habits + Logs (отметки). Статистика выполнения по неделям", "skills": "FastAPI, оконные/агрегаты", "complexity": "средне"},
            {"title": "Бюджет-трекер", "desc": "Users + Categories + Transactions. Отчёты по месяцам, лимиты", "skills": "FastAPI, агрегаты", "complexity": "средне"}
        ],
        "tasks": [
            "Выберите проект, спроектируйте схему и список эндпоинтов",
            "Создайте структуру проекта и модели"
        ],
        "xp": 20
    },
    {
        "id": 63, "phase": 2, "week": 13,
        "module": "FastAPI: мини-проект 7",
        "title": "Task Manager (часть 2): аутентификация",
        "goal": "Реализовать регистрацию и логин.",
        "points": [
            "Регистрация: bcrypt, уникальность email",
            "Логин → access + refresh",
            "get_current_user",
            "Профиль /me"
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: OAuth2 + JWT (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/security/oauth2-jwt/", "lang": "ru"}
        ],
        "tasks": [
            "Реализуйте /auth/register, /auth/login, /users/me",
            "Проверьте защиту токеном"
        ],
        "xp": 25
    },
    {
        "id": 64, "phase": 2, "week": 13,
        "module": "FastAPI: мини-проект 7",
        "title": "Task Manager (часть 3): CRUD + фильтры",
        "goal": "Реализовать основной функционал.",
        "points": [
            "CRUD задач с правами владельца",
            "Фильтры по статусу/приоритету",
            "Пагинация с total",
            "Валидация и ошибки"
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: response_model и фильтры", "url": "https://fastapi.tiangolo.com/ru/tutorial/response-model/", "lang": "ru"}
        ],
        "tasks": [
            "Реализуйте CRUD /tasks с ролями",
            "Добавьте фильтры и пагинацию"
        ],
        "xp": 25
    },
    {
        "id": 65, "phase": 2, "week": 13,
        "module": "FastAPI: мини-проект 7",
        "title": "Task Manager (часть 4): ошибки, рефакторинг",
        "goal": "Довести API до аккуратного состояния.",
        "points": [
            "Единый формат ошибок",
            "Обработка 404/403/422",
            "Рефакторинг: роутеры, схемы, сервисы",
            "Проверка всех эндпоинтов в /docs"
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: Handling Errors (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/handling-errors/", "lang": "ru"}
        ],
        "tasks": [
            "Стандартизируйте ошибки API",
            "Проверьте каждый эндпоинт через /docs"
        ],
        "xp": 20
    },
    {
        "id": 66, "phase": 2, "week": 13,
        "module": "FastAPI: мини-проект 7",
        "title": "Task Manager (часть 5): README и оформление",
        "goal": "Оформить проект для портфолио.",
        "points": [
            "README: описание, стек, запуск",
            "Скриншоты /docs",
            "Структура и .gitignore",
            "Запись в GitHub"
        ],
        "resources": [
            {"type": "article", "title": "Habr: как оформить README проекта", "url": "https://habr.com/ru/search/?q=как+оформить+readme+проекта", "lang": "ru"}
        ],
        "tasks": [
            "Напишите подробный README",
            "Запушьте проект на GitHub"
        ],
        "xp": 15,
        "achievement": "FastAPI-мастер"
    },
    # ============ Блок 2.3: Продвинутое FastAPI ============
    {
        "id": 67, "phase": 2, "week": 14,
        "module": "FastAPI: продвинутое",
        "title": "BackgroundTasks, загрузка файлов",
        "goal": "Фоновые задачи и файлы.",
        "points": [
            "BackgroundTasks: email после ответа",
            "UploadFile: сохранение файла",
            "StaticFiles: раздача статики",
            "Ограничения размера и типа файлов"
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: Background Tasks (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/background-tasks/", "lang": "ru"},
            {"type": "article", "title": "FastAPI: Request Files (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/request-files/", "lang": "ru"}
        ],
        "tasks": [
            "Добавьте фоновую задачу 'уведомление' после регистрации",
            "Реализуйте endpoint загрузки аватара"
        ],
        "xp": 10
    },
    {
        "id": 68, "phase": 2, "week": 14,
        "module": "FastAPI: продвинутое",
        "title": "WebSockets в FastAPI",
        "goal": "Реализовать real-time обмен.",
        "points": [
            "WebSocket в FastAPI (WS/WSS)",
            "accept, receive, send, close",
            "Менеджер соединений (рассылка)",
            "Простой чат"
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: WebSockets (RU)", "url": "https://fastapi.tiangolo.com/ru/advanced/websockets/", "lang": "ru"},
            {"type": "video", "title": "WebSocket + FastAPI чат (RU)", "url": "https://www.youtube.com/results?search_query=fastapi+websocket+чат+русский", "lang": "ru"}
        ],
        "tasks": [
            "Реализуйте WebSocket-эхо и клиент на JS",
            "Добавьте рассылку сообщений"
        ],
        "xp": 15
    },
    {
        "id": 69, "phase": 2, "week": 14,
        "module": "FastAPI: Redis",
        "title": "Redis: типы данных, redis-py",
        "goal": "Освоить Redis — ключевой инструмент бэкендера.",
        "points": [
            "Запуск Redis (Docker/local)",
            "redis-py: set, get, expire",
            "Типы: strings, hashes, lists, sets, sorted sets",
            "Когда что использовать"
        ],
        "resources": [
            {"type": "article", "title": "Habr: Redis для начинающих", "url": "https://habr.com/ru/search/?q=redis+для+начинающих", "lang": "ru"},
            {"type": "video", "title": "Redis простыми словами (RU)", "url": "https://www.youtube.com/results?search_query=redis+что+это+русский", "lang": "ru"}
        ],
        "tasks": [
            "Запустите Redis, сохраните и прочитайте значения",
            "Используйте expire и increment"
        ],
        "xp": 15
    },
    {
        "id": 70, "phase": 2, "week": 14,
        "module": "FastAPI: Redis",
        "title": "Кэширование: cache-aside, TTL",
        "goal": "Ускорить API кэшем.",
        "points": [
            "Паттерн cache-aside",
            "TTL и инвалидация кэша",
            "Защита от cache stampede",
            "Кэш ответов vs кэш данных"
        ],
        "resources": [
            {"type": "article", "title": "Habr: кэширование и паттерны кэша", "url": "https://habr.com/ru/search/?q=кэширование+redis+паттерны+cache+aside", "lang": "ru"},
            {"type": "article", "title": "Redis: caching patterns (EN)", "url": "https://redis.io/docs/latest/develop/use/caching/", "lang": "en"}
        ],
        "tasks": [
            "Закэшируйте GET-эндпоинт на 60 сек",
            "Инвалидируйте кэш при изменении данных"
        ],
        "xp": 15
    },
    {
        "id": 71, "phase": 2, "week": 15,
        "module": "FastAPI: наблюдение",
        "title": "Логирование и Sentry",
        "goal": "Наблюдать за приложением.",
        "points": [
            "Модуль logging: уровни, handlers",
            "JSON-логирование (structlog)",
            "Sentry: сбор ошибок",
            "Что логировать в API"
        ],
        "resources": [
            {"type": "article", "title": "Python docs (RU): логирование", "url": "https://docs.python.org/ru/3/howto/logging.html", "lang": "ru"},
            {"type": "article", "title": "Habr: логирование в Python правильно", "url": "https://habr.com/ru/search/?q=логирование+python+structlog", "lang": "ru"}
        ],
        "tasks": [
            "Настройте логирование запросов (метод, путь, статус, время)",
            "Подключите Sentry (free tier)"
        ],
        "xp": 10
    },
    {
        "id": 72, "phase": 2, "week": 15,
        "module": "asyncio: основы",
        "title": "Почему asyncio: GIL, I/O-bound vs CPU-bound",
        "goal": "Понять, когда асинхронность ускоряет, а когда нет.",
        "points": [
            "GIL: что это и как ограничивает",
            "I/O-bound (сеть, БД, файлы) vs CPU-bound",
            "Потоки vs процессы vs asyncio",
            "Почему asyncio идеален для веба"
        ],
        "resources": [
            {"type": "video", "title": "GIL и потоки в Python (EN)", "url": "https://www.youtube.com/results?search_query=python+gil+threads+explained", "lang": "en"},
            {"type": "article", "title": "Real Python: Async IO in Python", "url": "https://realpython.com/async-io-python/", "lang": "en"}
        ],
        "tasks": [
            "Напишите скрипт с 10 HTTP-запросами синхронно и посчитайте время",
            "Перепишите на asyncio и сравните скорость"
        ],
        "xp": 10
    },
    {
        "id": 73, "phase": 2, "week": 15,
        "module": "asyncio: основы",
        "title": "async/await, корутины, event loop",
        "goal": "Освоить базовые конструкции asyncio.",
        "points": [
            "Корутины: async def, await",
            "Event loop: как планирует задачи",
            "asyncio.run, create_task, gather",
            "sleep, Task, таймауты (asyncio.timeout)"
        ],
        "resources": [
            {"type": "article", "title": "Python docs: asyncio — базовые API", "url": "https://docs.python.org/3/library/asyncio-task.html", "lang": "en"},
            {"type": "video", "title": "Async/await в Python за 20 минут", "url": "https://www.youtube.com/results?search_query=python+asyncio+await+tutorial+русский", "lang": "ru"}
        ],
        "tasks": [
            "Напишите функцию, запускающую 5 корутин через gather",
            "Добавьте таймаут и обработку исключений"
        ],
        "xp": 15
    },
    {
        "id": 74, "phase": 2, "week": 15,
        "module": "asyncio: практика",
        "title": "Semaphore, Queue, async-клиенты (httpx)",
        "goal": "Управлять конкурентностью и ходить в внешние API.",
        "points": [
            "Semaphore: лимит одновременных задач",
            "Queue: распределение задач между воркерами",
            "httpx.AsyncClient: контекстный менеджер",
            "Ретраи и таймауты"
        ],
        "resources": [
            {"type": "article", "title": "Python docs: Synchronization Primitives", "url": "https://docs.python.org/3/library/asyncio-sync.html", "lang": "en"},
            {"type": "article", "title": "httpx: Async Client — документация", "url": "https://www.python-httpx.org/async/", "lang": "en"}
        ],
        "tasks": [
            "Реализуйте парсер с Semaphore(5) на 100 URL",
            "Напишите клиент к публичному API с ретраями и таймаутами"
        ],
        "xp": 15
    },
    {
        "id": 75, "phase": 2, "week": 15,
        "module": "FastAPI: async",
        "title": "async SQLAlchemy, asyncpg",
        "goal": "Перевести БД-слой на асинхронный.",
        "points": [
            "asyncpg vs psycopg3 async",
            "create_async_engine, AsyncSession",
            "async get_db",
            "Где нельзя использовать sync-код"
        ],
        "resources": [
            {"type": "article", "title": "SQLAlchemy: AsyncIO Support", "url": "https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html", "lang": "en"},
            {"type": "article", "title": "FastAPI: async БД (RU)", "url": "https://fastapi.tiangolo.com/ru/advanced/async-sql-databases/", "lang": "ru"}
        ],
        "tasks": [
            "Переведите get_db и модели на async",
            "Убедитесь, что всё работает"
        ],
        "xp": 20
    },
    {
        "id": 73, "phase": 2, "week": 15,
        "module": "FastAPI: защита",
        "title": "Rate limiting (slowapi)",
        "goal": "Защитить API от перебора и спама.",
        "points": [
            "slowapi: лимиты на эндпоинты",
            "Лимиты на /login",
            "Fixed window vs sliding window",
            "Блокировка после N попыток"
        ],
        "resources": [
            {"type": "article", "title": "slowapi: документация", "url": "https://slowapi.readthedocs.io/en/latest/", "lang": "en"},
            {"type": "article", "title": "Habr: rate limiting в API", "url": "https://habr.com/ru/search/?q=rate+limiting+api", "lang": "ru"}
        ],
        "tasks": [
            "Подключите slowapi, ограничьте логин",
            "Реализуйте блокировку после 5 попыток"
        ],
        "xp": 15
    },
    {
        "id": 74, "phase": 2, "week": 15,
        "module": "FastAPI: деплой",
        "title": "Деплой: uvicorn/gunicorn, VPS, Nginx, HTTPS",
        "goal": "Подготовить приложение к продакшену.",
        "points": [
            "uvicorn workers, gunicorn",
            "Запуск на VPS (Ubuntu)",
            "Nginx reverse proxy",
            "HTTPS: Let's Encrypt"
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: Deployment (RU)", "url": "https://fastapi.tiangolo.com/ru/deployment/", "lang": "ru"},
            {"type": "article", "title": "Habr: деплой FastAPI на VPS", "url": "https://habr.com/ru/search/?q=деплой+fastapi+vps+nginx", "lang": "ru"}
        ],
        "tasks": [
            "Настройте запуск uvicorn --workers 2",
            "Схематично разберите деплой: сервер → Nginx → uvicorn"
        ],
        "xp": 10
    },
    {
        "id": 75, "phase": 2, "week": 16,
        "module": "FastAPI: практика",
        "title": "Best practices и чек-лист продакшена",
        "goal": "Пройти прод-чек-лист проекта.",
        "points": [
            "Секреты в .env (pydantic-settings)",
            "CORS, rate limiting, ошибки, логи",
            "Компрессия ответов (GZip)",
            "Профилирование медленных запросов"
        ],
        "resources": [
            {"type": "article", "title": "Habr: best practices FastAPI", "url": "https://habr.com/ru/search/?q=fastapi+best+practices", "lang": "ru"},
            {"type": "article", "title": "FastAPI: Middleware (компрессия)", "url": "https://fastapi.tiangolo.com/ru/advanced/middleware/", "lang": "ru"}
        ],
        "tasks": [
            "Пройдите чек-лист продакшена на любом учебном API (CORS, rate limit, логи, .env)",
            "Включите GZip-компрессию"
        ],
        "xp": 15
    },
    # ============ Блок 2.3: Тестирование (pytest) ============
    {
        "id": 79, "phase": 2, "week": 16,
        "module": "Тестирование: pytest",
        "title": "pytest: основы, fixtures",
        "goal": "Писать тесты на Python.",
        "points": [
            "pip install pytest, запуск pytest",
            "test_*.py, assert",
            "fixtures: scope, yield",
            "parametrize"
        ],
        "resources": [
            {"type": "article", "title": "pytest: документация (EN)", "url": "https://docs.pytest.org/en/stable/", "lang": "en"},
            {"type": "article", "title": "Habr: pytest с нуля", "url": "https://habr.com/ru/search/?q=pytest+с+нуля", "lang": "ru"}
        ],
        "tasks": [
            "Напишите тесты для простых функций с fixtures",
            "Используйте parametrize на 5 кейсах"
        ],
        "xp": 15
    },
    {
        "id": 80, "phase": 2, "week": 16,
        "module": "Тестирование: pytest",
        "title": "Мокирование (monkeypatch, unittest.mock)",
        "goal": "Изолировать тесты от внешних сервисов.",
        "points": [
            "Зачем мокать",
            "monkeypatch.setattr",
            "patch/mock, assert_called_with",
            "patch.dict для env"
        ],
        "resources": [
            {"type": "article", "title": "unittest.mock: документация (EN)", "url": "https://docs.python.org/3/library/unittest.mock.html", "lang": "en"},
            {"type": "article", "title": "Habr: моки и стабы в Python", "url": "https://habr.com/ru/search/?q=mock+python+monkeypatch", "lang": "ru"}
        ],
        "tasks": [
            "Замокайте внешний HTTP-вызов в функции",
            "Проверьте, что вызов прошёл с нужными аргументами"
        ],
        "xp": 15
    },
    {
        "id": 81, "phase": 2, "week": 16,
        "module": "Тестирование: pytest",
        "title": "Тесты БД и фикстуры проекта",
        "goal": "Тестировать код с БД.",
        "points": [
            "Транзакция в фикстуре (откат после теста)",
            "Фабрики данных (factory_boy / вручную)",
            "Тестовая база",
            "Изоляция тестов"
        ],
        "resources": [
            {"type": "article", "title": "Habr: тесты с SQLAlchemy изолированно", "url": "https://habr.com/ru/search/?q=pytest+sqlalchemy+тесты", "lang": "ru"},
            {"type": "article", "title": "factory_boy: документация (EN)", "url": "https://factoryboy.readthedocs.io/", "lang": "en"}
        ],
        "tasks": [
            "Напишите фикстуру сессии с откатом",
            "Добавьте фабрику User"
        ],
        "xp": 15
    },
    {
        "id": 82, "phase": 2, "week": 16,
        "module": "Тестирование: FastAPI",
        "title": "TestClient FastAPI",
        "goal": "Интеграционные тесты API.",
        "points": [
            "TestClient, httpx-based",
            "Тесты эндпоинтов: статус, тело",
            "Переопределение зависимостей (app.dependency_overrides)",
            "Авторизация в тестах"
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: Testing (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/testing/", "lang": "ru"},
            {"type": "article", "title": "FastAPI: dependency_overrides", "url": "https://fastapi.tiangolo.com/ru/tutorial/dependencies/dependencies-in-path-operation-decorators/", "lang": "ru"}
        ],
        "tasks": [
            "Напишите интеграционные тесты для своих эндпоинтов",
            "Подмените зависимость авторизации"
        ],
        "xp": 20
    },
    {
        "id": 83, "phase": 2, "week": 17,
        "module": "Тестирование: практика",
        "title": "Покрытие кода, TDD",
        "goal": "Улучшать качество через тесты.",
        "points": [
            "pytest-cov: покрытие, как читать",
            "Минимальный порог (например, 60-70%)",
            "TDD: red-green-refactor",
            "Что тестировать в первую очередь"
        ],
        "resources": [
            {"type": "article", "title": "pytest-cov: документация (EN)", "url": "https://pytest-cov.readthedocs.io/en/latest/", "lang": "en"},
            {"type": "article", "title": "Habr: TDD на примерах", "url": "https://habr.com/ru/search/?q=TDD+python+пример", "lang": "ru"}
        ],
        "tasks": [
            "Доведите покрытие кода учебного API до 60%+",
            "Напишите один тест в стиле TDD"
        ],
        "xp": 15
    },
    {
        "id": 84, "phase": 2, "week": 17,
        "module": "Тестирование: практика",
        "title": "Юнит-тесты сервисов",
        "goal": "Тестировать бизнес-логику отдельно.",
        "points": [
            "Слои: router → service → repository",
            "Мокать репозитории/сессии",
            "Тесты краевых случаев",
            "Набор практических задач"
        ],
        "resources": [
            {"type": "article", "title": "Habr: юнит-тесты сервисного слоя", "url": "https://habr.com/ru/search/?q=юнит+тесты+сервисный+слой+python", "lang": "ru"}
        ],
        "tasks": [
            "Вынесите логику учебного API в сервисный слой",
            "Покройте сервисы юнит-тестами"
        ],
        "xp": 15
    },
    {
        "id": 85, "phase": 2, "week": 17,
        "module": "Тестирование: практика",
        "title": "Интеграционные сценарии",
        "goal": "Тестировать проект целиком.",
        "points": [
            "Полный сценарий: регистрация → логин → CRUD",
            "Тестовая БД (SQLite/Postgres в CI)",
            "Скорость и порядок тестов",
            "Небольшой мини-прогон на учебном API"
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: Testing (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/testing/", "lang": "ru"}
        ],
        "tasks": [
            "Напишите 3 интеграционных сценария",
            "Запустите в CI/локально"
        ],
        "xp": 15
    },
    {
        "id": 76, "phase": 2, "week": 17,
        "module": "FastAPI: мини-проект 8",
        "title": "TODO с фронтендом (часть 1): бэкенд",
        "goal": "Сделать полноценное приложение «сайт».",
        "points": [
            "Выберите проект",
            "FastAPI-бэкенд: auth + CRUD",
            "Redis-кэш и rate limiting",
            "Логирование и ошибки"
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: туториал (обзор)", "url": "https://fastapi.tiangolo.com/ru/tutorial/", "lang": "ru"}
        ],
        "projectOptions": [
            {"title": "TODO-приложение с фронтом", "desc": "Список задач, добавление, статусы; страница на fetch + JWT", "skills": "FastAPI, JWT, fetch", "complexity": "средне"},
            {"title": "Мини-блог с фронтом", "desc": "Посты, комментарии; лента на странице, авторизация авторов", "skills": "FastAPI, связи, fetch", "complexity": "средне"},
            {"title": "Каталог товаров + корзина", "desc": "Товары и корзина пользователя; страницы каталога", "skills": "FastAPI, M:N, fetch", "complexity": "средне"},
            {"title": "Трекер привычек с фронтом", "desc": "Привычки, отметки, календарь выполнения; страница-дашборд", "skills": "FastAPI, агрегаты, fetch", "complexity": "средне"}
        ],
        "tasks": [
            "Выберите проект, реализуйте бэкенд",
            "Добавьте кэш и rate limiting"
        ],
        "xp": 25
    },
    {
        "id": 77, "phase": 2, "week": 17,
        "module": "FastAPI: мини-проект 8",
        "title": "TODO с фронтендом (часть 2): связка",
        "goal": "Связать страницу с API.",
        "points": [
            "Страницы: логин, список, форма",
            "fetch + отображение данных",
            "Обработка 401 (refresh)",
            "Ошибки сервера на экране"
        ],
        "resources": [
            {"type": "article", "title": "MDN (RU): Using Fetch", "url": "https://developer.mozilla.org/ru/docs/Web/API/Fetch_API/Using_Fetch", "lang": "ru"}
        ],
        "tasks": [
            "Сделайте страницы и свяжите с API",
            "Обработайте 401 через refresh"
        ],
        "xp": 25
    },
    {
        "id": 78, "phase": 2, "week": 17,
        "module": "FastAPI: мини-проект 8",
        "title": "TODO с фронтендом (часть 3): финал",
        "goal": "Довести проект до «портфолио-готового».",
        "points": [
            "Стили: тёмная тема, карточки",
            "Обработка состояний (загрузка, пусто, ошибка)",
            "README + скринкаст",
            "Запись в GitHub"
        ],
        "resources": [
            {"type": "article", "title": "MDN (RU): CSS grid", "url": "https://developer.mozilla.org/ru/docs/Web/CSS/grid", "lang": "ru"}
        ],
        "tasks": [
            "Оформите UI и README",
            "Запушьте проект"
        ],
        "xp": 30,
        "achievement": "Полный стек"
    },
]