<p align="center">
  <img src="assets/banner.svg" width="100%" alt="Backend Roadmap Tracker">
</p>

<p align="center">
  <b>Интерактивный план обучения Python-разработчика</b> —
  трекер прогресса без привязки к датам, с офлайн-режимом.
</p>

<p align="center">
  <a href="https://danekemik.github.io/RoadMap-Tracker/">🌐 Открыть трекер</a>
</p>

---

## 📸 Что внутри

Персональный роадмап: от терминала и основ Python до FastAPI, Docker и трудоустройства. Отмечайте изученные темы — прогресс сохраняется автоматически и работает без интернета.

## ✨ Возможности

- **98 тем в 19 блоках**: Linux и Python → SQL и Git → Flask → FastAPI → Docker и сети → Карьера
- **Прогресс-панель**: общий процент и счётчик изученного
- **Цель и подпункты** у каждой темы — раскрываются по стрелке
- **Завершённые блоки** подсвечиваются зелёным прямо в меню
- **Разделы**: Главная · Тестирование · Настройки (пока заглушки)
- **Автосохранение** в `localStorage` — прогресс не пропадёт
- **PWA**: устанавливается на телефон/ПК и работает офлайн
- «Бумажный» интерфейс на округлом шрифте [Fredoka One Cyrillic](https://github.com/google/fonts/tree/main/ofl/fredokaone) (SIL OFL)

## 🚀 Запуск локально

### macOS

```bash
git clone https://github.com/danekemik/RoadMap-Tracker.git
cd RoadMap-Tracker/docs
python3 -m http.server 8317
# откройте http://localhost:8317
```

Или просто дважды кликните на `scripts/start.command` — он сам поднимет сервер и откроет браузер.

### Windows

```cmd
git clone https://github.com/danekemik/RoadMap-Tracker.git
cd RoadMap-Tracker\docs
python -m http.server 8317
start http://localhost:8317
```

> 💡 На обеих ОС можно открыть страницу в браузере и нажать «Установить» — приложение сохранится как PWA и будет работать офлайн.

## 🛠 Технологии

- **Фронтенд**: чистый HTML + CSS + JavaScript, без фреймворков
- **Сборка данных**: Python (`generator/build.py`) собирает `data.js` из модулей `days_*.py`
- **PWA**: Service Worker + Web App Manifest

## 📁 Структура

```
├── docs/                # приложение
│   ├── index.html       # интерфейс (единственная страница, экраны переключаются без перезагрузки)
│   ├── data.js          # программа обучения (98 тем)
│   ├── fonts/           # шрифт Fredoka One Cyrillic
│   ├── manifest.json    # PWA-манифест
│   ├── sw.js            # service worker (офлайн-режим)
│   └── icons/           # иконки приложения
├── assets/              # иллюстрации для README
├── scripts/             # start.command — запуск локального сервера (macOS)
└── generator/           # python-сборщик данных
    ├── build.py
    └── days_p0..p4.py
```

## 📄 Лицензия

MIT © danekemik
