#!/bin/zsh
# Роадмап: локальный сервер для PWA-приложения
cd "$HOME/Desktop/Backend-Roadmap-Tracker/docs" || exit 1
PORT=8317

if lsof -i :$PORT -sTCP:LISTEN >/dev/null 2>&1; then
  echo "Сервер уже запущен на http://localhost:$PORT"
else
  nohup python3 -m http.server $PORT --bind 127.0.0.1 >/dev/null 2>&1 &
  echo "Сервер запущен на http://localhost:$PORT"
fi

sleep 1
open "http://localhost:$PORT"