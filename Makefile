MODULE?=price_searcher_app
PORT?=8888
PY?=python
RUN?=pipenv run

run:
	FLASK_APP=$(MODULE).flask_app \
	$(RUN) $(PY) -m flask run --host 0.0.0.0 --port $(PORT) --no-reload --no-debugger

test:
	$(RUN) pytest tests/
