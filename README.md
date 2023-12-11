# FastAPI demo.

This demo is built by basic code of FastAPI. There are 2 demo code, currently itonly has 1st. 2nd part will be uploaded soon.

### For generating database from alembic.
alembic revision --autogenerate -m <message>

Besides, there are some commands about useful alembic commands:

### Show version.
alembic current

### Migration history.
alembic history --verbose

### Revert.
alembic downgrade 'base (all)' || '-1 (one by one)'

### Show raw SQL.
alembic upgrade head --sql

### Reset database.
alembic downgrade base && alembic upgrade head
