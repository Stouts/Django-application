VENV ?= $(CURDIR)/../venv
SETTINGS ?= main.settings.local
MANAGER = $(CURDIR)/project/manage.py
REQUIREMENTS = $(CURDIR)/requirements.txt
 
all: $(VENV)
	$(VENV)/bin/python $(MANAGER) $(ARGS) --settings=$(SETTINGS)

.PHONY: help
# target: help - Display callable targets
help:
	@egrep "^# target:" [Mm]akefile | sed -e 's/^# target: //g'

.PHONY: clean
# target: clean - Clean temporary files
clean:
	@find $(CURDIR) -name "*.py[co]" -delete
	@find $(CURDIR) -name "*.orig" -delete
	@find $(CURDIR) -name "*.deb" -delete
	@rm -rf build

$(VENV): $(REQUIREMENTS)
	[ -d $(VENV) ] || virtualenv --no-site-packages $(VENV)
	$(VENV)/bin/pip install -r $(REQUIREMENTS)

.PHONY: run
# target: run - Run Django development server
run: $(VENV)
	$(VENV)/bin/python $(MANAGER) runserver_plus 0.0.0.0:8000 --settings=$(SETTINGS) \
	    || $(VENV)/bin/python $(MANAGER) runserver 0.0.0.0:8000 --settings=$(SETTINGS) 

.PHONY: db
# target: db - Prepare database
db: $(VENV)
	$(VENV)/bin/python $(MANAGER) syncdb --settings=$(SETTINGS) --noinput || echo 'sync failed'
	$(VENV)/bin/python $(MANAGER) migrate --settings=$(SETTINGS) --noinput

.PHONY: shell
# target: shell - Run project shell
shell: $(VENV)
	$(VENV)/bin/python $(MANAGER) shell_plus --settings=$(SETTINGS) \
	    || $(VENV)/bin/python $(MANAGER) shell --settings=$(SETTINGS)

.PHONY: static
# target: static - Compile project static
static: $(VENV)
	@mkdir -p $(CURDIR)/static
	$(VENV)/bin/python $(MANAGER) collectstatic --settings=$(SETTINGS) --noinput -c

.PHONY: lint
# target: lint - Code audit
lint: $(VENV)
	@rm -rf pep8.pylama pylint.pylama
	$(VENV)/bin/pip install pylama pylama_pylint
	$(VENV)/bin/pylama . -r pep8.pylama -l pep257,pep8,pyflakes,mccabe || echo
	$(VENV)/bin/pylama . -r pylint.pylama -l pylint -f pylint || echo

.PHONY: test t
# target: test - Run project's tests
TEST ?=
test: $(VENV)
	$(VENV)/bin/py.test

t: test

.PHONY: celery
# target: celery - Run celery worker
celery: $(VENV)
	$(VENV)/bin/celery worker -A project.main
