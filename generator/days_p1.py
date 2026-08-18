# -*- coding: utf-8 -*-
# ФАЗА 1: Фундамент веб-разработки (дни 16-49)

DAYS_P1 = [
    # ============ Блок 1.1: SQL + PostgreSQL ============
    {
        "id": 16, "phase": 1, "week": 4,
        "module": "SQL: основы",
        "title": "Реляционная модель, установка PostgreSQL",
        "goal": "Понять реляционную модель и поднять локальный PostgreSQL.",
        "points": [
            "Таблица, столбец, строка, первичный ключ (PK), внешний ключ (FK)",
            "Связи: 1:1, 1:N, M:N",
            "Установка PostgreSQL + DBeaver/pgAdmin (или docker)",
            "Подключение и первые запросы"
        ],
        "resources": [
            {"type": "course", "title": "SQL Academy — интерактивный тренажёр (RU)", "url": "https://sql-academy.org/ru", "lang": "ru"},
            {"type": "article", "title": "Postgres Pro: документация на русском", "url": "https://postgrespro.ru/docs/postgresql", "lang": "ru"},
            {"type": "video", "title": "Установка PostgreSQL и первые запросы (RU)", "url": "https://www.youtube.com/results?search_query=установка+postgresql+первые+запросы", "lang": "ru"}
        ],
        "tasks": [
            "Установите PostgreSQL, создайте БД test",
            "Создайте таблицу users (id, name, email) и вставьте 5 строк"
        ],
        "xp": 10
    },
    {
        "id": 17, "phase": 1, "week": 4,
        "module": "SQL: основы",
        "title": "SELECT, WHERE, ORDER BY, LIMIT",
        "goal": "Освоить базовый синтаксис выборки.",
        "points": [
            "SELECT столбцов, alias, DISTINCT",
            "WHERE: =, <>, LIKE, IN, BETWEEN, IS NULL",
            "ORDER BY, LIMIT/OFFSET",
            "AND/OR/NOT"
        ],
        "resources": [
            {"type": "course", "title": "SQL Academy: тренажёр (SELECT/WHERE)", "url": "https://sql-academy.org/ru/trainer", "lang": "ru"},
            {"type": "article", "title": "Postgres Pro: SELECT с примерами", "url": "https://postgrespro.ru/docs/postgresql/16/sql-select", "lang": "ru"}
        ],
        "tasks": [
            "Выберите пользователей старше 18, отсортируйте по имени",
            "Найдите email, содержащие 'mail' через LIKE"
        ],
        "xp": 10
    },
    {
        "id": 18, "phase": 1, "week": 4,
        "module": "SQL: агрегаты",
        "title": "Агрегаты, GROUP BY, HAVING",
        "goal": "Считать статистику по группам.",
        "points": [
            "COUNT, SUM, AVG, MIN, MAX",
            "GROUP BY по столбцу",
            "HAVING — фильтр после группировки",
            "NULL в агрегатах"
        ],
        "resources": [
            {"type": "course", "title": "SQL Academy: GROUP BY и агрегаты", "url": "https://sql-academy.org/ru/trainer", "lang": "ru"},
            {"type": "article", "title": "Postgres Pro: агрегатные функции", "url": "https://postgrespro.ru/docs/postgresql/16/functions-aggregate", "lang": "ru"}
        ],
        "tasks": [
            "Посчитайте средний возраст по городам",
            "Выведите города, где больше 3 пользователей (HAVING)"
        ],
        "xp": 10
    },
    {
        "id": 19, "phase": 1, "week": 4,
        "module": "SQL: JOIN",
        "title": "JOIN: соединение таблиц",
        "goal": "Освоить все виды JOIN — 90% реальных запросов.",
        "points": [
            "INNER JOIN — совпадающие строки",
            "LEFT/RIGHT JOIN — сохраняем одну сторону",
            "FULL OUTER JOIN, CROSS JOIN",
            "ON vs WHERE при JOIN"
        ],
        "resources": [
            {"type": "article", "title": "Postgres Pro: JOIN на русском", "url": "https://postgrespro.ru/docs/postgresql/16/queries-table-expressions", "lang": "ru"},
            {"type": "video", "title": "SQL JOIN визуально и просто (RU)", "url": "https://www.youtube.com/results?search_query=sql+join+объяснение+русский", "lang": "ru"}
        ],
        "tasks": [
            "Создайте orders и customers, свяжите",
            "Выведите заказы с именами клиентов через INNER, затем LEFT JOIN"
        ],
        "xp": 15
    },
    {
        "id": 20, "phase": 1, "week": 4,
        "module": "SQL: подзапросы и CTE",
        "title": "Подзапросы и CTE (WITH)",
        "goal": "Писать многошаговые запросы.",
        "points": [
            "Подзапросы в SELECT, WHERE (IN, EXISTS), FROM",
            "Коррелированные подзапросы",
            "CTE: WITH name AS (...) — читаемость",
            "EXISTS vs IN"
        ],
        "resources": [
            {"type": "article", "title": "Postgres Pro: WITH (CTE) на русском", "url": "https://postgrespro.ru/docs/postgresql/16/queries-with", "lang": "ru"},
            {"type": "article", "title": "Habr: CTE в PostgreSQL с примерами", "url": "https://habr.com/ru/search/?q=postgresql+CTE", "lang": "ru"}
        ],
        "tasks": [
            "Через CTE выведите клиентов с суммой заказов выше среднего",
            "Решите то же подзапросом — сравните читаемость"
        ],
        "xp": 15
    },
    {
        "id": 21, "phase": 1, "week": 4,
        "module": "SQL: оконные функции",
        "title": "Оконные функции",
        "goal": "Освоить ROW_NUMBER, RANK, LAG/LEAD, PARTITION BY — must-have для Junior.",
        "points": [
            "Оконные vs агрегатные: сохраняют строки",
            "OVER(PARTITION BY ... ORDER BY ...)",
            "ROW_NUMBER, RANK, DENSE_RANK",
            "LAG/LEAD, SUM() OVER"
        ],
        "resources": [
            {"type": "video", "title": "Оконные функции SQL на русском", "url": "https://www.youtube.com/results?search_query=оконные+функции+sql+postgresql+русский", "lang": "ru"},
            {"type": "article", "title": "Postgres Pro: window functions", "url": "https://postgrespro.ru/docs/postgresql/16/tutorial-window", "lang": "ru"}
        ],
        "tasks": [
            "Пронумеруйте заказы каждого клиента по дате (ROW_NUMBER OVER PARTITION)",
            "Выведите сумму заказов за предыдущий день через LAG"
        ],
        "xp": 20,
        "achievement": "SQL-ниндзя"
    },
    {
        "id": 22, "phase": 1, "week": 5,
        "module": "SQL: проектирование",
        "title": "Нормализация (1NF–3NF)",
        "goal": "Проектировать корректные схемы БД.",
        "points": [
            "1NF: атомарность, нет повторяющихся групп",
            "2NF: нет частичной зависимости от составного ключа",
            "3NF: нет транзитивной зависимости",
            "Когда нужна денормализация"
        ],
        "resources": [
            {"type": "video", "title": "Нормализация БД простыми словами (RU)", "url": "https://www.youtube.com/results?search_query=нормализация+баз+данных+1nf+2nf+3nf+русский", "lang": "ru"},
            {"type": "article", "title": "Habr: нормализация БД", "url": "https://habr.com/ru/search/?q=нормализация+баз+данных", "lang": "ru"}
        ],
        "tasks": [
            "Спроектируйте схему интернет-магазина в 3NF",
            "Проверьте схему на избыточность"
        ],
        "xp": 15
    },
    {
        "id": 23, "phase": 1, "week": 5,
        "module": "PostgreSQL: транзакции",
        "title": "Транзакции и ACID",
        "goal": "Понять надёжность БД — топ-вопрос собеседований.",
        "points": [
            "BEGIN/COMMIT/ROLLBACK",
            "ACID: Atomicity, Consistency, Isolation, Durability",
            "Уровни изоляции: Read Committed, Repeatable Read, Serializable",
            "Аномалии: грязное чтение, фантомы, non-repeatable read"
        ],
        "resources": [
            {"type": "article", "title": "Habr: транзакции и изоляция в PostgreSQL", "url": "https://habr.com/ru/search/?q=транзакции+изоляция+postgresql", "lang": "ru"},
            {"type": "article", "title": "Postgres Pro: изоляция транзакций", "url": "https://postgrespro.ru/docs/postgresql/16/transaction-iso", "lang": "ru"}
        ],
        "tasks": [
            "Сымитируйте грязное чтение: две сессии",
            "Проверьте Read Committed vs Repeatable Read"
        ],
        "xp": 20
    },
    {
        "id": 24, "phase": 1, "week": 5,
        "module": "PostgreSQL: индексы",
        "title": "Индексы, EXPLAIN ANALYZE",
        "goal": "Ускорять запросы индексами и читать планы выполнения.",
        "points": [
            "Зачем индексы: B-tree, ускорение поиска",
            "CREATE INDEX, UNIQUE, частичные индексы",
            "EXPLAIN / EXPLAIN ANALYZE: Seq Scan vs Index Scan",
            "Когда индекс не поможет (LIKE '%x%', функции)"
        ],
        "resources": [
            {"type": "article", "title": "Postgres Pro: индексы на русском", "url": "https://postgrespro.ru/docs/postgresql/16/indexes", "lang": "ru"},
            {"type": "video", "title": "EXPLAIN ANALYZE простыми словами (RU)", "url": "https://www.youtube.com/results?search_query=postgresql+explain+analyze+русский", "lang": "ru"}
        ],
        "tasks": [
            "Создайте таблицу на 1 млн строк, сравните запрос с индексом и без",
            "Посмотрите EXPLAIN ANALYZE, добавьте индекс"
        ],
        "xp": 20
    },
    {
        "id": 25, "phase": 1, "week": 5,
        "module": "SQL: мини-проект 3",
        "title": "Мини-проект 3: проектируем БД",
        "goal": "Спроектировать схему, наполнить и написать аналитические запросы.",
        "points": [
            "Выберите предметную область",
            "Спроектируйте 5+ таблиц с FK и связями",
            "Наполните тестовыми данными",
            "Напишите запросы с JOIN, GROUP BY, оконными функциями"
        ],
        "resources": [
            {"type": "article", "title": "Postgres Pro: примеры моделирования", "url": "https://postgrespro.ru/docs/postgresql/16/ddl", "lang": "ru"}
        ],
        "projectOptions": [
            {"title": "БД интернет-магазина", "desc": "users, products, categories, orders, order_items. Запросы: выручка по категориям, топ товаров, средний чек", "skills": "ER-модель, JOIN, оконные", "complexity": "средне"},
            {"title": "БД кинотеатра", "desc": "films, sessions, halls, tickets, clients. Запросы: заполняемость залов, выручка по фильмам", "skills": "модель, агрегаты", "complexity": "средне"},
            {"title": "БД соцсети", "desc": "users, posts, likes, comments, friendships. Запросы: лайки за день, топ авторов", "skills": "M:N связи, оконные", "complexity": "средне"},
            {"title": "БД учёта в колледже", "desc": "students, groups, subjects, grades, teachers. Запросы: средний балл по группам, рейтинг", "skills": "модель, JOIN", "complexity": "легко"}
        ],
        "tasks": [
            "Создайте схему и наполните данными",
            "Напишите 5 аналитических запросов (JOIN + GROUP BY + оконная)"
        ],
        "xp": 30
    },
    {
        "id": 26, "phase": 1, "week": 6,
        "module": "Python + БД: драйверы",
        "title": "psycopg/asyncpg, пулы соединений",
        "goal": "Подключить PostgreSQL из Python безопасно.",
        "points": [
            "psycopg3: connect, cursor, execute, fetchall",
            "Параметризованные запросы (%s) — защита от SQL-инъекций",
            "asyncpg — асинхронный драйвер",
            "Пул соединений: почему нельзя новое подключение на запрос"
        ],
        "resources": [
            {"type": "article", "title": "Psycopg 3 — документация", "url": "https://www.psycopg.org/psycopg3/docs/", "lang": "en"},
            {"type": "article", "title": "asyncpg — документация", "url": "https://magicstack.github.io/asyncpg/current/", "lang": "en"},
            {"type": "article", "title": "Habr: SQL-инъекции и как защититься", "url": "https://habr.com/ru/search/?q=sql+инъекции+защита", "lang": "ru"}
        ],
        "tasks": [
            "Напишите скрипт: подключение + вставка + выборка через psycopg",
            "Покажите, почему f-string с SQL опасен, а %s безопасен"
        ],
        "xp": 15
    },
    {
        "id": 27, "phase": 1, "week": 6,
        "module": "Python + БД: SQLAlchemy",
        "title": "SQLAlchemy 2.0: модели, сессии, CRUD",
        "goal": "Освоить главный ORM Python.",
        "points": [
            "SQLAlchemy Core vs ORM",
            "Declarative models: Mapped, mapped_column",
            "Engine и Session: select, add, commit, rollback",
            "Query API: select, where, order_by, limit"
        ],
        "resources": [
            {"type": "article", "title": "SQLAlchemy 2.0 — официальный туториал", "url": "https://docs.sqlalchemy.org/en/20/tutorial/", "lang": "en"},
            {"type": "video", "title": "SQLAlchemy 2.0 с нуля (RU)", "url": "https://www.youtube.com/results?search_query=sqlalchemy+2.0+русский+урок", "lang": "ru"}
        ],
        "tasks": [
            "Опишите модели User и Post, создайте таблицы",
            "Напишите CRUD-функции через сессию"
        ],
        "xp": 20
    },
    # ============ Блок 1.2: Python + БД ============
    {
        "id": 28, "phase": 1, "week": 6,
        "module": "Python + БД: отношения и миграции",
        "title": "Отношения, N+1, Alembic-миграции",
        "goal": "Работать со связями моделей и версионировать схему.",
        "points": [
            "relationship(), ForeignKey, back_populates",
            "Один-ко-многим, многие-ко-многим",
            "Проблема N+1 и её решение (selectinload, joinedload)",
            "Alembic: init, autogenerate, upgrade/downgrade"
        ],
        "resources": [
            {"type": "article", "title": "SQLAlchemy: Relationships API", "url": "https://docs.sqlalchemy.org/en/20/orm/relationships.html", "lang": "en"},
            {"type": "article", "title": "Alembic — документация", "url": "https://alembic.sqlalchemy.org/en/latest/tutorial.html", "lang": "en"},
            {"type": "article", "title": "Habr: проблема N+1 в ORM", "url": "https://habr.com/ru/search/?q=проблема+N%2B1+ORM", "lang": "ru"}
        ],
        "tasks": [
            "Создайте User(1)→Post(N), выведите посты пользователя",
            "Настройте Alembic, сделайте миграцию и откат"
        ],
        "xp": 20
    },
    {
        "id": 29, "phase": 1, "week": 6,
        "module": "Python + БД: мини-проект 4",
        "title": "Мини-проект 4: приложение на SQLAlchemy",
        "goal": "Собрать консольное приложение с БД через ORM.",
        "points": [
            "Выберите предметную область",
            "Модели со связями + миграции Alembic",
            "CRUD-функции через сессию",
            "Запросы с join/selectinload"
        ],
        "resources": [
            {"type": "article", "title": "SQLAlchemy 2.0 — туториал (модели и сессии)", "url": "https://docs.sqlalchemy.org/en/20/tutorial/", "lang": "en"}
        ],
        "projectOptions": [
            {"title": "Библиотека на SQLAlchemy", "desc": "Book↔Author (M:N), Book↔Reader (выдача), CRUD и поиск, Alembic", "skills": "ORM, M:N, миграции", "complexity": "средне"},
            {"title": "Магазин: каталог и корзина", "desc": "Product, Category, CartItem; CRUD товаров, добавление в корзину, сумма", "skills": "ORM, связи, агрегация", "complexity": "средне"},
            {"title": "Журнал оценок", "desc": "Student↔Subject (M:N), Grade; вывод среднего балла, рейтинга", "skills": "ORM, оконные по SQL", "complexity": "средне"},
            {"title": "Кинотеатр: расписание", "desc": "Film, Session, Hall; CRUD сеансов, билеты, заполняемость", "skills": "ORM, связи", "complexity": "средне"}
        ],
        "tasks": [
            "Реализуйте выбранное приложение с ORM",
            "Добавьте миграции Alembic и 3 аналитических запроса"
        ],
        "xp": 30
    },
    # ============ Блок 1.3: Как работает интернет ============
    {
        "id": 30, "phase": 1, "week": 6,
        "module": "Сети: основы",
        "title": "OSI, TCP/IP, UDP",
        "goal": "Понять, как данные путешествуют по сети.",
        "points": [
            "Модель OSI (7 уровней) vs TCP/IP (4 уровня)",
            "TCP: 3-way handshake, надёжность",
            "UDP: быстрый, без гарантий",
            "IP-адреса, порты, сокеты"
        ],
        "resources": [
            {"type": "article", "title": "Сети для самых маленьких (linkmeup) — курс с нуля", "url": "https://linkmeup.ru/blog/19.html", "lang": "ru"},
            {"type": "video", "title": "OSI и TCP/IP простыми словами (RU)", "url": "https://www.youtube.com/results?search_query=модель+osi+tcp+ip+объяснение+русский", "lang": "ru"}
        ],
        "tasks": [
            "Нарисуйте схему передачи HTTP-запроса по уровням",
            "Откройте TCP-соединение через python socket"
        ],
        "xp": 10
    },
    {
        "id": 31, "phase": 1, "week": 6,
        "module": "Сети: DNS",
        "title": "DNS: имена в адреса",
        "goal": "Разобраться в работе DNS.",
        "points": [
            "Что такое DNS: hostname → IP",
            "Записи: A, AAAA, CNAME, MX, TXT, NS",
            "Рекурсивные vs авторитативные серверы, TTL",
            "nslookup, dig"
        ],
        "resources": [
            {"type": "article", "title": "Habr: как работает DNS", "url": "https://habr.com/ru/search/?q=как+работает+DNS", "lang": "ru"},
            {"type": "video", "title": "DNS простыми словами (RU)", "url": "https://www.youtube.com/results?search_query=dns+как+работает+русский", "lang": "ru"}
        ],
        "tasks": [
            "Выполните dig google.com и разберите ответ",
            "Объясните, что произойдёт при смене A-записи"
        ],
        "xp": 10
    },
    {
        "id": 32, "phase": 1, "week": 7,
        "module": "Сети: HTTP",
        "title": "HTTP: методы, статусы, заголовки",
        "goal": "Разобрать HTTP-запрос и ответ насквозь.",
        "points": [
            "Структура запроса: метод, URI, версия, заголовки, тело",
            "Методы: GET, POST, PUT, PATCH, DELETE, идемпотентность",
            "Статусы: 1xx, 2xx, 3xx, 4xx, 5xx",
            "Заголовки: Content-Type, Accept, Authorization, Cache-Control"
        ],
        "resources": [
            {"type": "article", "title": "MDN (RU): HTTP — основы протокола", "url": "https://developer.mozilla.org/ru/docs/Web/HTTP", "lang": "ru"},
            {"type": "video", "title": "HTTP и статус-коды простыми словами (RU)", "url": "https://www.youtube.com/results?search_query=http+статус+коды+что+это+русский", "lang": "ru"}
        ],
        "tasks": [
            "Сделайте curl -v и разберите каждый заголовок ответа",
            "Составьте таблицу: какой метод для каких операций CRUD"
        ],
        "xp": 15
    },
    {
        "id": 33, "phase": 1, "week": 7,
        "module": "Сети: HTTPS",
        "title": "HTTPS/TLS",
        "goal": "Понять шифрование TLS и клиент-серверную архитектуру.",
        "points": [
            "Зачем HTTPS: конфиденциальность, целостность, аутентичность",
            "TLS handshake: симметричное + асимметричное шифрование",
            "Сертификаты и цепочка доверия",
            "Reverse Proxy, Load Balancer — первые понятия"
        ],
        "resources": [
            {"type": "article", "title": "Habr: как работает HTTPS/TLS", "url": "https://habr.com/ru/search/?q=как+работает+HTTPS+TLS", "lang": "ru"},
            {"type": "video", "title": "HTTPS и TLS за 15 минут (RU)", "url": "https://www.youtube.com/results?search_query=https+tls+как+работает+русский", "lang": "ru"}
        ],
        "tasks": [
            "Проверьте сертификат сайта в браузере, разберите цепочку",
            "Объясните, почему нельзя слать пароль по HTTP"
        ],
        "xp": 10
    },
    {
        "id": 34, "phase": 1, "week": 7,
        "module": "Сети: REST и WebSocket",
        "title": "REST, WebSocket, API-конвенции",
        "goal": "Связать HTTP с разработкой API.",
        "points": [
            "REST: ресурсы, методы, stateless, версионирование",
            "JSON API: структура, ошибки, пагинация",
            "WebSockets: двусторонняя связь, когда нужны",
            "gRPC/GraphQL — обзорно"
        ],
        "resources": [
            {"type": "article", "title": "Habr: REST API — принципы", "url": "https://habr.com/ru/search/?q=REST+API+принципы+json", "lang": "ru"},
            {"type": "video", "title": "REST API простыми словами (RU)", "url": "https://www.youtube.com/results?search_query=rest+api+что+это+русский", "lang": "ru"}
        ],
        "tasks": [
            "Спроектируйте REST API для блога (ресурсы, методы, статусы)",
            "Опишите сценарий, где нужен WebSocket"
        ],
        "xp": 10
    },
    # ============ Блок 1.4: Git ============
    {
        "id": 35, "phase": 1, "week": 7,
        "module": "Git: основы",
        "title": "Git: локальный репозиторий",
        "goal": "Уверенно делать коммиты.",
        "points": [
            "init, add, commit, status, log, diff",
            "Working → Staging → Repository",
            ".gitignore: venv, .env, __pycache__",
            "stash, restore, reset"
        ],
        "resources": [
            {"type": "course", "title": "Learn Git Branching — тренажёр (RU)", "url": "https://learngitbranching.js.org/?locale=ru_RU", "lang": "ru"},
            {"type": "article", "title": "git-scm: книга на русском", "url": "https://git-scm.com/book/ru/v2", "lang": "ru"}
        ],
        "tasks": [
            "Создайте репозиторий, сделайте 5 осмысленных коммитов",
            "Настройте .gitignore"
        ],
        "xp": 10
    },
    {
        "id": 36, "phase": 1, "week": 7,
        "module": "Git: ветки",
        "title": "Ветки, merge, rebase",
        "goal": "Освоить ветвление.",
        "points": [
            "git branch, checkout/switch",
            "merge: fast-forward и 3-way",
            "rebase vs merge — разница",
            "Конфликты и их разрешение"
        ],
        "resources": [
            {"type": "course", "title": "Learn Git Branching — ветки и rebase (RU)", "url": "https://learngitbranching.js.org/?locale=ru_RU", "lang": "ru"},
            {"type": "article", "title": "Habr: merge vs rebase", "url": "https://habr.com/ru/search/?q=git+merge+rebase+разница", "lang": "ru"}
        ],
        "tasks": [
            "Создайте ветку feature, влейте в main",
            "Сымитируйте и разрешите конфликт"
        ],
        "xp": 15
    },
    {
        "id": 37, "phase": 1, "week": 8,
        "module": "Git: GitHub",
        "title": "GitHub: remote, push, PR",
        "goal": "Освоить работу с удалённым репозиторием.",
        "points": [
            "remote add, push, pull, fetch",
            "SSH-ключи и аутентификация",
            "Pull Request: цикл code review",
            "Fork, clone"
        ],
        "resources": [
            {"type": "article", "title": "GitHub Docs (RU): Hello World / PR flow", "url": "https://docs.github.com/ru/get-started/quickstart/hello-world", "lang": "ru"},
            {"type": "article", "title": "GitHub Docs (RU): настройка SSH", "url": "https://docs.github.com/ru/authentication/connecting-to-github-with-ssh", "lang": "ru"}
        ],
        "tasks": [
            "Создайте репозиторий на GitHub, запушьте проект",
            "Сделайте ветку, PR и смержите"
        ],
        "xp": 10
    },
    {
        "id": 38, "phase": 1, "week": 8,
        "module": "Git: стратегии",
        "title": "Git-стратегии и командная работа",
        "goal": "Понять рабочие процессы команд.",
        "points": [
            "Git Flow: main, develop, feature, release, hotfix",
            "GitHub Flow: короткие ветки, PR в main",
            "Trunk-based",
            "Conventional Commits"
        ],
        "resources": [
            {"type": "article", "title": "Habr: Git Flow и другие модели ветвления", "url": "https://habr.com/ru/search/?q=git+flow+стратегии+ветвления", "lang": "ru"},
            {"type": "video", "title": "Git Flow за 10 минут (RU)", "url": "https://www.youtube.com/results?search_query=git+flow+что+это+русский", "lang": "ru"}
        ],
        "tasks": [
            "Нарисуйте схему Git Flow",
            "Перепишите 3 коммита в формате Conventional Commits"
        ],
        "xp": 10
    },
    {
        "id": 39, "phase": 1, "week": 8,
        "module": "Git: практика",
        "title": "Профиль GitHub и README",
        "goal": "Оформить профиль, который увидит рекрутер.",
        "points": [
            "README профиля: стек, контакты, чем занимаюсь",
            "README проектов: бейджи, скриншоты, инструкция запуска",
            "Пины лучших репозиториев",
            "Никаких секретов в репозиториях"
        ],
        "resources": [
            {"type": "article", "title": "Habr: как оформить GitHub-профиль", "url": "https://habr.com/ru/search/?q=оформление+github+профиль", "lang": "ru"},
            {"type": "article", "title": "Make a README (шаблоны)", "url": "https://www.makeareadme.com/", "lang": "en"}
        ],
        "tasks": [
            "Создайте README профиля",
            "Приведите в порядок 2-3 репозитория"
        ],
        "xp": 15
    },
    # ============ Блок 1.5: Фронтенд-основы ============
    {
        "id": 40, "phase": 1, "week": 8,
        "module": "Фронтенд: HTML/CSS",
        "title": "HTML + CSS: вёрстка",
        "goal": "Понимать и верстать простые страницы.",
        "points": [
            "Семантика: div, section, form, input",
            "Селекторы, классы, flex/grid",
            "DOM: как браузер строит страницу",
            "Responsive: media queries"
        ],
        "resources": [
            {"type": "article", "title": "MDN (RU): HTML — введение", "url": "https://developer.mozilla.org/ru/docs/Learn/HTML", "lang": "ru"},
            {"type": "article", "title": "MDN (RU): CSS — введение", "url": "https://developer.mozilla.org/ru/docs/Learn/CSS", "lang": "ru"}
        ],
        "tasks": [
            "Сверстайте форму логина (HTML+CSS)",
            "Разберите DOM-дерево через DevTools"
        ],
        "xp": 10
    },
    {
        "id": 41, "phase": 1, "week": 9,
        "module": "Фронтенд: JavaScript",
        "title": "JavaScript: основы",
        "goal": "Базово понимать JS — для работы с API.",
        "points": [
            "Переменные (let/const), типы",
            "Функции, стрелочные функции",
            "async/await, Promise",
            "События, DOM-манипуляции"
        ],
        "resources": [
            {"type": "article", "title": "Learn JavaScript (RU) — интерактивный учебник", "url": "https://learn.javascript.ru/", "lang": "ru"},
            {"type": "video", "title": "JavaScript с нуля (RU)", "url": "https://www.youtube.com/results?search_query=javascript+с+нуля+основы+русский", "lang": "ru"}
        ],
        "tasks": [
            "Напишите функцию, складывающую два числа, вызовите из консоли",
            "Напишите async-функцию с await fetch"
        ],
        "xp": 10
    },
    {
        "id": 42, "phase": 1, "week": 9,
        "module": "Фронтенд: DOM и fetch",
        "title": "DOM, fetch/AJAX",
        "goal": "Уметь запрашивать данные у своего API.",
        "points": [
            "querySelector, addEventListener",
            "fetch: GET, POST, обработка JSON",
            "Обработка ошибок и статусов",
            "localStorage для токена"
        ],
        "resources": [
            {"type": "article", "title": "MDN (RU): Using Fetch", "url": "https://developer.mozilla.org/ru/docs/Web/API/Fetch_API/Using_Fetch", "lang": "ru"},
            {"type": "article", "title": "Learn JavaScript (RU): промисы и fetch", "url": "https://learn.javascript.ru/fetch", "lang": "ru"}
        ],
        "tasks": [
            "Напишите fetch к своему API, выведите данные в div",
            "Реализуйте отправку POST с JSON-телом"
        ],
        "xp": 15
    },
    # ============ Блок 1.6: Flask ============
    {
        "id": 47, "phase": 1, "week": 10,
        "module": "Flask: основы",
        "title": "Flask: маршруты, WSGI",
        "goal": "Понять, что происходит 'под капотом' веб-фреймворка.",
        "points": [
            "Минимальное приложение: route, request/response",
            "Маршрутизация: <int:id>, методы",
            "Что такое WSGI",
            "JSON-ответы (jsonify)"
        ],
        "resources": [
            {"type": "article", "title": "Flask: официальный туториал (EN)", "url": "https://flask.palletsprojects.com/en/stable/tutorial/", "lang": "en"},
            {"type": "video", "title": "Flask с нуля на русском", "url": "https://www.youtube.com/results?search_query=flask+с+нуля+русский+урок", "lang": "ru"}
        ],
        "tasks": [
            "Напишите Flask-приложение с 3 маршрутами",
            "Верните JSON через jsonify"
        ],
        "xp": 10
    },
    {
        "id": 48, "phase": 1, "week": 10,
        "module": "Flask: формы и БД",
        "title": "Flask: формы, сессии, подключение БД",
        "goal": "Связать HTTP, пользователя и данные.",
        "points": [
            "POST-формы, query-параметры",
            "Сессии: подписанная cookie",
            "SQLAlchemy в Flask",
            "app.config"
        ],
        "resources": [
            {"type": "article", "title": "Flask: Quickstart (request, session)", "url": "https://flask.palletsprojects.com/en/stable/quickstart/", "lang": "en"},
            {"type": "article", "title": "Flask-SQLAlchemy: документация", "url": "https://flask-sqlalchemy.palletsprojects.com/", "lang": "en"}
        ],
        "tasks": [
            "Добавьте форму логина и сессию",
            "Подключите SQLAlchemy и сохраняйте пользователей"
        ],
        "xp": 10
    },
    {
        "id": 49, "phase": 1, "week": 10,
        "module": "Flask: мини-проект 6",
        "title": "Мини-проект 6: TODO на Flask",
        "goal": "Собрать полноценное мини-приложение «веб без магии».",
        "points": [
            "Выберите вариант проекта",
            "CRUD + БД + шаблоны Jinja2",
            "Формы и валидация",
            "Деплой на localhost + README"
        ],
        "resources": [
            {"type": "article", "title": "Flask: туториал «Блог» (EN)", "url": "https://flask.palletsprojects.com/en/stable/tutorial/", "lang": "en"}
        ],
        "projectOptions": [
            {"title": "TODO-приложение", "desc": "Список задач, добавление, отметка выполнения, удаление; хранение в БД", "skills": "Flask, формы, Jinja2", "complexity": "легко"},
            {"title": "Гостевая книга", "desc": "Отзывы/записи с именем и текстом, список + форма добавления", "skills": "Flask, Jinja2, БД", "complexity": "легко"},
            {"title": "Конвертер валют с историей", "desc": "Страница конвертации + история запросов в таблице", "skills": "Flask, внешний API", "complexity": "средне"},
            {"title": "Анкета-опрос", "desc": "Форма с вопросами, сохранение ответов в БД, страница со статистикой", "skills": "Flask, формы, агрегаты", "complexity": "средне"}
        ],
        "tasks": [
            "Реализуйте выбранное приложение",
            "Запушьте на GitHub с README"
        ],
        "xp": 25,
        "achievement": "Понял веб без магии"
    },
]