import json
import os
from sqlalchemy import create_engine, insert
from models import Parceiro, CoverageArea

from dotenv import load_dotenv

# Dados para conectar com o banco de dados
load_dotenv()
USER = os.environ.get('DB_USER')
PASSWORD = os.environ.get('DB_PASSWORD')
DATABASE = os.environ.get('DATABASE')

print(USER, PASSWORD, DATABASE)

with open('pdvs.json', 'r') as f:
    pdvs = json.load(f)['pdvs']

# engine = create_engine("sqlite:///ze_code_challlenge.sqlite")
engine = create_engine(f'mysql://{USER}:{PASSWORD}@localhost/{DATABASE}')

for dados_parceiro in pdvs:
    parceiro = {
        'id': int(dados_parceiro['id']),
        'tradingName': dados_parceiro['tradingName'],
        'ownerName': dados_parceiro['ownerName'],
        'document': dados_parceiro['document'],
        'address_longitude': float(dados_parceiro['address']['coordinates'][0]),
        'address_latitude': float(dados_parceiro['address']['coordinates'][1]),
    }

    coordinates_list = dados_parceiro['coverageArea']['coordinates'][0][0]
    parceiro_coverageArea = []

    coverageArea_coordinates = {
        'id_parceiro': int(dados_parceiro['id']),
    }

    for i in range(len(coordinates_list)):
        coordinate = coordinates_list[i]

        coverageArea_coordinates = {
            'coordinate_id': i + 1,
            'id_parceiro': int(dados_parceiro['id']),
            'longitude': float(coordinate[0]),
            'latitude': float(coordinate[1]),
        }

        parceiro_coverageArea.append(coverageArea_coordinates)

    
    with engine.connect() as conn:
        insert_parceiro = insert(Parceiro).values(parceiro)
        conn.execute(insert_parceiro)

        for i in parceiro_coverageArea:
            stmt = insert(CoverageArea).values(i)
            conn.execute(stmt)
    
        conn.commit()


