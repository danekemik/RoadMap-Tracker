# -*- coding: utf-8 -*-
# ФАЗА 0: Основа Python (дни 1-15)

DAYS_P0 = [
    # ============ Блок 0.0: Linux и терминал ============
    {
        "id": 1, "phase": 0, "week": 1,
        "module": "Linux: терминал и bash",
        "title": "Терминал, файлы, команды",
        "goal": "Уверенно работать в командной строке — это база для Docker, деплоя и всего дальнейшего курса.",
        "points": [
            "Навигация: pwd, ls, cd, mkdir, rm, cp, mv, touch",
            "Чтение файлов: cat, less, head, tail, grep, wc",
            "Перенаправление и конвейеры: >, >>, |, tee",
            "Права доступа: chmod, chown, umask",
            "Псевдонимы и PATH: alias, export, ~/.bashrc"
        ],
        "resources": [
            {"type": "video", "title": "Linux для начинающих: базовые команды (RU)", "url": "https://www.youtube.com/results?search_query=linux+терминал+основы+bash+русский", "lang": "ru"},
            {"type": "article", "title": "Bash Guide: основные команды (EN)", "url": "https://www.gnu.org/software/bash/manual/", "lang": "en"}
        ],
        "tasks": [
            "Создайте дерево каталогов и переименуйте файлы командами",
            "Найдите все файлы с расширением .py через find/grep"
        ],
        "xp": 10,
        "achievement": "Первый день — поехали!"
    },
    {
        "id": 2, "phase": 0, "week": 1,
        "module": "Linux: терминал и bash",
        "title": "Процессы, окружение, .env",
        "goal": "Понимать процессы, переменные окружения и уметь хранить секреты вне кода.",
        "points": [
            "Процессы: ps, top, kill, jobs, фоновые процессы",
            "Переменные окружения: env, export, $VAR",
            "Метасимволы и globbing: *, ?, [...]",
            "Файлы .env и их роль в приложениях",
            "Владелец процесса и права (setuid, sudo)"
        ],
        "resources": [
            {"type": "article", "title": "Переменные окружения в Linux (RU)", "url": "https://habr.com/ru/search/?q=переменные+окружения+linux+bash", "lang": "ru"},
            {"type": "article", "title": "12 Factor App: конфигурация через окружение (EN)", "url": "https://12factor.net/config", "lang": "en"}
        ],
        "tasks": [
            "Запустите процесс в фоне, найдите его через ps и остановите через kill",
            "Создайте .env с SECRET_KEY и прочитайте его из скрипта"
        ],
        "xp": 10
    },
    {
        "id": 3, "phase": 0, "week": 1,
        "module": "Linux: терминал и bash",
        "title": "Скрипты bash и полезные утилиты",
        "goal": "Автоматизировать рутину: писать простые скрипты и комбинировать утилиты.",
        "points": [
            "Структура скрипта: shebang, chmod +x, exit-коды",
            "Переменные и аргументы в bash: $1, $@, $?",
            "Условные операторы: if, for, while",
            "Утилиты: curl, wget, tar, zip, diff, sort, uniq",
            "curl для проверки HTTP API"
        ],
        "resources": [
            {"type": "video", "title": "Bash-скрипты для начинающих (RU)", "url": "https://www.youtube.com/results?search_query=bash+скрипты+с+нуля+русский", "lang": "ru"},
            {"type": "article", "title": "Bash scripting cheatsheet (EN)", "url": "https://devhints.io/bash", "lang": "en"}
        ],
        "tasks": [
            "Напишите скрипт, архивирующий каталог с датой в имени",
            "Проверьте HTTP-ответ API через curl -i"
        ],
        "xp": 10
    },
    # ============ Блок 0.1: Ядро языка ============
    {
        "id": 1, "phase": 0, "week": 1,
        "module": "Python: ядро языка",
        "title": "Переменные, типы, изменяемость, память",
        "goal": "Разобраться, как Python хранит данные, и понять разницу между изменяемыми и неизменяемыми типами.",
        "points": [
            "Всё в Python — объект: id(), type(), == vs is",
            "Изменяемые (list, dict, set) vs неизменяемые (tuple, str, int, frozenset)",
            "Передача объектов по ссылке: почему изменяемые аргументы опасны в функциях",
            "Изменяемые объекты НЕ должны быть дефолтными аргументами",
            "Сборка мусора: ссылочный подсчёт + циклический GC"
        ],
        "resources": [
            {"type": "video", "title": "Python: ссылки и мутабельность (Selfedu)", "url": "https://www.youtube.com/results?search_query=python+мутабельность+переменные+selfedu", "lang": "ru"},
            {"type": "article", "title": "Python docs RU: встроенные типы", "url": "https://docs.python.org/ru/3/library/stdtypes.html", "lang": "ru"},
            {"type": "article", "title": "Pythontutor — визуализатор выполнения кода", "url": "https://pythontutor.ru/", "lang": "ru"}
        ],
        "tasks": [
            "Напишите функцию, которая мутирует список-аргумент, и объясните поведение",
            "Создайте класс, переопределив __eq__, покажите разницу == и is"
        ],
        "xp": 10,
        "achievement": "Первый день — поехали!"
    },
    {
        "id": 2, "phase": 0, "week": 1,
        "module": "Python: ядро языка",
        "title": "Коллекции: list, tuple, dict, set, строки, срезы",
        "goal": "Свободно работать с коллекциями и строками — 80% кода на Python.",
        "points": [
            "list: append, extend, insert, remove, pop, count, index",
            "tuple: неизменяемость, распаковка, tuple unpacking",
            "dict: get, setdefault, update, keys/values/items, дефолтные значения",
            "set: add, union, intersection, difference",
            "Строки: f-строки, методы split/join/strip/replace, срезы [start:stop:step]"
        ],
        "resources": [
            {"type": "video", "title": "Списки и словари в Python (Selfedu)", "url": "https://www.youtube.com/results?search_query=python+списки+словари+selfedu", "lang": "ru"},
            {"type": "article", "title": "Python docs RU: методы списков", "url": "https://docs.python.org/ru/3/tutorial/datastructures.html", "lang": "ru"},
            {"type": "course", "title": "Pythontutor — задачи на коллекции", "url": "https://pythontutor.ru/lessons/lists/", "lang": "ru"}
        ],
        "tasks": [
            "Напишите функцию, которая разворачивает список срезом и без среза",
            "Посчитайте частоту слов в строке через dict (defaultdict не использовать)"
        ],
        "xp": 10
    },
    {
        "id": 3, "phase": 0, "week": 1,
        "module": "Python: ядро языка",
        "title": "Функции: *args/**kwargs, LEGB, lambda, замыкания",
        "goal": "Довести работу с функциями до автоматизма — это база для декораторов и API.",
        "points": [
            "Аргументы: позиционные, keyword-only (*), только позиционные (/)",
            "*args / **kwargs и распаковка (*list, **dict)",
            "Правило LEGB: Local → Enclosing → Global → Built-in",
            "lambda: анонимные функции, где используют (sorted key, map/filter)",
            "Замыкания: функция, запоминающая внешнее состояние"
        ],
        "resources": [
            {"type": "video", "title": "Функции и LEGB в Python (Selfedu)", "url": "https://www.youtube.com/results?search_query=python+функции+legb+замыкания+selfedu", "lang": "ru"},
            {"type": "article", "title": "Python docs RU: определения функций", "url": "https://docs.python.org/ru/3/tutorial/controlflow.html#defining-functions", "lang": "ru"},
            {"type": "article", "title": "Habr: *args и **kwargs на примерах", "url": "https://habr.com/ru/search/?q=python+args+kwargs", "lang": "ru"}
        ],
        "tasks": [
            "Напишите функцию с *args и **kwargs, которая логирует все вызовы",
            "Напишите замыкание counter(), которое считает вызовы"
        ],
        "xp": 10
    },
    {
        "id": 4, "phase": 0, "week": 1,
        "module": "Python: ядро языка",
        "title": "Декораторы",
        "goal": "Понять, как работают декораторы, и писать свои — они повсюду во фреймворках.",
        "points": [
            "Декоратор = функция, оборачивающая функцию",
            "@functools.wraps — сохраняем __name__ и __doc__",
            "Декораторы с аргументами (двойная обёртка)",
            "Классы-декораторы (__call__)",
            "Примеры из реальности: @app.get, @login_required, @lru_cache"
        ],
        "resources": [
            {"type": "video", "title": "Декораторы в Python (Selfedu)", "url": "https://www.youtube.com/results?search_query=python+декораторы+selfedu", "lang": "ru"},
            {"type": "article", "title": "Habr: декораторы Python на пальцах", "url": "https://habr.com/ru/search/?q=декораторы+python", "lang": "ru"}
        ],
        "tasks": [
            "Напишите декоратор, замеряющий время выполнения",
            "Напишите декоратор retry(max_attempts=3) с повторным вызовом при исключении"
        ],
        "xp": 15,
        "achievement": "Мастер декораторов"
    },
    {
        "id": 5, "phase": 0, "week": 1,
        "module": "Python: ядро языка",
        "title": "Генераторы, итераторы, контекстные менеджеры",
        "goal": "Освоить ленивые вычисления и безопасную работу с ресурсами.",
        "points": [
            "Протокол итерации: __iter__/__next__, StopIteration",
            "Генераторы: yield, yield from, ленивость",
            "itertools: chain, groupby, product, combinations",
            "with и __enter__/__exit__",
            "contextlib.contextmanager — генератор как менеджер контекста"
        ],
        "resources": [
            {"type": "video", "title": "Генераторы и yield (Selfedu)", "url": "https://www.youtube.com/results?search_query=python+генераторы+yield+selfedu", "lang": "ru"},
            {"type": "video", "title": "Контекстные менеджеры и with (Selfedu)", "url": "https://www.youtube.com/results?search_query=python+контекстные+менеджеры+with", "lang": "ru"},
            {"type": "article", "title": "Python docs RU: итераторы и генераторы", "url": "https://docs.python.org/ru/3/tutorial/classes.html#iterators", "lang": "ru"}
        ],
        "tasks": [
            "Напишите генератор чисел Фибоначчи через yield",
            "Напишите contextmanager, перехватывающий и логирующий исключения"
        ],
        "xp": 15
    },
    {
        "id": 6, "phase": 0, "week": 1,
        "module": "Python: мини-проект 1",
        "title": "Мини-проект 1: выбираем и делаем",
        "goal": "Применить всё из блока 0.1: функции, декораторы, генераторы, коллекции.",
        "points": [
            "Выберите 1 из предложенных проектов",
            "Разбейте задачу на функции",
            "Примените декоратор для логирования/таймера",
            "Сделайте код читаемым и типизированным"
        ],
        "resources": [
            {"type": "article", "title": "PEP 8 — руководство по стилю кода (RU)", "url": "https://peps.python.org/pep-0008/#introduction", "lang": "ru"},
            {"type": "video", "title": "Как писать чистый код на Python (RU)", "url": "https://www.youtube.com/results?search_query=чистый+код+python", "lang": "ru"}
        ],
        "projectOptions": [
            {"title": "Консольный TODO-менеджер", "desc": "Хранение задач в файле JSON, добавление/удаление/выполнение, вывод списка с генератором-пагинацией", "skills": "функции, JSON, генераторы", "complexity": "средне"},
            {"title": "Конвертер валют", "desc": "Загрузка курсов с публичного API, конвертация, кэширование в файле, история операций", "skills": "httpx/requests, JSON, декоратор кэша", "complexity": "средне"},
            {"title": "Генератор паролей и чекер", "desc": "Генерация надёжных паролей + проверка их силы по правилам, сохранение в файл", "skills": "random, функции, валидация", "complexity": "легко"},
            {"title": "Анализ лог-файла", "desc": "Чтение большого лога генератором построчно, подсчёт ошибок по типам через dict, вывод топ-10", "skills": "генераторы, dict, regex", "complexity": "средне"}
        ],
        "tasks": [
            "Выберите проект и реализуйте его",
            "Добавьте декоратор времени выполнения и аннотации типов"
        ],
        "xp": 25
    },
    # ============ Блок 0.2: ООП и типизация ============
    {
        "id": 7, "phase": 0, "week": 2,
        "module": "Python: ООП",
        "title": "Классы, инкапсуляция, @property, @classmethod",
        "goal": "Писать классы правильно: инкапсуляция, свойства, методы разных типов.",
        "points": [
            "Класс и объект, __init__, self",
            "Инкапсуляция: _protected, __private (name mangling)",
            "@property / @setter — контролируемый доступ к атрибутам",
            "@classmethod vs @staticmethod — когда что",
            "__repr__ / __str__ — отображение объекта"
        ],
        "resources": [
            {"type": "video", "title": "Классы и ООП в Python (Selfedu)", "url": "https://www.youtube.com/results?search_query=python+классы+ооп+property+selfedu", "lang": "ru"},
            {"type": "course", "title": "Stepik: ООП на Python (Сергей Балакирев)", "url": "https://stepik.org/course/116336/syllabus", "lang": "ru"}
        ],
        "tasks": [
            "Реализуйте класс BankAccount: @property balance, __balance приватный, deposit/withdraw",
            "Добавьте @classmethod from_string и @staticmethod validate_iban"
        ],
        "xp": 15
    },
    {
        "id": 8, "phase": 0, "week": 2,
        "module": "Python: ООП",
        "title": "Наследование, MRO, super, магические методы",
        "goal": "Понять иерархии классов и расширение поведения через наследование.",
        "points": [
            "Наследование: class Child(Parent), override",
            "MRO (порядок разрешения методов) и множественное наследование",
            "super() — вызов родительского метода",
            "Магические методы: __eq__, __hash__, __lt__, __call__, __len__",
            "Композиция vs наследование: что выбрать"
        ],
        "resources": [
            {"type": "video", "title": "Наследование и super() (Selfedu)", "url": "https://www.youtube.com/results?search_query=python+наследование+mro+super+selfedu", "lang": "ru"},
            {"type": "article", "title": "Habr: MRO и множественное наследование", "url": "https://habr.com/ru/search/?q=python+MRO+наследование", "lang": "ru"}
        ],
        "tasks": [
            "Создайте иерархию Фигура→Круг/Прямоугольник с методом area()",
            "Реализуйте класс, поддерживающий сравнение через __lt__/__eq__"
        ],
        "xp": 15
    },
    {
        "id": 9, "phase": 0, "week": 2,
        "module": "Python: типизация и данные",
        "title": "dataclasses, typing, pydantic v2",
        "goal": "Описать данные строго: это напрямую ведёт к Pydantic в FastAPI.",
        "points": [
            "dataclasses: fields, default_factory, slots, frozen, __post_init__",
            "typing: Optional, Union, Literal, TypeVar, Protocol",
            "Аннотации и mypy/pyright",
            "pydantic v2: BaseModel, Field, validators",
            "Pydantic vs dataclass: валидация и сериализация"
        ],
        "resources": [
            {"type": "video", "title": "Dataclasses в Python (Selfedu)", "url": "https://www.youtube.com/results?search_query=python+dataclasses+selfedu", "lang": "ru"},
            {"type": "article", "title": "Pydantic v2: модели и валидаторы (RU-раздел)", "url": "https://docs.pydantic.dev/latest/concepts/models/", "lang": "en"}
        ],
        "tasks": [
            "Опишите модель User в pydantic: имя, email, возраст + проверка email",
            "Перепишите на dataclass с валидацией в __post_init__"
        ],
        "xp": 15
    },
    {
        "id": 10, "phase": 0, "week": 2,
        "module": "Python: ООП и паттерны",
        "title": "SOLID и паттерны проектирования",
        "goal": "Понять принципы SOLID и 3 самых частых паттерна — это спрашивают на собеседованиях.",
        "points": [
            "SOLID: S (одна ответственность), O (открыт/закрыт), L, I, D",
            "Dependency Injection — базовое понятие для FastAPI Depends",
            "Singleton: единственный экземпляр",
            "Factory: создание объектов по параметру",
            "Strategy: выбор алгоритма на лету"
        ],
        "resources": [
            {"type": "video", "title": "SOLID простыми словами на Python (RU)", "url": "https://www.youtube.com/results?search_query=solid+python+русский", "lang": "ru"},
            {"type": "article", "title": "Refactoring Guru RU: паттерны проектирования", "url": "https://refactoring.guru/ru/design-patterns", "lang": "ru"}
        ],
        "tasks": [
            "Разбейте 'жирный' класс OrderService по принципу S",
            "Реализуйте Singleton через __new__"
        ],
        "xp": 20,
        "achievement": "Архитектор SOLID"
    },
    {
        "id": 11, "phase": 0, "week": 2,
        "module": "Python: мини-проект 2",
        "title": "Мини-проект 2: выбираем и делаем",
        "goal": "Применить ООП, типизацию, SOLID в небольшом проекте.",
        "points": [
            "Выберите 1 из 4 проектов",
            "Спроектируйте классы и их связи",
            "Добавьте типизацию и валидацию (pydantic или dataclass)",
            "Соблюдайте принцип единственной ответственности"
        ],
        "resources": [
            {"type": "article", "title": "Refactoring Guru RU: SOLID", "url": "https://refactoring.guru/ru/solid", "lang": "ru"}
        ],
        "projectOptions": [
            {"title": "Электронная библиотека", "desc": "Классы Book/Library/Reader, поиск, выдача и возврат книг, валидация через pydantic", "skills": "ООП, pydantic, SOLID", "complexity": "средне"},
            {"title": "Каталог товаров", "desc": "Товары, категории, поиск по цене, корзина; dataclasses + сортировки", "skills": "dataclasses, классы, коллекции", "complexity": "средне"},
            {"title": "Планировщик задач (ООП)", "desc": "Task с приоритетом/дедлайном, сортировка по важности, статусы, переиспользование с мини-проекта 1", "skills": "ООП, enum, сортировка", "complexity": "средне"},
            {"title": "Консольная бухгалтерия", "desc": "Счета, транзакции, категории расходов, отчёт по месяцам — всё через классы", "skills": "ООП, datetime, агрегация", "complexity": "средне"}
        ],
        "tasks": [
            "Реализуйте выбранный проект с классами и типизацией",
            "Проверьте код на соблюдение SOLID"
        ],
        "xp": 25
    },
    # ============ Блок 0.3: Алгоритмы ============
    {
        "id": 12, "phase": 0, "week": 3,
        "module": "Алгоритмы: сложность",
        "title": "Big O: оценка сложности",
        "goal": "Научиться оценивать время и память алгоритмов — базовый вопрос на скрининге.",
        "points": [
            "O(1), O(log n), O(n), O(n log n), O(n²)",
            "Лучший/средний/худший случай",
            "Сложность операций с коллекциями Python",
            "Правила суммирования и умножения"
        ],
        "resources": [
            {"type": "video", "title": "Big O нотация простыми словами (RU)", "url": "https://www.youtube.com/results?search_query=big+o+нотация+объяснение+русский", "lang": "ru"},
            {"type": "article", "title": "Habr: сложность алгоритмов для начинающих", "url": "https://habr.com/ru/search/?q=сложность+алгоритмов+big+o", "lang": "ru"}
        ],
        "tasks": [
            "Определите сложность 5 функций (вложенные циклы, словари, sorted)",
            "Объясните: почему dict.get() быстрее линейного поиска в списке"
        ],
        "xp": 10
    },
    {
        "id": 13, "phase": 0, "week": 3,
        "module": "Алгоритмы: структуры данных",
        "title": "Стек, очередь, хэш-таблицы (задачи)",
        "goal": "Понять линейные структуры и решить типовые задачи.",
        "points": [
            "Стек (LIFO) и очередь (FIFO), deque в Python",
            "Хэш-таблица: устройство dict/set, коллизии",
            "Паттерны задач: подсчёт частот, поиск пар, дедупликация",
            "Связные списки (концептуально)"
        ],
        "resources": [
            {"type": "practice", "title": "LeetCode: 20. Valid Parentheses", "url": "https://leetcode.com/problems/valid-parentheses/", "lang": "en"},
            {"type": "practice", "title": "LeetCode: 1. Two Sum", "url": "https://leetcode.com/problems/two-sum/", "lang": "en"},
            {"type": "article", "title": "Habr: структуры данных простыми словами", "url": "https://habr.com/ru/search/?q=структуры+данных+стек+очередь", "lang": "ru"}
        ],
        "tasks": [
            "Решите Valid Parentheses через стек",
            "Решите Two Sum за O(n) через dict"
        ],
        "xp": 10
    },
    {
        "id": 14, "phase": 0, "week": 3,
        "module": "Алгоритмы: деревья и поиск",
        "title": "Деревья, DFS/BFS, бинарный поиск (задачи)",
        "goal": "Понять деревья, обходы, рекурсию и сортировки — частая тема собеседований.",
        "points": [
            "Дерево: root, leafs; двоичное дерево",
            "Обходы: preorder/inorder/postorder (DFS), level-order (BFS)",
            "Рекурсия и её глубина",
            "Бинарный поиск по данным",
            "Сортировки: quicksort, mergesort, их сложность O(n log n)"
        ],
        "resources": [
            {"type": "practice", "title": "LeetCode: 104. Maximum Depth of Binary Tree", "url": "https://leetcode.com/problems/maximum-depth-of-binary-tree/", "lang": "en"},
            {"type": "practice", "title": "LeetCode: 226. Invert Binary Tree", "url": "https://leetcode.com/problems/invert-binary-tree/", "lang": "en"},
            {"type": "video", "title": "Деревья и обходы (Тимофей Хирьянов)", "url": "https://www.youtube.com/results?search_query=хирьянов+деревья+алгоритмы", "lang": "ru"},
            {"type": "video", "title": "Quicksort и Mergesort за 15 минут", "url": "https://www.youtube.com/results?search_query=quicksort+mergesort+русский+разбор", "lang": "ru"}
        ],
        "tasks": [
            "Решите Maximum Depth of Binary Tree рекурсивно",
            "Решите Invert Binary Tree",
            "Реализуйте quicksort и mergesort, сравните на случайном массиве"
        ],
        "xp": 15,
        "achievement": "Покоритель деревьев"
    },
    {
        "id": 15, "phase": 0, "week": 3,
        "module": "Алгоритмы: практика",
        "title": "Практика и ревизия блока 0",
        "goal": "Закрепить Python и алгоритмы комплексными задачами.",
        "points": [
            "5-7 задач на смесь: декораторы, генераторы, dict, ООП",
            "Повторить Big O",
            "Разобрать свои решения из LeetCode",
            "Пройти тест по всему блоку"
        ],
        "resources": [
            {"type": "practice", "title": "LeetCode: подборка Easy для разогрева", "url": "https://leetcode.com/problemset/?difficulty=EASY", "lang": "en"}
        ],
        "tasks": [
            "Решите 5 задач с таймером",
            "Пройдите тест по блоку (в разделе самопроверки)"
        ],
        "xp": 25
    },
]