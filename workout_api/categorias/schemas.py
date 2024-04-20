from typing import Annotated
from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseSchema


class CategoriaIn(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome da categoria", example="Scale", max_length=10)
    ]


class CentroTreinamento(CategoriaIn):
    id: Annotated[UUID4, Field(description="Identificador de categoria")]
