# Менеджер личных финансов

Консольное приложение на Python для учёта доходов и расходов, контроля баланса и анализа бюджета.

## Возможности
- Добавление доходов и расходов с категорией и описанием.
- Сохранение операций между запусками.
- Просмотр баланса, истории и отчёта по категориям.
- Проверка ввода и отмена операции.
- Интерфейс Lavender Dream с пастельными лавандовыми, голубыми и розовыми акцентами.

## Установка и запуск
Требуется Python 3.12+.

```bash
git clone git@github.com:skKristinka/finance-manager.git
cd finance-manager
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

В Windows активируйте окружение командой `.venv\\Scripts\\activate`.

Операции хранятся в `data/transactions.json`. Для другого расположения задайте переменную окружения `FINANCE_MANAGER_DATA`. Подробности: [docs/USER_GUIDE.md](docs/USER_GUIDE.md).

## Тесты
```bash
python -m pytest
```

Подробная инструкция по работе с приложением находится в [USER_GUIDE.md](USER_GUIDE.md).
