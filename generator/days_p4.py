# -*- coding: utf-8 -*-
# ФАЗА 3: Дипломный проект + карьера (дни 98-137)

DAYS_P4 = [
    {
        "id": 101, "phase": 3, "week": 22,
        "module": "Диплом: планирование",
        "title": "Блог-платформа: ТЗ и архитектура",
        "goal": "Спроектировать полноценный продукт.",
        "points": [
            "Функционал: посты, комментарии, лайки, подписки, теги",
            "Схема БД: users, posts, comments, likes, follows, tags",
            "Список эндпоинтов API",
            "Архитектура и структура репозитория",
        ],
        "resources": [
            {"type": "article", "title": "ТЗ, за которое не стыдно (Habr)", "url": "https://habr.com/ru/articles/912798/", "lang": "ru"},
            {"type": "article", "title": "FastAPI: структура больших приложений (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/bigger-applications/", "lang": "ru"},
        ],
        "tasks": [
            "Выберите проект, составьте ТЗ и схему БД",
            "Соберите список эндпоинтов",
        ],
        "xp": 20
    },
    {
        "id": 102, "phase": 3, "week": 22,
        "module": "Диплом: основа",
        "title": "Блог-платформа: скелет и модели",
        "goal": "Поднять проект и описать БД.",
        "points": [
            "Структура: app, routers, models, schemas, core",
            "SQLAlchemy-модели всех сущностей",
            "Связи и индексы",
            "Alembic: первая миграция",
        ],
        "resources": [
            {"type": "article", "title": "SQLAlchemy: ORM (EN)", "url": "https://docs.sqlalchemy.org/en/20/orm/index.html", "lang": "en"},
            {"type": "article", "title": "Alembic: туториал (EN)", "url": "https://alembic.sqlalchemy.org/en/latest/tutorial.html", "lang": "en"},
        ],
        "tasks": [
            "Создайте структуру проекта и все модели",
            "Сгенерируйте миграции",
        ],
        "xp": 20
    },
    {
        "id": 103, "phase": 3, "week": 22,
        "module": "Диплом: auth",
        "title": "Блог-платформа: аутентификация",
        "goal": "Полный цикл auth и ролей.",
        "points": [
            "Регистрация, логин, refresh",
            "Роли: user/admin/moderator",
            "get_current_user, require_role",
            "Защита модераторских действий",
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: OAuth2 + JWT (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/security/oauth2-jwt/", "lang": "ru"},
            {"type": "article", "title": "Создание собственного API на Python (FastAPI): Авторизация, Аутентификация и роли пользователей", "url": "https://habr.com/ru/articles/829742/", "lang": "ru"},
            {"type": "article", "title": "Добавляем Refresh Token", "url": "https://habr.com/ru/articles/466929/", "lang": "ru"},
        ],
        "tasks": [
            "Реализуйте auth и роли",
            "Добавьте права модератора на удаление постов",
        ],
        "xp": 20
    },
    {
        "id": 104, "phase": 3, "week": 22,
        "module": "Диплом: посты",
        "title": "Блог-платформа: CRUD постов",
        "goal": "Основной контент-функционал.",
        "points": [
            "Создание, редактирование, удаление постов",
            "Права владельца",
            "Теги (M:N)",
            "Пагинация ленты",
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: CRUD паттерн (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/response-model/", "lang": "ru"},
            {"type": "article", "title": "Фильтрация и пагинация в FastAPI", "url": "https://habr.com/ru/articles/714570/", "lang": "ru"},
            {"type": "article", "title": "Крадущийся тигр, затаившийся SQLAlchemy. Основы", "url": "https://habr.com/ru/articles/470285/", "lang": "ru"},
        ],
        "tasks": [
            "Реализуйте CRUD постов с тегами",
            "Добавьте пагинацию",
        ],
        "xp": 25
    },
    {
        "id": 105, "phase": 3, "week": 23,
        "module": "Диплом: соц.функции",
        "title": "Блог-платформа: лайки, комментарии",
        "goal": "Добавить социальные механики.",
        "points": [
            "Лайки (M:N user-post, уникальность)",
            "Счётчик лайков (counter кэш)",
            "Комментарии: дерево или плоские",
            "Права на удаление комментария",
        ],
        "resources": [
            {"type": "article", "title": "SQLAlchemy: многие-ко-многим (EN)", "url": "https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html", "lang": "en"},
        ],
        "tasks": [
            "Реализуйте лайки и комментарии",
            "Оптимизируйте счётчик через Redis",
        ],
        "xp": 25
    },
    {
        "id": 106, "phase": 3, "week": 23,
        "module": "Диплом: подписки",
        "title": "Блог-платформа: подписки и лента",
        "goal": "Персональная лента из подписок.",
        "points": [
            "follows: подписка/отписка",
            "Лента: посты авторов на кого подписан",
            "Сортировка по дате",
            "Счётчик подписчиков",
        ],
        "resources": [
            {"type": "article", "title": "PostgreSQL: JOIN (EN)", "url": "https://www.postgresql.org/docs/current/tutorial-join.html", "lang": "en"},
        ],
        "tasks": [
            "Реализуйте подписки",
            "Постройте ленту через JOIN",
        ],
        "xp": 20
    },
    {
        "id": 107, "phase": 3, "week": 23,
        "module": "Диплом: поиск",
        "title": "Блог-платформа: поиск и фильтры",
        "goal": "Искать посты по тексту и тегам.",
        "points": [
            "ILIKE поиск по заголовку/тексту",
            "Фильтр по тегам",
            "Продвинутый поиск (обзор full-text)",
            "Индексы для поиска",
        ],
        "resources": [
            {"type": "article", "title": "PostgreSQL: Full Text Search (EN)", "url": "https://www.postgresql.org/docs/current/textsearch.html", "lang": "en"},
        ],
        "tasks": [
            "Добавьте поиск и фильтр по тегам",
            "Поставьте индекс на поле",
        ],
        "xp": 20
    },
    {
        "id": 108, "phase": 3, "week": 23,
        "module": "Диплом: кэш",
        "title": "Блог-платформа: кэш и оптимизация",
        "goal": "Ускорить горячие эндпоинты.",
        "points": [
            "Кэш ленты и топ-постов в Redis",
            "Инвалидация при изменениях",
            "Счётчики в Redis",
            "Профилирование медленных запросов",
        ],
        "resources": [
            {"type": "article", "title": "Ускорение микросервиса кэшем: FastAPI, Redis (Habr)", "url": "https://habr.com/ru/companies/vk/articles/557232/", "lang": "en"},
        ],
        "tasks": [
            "Закэшируйте топ-посты",
            "Добавьте инвалидацию",
        ],
        "xp": 20
    },
    {
        "id": 109, "phase": 3, "week": 24,
        "module": "Диплом: async",
        "title": "Блог-платформа: async-слой и rate limiting",
        "goal": "Перевести на async и защитить.",
        "points": [
            "AsyncEngine, AsyncSession",
            "async get_db",
            "slowapi: лимиты на лайки/логин",
            "Проверка корректности",
        ],
        "resources": [
            {"type": "article", "title": "Асинхронный SQLAlchemy 2: гайд (Habr)", "url": "https://habr.com/ru/companies/amvera/articles/849836/", "lang": "ru"},
            {"type": "article", "title": "SlowApi: ограничение частоты запросов в FastAPI (документация)", "url": "https://slowapi.readthedocs.io/en/latest/", "lang": "ru"},
        ],
        "tasks": [
            "Переведите проект на async",
            "Добавьте rate limiting",
        ],
        "xp": 25
    },
    {
        "id": 110, "phase": 3, "week": 24,
        "module": "Диплом: фоновые",
        "title": "Блог-платформа: уведомления",
        "goal": "Фоновые уведомления (подписки/лайки).",
        "points": [
            "События: комментарий/лайк",
            "Celery-задача отправки уведомления",
            "Хранение уведомлений",
            "WebSocket или poll",
        ],
        "resources": [
            {"type": "article", "title": "Celery: first steps (EN)", "url": "https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html", "lang": "en"},
        ],
        "tasks": [
            "Добавьте уведомления через Celery",
            "Сделайте список уведомлений в API",
        ],
        "xp": 20
    },
    {
        "id": 111, "phase": 3, "week": 24,
        "module": "Диплом: фронт",
        "title": "Блог-платформа: лёгкий фронтенд",
        "goal": "Минимальный UI для демонстрации.",
        "points": [
            "Страницы: лента, пост, профиль, логин",
            "fetch к API",
            "Обработка 401/ошибок",
            "Простая вёрстка",
        ],
        "resources": [
            {"type": "article", "title": "MDN (RU): Fetch API", "url": "https://developer.mozilla.org/ru/docs/Web/API/Fetch_API/Using_Fetch", "lang": "ru"},
        ],
        "tasks": [
            "Сделайте страницы и свяжите с API",
            "Показывайте ошибки сервера",
        ],
        "xp": 20
    },
    {
        "id": 112, "phase": 3, "week": 24,
        "module": "Диплом: тесты",
        "title": "Блог-платформа: тесты",
        "goal": "Покрыть ключевую логику тестами.",
        "points": [
            "Юнит-тесты сервисов",
            "Интеграционные тесты эндпоинтов",
            "Фикстуры БД и auth",
            "Покрытие > 60%",
        ],
        "resources": [
            {"type": "article", "title": "FastAPI: Testing (RU)", "url": "https://fastapi.tiangolo.com/ru/tutorial/testing/", "lang": "ru"},
        ],
        "tasks": [
            "Напишите тесты на auth, посты, лайки",
            "Доведите покрытие до 60%+",
        ],
        "xp": 30
    },
    {
        "id": 113, "phase": 3, "week": 25,
        "module": "Диплом: docker",
        "title": "Блог-платформа: Docker + compose",
        "goal": "Собрать весь стек в контейнеры.",
        "points": [
            "Dockerfile app",
            "compose: app + postgres + redis + worker + nginx",
            "healthcheck, миграции при старте",
            "Проверка запуска одной командой",
        ],
        "resources": [
            {"type": "article", "title": "Docker Compose: getting started (docs)", "url": "https://docs.docker.com/compose/gettingstarted/", "lang": "ru"},
        ],
        "tasks": [
            "Соберите compose для всего стека",
            "Убедитесь, что всё стартует вместе",
        ],
        "xp": 25
    },
    {
        "id": 114, "phase": 3, "week": 25,
        "module": "Диплом: CI",
        "title": "Блог-платформа: CI/CD (GitHub Actions)",
        "goal": "Автоматизировать проверку и деплой.",
        "points": [
            "GitHub Actions: workflow",
            "Запуск линтера и тестов на push",
            "Автодеплой на VPS (SSH)",
            "Плохой/хороший workflow",
        ],
        "resources": [
            {"type": "article", "title": "GitHub Actions: docs (RU)", "url": "https://docs.github.com/ru/actions", "lang": "ru"},
            {"type": "article", "title": "CI/CD в GitHub Actions для Python (Habr)", "url": "https://habr.com/ru/articles/1037002/", "lang": "ru"},
        ],
        "tasks": [
            "Настройте CI: lint + test на каждый push",
            "Добавьте автодеплой (или схему)",
        ],
        "xp": 25
    },
    {
        "id": 115, "phase": 3, "week": 25,
        "module": "Диплом: деплой",
        "title": "Блог-платформа: деплой на VPS",
        "goal": "Запустить проект на реальном сервере.",
        "points": [
            "Аренда VPS (рекоменд. варианты)",
            "SSH, nginx, HTTPS (Let's Encrypt)",
            "Запуск через docker compose",
            "Проверка доступности по HTTPS",
        ],
        "resources": [
            {"type": "article", "title": "Настройка VPS, NGINX и FastAPI (Habr)", "url": "https://habr.com/ru/articles/820093/", "lang": "ru"},
            {"type": "article", "title": "Let's Encrypt: как получить сертификат", "url": "https://letsencrypt.org/getting-started/", "lang": "en"},
        ],
        "tasks": [
            "Задеплойте блог на VPS (или запишите план)",
            "Настройте HTTPS",
        ],
        "xp": 30
    },
    {
        "id": 116, "phase": 3, "week": 25,
        "module": "Диплом: README",
        "title": "Блог-платформа: README, документация, портфолио",
        "goal": "Превратить проект в сильную заявку.",
        "points": [
            "README: описание, стек, схема БД, скриншоты",
            "Демо-ссылка (VPS)",
            "Структурированный репозиторий",
            "Красивый профиль GitHub",
        ],
        "resources": [
            {"type": "article", "title": "Оформляем README-файл профиля на GitHub (Habr)", "url": "https://habr.com/ru/articles/649363/", "lang": "ru"},
        ],
        "tasks": [
            "Напишите детальный README со скриншотами",
            "Оформите GitHub-профиль",
        ],
        "xp": 20,
        "achievement": "Дипломный проект готов"
    },
    {
        "id": 117, "phase": 3, "week": 26,
        "module": "Карьера: резюме",
        "title": "Резюме для Junior Python",
        "goal": "Составить резюме, которое читают.",
        "points": [
            "Структура: о себе, стек, проекты, образование",
            "Проекты с описанием задач и результата",
            "Правильные ключевые слова (A/B)",
            "Шаблоны (Хабр Карьера, hh)",
        ],
        "resources": [
            {"type": "article", "title": "Что написать в резюме без опыта работы (Habr)", "url": "https://habr.com/ru/companies/htmlacademy/articles/543444/", "lang": "ru"},
            {"type": "article", "title": "Что видят в вашем резюме Python-рекрутеры (Habr)", "url": "https://habr.com/ru/companies/oleg-bunin/articles/575956/", "lang": "ru"},
        ],
        "tasks": [
            "Составьте резюме по шаблону",
            "Опишите 3 проекта с цифрами",
        ],
        "xp": 15
    },
    {
        "id": 119, "phase": 3, "week": 26,
        "module": "Карьера: собесы",
        "title": "Тестовые задания: как решать",
        "goal": "Эффективно проходить тестовые.",
        "points": [
            "Стратегия: план → код → тесты → README",
            "Читать ТЗ внимательно",
            "Проверять edge cases",
            "Тайм-менеджмент",
        ],
        "resources": [
            {"type": "article", "title": "Как правильно делать тестовые задания (Habr)", "url": "https://habr.com/ru/articles/877180/", "lang": "ru"},
        ],
        "tasks": [
            "Решите одно тестовое из открытых источников",
            "Оформите его по чек-листу",
        ],
        "xp": 15
    },
    {
        "id": 120, "phase": 3, "week": 26,
        "module": "Карьера: собесы",
        "title": "Теория для интервью: Python",
        "goal": "Отвечать на типовые вопросы по Python.",
        "points": [
            "GIL, mutable/immutable, list vs tuple",
            "Декораторы, генераторы, контекстные менеджеры",
            "Сложности структур данных",
            "Функциональные/ООП вопросы",
        ],
        "resources": [
            {"type": "article", "title": "10 вопросов для Junior Python-разработчика (Habr)", "url": "https://habr.com/ru/articles/654489/", "lang": "ru"},
            {"type": "article", "title": "Real Python: типовые вопросы (EN)", "url": "https://realpython.com/python-coding-interview-tips/", "lang": "en"},
        ],
        "tasks": [
            "Прорепетируйте 20 вопросов по Python",
            "Запишите свои ответы",
        ],
        "xp": 20
    },
    {
        "id": 121, "phase": 3, "week": 27,
        "module": "Карьера: собесы",
        "title": "Теория для интервью: БД и SQL",
        "goal": "Отвечать на вопросы по БД.",
        "points": [
            "Индексы: B-tree, когда работают",
            "Транзакции, ACID, уровни изоляции",
            "JOIN, GROUP BY, агрегаты",
            "N+1, пагинация",
        ],
        "resources": [
            {"type": "article", "title": "Вопросы по SQL на собеседовании. Часть 1 (Habr)", "url": "https://habr.com/ru/articles/790850/", "lang": "ru"},
            {"type": "article", "title": "B-Tree индекс и его производные в PostgreSQL (Хабр/Quadcode)", "url": "https://habr.com/ru/companies/quadcode/articles/696498/", "lang": "ru"},
            {"type": "article", "title": "Как я SQLAlchemy удобной сделал — решение проблемы N+1 (Хабр)", "url": "https://habr.com/ru/articles/324876/", "lang": "ru"},
        ],
        "tasks": [
            "Прорепетируйте вопросы по SQL",
            "Повторите ACID и индексы",
        ],
        "xp": 20
    },
    {
        "id": 124, "phase": 3, "week": 27,
        "module": "Карьера: поиск",
        "title": "Стратегия поиска работы",
        "goal": "Построить системный поиск вакансий.",
        "points": [
            "Где искать: hh, Хабр Карьера, LinkedIn, телеграм-чаты",
            "Отклики: кастомные сообщения",
            "Ведение таблицы воронки",
            "Сколько откликов в день",
        ],
        "resources": [
            {"type": "article", "title": "Habr Карьера: как искать работу junior", "url": "https://career.habr.com/", "lang": "ru"},
            {"type": "article", "title": "Исследование влияния сопроводительного письма: как я сделал 1000 откликов на вакансии", "url": "https://habr.com/ru/articles/836634/", "lang": "ru"},
        ],
        "tasks": [
            "Составьте список из 20 компаний",
            "Настройте отслеживание откликов",
        ],
        "xp": 10
    },
    {
        "id": 125, "phase": 3, "week": 28,
        "module": "Карьера: собесы",
        "title": "Мок-собеседование",
        "goal": "Пройти тренировочное интервью.",
        "points": [
            "Найти мок-собеседование (знакомые, чаты)",
            "Пройти весь цикл",
            "Разбор ошибок",
            "Уверенность и презентация",
        ],
        "resources": [
            {"type": "article", "title": "Топ вопросов на Junior-собеседованиях (Habr)", "url": "https://habr.com/ru/articles/718282/", "lang": "ru"},
        ],
        "tasks": [
            "Пройдите одно мок-собеседование",
            "Разберите слабые места",
        ],
        "xp": 20
    },
    {
        "id": 131, "phase": 3, "week": 29,
        "module": "Финал: оффер",
        "title": "Офферы, переговоры, выбор",
        "goal": "Правильно выбрать и принять оффер.",
        "points": [
            "Оценка оффера: ЗП, стек, рост, удалёнка",
            "Мягкие переговоры о ЗП",
            "Сравнение нескольких офферов",
            "Что спросить перед принятием",
        ],
        "resources": [
            {"type": "article", "title": "Как оценить и выбрать оффер (Habr)", "url": "https://habr.com/ru/companies/getmatch/articles/517068/", "lang": "ru"},
        ],
        "tasks": [
            "Составьте критерии идеального оффера",
            "Оцените текущие варианты",
        ],
        "xp": 15
    },
    {
        "id": 135, "phase": 3, "week": 30,
        "module": "Финал: подведение",
        "title": "Подведение итогов и планы развития",
        "goal": "Осознать путь и спланировать рост.",
        "points": [
            "Пройдите по своему прогрессу",
            "Оцените достижения и gap",
            "План на следующие 6 месяцев",
            "Что дальше: Go, cloud, системный дизайн",
        ],
        "resources": [
            {"type": "article", "title": "Роадмеп бэкенд-разработчика на Python (Habr)", "url": "https://habr.com/ru/articles/919588/", "lang": "ru"},
        ],
        "tasks": [
            "Напишите рефлексию о пройденном пути",
            "Составьте план на 6 месяцев вперёд",
        ],
        "xp": 15
    },
    {
        "id": 137, "phase": 3, "week": 30,
        "module": "Финал: итог",
        "title": "Финальный день: праздник и старт",
        "goal": "Зафиксировать результат и двигаться дальше.",
        "points": [
            "Пройдите по всем пройденным темам",
            "Подсчитайте XP и свои достижения",
            "Поставьте цели на следующий этап",
            "Отпразднуйте",
        ],
        "resources": [
        ],
        "tasks": [
            "Пройдите по своим достижениям",
            "Напишите итоговый пост/рефлексию",
        ],
        "xp": 10,
        "achievement": "Вы стали Junior Backend Developer!"
    },
]