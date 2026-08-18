# -*- coding: utf-8 -*-
"""Сборщик базы знаний: объединяет все дни в один data.js"""
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from days_p0 import DAYS_P0
from days_p1 import DAYS_P1
from days_p2 import DAYS_P2
from days_p3 import DAYS_P3
from days_p4 import DAYS_P4

# Проекты исключаются из роадмапа — остаются только темы
def is_project(d):
    return ("мини-проект" in d["module"] or "мини-проект" in d.get("title", "").lower()
            or "Диплом" in d["module"] or d["module"] == "Повторение")

ALL = [d for d in (DAYS_P0 + DAYS_P1 + DAYS_P2 + DAYS_P3 + DAYS_P4) if not is_project(d)]

# Деплой переносим после блока тестирования: сначала тесты, потом выкладка.
def _move_deploy_after_tests(days):
    idx_deploy = next((i for i, d in enumerate(days) if d["module"].startswith("FastAPI: деплой")), None)
    idx_last_test = next((i for i in range(len(days) - 1, -1, -1) if days[i]["module"].startswith("Тестирование")), None)
    if idx_deploy is not None and idx_last_test is not None and idx_deploy < idx_last_test:
        deploy = days.pop(idx_deploy)
        days.insert(idx_last_test, deploy)
        deploy["week"] = days[idx_last_test - 1]["week"]
    return days

# применяем перестановку только к блоку фазы 2, остальные фазы не трогаем
out = []
buf = []
for d in ALL:
    if d["phase"] == 2:
        buf.append(d)
    else:
        if buf:
            out.extend(_move_deploy_after_tests(buf))
            buf = []
        out.append(d)
if buf:
    out.extend(_move_deploy_after_tests(buf))
ALL = out

# Перенумерация недель без пропусков (проектные недели выпали)
weeks_seen = {}
week_seq = []
for d in ALL:
    if d["week"] not in weeks_seen:
        weeks_seen[d["week"]] = len(week_seq) + 1
        week_seq.append(d["week"])
for d in ALL:
    d["week"] = weeks_seen[d["week"]]

# Перенумерация по порядку (избавляет от ручных ошибок id)
for i, d in enumerate(ALL, 1):
    d["id"] = i

# Расчёт примерного времени на день (минуты) на основе объёма материалов
# Реалистичная оценка сфокусированной сессии: одна тема = одна сессия
TYPE_MIN = {"article": 22, "video": 15, "course": 26, "practice": 18}
def estimate_minutes(d):
    base = 32
    base += sum(TYPE_MIN.get(r["type"], 18) for r in d["resources"])
    base += 10 * len(d["tasks"])
    return max(50, min(base, 130))

for d in ALL:
    d["minutes"] = estimate_minutes(d)

# Проверка целостности
ids = [d["id"] for d in ALL]
assert len(ids) == len(set(ids)), "Дубликаты id!"
assert ids == sorted(ids), "Порядок id нарушен!"

# Каждый день обязан иметь ресурсы/задания
for d in ALL:
    for r in d["resources"]:
        assert r.get("lang") in ("ru", "en"), f"День {d['id']}: ресурс без lang: {r.get('title')}"
    for r in d["resources"]:
        assert r.get("url", "").startswith("http"), f"День {d['id']}: плохой url: {r.get('url')}"

# Статистика
from collections import Counter
weeks = sorted(set(d["week"] for d in ALL))
modules = Counter(d["module"] for d in ALL)
phases = Counter(d["phase"] for d in ALL)
total_xp = sum(d["xp"] for d in ALL)
total_res = sum(len(d["resources"]) for d in ALL)
total_tasks = sum(len(d["tasks"]) for d in ALL)

print(f"Всего дней: {len(ALL)}")
print(f"Недель: {min(weeks)}-{max(weeks)}")
print(f"Фазы: {dict(phases)}")
print(f"Модулей: {len(modules)}")
print(f"Суммарный XP: {total_xp}")
print(f"Всего ресурсов: {total_res}")
print(f"Всего заданий: {total_tasks}")
total_min = sum(d["minutes"] for d in ALL)
print(f"Суммарное время: {total_min} мин = {total_min/60:.1f} ч")
print(f"Среднее на день: {total_min/len(ALL):.0f} мин")
print(f"Мин день: {min(d['minutes'] for d in ALL)} мин, Макс день: {max(d['minutes'] for d in ALL)} мин")
print(f"Дней в блоке 1 (семестр): {sum(1 for d in ALL if d['phase']==1)}")
phase1_min = sum(d["minutes"] for d in ALL if d["phase"]==1)
print(f"Блок 1: {phase1_min} мин = {phase1_min/60:.1f} ч при 1-2 ч/день")
print(f"  Займёт дней по 2ч: {phase1_min/120:.1f} дн; по 1.5ч: {phase1_min/90:.1f} дн; по 1ч: {phase1_min/60:.1f} дн")
print(f"Дней в блоке 2 (FastAPI): {sum(1 for d in ALL if d['phase']==2)}")
print(f"Дней в блоке 3 (финал): {sum(1 for d in ALL if d['phase']==3)}")

# Дни с ачивками
ach = [d for d in ALL if d.get("achievement")]
print(f"\nДней с ачивками: {len(ach)}")
for d in ach:
    print(f"  День {d['id']}: {d['achievement']}")

# Модули с количеством дней
print("\nМодули (дней):")
for m, c in modules.most_common():
    print(f"  {m}: {c}")

# Запись data.js
output = {
    "startDate": "2026-08-17",
    "meta": {
        "title": "Роадмап Python Backend Junior",
        "totalDays": len(ALL),
        "totalXp": total_xp,
        "phases": {
            0: {"name": "Python", "days": "17–31 августа", "note": "Python углублённо + алгоритмы, 2-3 ч/день"},
            1: {"name": "Семестр", "days": "1 сентября – 4 октября", "note": "SQL, Git, веб, Flask, 1-2 ч/день"},
            2: {"name": "FastAPI + инструменты", "days": "5 октября – 24 ноября", "note": "FastAPI, тесты, Docker, безопасность, очереди"},
            3: {"name": "Карьера", "days": "25 ноября – 31 декабря", "note": "Резюме, собеседования, трудоустройство"}
        }
    },
    "days": ALL
}

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data.js"), "w", encoding="utf-8") as f:
    f.write("const ROADMAP = ")
    f.write(json.dumps(output, ensure_ascii=False, indent=1))
    f.write(";")
    f.write("\n")

print("\nГотово: data.js записан")