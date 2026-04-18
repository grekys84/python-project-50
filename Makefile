.PHONY: install lint format test check test-coverage test-coverage-html check clean

# Установка зависимостей через uv
install:
	uv sync --all-extras --dev

# Запуск проверки
lint:
	uv run ruff check hexlet_code

# Запуск форматирования
format:
	uv run ruff format hexlet_code

# Запуск тестов
test:
	uv run pytest

# Базовый coverage (XML + консоль)
test-coverage:
	# Запускаем pytest с плагином coverage, генерируем lcov и xml отчеты
	uv run pytest --cov=hexlet_code --cov-report=xml --cov-report=term-missing

# HTML отчет для детального просмотра
test-coverage-html:
	uv run pytest --cov=gendiff --cov-report=html --cov-report=term-missing
	@echo "HTML coverage report generated in htmlcov/"

# Проверка без исправлений (для CI)
check:
	uv run ruff check hexlet_code
	uv run ruff format --check hexlet_code

# Очистка временных файлов
clean:
	rm -rf .pytest_cache .coverage coverage.xml htmlcov .ruff_cache
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true