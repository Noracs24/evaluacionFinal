.PHONY: help install install-py install-js test test-py test-js clean

help:
	@echo "Comandos disponibles:"
	@echo "  install       - Instalar todas las dependencias"
	@echo "  install-py    - Instalar dependencias de Python"
	@echo "  install-js    - Instalar dependencias de JavaScript"
	@echo "  test          - Ejecutar todas las pruebas"
	@echo "  test-py       - Ejecutar pruebas de Python"
	@echo "  test-js       - Ejecutar pruebas de JavaScript"
	@echo "  clean         - Limpiar archivos temporales"

install: install-py install-js

install-py:
	pip install -r requirements.txt --break-system-packages

install-js:
	npm install

test: test-py test-js

test-py:
	python -m pytest tests/python/ -v

test-js:
	npm test

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache node_modules/.cache