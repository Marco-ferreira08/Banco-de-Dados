import os

from sqlalchemy import (
    create_engine,
    ForeignKey,
    )

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped, mapped_column,
    relationship
)

from dotenv import load_dotenv

# Dados para conectar com o banco de dados
load_dotenv()
USER = os.environ.get('DB_USER')
PASSWORD = os.environ.get('DB_PASSWORD')
DATABASE = os.environ.get('DATABASE')

print(USER, PASSWORD, DATABASE)
class Base(DeclarativeBase):
    ''' Classe base para as tabela do banco de dados '''
    pass

class Parceiro(Base):
    ''' Tabela com os dados gerais dos parceiros do Zé Delivery '''
    __tablename__ = 'parceiros'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tradingName: Mapped[str] = mapped_column(nullable=False)
    ownerName: Mapped[str] = mapped_column(nullable=False)
    document: Mapped[str] = mapped_column(nullable=False)
    address_longitude: Mapped[float] = mapped_column(nullable=False)
    address_latitude: Mapped[float] = mapped_column(nullable=False)

class CoverageArea(Base):
    ''' Tabela secundária que armazena as áreas de atuação dos parceiros '''
    __tablename__ = "coverage_area"

    coordinate_id: Mapped[int] = mapped_column(nullable=False, primary_key=True)
    id_parceiro: Mapped[int] = mapped_column(ForeignKey('parceiros.id'), nullable=False, primary_key=True)
    parceiro: Mapped[Parceiro] = relationship(back_populates="coverage_area")
    longitude: Mapped[float] = mapped_column(nullable=False)
    latitude: Mapped[float] = mapped_column(nullable=False)
                                             
engine = create_engine(f'mysql://{USER}:{PASSWORD}@localhost/{DATABASE}')
# engine = create_engine("sqlite:///ze_code_challlenge.sqlite")
Base.metadata.create_all(engine)