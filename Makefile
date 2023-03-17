.PHONY: deploy/build deploy/run

deploy/build:
	pip install -r requirements.txt
	python manage.py collectstatic

deploy/run:
	gunicorn tutorial.wsgi \
		--capture-output \
		-b 0.0.0.0:10000
