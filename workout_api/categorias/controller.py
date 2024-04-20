from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy import select
from workout_api.categorias.schemas import CategoriaIn, CentroTreinamento
from workout_api.contrib.dependencies import DatabaseDependency
from workout_api.categorias.models import CategoriaModel

router = APIRouter()


@router.post(
    "/",
    summary="Criar uma nova Categoria",
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamento,
)
async def post(
    db_session: DatabaseDependency, categoria_in: CategoriaIn = Body(...)
) -> CentroTreinamento:

    categoria_out = CentroTreinamento(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())

    db_session.add(categoria_model)
    await db_session.commit()

    return categoria_out


@router.get(
    "/",
    summary="Consultar todas Categorias",
    status_code=status.HTTP_200_OK,
    response_model=list[CentroTreinamento],
)
async def query(
    db_session: DatabaseDependency,
) -> list[CentroTreinamento]:
    categorias: list[CentroTreinamento] = (
        (await db_session.execute(select(CategoriaModel))).scalars().all()
    )

    return categorias


@router.get(
    "/{id}",
    summary="Consultar uma Categorias pelo id",
    status_code=status.HTTP_200_OK,
    response_model=CentroTreinamento,
)
async def get(
    id: UUID4,
    db_session: DatabaseDependency,
) -> CentroTreinamento:
    categoria: CentroTreinamento = (
        (await db_session.execute(select(CategoriaModel).filter_by(id=id)))
        .scalars()
        .first()
    )

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria não encontrada no id: {id}",
        )

    return categoria
