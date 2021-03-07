# Setup
.pip:
	pip install pip --upgrade

setup-dev: .pip
	pip install poetry
	poetry shell
	poetry install

# Test
.api-test:
	@behave api_tests_exercises/features

.e2e-test:
	@behave e2e_tests/features

test: .api-test .e2e-test
