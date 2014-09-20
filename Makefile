ENV ?= $(CURDIR)/../env
SETTINGS ?= project.settings.local
MANAGER = $(CURDIR)/project/manage.py
REQUIREMENTS = $(CURDIR)/requirements.txt
 
all: $(ENV)
	$(ENV)/bin/python $(MANAGER) $(ARGS) --settings=$(SETTINGS)

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

$(ENV): $(REQUIREMENTS)
	[ -d $(ENV) ] || virtualenv --no-site-packages $(ENV)
	$(ENV)/bin/pip install -r $(REQUIREMENTS)

.PHONY: run
# target: run - Run Django development server
run: $(ENV)
	$(ENV)/bin/python $(MANAGER) runserver_plus 0.0.0.0:8000 --settings=$(SETTINGS) \
	    || $(ENV)/bin/python $(MANAGER) runserver 0.0.0.0:8000 --settings=$(SETTINGS) 

.PHONY: db
# target: db - Prepare database
db: $(ENV)
	$(ENV)/bin/python $(MANAGER) syncdb --settings=$(SETTINGS) --noinput || echo 'sync failed'
	$(ENV)/bin/python $(MANAGER) migrate --settings=$(SETTINGS) --noinput

.PHONY: shell
# target: shell - Run project shell
shell: $(ENV)
	$(ENV)/bin/python $(MANAGER) shell_plus --settings=$(SETTINGS) \
	    || $(ENV)/bin/python $(MANAGER) shell --settings=$(SETTINGS)

.PHONY: static
# target: static - Compile project static
static: $(ENV)
	@mkdir -p $(CURDIR)/static
	$(ENV)/bin/python $(MANAGER) collectstatic --settings=$(SETTINGS) --noinput -c

.PHONY: lint
# target: lint - Code audit
lint: $(ENV)
	@rm -rf pep8.pylama pylint.pylama
	$(ENV)/bin/pip install pylama pylama_pylint
	$(ENV)/bin/pylama . -r pep8.pylama -l pep257,pep8,pyflakes,mccabe || echo
	$(ENV)/bin/pylama . -r pylint.pylama -l pylint -f pylint || echo

.PHONY: test t
# target: test - Run project's tests
TEST ?=
test: $(ENV)
	$(ENV)/bin/py.test

t: test

.PHONY: celery
# target: celery - Run celery worker
celery: $(ENV)
	$(ENV)/bin/celery worker -A project
