from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from core.configs import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL, echo=False)


def get_session() -> AsyncSession:
    __async_session = sessionmaker(
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
        class_=AsyncSession,
        bind=engine
    )

    session: AsyncSession = __async_session()
    return session


async def create_tables() -> None:
    import models.__all_models
    print('Criando as tabelas no BD')
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print('Tabelas criadas com sucesso')

"""
import sqlalchemy as sa

from sqlalchemy.future.engine import Engine
from pathlib import Path  # Usado no SQLite
from typing import Optional
from models.model_base import ModelBase

__engine: Optional[Engine] = None


def create_engine(sqlite: bool = False) -> Engine:
    
    #Função para configurar a conexão ao banco de dados
    
    global __engine

    if __engine:
        return

    if sqlite:
        arquivo_bd = 'db/picoles.sqlite'
        folder = Path(arquivo_bd).parent
        folder.mkdir(parents=True, exist_ok=True)
        conn_str = f"sqlite///{arquivo_bd}"
        __engine = sa.create_engine(url=conn_str, echo=False, connect_args={
                                    "check_same_thread": False})
    else:
        conn_str = "postgresql://postgres.kwruoxeepphdvxdzwksl:c1c2c3c4C5%23@aws-1-us-east-2.pooler.supabase.com:5432/postgres"
        # pool_pre_ping testa se a conexão ainda está viva antes de usar
        __engine = sa.create_engine(
            url=conn_str, echo=False, pool_pre_ping=True)

    return __engine


def create_session() -> Session:
    
    #Função para criar a sessão de conexão ao banco de dados
    
    global __engine

    if not __engine:
        create_engine()  # create_engine(sqlite=True)

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)
    session: Session = __session()

    return session


def create_tables() -> None:
    global __engine

    if not __engine:
        create_engine()  # create_engine(sqlite=True)

    try:
        import models.__all_models
        ModelBase.metadata.drop_all(__engine)
        ModelBase.metadata.create_all(__engine)
    except Exception as e:
        print(f"Failed to connect: {e}")
    finally:
        if __engine:
            __engine.dispose()
"""

"""
if not __engine:
    create_engine()

try:
    with __engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"Failed to connect: {e}")
finally:
    if __engine:
        __engine.dispose()
"""
