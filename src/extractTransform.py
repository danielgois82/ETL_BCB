import requests
import pandas as pd


def requestAPIBCB(data: str) -> pd.DataFrame:
    """
    Requisicao da API do BCB sobre dados publicos referente a meios de pagamentos \n
    Parametro: Data - string, formato AAAAT, ex: 20191 \n
    Saida: Um Pandas DataFrame
    """
    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre='{data}'&$format=json"
    req = requests.get(url)
    print("Status code:", req.status_code)
    dados = req.json()
    df = pd.json_normalize(dados["value"])
    df["datatrimestre"] = pd.to_datetime(df["datatrimestre"])
    return df
