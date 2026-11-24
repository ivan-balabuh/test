# Звіт до лабораторної роботи №3: Аналіз покриття коду (Code Coverage)

## 1. Мета роботи
Ознайомитися з інструментами вимірювання покриття коду [coverage.py](https://coverage.readthedocs.io/) та [pytest-cov](https://pytest-cov.readthedocs.io/) у Python: навчитися розрізняти покриття рядків (*Line coverage*) та розгалужень (*Branch coverage*), правильно очищати дані між запусками (`coverage erase`), налаштовувати фільтрацію файлів у `.coveragerc` та директиву `# pragma: no cover`, а також генерувати візуальні HTML-звіти та XML-звіти для CI/CD.

---

## 2. Налаштування середовища та команди запуску
Для роботи використовувалося віртуальне середовище `.venv` та бібліотеки `coverage`, `pytest` і `pytest-cov`.

### Основні команди, використані під час виконання роботи:
```bash
# Встановлення необхідних пакетів у віртуальне середовище
/Users/admin/Desktop/testing/.venv/bin/python -m pip install coverage pytest pytest-cov

# Окремий запуск тестів unittest із вимірюванням покриття
python -m coverage erase
python -m coverage run -m unittest discover
python -m coverage report -m

# Окремий запуск тестів pytest із вимірюванням покриття
python -m coverage erase
python -m coverage run -m pytest
python -m coverage report -m

# Запуск із перевіркою покриття розгалужень та порогу у 90%
python -m pytest --cov=app --cov-branch --cov-report=term-missing -v
python -m pytest --cov=app --cov-branch --cov-fail-under=90

# Генерація HTML та XML звітів
python -m coverage html
python -m coverage xml

```
---

### Результати тестувань 
![](./img/Знімок%20екрана%202026-11-24%20о%2020.42.13.png)

![](./img/Знімок%20екрана%202026-11-24%20о%2020.43.17.png)

![](./img/Знімок%20екрана%202026-11-24%20о%2020.44.07.png)


![](./img/Знімок%20екрана%202026-11-24%20о%2020.44.16.png)

![](./img/Знімок%20екрана%202026-11-24%20о%2020.44.27.png)

![](./img/Знімок%20екрана%202026-11-24%20о%2020.44.51.png)