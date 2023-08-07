run-dev:
	uvicorn main:app --reload

run-seeder:
	alembic upgrade head && python ./scripts/seeder.py

reset-db:
	alembic downgrade base && make run-seeder