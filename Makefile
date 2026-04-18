# Makefile

# Установка зависимостей через uv
install:
	uv sync --all-extras --dev

# Запуск линтера
lint:
	uv run ruff tests scripts

# Запуск тестов
test:
	uv run pytest

# Запуск линтера и тестов
check: lint test

# Новая цель: запуск тестов с покрытием и генерация coverage.xml
test-coverage:
	# Запускаем pytest с плагином coverage, генерируем lcov и xml отчеты
	# pytest-cov должен быть установлен как часть dev зависимостей (он входит в pytest)
	uv run pytest --cov=gendiff --cov-report=xml --cov-report=term-missing

# (Опционально) цель для генерации HTML отчета локально
test-coverage-html:
	uv run pytest --cov=gendiff --cov-report=html --cov-report=term-missing
	@echo "HTML coverage report generated in htmlcov/"

.PHONY: install lint test check test-coverage test-coverage-html