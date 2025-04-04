import pandas as pd
from src.extractTransform import requestAPIBCB
from src.load import salvarCSV, salvarSQLite, salvarMySQL

dados_bcb = requestAPIBCB("20191")

# salvarCSV(dados_bcb, 'src/datasets/meiosPagamentosTri.csv', ';', '.')

# salvarSQLite(dados_bcb, 'src/datasets/etlbcb.db', 'meios_pagamentos_tri')

salvarMySQL(dados_bcb, "root", "root", "localhost", "etlbcb", "meios_pagamento_tri")
