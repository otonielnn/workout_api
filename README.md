# WorkoutAPI
Esta é uma API de competição de crossfire chamada WorkoutAPI. É uma API pequena, apenas para entender como utilizar o FastAPI.

## Modelagem de entidade e relacionamento - MER
![MER](mer.jpg "Modelagem de entidade e relacionamento")

## Stack da API
A API foi desenvolvida utilizando `fastapi` (async), junto das seguintes libs: `alembic`, `SQLAlchquemy`, `pydantic`. Para salvar os dados está sendo utilizado o `postgres`, por meio de um conteiner `docker`.