const ROADMAP = {
 "startDate": "2026-08-17",
 "meta": {
  "title": "Роадмап Python Backend Junior",
  "totalDays": 98,
  "totalXp": 1355,
  "phases": {
   "0": {
    "name": "Python",
    "days": "17–31 августа",
    "note": "Python углублённо + алгоритмы, 2-3 ч/день"
   },
   "1": {
    "name": "Семестр",
    "days": "1 сентября – 4 октября",
    "note": "SQL, Git, веб, Flask, 1-2 ч/день"
   },
   "2": {
    "name": "FastAPI + инструменты",
    "days": "5 октября – 24 ноября",
    "note": "FastAPI, тесты, Docker, безопасность, очереди"
   },
   "3": {
    "name": "Карьера",
    "days": "25 ноября – 31 декабря",
    "note": "Резюме, собеседования, трудоустройство"
   }
  }
 },
 "days": [
  {
   "id": 1,
   "phase": 0,
   "week": 1,
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
    {
     "type": "video",
     "title": "Linux для начинающих: базовые команды (RU)",
     "url": "https://www.youtube.com/results?search_query=linux+терминал+основы+bash+русский",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Bash Guide: основные команды (EN)",
     "url": "https://www.gnu.org/software/bash/manual/",
     "lang": "en"
    }
   ],
   "tasks": [
    "Создайте дерево каталогов и переименуйте файлы командами",
    "Найдите все файлы с расширением .py через find/grep"
   ],
   "xp": 10,
   "achievement": "Первый день — поехали!",
   "minutes": 89
  },
  {
   "id": 2,
   "phase": 0,
   "week": 1,
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
    {
     "type": "article",
     "title": "Переменные окружения в Linux (RU)",
     "url": "https://habr.com/ru/search/?q=переменные+окружения+linux+bash",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "12 Factor App: конфигурация через окружение (EN)",
     "url": "https://12factor.net/config",
     "lang": "en"
    }
   ],
   "tasks": [
    "Запустите процесс в фоне, найдите его через ps и остановите через kill",
    "Создайте .env с SECRET_KEY и прочитайте его из скрипта"
   ],
   "xp": 10,
   "minutes": 96
  },
  {
   "id": 3,
   "phase": 0,
   "week": 1,
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
    {
     "type": "video",
     "title": "Bash-скрипты для начинающих (RU)",
     "url": "https://www.youtube.com/results?search_query=bash+скрипты+с+нуля+русский",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Bash scripting cheatsheet (EN)",
     "url": "https://devhints.io/bash",
     "lang": "en"
    }
   ],
   "tasks": [
    "Напишите скрипт, архивирующий каталог с датой в имени",
    "Проверьте HTTP-ответ API через curl -i"
   ],
   "xp": 10,
   "minutes": 89
  },
  {
   "id": 4,
   "phase": 0,
   "week": 1,
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
    {
     "type": "video",
     "title": "Python: ссылки и мутабельность (Selfedu)",
     "url": "https://www.youtube.com/results?search_query=python+мутабельность+переменные+selfedu",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Python docs RU: встроенные типы",
     "url": "https://docs.python.org/ru/3/library/stdtypes.html",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Pythontutor — визуализатор выполнения кода",
     "url": "https://pythontutor.ru/",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Напишите функцию, которая мутирует список-аргумент, и объясните поведение",
    "Создайте класс, переопределив __eq__, покажите разницу == и is"
   ],
   "xp": 10,
   "achievement": "Первый день — поехали!",
   "minutes": 111
  },
  {
   "id": 5,
   "phase": 0,
   "week": 1,
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
    {
     "type": "video",
     "title": "Списки и словари в Python (Selfedu)",
     "url": "https://www.youtube.com/results?search_query=python+списки+словари+selfedu",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Python docs RU: методы списков",
     "url": "https://docs.python.org/ru/3/tutorial/datastructures.html",
     "lang": "ru"
    },
    {
     "type": "course",
     "title": "Pythontutor — задачи на коллекции",
     "url": "https://pythontutor.ru/lessons/lists/",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Напишите функцию, которая разворачивает список срезом и без среза",
    "Посчитайте частоту слов в строке через dict (defaultdict не использовать)"
   ],
   "xp": 10,
   "minutes": 115
  },
  {
   "id": 6,
   "phase": 0,
   "week": 1,
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
    {
     "type": "video",
     "title": "Функции и LEGB в Python (Selfedu)",
     "url": "https://www.youtube.com/results?search_query=python+функции+legb+замыкания+selfedu",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Python docs RU: определения функций",
     "url": "https://docs.python.org/ru/3/tutorial/controlflow.html#defining-functions",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Habr: *args и **kwargs на примерах",
     "url": "https://habr.com/ru/search/?q=python+args+kwargs",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Напишите функцию с *args и **kwargs, которая логирует все вызовы",
    "Напишите замыкание counter(), которое считает вызовы"
   ],
   "xp": 10,
   "minutes": 111
  },
  {
   "id": 7,
   "phase": 0,
   "week": 1,
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
    {
     "type": "video",
     "title": "Декораторы в Python (Selfedu)",
     "url": "https://www.youtube.com/results?search_query=python+декораторы+selfedu",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Habr: декораторы Python на пальцах",
     "url": "https://habr.com/ru/search/?q=декораторы+python",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Напишите декоратор, замеряющий время выполнения",
    "Напишите декоратор retry(max_attempts=3) с повторным вызовом при исключении"
   ],
   "xp": 15,
   "achievement": "Мастер декораторов",
   "minutes": 89
  },
  {
   "id": 8,
   "phase": 0,
   "week": 1,
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
    {
     "type": "video",
     "title": "Генераторы и yield (Selfedu)",
     "url": "https://www.youtube.com/results?search_query=python+генераторы+yield+selfedu",
     "lang": "ru"
    },
    {
     "type": "video",
     "title": "Контекстные менеджеры и with (Selfedu)",
     "url": "https://www.youtube.com/results?search_query=python+контекстные+менеджеры+with",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Python docs RU: итераторы и генераторы",
     "url": "https://docs.python.org/ru/3/tutorial/classes.html#iterators",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Напишите генератор чисел Фибоначчи через yield",
    "Напишите contextmanager, перехватывающий и логирующий исключения"
   ],
   "xp": 15,
   "minutes": 104
  },
  {
   "id": 9,
   "phase": 0,
   "week": 2,
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
    {
     "type": "video",
     "title": "Классы и ООП в Python (Selfedu)",
     "url": "https://www.youtube.com/results?search_query=python+классы+ооп+property+selfedu",
     "lang": "ru"
    },
    {
     "type": "course",
     "title": "Stepik: ООП на Python (Сергей Балакирев)",
     "url": "https://stepik.org/course/116336/syllabus",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Реализуйте класс BankAccount: @property balance, __balance приватный, deposit/withdraw",
    "Добавьте @classmethod from_string и @staticmethod validate_iban"
   ],
   "xp": 15,
   "minutes": 93
  },
  {
   "id": 10,
   "phase": 0,
   "week": 2,
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
    {
     "type": "video",
     "title": "Наследование и super() (Selfedu)",
     "url": "https://www.youtube.com/results?search_query=python+наследование+mro+super+selfedu",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Habr: MRO и множественное наследование",
     "url": "https://habr.com/ru/search/?q=python+MRO+наследование",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Создайте иерархию Фигура→Круг/Прямоугольник с методом area()",
    "Реализуйте класс, поддерживающий сравнение через __lt__/__eq__"
   ],
   "xp": 15,
   "minutes": 89
  },
  {
   "id": 11,
   "phase": 0,
   "week": 2,
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
    {
     "type": "video",
     "title": "Dataclasses в Python (Selfedu)",
     "url": "https://www.youtube.com/results?search_query=python+dataclasses+selfedu",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Pydantic v2: модели и валидаторы (RU-раздел)",
     "url": "https://docs.pydantic.dev/latest/concepts/models/",
     "lang": "en"
    }
   ],
   "tasks": [
    "Опишите модель User в pydantic: имя, email, возраст + проверка email",
    "Перепишите на dataclass с валидацией в __post_init__"
   ],
   "xp": 15,
   "minutes": 89
  },
  {
   "id": 12,
   "phase": 0,
   "week": 2,
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
    {
     "type": "video",
     "title": "SOLID простыми словами на Python (RU)",
     "url": "https://www.youtube.com/results?search_query=solid+python+русский",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Refactoring Guru RU: паттерны проектирования",
     "url": "https://refactoring.guru/ru/design-patterns",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Разбейте 'жирный' класс OrderService по принципу S",
    "Реализуйте Singleton через __new__"
   ],
   "xp": 20,
   "achievement": "Архитектор SOLID",
   "minutes": 89
  },
  {
   "id": 13,
   "phase": 0,
   "week": 3,
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
    {
     "type": "video",
     "title": "Big O нотация простыми словами (RU)",
     "url": "https://www.youtube.com/results?search_query=big+o+нотация+объяснение+русский",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Habr: сложность алгоритмов для начинающих",
     "url": "https://habr.com/ru/search/?q=сложность+алгоритмов+big+o",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Определите сложность 5 функций (вложенные циклы, словари, sorted)",
    "Объясните: почему dict.get() быстрее линейного поиска в списке"
   ],
   "xp": 10,
   "minutes": 89
  },
  {
   "id": 14,
   "phase": 0,
   "week": 3,
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
    {
     "type": "practice",
     "title": "LeetCode: 20. Valid Parentheses",
     "url": "https://leetcode.com/problems/valid-parentheses/",
     "lang": "en"
    },
    {
     "type": "practice",
     "title": "LeetCode: 1. Two Sum",
     "url": "https://leetcode.com/problems/two-sum/",
     "lang": "en"
    },
    {
     "type": "article",
     "title": "Habr: структуры данных простыми словами",
     "url": "https://habr.com/ru/search/?q=структуры+данных+стек+очередь",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Решите Valid Parentheses через стек",
    "Решите Two Sum за O(n) через dict"
   ],
   "xp": 10,
   "minutes": 110
  },
  {
   "id": 15,
   "phase": 0,
   "week": 3,
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
    {
     "type": "practice",
     "title": "LeetCode: 104. Maximum Depth of Binary Tree",
     "url": "https://leetcode.com/problems/maximum-depth-of-binary-tree/",
     "lang": "en"
    },
    {
     "type": "practice",
     "title": "LeetCode: 226. Invert Binary Tree",
     "url": "https://leetcode.com/problems/invert-binary-tree/",
     "lang": "en"
    },
    {
     "type": "video",
     "title": "Деревья и обходы (Тимофей Хирьянов)",
     "url": "https://www.youtube.com/results?search_query=хирьянов+деревья+алгоритмы",
     "lang": "ru"
    },
    {
     "type": "video",
     "title": "Quicksort и Mergesort за 15 минут",
     "url": "https://www.youtube.com/results?search_query=quicksort+mergesort+русский+разбор",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Решите Maximum Depth of Binary Tree рекурсивно",
    "Решите Invert Binary Tree",
    "Реализуйте quicksort и mergesort, сравните на случайном массиве"
   ],
   "xp": 15,
   "achievement": "Покоритель деревьев",
   "minutes": 128
  },
  {
   "id": 16,
   "phase": 0,
   "week": 3,
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
    {
     "type": "practice",
     "title": "LeetCode: подборка Easy для разогрева",
     "url": "https://leetcode.com/problemset/?difficulty=EASY",
     "lang": "en"
    }
   ],
   "tasks": [
    "Решите 5 задач с таймером",
    "Пройдите тест по блоку (в разделе самопроверки)"
   ],
   "xp": 25,
   "minutes": 70
  },
  {
   "id": 17,
   "phase": 1,
   "week": 4,
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
    {
     "type": "course",
     "title": "SQL Academy — интерактивный тренажёр (RU)",
     "url": "https://sql-academy.org/ru",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Postgres Pro: документация на русском",
     "url": "https://postgrespro.ru/docs/postgresql",
     "lang": "ru"
    },
    {
     "type": "video",
     "title": "Установка PostgreSQL и первые запросы (RU)",
     "url": "https://www.youtube.com/results?search_query=установка+postgresql+первые+запросы",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Установите PostgreSQL, создайте БД test",
    "Создайте таблицу users (id, name, email) и вставьте 5 строк"
   ],
   "xp": 10,
   "minutes": 115
  },
  {
   "id": 18,
   "phase": 1,
   "week": 4,
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
    {
     "type": "course",
     "title": "SQL Academy: тренажёр (SELECT/WHERE)",
     "url": "https://sql-academy.org/ru/trainer",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Postgres Pro: SELECT с примерами",
     "url": "https://postgrespro.ru/docs/postgresql/16/sql-select",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Выберите пользователей старше 18, отсортируйте по имени",
    "Найдите email, содержащие 'mail' через LIKE"
   ],
   "xp": 10,
   "minutes": 100
  },
  {
   "id": 19,
   "phase": 1,
   "week": 4,
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
    {
     "type": "course",
     "title": "SQL Academy: GROUP BY и агрегаты",
     "url": "https://sql-academy.org/ru/trainer",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Postgres Pro: агрегатные функции",
     "url": "https://postgrespro.ru/docs/postgresql/16/functions-aggregate",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Посчитайте средний возраст по городам",
    "Выведите города, где больше 3 пользователей (HAVING)"
   ],
   "xp": 10,
   "minutes": 100
  },
  {
   "id": 20,
   "phase": 1,
   "week": 4,
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
    {
     "type": "article",
     "title": "Postgres Pro: JOIN на русском",
     "url": "https://postgrespro.ru/docs/postgresql/16/queries-table-expressions",
     "lang": "ru"
    },
    {
     "type": "video",
     "title": "SQL JOIN визуально и просто (RU)",
     "url": "https://www.youtube.com/results?search_query=sql+join+объяснение+русский",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Создайте orders и customers, свяжите",
    "Выведите заказы с именами клиентов через INNER, затем LEFT JOIN"
   ],
   "xp": 15,
   "minutes": 89
  },
  {
   "id": 21,
   "phase": 1,
   "week": 4,
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
    {
     "type": "article",
     "title": "Postgres Pro: WITH (CTE) на русском",
     "url": "https://postgrespro.ru/docs/postgresql/16/queries-with",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Habr: CTE в PostgreSQL с примерами",
     "url": "https://habr.com/ru/search/?q=postgresql+CTE",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Через CTE выведите клиентов с суммой заказов выше среднего",
    "Решите то же подзапросом — сравните читаемость"
   ],
   "xp": 15,
   "minutes": 96
  },
  {
   "id": 22,
   "phase": 1,
   "week": 4,
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
    {
     "type": "video",
     "title": "Оконные функции SQL на русском",
     "url": "https://www.youtube.com/results?search_query=оконные+функции+sql+postgresql+русский",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Postgres Pro: window functions",
     "url": "https://postgrespro.ru/docs/postgresql/16/tutorial-window",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Пронумеруйте заказы каждого клиента по дате (ROW_NUMBER OVER PARTITION)",
    "Выведите сумму заказов за предыдущий день через LAG"
   ],
   "xp": 20,
   "achievement": "SQL-ниндзя",
   "minutes": 89
  },
  {
   "id": 23,
   "phase": 1,
   "week": 5,
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
    {
     "type": "video",
     "title": "Нормализация БД простыми словами (RU)",
     "url": "https://www.youtube.com/results?search_query=нормализация+баз+данных+1nf+2nf+3nf+русский",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Habr: нормализация БД",
     "url": "https://habr.com/ru/search/?q=нормализация+баз+данных",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Спроектируйте схему интернет-магазина в 3NF",
    "Проверьте схему на избыточность"
   ],
   "xp": 15,
   "minutes": 89
  },
  {
   "id": 24,
   "phase": 1,
   "week": 5,
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
    {
     "type": "article",
     "title": "Habr: транзакции и изоляция в PostgreSQL",
     "url": "https://habr.com/ru/search/?q=транзакции+изоляция+postgresql",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Postgres Pro: изоляция транзакций",
     "url": "https://postgrespro.ru/docs/postgresql/16/transaction-iso",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Сымитируйте грязное чтение: две сессии",
    "Проверьте Read Committed vs Repeatable Read"
   ],
   "xp": 20,
   "minutes": 96
  },
  {
   "id": 25,
   "phase": 1,
   "week": 5,
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
    {
     "type": "article",
     "title": "Postgres Pro: индексы на русском",
     "url": "https://postgrespro.ru/docs/postgresql/16/indexes",
     "lang": "ru"
    },
    {
     "type": "video",
     "title": "EXPLAIN ANALYZE простыми словами (RU)",
     "url": "https://www.youtube.com/results?search_query=postgresql+explain+analyze+русский",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Создайте таблицу на 1 млн строк, сравните запрос с индексом и без",
    "Посмотрите EXPLAIN ANALYZE, добавьте индекс"
   ],
   "xp": 20,
   "minutes": 89
  },
  {
   "id": 26,
   "phase": 1,
   "week": 6,
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
    {
     "type": "article",
     "title": "Psycopg 3 — документация",
     "url": "https://www.psycopg.org/psycopg3/docs/",
     "lang": "en"
    },
    {
     "type": "article",
     "title": "asyncpg — документация",
     "url": "https://magicstack.github.io/asyncpg/current/",
     "lang": "en"
    },
    {
     "type": "article",
     "title": "Habr: SQL-инъекции и как защититься",
     "url": "https://habr.com/ru/search/?q=sql+инъекции+защита",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Напишите скрипт: подключение + вставка + выборка через psycopg",
    "Покажите, почему f-string с SQL опасен, а %s безопасен"
   ],
   "xp": 15,
   "minutes": 118
  },
  {
   "id": 27,
   "phase": 1,
   "week": 6,
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
    {
     "type": "article",
     "title": "SQLAlchemy 2.0 — официальный туториал",
     "url": "https://docs.sqlalchemy.org/en/20/tutorial/",
     "lang": "en"
    },
    {
     "type": "video",
     "title": "SQLAlchemy 2.0 с нуля (RU)",
     "url": "https://www.youtube.com/results?search_query=sqlalchemy+2.0+русский+урок",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Опишите модели User и Post, создайте таблицы",
    "Напишите CRUD-функции через сессию"
   ],
   "xp": 20,
   "minutes": 89
  },
  {
   "id": 28,
   "phase": 1,
   "week": 6,
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
    {
     "type": "article",
     "title": "SQLAlchemy: Relationships API",
     "url": "https://docs.sqlalchemy.org/en/20/orm/relationships.html",
     "lang": "en"
    },
    {
     "type": "article",
     "title": "Alembic — документация",
     "url": "https://alembic.sqlalchemy.org/en/latest/tutorial.html",
     "lang": "en"
    },
    {
     "type": "article",
     "title": "Habr: проблема N+1 в ORM",
     "url": "https://habr.com/ru/search/?q=проблема+N%2B1+ORM",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Создайте User(1)→Post(N), выведите посты пользователя",
    "Настройте Alembic, сделайте миграцию и откат"
   ],
   "xp": 20,
   "minutes": 118
  },
  {
   "id": 29,
   "phase": 1,
   "week": 6,
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
    {
     "type": "article",
     "title": "Сети для самых маленьких (linkmeup) — курс с нуля",
     "url": "https://linkmeup.ru/blog/19.html",
     "lang": "ru"
    },
    {
     "type": "video",
     "title": "OSI и TCP/IP простыми словами (RU)",
     "url": "https://www.youtube.com/results?search_query=модель+osi+tcp+ip+объяснение+русский",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Нарисуйте схему передачи HTTP-запроса по уровням",
    "Откройте TCP-соединение через python socket"
   ],
   "xp": 10,
   "minutes": 89
  },
  {
   "id": 30,
   "phase": 1,
   "week": 6,
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
    {
     "type": "article",
     "title": "Habr: как работает DNS",
     "url": "https://habr.com/ru/search/?q=как+работает+DNS",
     "lang": "ru"
    },
    {
     "type": "video",
     "title": "DNS простыми словами (RU)",
     "url": "https://www.youtube.com/results?search_query=dns+как+работает+русский",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Выполните dig google.com и разберите ответ",
    "Объясните, что произойдёт при смене A-записи"
   ],
   "xp": 10,
   "minutes": 89
  },
  {
   "id": 31,
   "phase": 1,
   "week": 7,
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
    {
     "type": "article",
     "title": "MDN (RU): HTTP — основы протокола",
     "url": "https://developer.mozilla.org/ru/docs/Web/HTTP",
     "lang": "ru"
    },
    {
     "type": "video",
     "title": "HTTP и статус-коды простыми словами (RU)",
     "url": "https://www.youtube.com/results?search_query=http+статус+коды+что+это+русский",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Сделайте curl -v и разберите каждый заголовок ответа",
    "Составьте таблицу: какой метод для каких операций CRUD"
   ],
   "xp": 15,
   "minutes": 89
  },
  {
   "id": 32,
   "phase": 1,
   "week": 7,
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
    {
     "type": "article",
     "title": "Habr: как работает HTTPS/TLS",
     "url": "https://habr.com/ru/search/?q=как+работает+HTTPS+TLS",
     "lang": "ru"
    },
    {
     "type": "video",
     "title": "HTTPS и TLS за 15 минут (RU)",
     "url": "https://www.youtube.com/results?search_query=https+tls+как+работает+русский",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Проверьте сертификат сайта в браузере, разберите цепочку",
    "Объясните, почему нельзя слать пароль по HTTP"
   ],
   "xp": 10,
   "minutes": 89
  },
  {
   "id": 33,
   "phase": 1,
   "week": 7,
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
    {
     "type": "article",
     "title": "Habr: REST API — принципы",
     "url": "https://habr.com/ru/search/?q=REST+API+принципы+json",
     "lang": "ru"
    },
    {
     "type": "video",
     "title": "REST API простыми словами (RU)",
     "url": "https://www.youtube.com/results?search_query=rest+api+что+это+русский",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Спроектируйте REST API для блога (ресурсы, методы, статусы)",
    "Опишите сценарий, где нужен WebSocket"
   ],
   "xp": 10,
   "minutes": 89
  },
  {
   "id": 34,
   "phase": 1,
   "week": 7,
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
    {
     "type": "course",
     "title": "Learn Git Branching — тренажёр (RU)",
     "url": "https://learngitbranching.js.org/?locale=ru_RU",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "git-scm: книга на русском",
     "url": "https://git-scm.com/book/ru/v2",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Создайте репозиторий, сделайте 5 осмысленных коммитов",
    "Настройте .gitignore"
   ],
   "xp": 10,
   "minutes": 100
  },
  {
   "id": 35,
   "phase": 1,
   "week": 7,
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
    {
     "type": "course",
     "title": "Learn Git Branching — ветки и rebase (RU)",
     "url": "https://learngitbranching.js.org/?locale=ru_RU",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Habr: merge vs rebase",
     "url": "https://habr.com/ru/search/?q=git+merge+rebase+разница",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Создайте ветку feature, влейте в main",
    "Сымитируйте и разрешите конфликт"
   ],
   "xp": 15,
   "minutes": 100
  },
  {
   "id": 36,
   "phase": 1,
   "week": 8,
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
    {
     "type": "article",
     "title": "GitHub Docs (RU): Hello World / PR flow",
     "url": "https://docs.github.com/ru/get-started/quickstart/hello-world",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "GitHub Docs (RU): настройка SSH",
     "url": "https://docs.github.com/ru/authentication/connecting-to-github-with-ssh",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Создайте репозиторий на GitHub, запушьте проект",
    "Сделайте ветку, PR и смержите"
   ],
   "xp": 10,
   "minutes": 96
  },
  {
   "id": 37,
   "phase": 1,
   "week": 8,
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
    {
     "type": "article",
     "title": "Habr: Git Flow и другие модели ветвления",
     "url": "https://habr.com/ru/search/?q=git+flow+стратегии+ветвления",
     "lang": "ru"
    },
    {
     "type": "video",
     "title": "Git Flow за 10 минут (RU)",
     "url": "https://www.youtube.com/results?search_query=git+flow+что+это+русский",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Нарисуйте схему Git Flow",
    "Перепишите 3 коммита в формате Conventional Commits"
   ],
   "xp": 10,
   "minutes": 89
  },
  {
   "id": 38,
   "phase": 1,
   "week": 8,
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
    {
     "type": "article",
     "title": "Habr: как оформить GitHub-профиль",
     "url": "https://habr.com/ru/search/?q=оформление+github+профиль",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Make a README (шаблоны)",
     "url": "https://www.makeareadme.com/",
     "lang": "en"
    }
   ],
   "tasks": [
    "Создайте README профиля",
    "Приведите в порядок 2-3 репозитория"
   ],
   "xp": 15,
   "minutes": 96
  },
  {
   "id": 39,
   "phase": 1,
   "week": 8,
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
    {
     "type": "article",
     "title": "MDN (RU): HTML — введение",
     "url": "https://developer.mozilla.org/ru/docs/Learn/HTML",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "MDN (RU): CSS — введение",
     "url": "https://developer.mozilla.org/ru/docs/Learn/CSS",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Сверстайте форму логина (HTML+CSS)",
    "Разберите DOM-дерево через DevTools"
   ],
   "xp": 10,
   "minutes": 96
  },
  {
   "id": 40,
   "phase": 1,
   "week": 9,
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
    {
     "type": "article",
     "title": "Learn JavaScript (RU) — интерактивный учебник",
     "url": "https://learn.javascript.ru/",
     "lang": "ru"
    },
    {
     "type": "video",
     "title": "JavaScript с нуля (RU)",
     "url": "https://www.youtube.com/results?search_query=javascript+с+нуля+основы+русский",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Напишите функцию, складывающую два числа, вызовите из консоли",
    "Напишите async-функцию с await fetch"
   ],
   "xp": 10,
   "minutes": 89
  },
  {
   "id": 41,
   "phase": 1,
   "week": 9,
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
    {
     "type": "article",
     "title": "MDN (RU): Using Fetch",
     "url": "https://developer.mozilla.org/ru/docs/Web/API/Fetch_API/Using_Fetch",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Learn JavaScript (RU): промисы и fetch",
     "url": "https://learn.javascript.ru/fetch",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Напишите fetch к своему API, выведите данные в div",
    "Реализуйте отправку POST с JSON-телом"
   ],
   "xp": 15,
   "minutes": 96
  },
  {
   "id": 42,
   "phase": 1,
   "week": 10,
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
    {
     "type": "article",
     "title": "Flask: официальный туториал (EN)",
     "url": "https://flask.palletsprojects.com/en/stable/tutorial/",
     "lang": "en"
    },
    {
     "type": "video",
     "title": "Flask с нуля на русском",
     "url": "https://www.youtube.com/results?search_query=flask+с+нуля+русский+урок",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Напишите Flask-приложение с 3 маршрутами",
    "Верните JSON через jsonify"
   ],
   "xp": 10,
   "minutes": 89
  },
  {
   "id": 43,
   "phase": 1,
   "week": 10,
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
    {
     "type": "article",
     "title": "Flask: Quickstart (request, session)",
     "url": "https://flask.palletsprojects.com/en/stable/quickstart/",
     "lang": "en"
    },
    {
     "type": "article",
     "title": "Flask-SQLAlchemy: документация",
     "url": "https://flask-sqlalchemy.palletsprojects.com/",
     "lang": "en"
    }
   ],
   "tasks": [
    "Добавьте форму логина и сессию",
    "Подключите SQLAlchemy и сохраняйте пользователей"
   ],
   "xp": 10,
   "minutes": 96
  },
  {
   "id": 44,
   "phase": 2,
   "week": 10,
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
    {
     "type": "article",
     "title": "Microsoft REST API guidelines (EN)",
     "url": "https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design",
     "lang": "en"
    },
    {
     "type": "video",
     "title": "Проектирование REST API (RU)",
     "url": "https://www.youtube.com/results?search_query=проектирование+rest+api+с+нуля+русский",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Спроектируйте API для блога: список ресурсов, методов и статусов",
    "Обоснуйте выбор методов и кодов ответов"
   ],
   "xp": 10,
   "minutes": 89
  },
  {
   "id": 45,
   "phase": 2,
   "week": 10,
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
    {
     "type": "article",
     "title": "OpenAPI Specification (EN)",
     "url": "https://swagger.io/specification/",
     "lang": "en"
    },
    {
     "type": "article",
     "title": "FastAPI: дополнительные возможности (RU)",
     "url": "https://fastapi.tiangolo.com/ru/tutorial/extra-models/",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Опишите схему ответа и ошибки для POST /users",
    "Настройте теги и описание в /docs"
   ],
   "xp": 10,
   "minutes": 96
  },
  {
   "id": 46,
   "phase": 2,
   "week": 10,
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
    {
     "type": "article",
     "title": "FastAPI: официальный туториал (RU)",
     "url": "https://fastapi.tiangolo.com/ru/tutorial/",
     "lang": "ru"
    },
    {
     "type": "video",
     "title": "FastAPI с нуля на русском",
     "url": "https://www.youtube.com/results?search_query=fastapi+с+нуля+русский+урок",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Создайте приложение с GET /health и POST /echo",
    "Откройте /docs и потренируйтесь"
   ],
   "xp": 10,
   "minutes": 89
  },
  {
   "id": 47,
   "phase": 2,
   "week": 10,
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
    {
     "type": "article",
     "title": "FastAPI: Path Parameters (RU)",
     "url": "https://fastapi.tiangolo.com/ru/tutorial/path-params/",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "FastAPI: Query Parameters (RU)",
     "url": "https://fastapi.tiangolo.com/ru/tutorial/query-params/",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Создайте endpoint с path, query и body параметрами",
    "Добавьте Enum и ограничения (gt, le)"
   ],
   "xp": 10,
   "minutes": 96
  },
  {
   "id": 48,
   "phase": 2,
   "week": 10,
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
    {
     "type": "article",
     "title": "Pydantic v2: поля и валидаторы",
     "url": "https://docs.pydantic.dev/latest/concepts/fields/",
     "lang": "en"
    },
    {
     "type": "article",
     "title": "FastAPI: response_model (RU)",
     "url": "https://fastapi.tiangolo.com/ru/tutorial/response-model/",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Опишите UserCreate (name, email, password) с валидацией",
    "Сделайте response_model без пароля"
   ],
   "xp": 15,
   "minutes": 96
  },
  {
   "id": 49,
   "phase": 2,
   "week": 11,
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
    {
     "type": "article",
     "title": "FastAPI: Dependencies (RU)",
     "url": "https://fastapi.tiangolo.com/ru/tutorial/dependencies/",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "FastAPI: структура больших приложений (RU)",
     "url": "https://fastapi.tiangolo.com/ru/tutorial/bigger-applications/",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Реструктурируйте проект: роутеры + общая зависимость",
    "Напишите зависимость get_db-заглушку"
   ],
   "xp": 15,
   "minutes": 96
  },
  {
   "id": 50,
   "phase": 2,
   "week": 11,
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
    {
     "type": "article",
     "title": "FastAPI: SQL Databases (RU)",
     "url": "https://fastapi.tiangolo.com/ru/tutorial/sql-databases/",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "SQLAlchemy: работа с сессиями",
     "url": "https://docs.sqlalchemy.org/en/20/orm/session_basics.html",
     "lang": "en"
    }
   ],
   "tasks": [
    "Соберите CRUD для модели User через SQLAlchemy",
    "Настройте get_db с закрытием сессии"
   ],
   "xp": 20,
   "minutes": 96
  },
  {
   "id": 51,
   "phase": 2,
   "week": 11,
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
    {
     "type": "article",
     "title": "FastAPI: Pydantic + SQLAlchemy отношения",
     "url": "https://fastapi.tiangolo.com/ru/tutorial/sql-databases/",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Habr: пагинация в REST API",
     "url": "https://habr.com/ru/search/?q=пагинация+REST+API",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Добавьте связь User→Post, endpoint /users/{id}/posts",
    "Реализуйте limit/offset пагинацию с total"
   ],
   "xp": 15,
   "minutes": 96
  },
  {
   "id": 52,
   "phase": 2,
   "week": 11,
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
    {
     "type": "article",
     "title": "FastAPI: Handling Errors (RU)",
     "url": "https://fastapi.tiangolo.com/ru/tutorial/handling-errors/",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Google API: дизайн ошибок (RU-перевод есть в статьях Habr)",
     "url": "https://habr.com/ru/search/?q=формат+ошибок+REST+API",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Добавьте обработчик 404 с JSON-ответом",
    "Напишите обработчик ValidationError с деталями"
   ],
   "xp": 10,
   "minutes": 96
  },
  {
   "id": 53,
   "phase": 2,
   "week": 12,
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
    {
     "type": "article",
     "title": "FastAPI: CORS (RU)",
     "url": "https://fastapi.tiangolo.com/ru/tutorial/cors/",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "MDN (RU): CORS",
     "url": "https://developer.mozilla.org/ru/docs/Web/HTTP/CORS",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Настройте CORS для localhost:3000",
    "Напишите middleware с X-Request-Id"
   ],
   "xp": 10,
   "minutes": 96
  },
  {
   "id": 54,
   "phase": 2,
   "week": 12,
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
    {
     "type": "article",
     "title": "Habr: хэширование паролей правильно",
     "url": "https://habr.com/ru/search/?q=хэширование+паролей+bcrypt",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "OWASP: хранение паролей (EN)",
     "url": "https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html",
     "lang": "en"
    }
   ],
   "tasks": [
    "Напишите hash_password/verify_password на bcrypt",
    "Интегрируйте в регистрацию"
   ],
   "xp": 10,
   "minutes": 96
  },
  {
   "id": 55,
   "phase": 2,
   "week": 12,
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
    {
     "type": "article",
     "title": "FastAPI: OAuth2 с JWT (RU)",
     "url": "https://fastapi.tiangolo.com/ru/tutorial/security/oauth2-jwt/",
     "lang": "ru"
    },
    {
     "type": "video",
     "title": "JWT простыми словами (RU)",
     "url": "https://www.youtube.com/results?search_query=jwt+что+это+русский",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Реализуйте /auth/login → access token",
    "Защитите /me зависимостью get_current_user"
   ],
   "xp": 20,
   "minutes": 89
  },
  {
   "id": 56,
   "phase": 2,
   "week": 12,
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
    {
     "type": "article",
     "title": "Habr: refresh-токены правильно",
     "url": "https://habr.com/ru/search/?q=refresh+токены+jwt",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Auth0: Refresh Tokens (EN)",
     "url": "https://auth0.com/learn/refresh-tokens",
     "lang": "en"
    }
   ],
   "tasks": [
    "Добавьте refresh-токен и /auth/refresh",
    "Реализуйте logout с инвалидацией"
   ],
   "xp": 20,
   "minutes": 96
  },
  {
   "id": 57,
   "phase": 2,
   "week": 12,
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
    {
     "type": "article",
     "title": "FastAPI: зависимости с проверками ролей",
     "url": "https://fastapi.tiangolo.com/ru/tutorial/security/",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Habr: RBAC в веб-приложениях",
     "url": "https://habr.com/ru/search/?q=RBAC+роли+доступ",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Добавьте роли и защитите админ-эндпоинт",
    "Реализуйте проверку владельца ресурса"
   ],
   "xp": 15,
   "minutes": 96
  },
  {
   "id": 58,
   "phase": 2,
   "week": 13,
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
    {
     "type": "article",
     "title": "FastAPI: Background Tasks (RU)",
     "url": "https://fastapi.tiangolo.com/ru/tutorial/background-tasks/",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "FastAPI: Request Files (RU)",
     "url": "https://fastapi.tiangolo.com/ru/tutorial/request-files/",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Добавьте фоновую задачу 'уведомление' после регистрации",
    "Реализуйте endpoint загрузки аватара"
   ],
   "xp": 10,
   "minutes": 96
  },
  {
   "id": 59,
   "phase": 2,
   "week": 13,
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
    {
     "type": "article",
     "title": "FastAPI: WebSockets (RU)",
     "url": "https://fastapi.tiangolo.com/ru/advanced/websockets/",
     "lang": "ru"
    },
    {
     "type": "video",
     "title": "WebSocket + FastAPI чат (RU)",
     "url": "https://www.youtube.com/results?search_query=fastapi+websocket+чат+русский",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Реализуйте WebSocket-эхо и клиент на JS",
    "Добавьте рассылку сообщений"
   ],
   "xp": 15,
   "minutes": 89
  },
  {
   "id": 60,
   "phase": 2,
   "week": 13,
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
    {
     "type": "article",
     "title": "Habr: Redis для начинающих",
     "url": "https://habr.com/ru/search/?q=redis+для+начинающих",
     "lang": "ru"
    },
    {
     "type": "video",
     "title": "Redis простыми словами (RU)",
     "url": "https://www.youtube.com/results?search_query=redis+что+это+русский",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Запустите Redis, сохраните и прочитайте значения",
    "Используйте expire и increment"
   ],
   "xp": 15,
   "minutes": 89
  },
  {
   "id": 61,
   "phase": 2,
   "week": 13,
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
    {
     "type": "article",
     "title": "Habr: кэширование и паттерны кэша",
     "url": "https://habr.com/ru/search/?q=кэширование+redis+паттерны+cache+aside",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Redis: caching patterns (EN)",
     "url": "https://redis.io/docs/latest/develop/use/caching/",
     "lang": "en"
    }
   ],
   "tasks": [
    "Закэшируйте GET-эндпоинт на 60 сек",
    "Инвалидируйте кэш при изменении данных"
   ],
   "xp": 15,
   "minutes": 96
  },
  {
   "id": 62,
   "phase": 2,
   "week": 14,
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
    {
     "type": "article",
     "title": "Python docs (RU): логирование",
     "url": "https://docs.python.org/ru/3/howto/logging.html",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Habr: логирование в Python правильно",
     "url": "https://habr.com/ru/search/?q=логирование+python+structlog",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Настройте логирование запросов (метод, путь, статус, время)",
    "Подключите Sentry (free tier)"
   ],
   "xp": 10,
   "minutes": 96
  },
  {
   "id": 63,
   "phase": 2,
   "week": 14,
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
    {
     "type": "video",
     "title": "GIL и потоки в Python (EN)",
     "url": "https://www.youtube.com/results?search_query=python+gil+threads+explained",
     "lang": "en"
    },
    {
     "type": "article",
     "title": "Real Python: Async IO in Python",
     "url": "https://realpython.com/async-io-python/",
     "lang": "en"
    }
   ],
   "tasks": [
    "Напишите скрипт с 10 HTTP-запросами синхронно и посчитайте время",
    "Перепишите на asyncio и сравните скорость"
   ],
   "xp": 10,
   "minutes": 89
  },
  {
   "id": 64,
   "phase": 2,
   "week": 14,
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
    {
     "type": "article",
     "title": "Python docs: asyncio — базовые API",
     "url": "https://docs.python.org/3/library/asyncio-task.html",
     "lang": "en"
    },
    {
     "type": "video",
     "title": "Async/await в Python за 20 минут",
     "url": "https://www.youtube.com/results?search_query=python+asyncio+await+tutorial+русский",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Напишите функцию, запускающую 5 корутин через gather",
    "Добавьте таймаут и обработку исключений"
   ],
   "xp": 15,
   "minutes": 89
  },
  {
   "id": 65,
   "phase": 2,
   "week": 14,
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
    {
     "type": "article",
     "title": "Python docs: Synchronization Primitives",
     "url": "https://docs.python.org/3/library/asyncio-sync.html",
     "lang": "en"
    },
    {
     "type": "article",
     "title": "httpx: Async Client — документация",
     "url": "https://www.python-httpx.org/async/",
     "lang": "en"
    }
   ],
   "tasks": [
    "Реализуйте парсер с Semaphore(5) на 100 URL",
    "Напишите клиент к публичному API с ретраями и таймаутами"
   ],
   "xp": 15,
   "minutes": 96
  },
  {
   "id": 66,
   "phase": 2,
   "week": 14,
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
    {
     "type": "article",
     "title": "SQLAlchemy: AsyncIO Support",
     "url": "https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html",
     "lang": "en"
    },
    {
     "type": "article",
     "title": "FastAPI: async БД (RU)",
     "url": "https://fastapi.tiangolo.com/ru/advanced/async-sql-databases/",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Переведите get_db и модели на async",
    "Убедитесь, что всё работает"
   ],
   "xp": 20,
   "minutes": 96
  },
  {
   "id": 67,
   "phase": 2,
   "week": 14,
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
    {
     "type": "article",
     "title": "slowapi: документация",
     "url": "https://slowapi.readthedocs.io/en/latest/",
     "lang": "en"
    },
    {
     "type": "article",
     "title": "Habr: rate limiting в API",
     "url": "https://habr.com/ru/search/?q=rate+limiting+api",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Подключите slowapi, ограничьте логин",
    "Реализуйте блокировку после 5 попыток"
   ],
   "xp": 15,
   "minutes": 96
  },
  {
   "id": 68,
   "phase": 2,
   "week": 15,
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
    {
     "type": "article",
     "title": "Habr: best practices FastAPI",
     "url": "https://habr.com/ru/search/?q=fastapi+best+practices",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "FastAPI: Middleware (компрессия)",
     "url": "https://fastapi.tiangolo.com/ru/advanced/middleware/",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Пройдите чек-лист продакшена на любом учебном API (CORS, rate limit, логи, .env)",
    "Включите GZip-компрессию"
   ],
   "xp": 15,
   "minutes": 96
  },
  {
   "id": 69,
   "phase": 2,
   "week": 15,
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
    {
     "type": "article",
     "title": "pytest: документация (EN)",
     "url": "https://docs.pytest.org/en/stable/",
     "lang": "en"
    },
    {
     "type": "article",
     "title": "Habr: pytest с нуля",
     "url": "https://habr.com/ru/search/?q=pytest+с+нуля",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Напишите тесты для простых функций с fixtures",
    "Используйте parametrize на 5 кейсах"
   ],
   "xp": 15,
   "minutes": 96
  },
  {
   "id": 70,
   "phase": 2,
   "week": 15,
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
    {
     "type": "article",
     "title": "unittest.mock: документация (EN)",
     "url": "https://docs.python.org/3/library/unittest.mock.html",
     "lang": "en"
    },
    {
     "type": "article",
     "title": "Habr: моки и стабы в Python",
     "url": "https://habr.com/ru/search/?q=mock+python+monkeypatch",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Замокайте внешний HTTP-вызов в функции",
    "Проверьте, что вызов прошёл с нужными аргументами"
   ],
   "xp": 15,
   "minutes": 96
  },
  {
   "id": 71,
   "phase": 2,
   "week": 15,
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
    {
     "type": "article",
     "title": "Habr: тесты с SQLAlchemy изолированно",
     "url": "https://habr.com/ru/search/?q=pytest+sqlalchemy+тесты",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "factory_boy: документация (EN)",
     "url": "https://factoryboy.readthedocs.io/",
     "lang": "en"
    }
   ],
   "tasks": [
    "Напишите фикстуру сессии с откатом",
    "Добавьте фабрику User"
   ],
   "xp": 15,
   "minutes": 96
  },
  {
   "id": 72,
   "phase": 2,
   "week": 15,
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
    {
     "type": "article",
     "title": "FastAPI: Testing (RU)",
     "url": "https://fastapi.tiangolo.com/ru/tutorial/testing/",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "FastAPI: dependency_overrides",
     "url": "https://fastapi.tiangolo.com/ru/tutorial/dependencies/dependencies-in-path-operation-decorators/",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Напишите интеграционные тесты для своих эндпоинтов",
    "Подмените зависимость авторизации"
   ],
   "xp": 20,
   "minutes": 96
  },
  {
   "id": 73,
   "phase": 2,
   "week": 16,
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
    {
     "type": "article",
     "title": "pytest-cov: документация (EN)",
     "url": "https://pytest-cov.readthedocs.io/en/latest/",
     "lang": "en"
    },
    {
     "type": "article",
     "title": "Habr: TDD на примерах",
     "url": "https://habr.com/ru/search/?q=TDD+python+пример",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Доведите покрытие кода учебного API до 60%+",
    "Напишите один тест в стиле TDD"
   ],
   "xp": 15,
   "minutes": 96
  },
  {
   "id": 74,
   "phase": 2,
   "week": 16,
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
    {
     "type": "article",
     "title": "Habr: юнит-тесты сервисного слоя",
     "url": "https://habr.com/ru/search/?q=юнит+тесты+сервисный+слой+python",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Вынесите логику учебного API в сервисный слой",
    "Покройте сервисы юнит-тестами"
   ],
   "xp": 15,
   "minutes": 74
  },
  {
   "id": 75,
   "phase": 2,
   "week": 16,
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
    {
     "type": "article",
     "title": "FastAPI: Testing (RU)",
     "url": "https://fastapi.tiangolo.com/ru/tutorial/testing/",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Напишите 3 интеграционных сценария",
    "Запустите в CI/локально"
   ],
   "xp": 15,
   "minutes": 74
  },
  {
   "id": 76,
   "phase": 2,
   "week": 16,
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
    {
     "type": "article",
     "title": "FastAPI: Deployment (RU)",
     "url": "https://fastapi.tiangolo.com/ru/deployment/",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Habr: деплой FastAPI на VPS",
     "url": "https://habr.com/ru/search/?q=деплой+fastapi+vps+nginx",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Настройте запуск uvicorn --workers 2",
    "Схематично разберите деплой: сервер → Nginx → uvicorn"
   ],
   "xp": 10,
   "minutes": 96
  },
  {
   "id": 77,
   "phase": 2,
   "week": 17,
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
    {
     "type": "article",
     "title": "Habr: Docker для начинающих",
     "url": "https://habr.com/ru/search/?q=docker+для+начинающих+пособие",
     "lang": "ru"
    },
    {
     "type": "video",
     "title": "Docker с нуля (RU)",
     "url": "https://www.youtube.com/results?search_query=docker+с+нуля+русский+урок",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Установите Docker",
    "Соберите Dockerfile для Python-приложения"
   ],
   "xp": 15,
   "minutes": 89
  },
  {
   "id": 78,
   "phase": 2,
   "week": 18,
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
    {
     "type": "article",
     "title": "Docker best practices (EN)",
     "url": "https://docs.docker.com/build/building/best-practices/",
     "lang": "en"
    },
    {
     "type": "article",
     "title": "Habr: уменьшение размера docker-образа",
     "url": "https://habr.com/ru/search/?q=уменьшение+размера+docker+образа+python",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Соберите python:slim и посмотрите размер",
    "Оптимизируйте порядок инструкций"
   ],
   "xp": 10,
   "minutes": 96
  },
  {
   "id": 79,
   "phase": 2,
   "week": 18,
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
    {
     "type": "article",
     "title": "Docker: Compose docs (RU)",
     "url": "https://docs.docker.com/get-started/compose/",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Habr: docker-compose для разработки",
     "url": "https://habr.com/ru/search/?q=docker+compose+python+postgres",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Соберите compose: app + postgres + redis",
    "Поднимите всё через docker compose up"
   ],
   "xp": 15,
   "minutes": 96
  },
  {
   "id": 80,
   "phase": 2,
   "week": 18,
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
    {
     "type": "article",
     "title": "Docker: Volumes docs (EN)",
     "url": "https://docs.docker.com/engine/storage/volumes/",
     "lang": "en"
    },
    {
     "type": "article",
     "title": "Habr: volumes в docker",
     "url": "https://habr.com/ru/search/?q=docker+volumes+пособие",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Сохраните данные Postgres в volume",
    "Подключитесь из app-контейнера по имени"
   ],
   "xp": 10,
   "minutes": 96
  },
  {
   "id": 81,
   "phase": 2,
   "week": 18,
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
    {
     "type": "article",
     "title": "Docker best practices (EN)",
     "url": "https://docs.docker.com/build/building/best-practices/",
     "lang": "en"
    },
    {
     "type": "article",
     "title": "Habr: python в docker правильно",
     "url": "https://habr.com/ru/search/?q=docker+python+многоступенчатая+сборка",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Соберите multi-stage образ",
    "Запустите контейнер от непривилегированного пользователя"
   ],
   "xp": 15,
   "minutes": 96
  },
  {
   "id": 82,
   "phase": 2,
   "week": 19,
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
    {
     "type": "article",
     "title": "Docker best practices (EN)",
     "url": "https://docs.docker.com/build/building/best-practices/",
     "lang": "en"
    }
   ],
   "tasks": [
    "Соберите прод-Dockerfile для учебного API",
    "Проверьте запуск всего стека одной командой"
   ],
   "xp": 20,
   "minutes": 74
  },
  {
   "id": 83,
   "phase": 2,
   "week": 19,
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
    {
     "type": "article",
     "title": "OWASP Top 10 (RU)",
     "url": "https://owasp.org/www-project-top-ten/",
     "lang": "en"
    },
    {
     "type": "video",
     "title": "OWASP Top 10 разбор (RU)",
     "url": "https://www.youtube.com/results?search_query=owasp+top+10+русский+разбор",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Изучите список и отметьте 3 уязвимости в своём коде",
    "Исправьте хотя бы одну"
   ],
   "xp": 15,
   "minutes": 89
  },
  {
   "id": 84,
   "phase": 2,
   "week": 19,
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
    {
     "type": "article",
     "title": "Habr: XSS для начинающих",
     "url": "https://habr.com/ru/search/?q=XSS+атака+объяснение",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Habr: CSRF атаки",
     "url": "https://habr.com/ru/search/?q=CSRF+атака+защита",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Проверьте, экранируется ли вывод пользовательского контента",
    "Добавьте CSP-заголовки"
   ],
   "xp": 10,
   "minutes": 96
  },
  {
   "id": 85,
   "phase": 2,
   "week": 19,
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
    {
     "type": "article",
     "title": "Habr: шифрование простыми словами",
     "url": "https://habr.com/ru/search/?q=шифрование+простыми+словами",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "OWASP: secrets management (EN)",
     "url": "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html",
     "lang": "en"
    }
   ],
   "tasks": [
    "Проверьте git-историю на утечки секретов",
    "Вынесите все ключи в .env + .gitignore"
   ],
   "xp": 10,
   "minutes": 96
  },
  {
   "id": 86,
   "phase": 2,
   "week": 20,
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
    {
     "type": "article",
     "title": "pip-audit: документация (EN)",
     "url": "https://pypi.org/project/pip-audit/",
     "lang": "en"
    },
    {
     "type": "article",
     "title": "Habr: аудит безопасности Python-приложения",
     "url": "https://habr.com/ru/search/?q=аудит+безопасности+python+приложения",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Пройдите чек-лист аудита по учебному API",
    "Запустите pip-audit и исправьте критичные уязвимости"
   ],
   "xp": 15,
   "minutes": 96
  },
  {
   "id": 87,
   "phase": 2,
   "week": 20,
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
    {
     "type": "article",
     "title": "Celery: First Steps (EN)",
     "url": "https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html",
     "lang": "en"
    },
    {
     "type": "video",
     "title": "Celery для начинающих (RU)",
     "url": "https://www.youtube.com/results?search_query=celery+python+русский+урок",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Настройте Celery с Redis",
    "Перенесите тяжёлую задачу в фоновый воркер"
   ],
   "xp": 15,
   "minutes": 89
  },
  {
   "id": 88,
   "phase": 2,
   "week": 20,
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
    {
     "type": "article",
     "title": "Celery: Beat docs (EN)",
     "url": "https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html",
     "lang": "en"
    },
    {
     "type": "article",
     "title": "Habr: celery beat расписание",
     "url": "https://habr.com/ru/search/?q=celery+beat+периодические+задачи",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Настройте периодическую задачу (например, напоминание)",
    "Добавьте retry с экспоненциальным backoff"
   ],
   "xp": 15,
   "minutes": 96
  },
  {
   "id": 89,
   "phase": 2,
   "week": 20,
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
    {
     "type": "article",
     "title": "RabbitMQ: Tutorials (EN)",
     "url": "https://www.rabbitmq.com/tutorials",
     "lang": "en"
    },
    {
     "type": "video",
     "title": "RabbitMQ за 20 минут (RU)",
     "url": "https://www.youtube.com/results?search_query=rabbitmq+русский+обзор",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Разберите модель exchange/queue",
    "Сравните Redis и RabbitMQ в конспекте"
   ],
   "xp": 10,
   "minutes": 89
  },
  {
   "id": 90,
   "phase": 3,
   "week": 21,
   "module": "Карьера: резюме",
   "title": "Резюме для Junior Python",
   "goal": "Составить резюме, которое читают.",
   "points": [
    "Структура: о себе, стек, проекты, образование",
    "Проекты с описанием задач и результата",
    "Правильные ключевые слова (A/B)",
    "Шаблоны (Хабр Карьера, hh)"
   ],
   "resources": [
    {
     "type": "article",
     "title": "Что написать в резюме без опыта работы (Habr)",
     "url": "https://habr.com/ru/companies/htmlacademy/articles/543444/",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Что видят в вашем резюме Python-рекрутеры (Habr)",
     "url": "https://habr.com/ru/companies/oleg-bunin/articles/575956/",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Составьте резюме по шаблону",
    "Опишите 3 проекта с цифрами"
   ],
   "xp": 15,
   "minutes": 96
  },
  {
   "id": 91,
   "phase": 3,
   "week": 21,
   "module": "Карьера: собесы",
   "title": "Тестовые задания: как решать",
   "goal": "Эффективно проходить тестовые.",
   "points": [
    "Стратегия: план → код → тесты → README",
    "Читать ТЗ внимательно",
    "Проверять edge cases",
    "Тайм-менеджмент"
   ],
   "resources": [
    {
     "type": "article",
     "title": "Как правильно делать тестовые задания (Habr)",
     "url": "https://habr.com/ru/articles/877180/",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Решите одно тестовое из открытых источников",
    "Оформите его по чек-листу"
   ],
   "xp": 15,
   "minutes": 74
  },
  {
   "id": 92,
   "phase": 3,
   "week": 21,
   "module": "Карьера: собесы",
   "title": "Теория для интервью: Python",
   "goal": "Отвечать на типовые вопросы по Python.",
   "points": [
    "GIL, mutable/immutable, list vs tuple",
    "Декораторы, генераторы, контекстные менеджеры",
    "Сложности структур данных",
    "Функциональные/ООП вопросы"
   ],
   "resources": [
    {
     "type": "article",
     "title": "10 вопросов для Junior Python-разработчика (Habr)",
     "url": "https://habr.com/ru/articles/654489/",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Real Python: типовые вопросы (EN)",
     "url": "https://realpython.com/python-coding-interview-tips/",
     "lang": "en"
    }
   ],
   "tasks": [
    "Прорепетируйте 20 вопросов по Python",
    "Запишите свои ответы"
   ],
   "xp": 20,
   "minutes": 96
  },
  {
   "id": 93,
   "phase": 3,
   "week": 22,
   "module": "Карьера: собесы",
   "title": "Теория для интервью: БД и SQL",
   "goal": "Отвечать на вопросы по БД.",
   "points": [
    "Индексы: B-tree, когда работают",
    "Транзакции, ACID, уровни изоляции",
    "JOIN, GROUP BY, агрегаты",
    "N+1, пагинация"
   ],
   "resources": [
    {
     "type": "article",
     "title": "Вопросы по SQL на собеседовании. Часть 1 (Habr)",
     "url": "https://habr.com/ru/articles/790850/",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "B-Tree индекс и его производные в PostgreSQL (Хабр/Quadcode)",
     "url": "https://habr.com/ru/companies/quadcode/articles/696498/",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Как я SQLAlchemy удобной сделал — решение проблемы N+1 (Хабр)",
     "url": "https://habr.com/ru/articles/324876/",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Прорепетируйте вопросы по SQL",
    "Повторите ACID и индексы"
   ],
   "xp": 20,
   "minutes": 118
  },
  {
   "id": 94,
   "phase": 3,
   "week": 22,
   "module": "Карьера: поиск",
   "title": "Стратегия поиска работы",
   "goal": "Построить системный поиск вакансий.",
   "points": [
    "Где искать: hh, Хабр Карьера, LinkedIn, телеграм-чаты",
    "Отклики: кастомные сообщения",
    "Ведение таблицы воронки",
    "Сколько откликов в день"
   ],
   "resources": [
    {
     "type": "article",
     "title": "Habr Карьера: как искать работу junior",
     "url": "https://career.habr.com/",
     "lang": "ru"
    },
    {
     "type": "article",
     "title": "Исследование влияния сопроводительного письма: как я сделал 1000 откликов на вакансии",
     "url": "https://habr.com/ru/articles/836634/",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Составьте список из 20 компаний",
    "Настройте отслеживание откликов"
   ],
   "xp": 10,
   "minutes": 96
  },
  {
   "id": 95,
   "phase": 3,
   "week": 23,
   "module": "Карьера: собесы",
   "title": "Мок-собеседование",
   "goal": "Пройти тренировочное интервью.",
   "points": [
    "Найти мок-собеседование (знакомые, чаты)",
    "Пройти весь цикл",
    "Разбор ошибок",
    "Уверенность и презентация"
   ],
   "resources": [
    {
     "type": "article",
     "title": "Топ вопросов на Junior-собеседованиях (Habr)",
     "url": "https://habr.com/ru/articles/718282/",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Пройдите одно мок-собеседование",
    "Разберите слабые места"
   ],
   "xp": 20,
   "minutes": 74
  },
  {
   "id": 96,
   "phase": 3,
   "week": 24,
   "module": "Финал: оффер",
   "title": "Офферы, переговоры, выбор",
   "goal": "Правильно выбрать и принять оффер.",
   "points": [
    "Оценка оффера: ЗП, стек, рост, удалёнка",
    "Мягкие переговоры о ЗП",
    "Сравнение нескольких офферов",
    "Что спросить перед принятием"
   ],
   "resources": [
    {
     "type": "article",
     "title": "Как оценить и выбрать оффер (Habr)",
     "url": "https://habr.com/ru/companies/getmatch/articles/517068/",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Составьте критерии идеального оффера",
    "Оцените текущие варианты"
   ],
   "xp": 15,
   "minutes": 74
  },
  {
   "id": 97,
   "phase": 3,
   "week": 25,
   "module": "Финал: подведение",
   "title": "Подведение итогов и планы развития",
   "goal": "Осознать путь и спланировать рост.",
   "points": [
    "Пройдите по своему прогрессу",
    "Оцените достижения и gap",
    "План на следующие 6 месяцев",
    "Что дальше: Go, cloud, системный дизайн"
   ],
   "resources": [
    {
     "type": "article",
     "title": "Роадмеп бэкенд-разработчика на Python (Habr)",
     "url": "https://habr.com/ru/articles/919588/",
     "lang": "ru"
    }
   ],
   "tasks": [
    "Напишите рефлексию о пройденном пути",
    "Составьте план на 6 месяцев вперёд"
   ],
   "xp": 15,
   "minutes": 74
  },
  {
   "id": 98,
   "phase": 3,
   "week": 25,
   "module": "Финал: итог",
   "title": "Финальный день: праздник и старт",
   "goal": "Зафиксировать результат и двигаться дальше.",
   "points": [
    "Пройдите по всем пройденным темам",
    "Подсчитайте XP и свои достижения",
    "Поставьте цели на следующий этап",
    "Отпразднуйте"
   ],
   "resources": [],
   "tasks": [
    "Пройдите по своим достижениям",
    "Напишите итоговый пост/рефлексию"
   ],
   "xp": 10,
   "achievement": "Вы стали Junior Backend Developer!",
   "minutes": 52
  }
 ]
};
