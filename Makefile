.PHONY: install lint test check test-coverage test-coverage-html

# Установка зависимостей через uv
install:
	uv sync --all-extras --dev

# Запуск проверки
lint:
	uv run ruff check hexlet_code scripts tests

# Запуск форматирования
format:
	uv run ruff format hexlet_code scripts tests

# Запуск тестов
test:
	uv run pytest

# Базовый coverage (XML + консоль)
test-coverage:
	# Запускаем pytest с плагином coverage, генерируем lcov и xml отчеты
	uv run pytest --cov=gendiff --cov-report=xml --cov-report=term-missing

# HTML отчет для детального просмотра
test-coverage-html:
	uv run pytest --cov=gendiff --cov-report=html --cov-report=term-missing
	@echo "HTML coverage report generated in htmlcov/"

# Проверка без исправлений (для CI)
check:
	uv run ruff check gendiff tests
	uv run ruff format --check gendiff tests

# Очистка временных файлов
clean:
	rm -rf .pytest_cache .coverage coverage.xml htmlcov .ruff_cache
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true