import pandas as pd
from src.extractTransform import requestAPIBCB
from src.load import salvarCSV

dados_bcb = requestAPIBCB('20191')

salvarCSV(dados_bcb, 'ETL_BCB/src/datasets/meiosPagamentosTri.csv', ';', '.')