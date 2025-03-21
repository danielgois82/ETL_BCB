import requests
import pandas as pd

def requestAPIBCB(data):
    '''
    Requisicao da API do BCB sobre dados publicos sobre meios de pagamentos \n
    Parametro: data - string, format AAAAT, ex: 20191
    '''
    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre='{data}'&$format=json"
    req = requests.get(url)
    # print(req.status_code)
    dados = req.json()
    df = pd.json_normalize(dados['value'])
    return print(df)

requestAPIBCB('20241')