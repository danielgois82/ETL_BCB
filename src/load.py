import pandas as pd

def salvarCSV(df: pd.DataFrame, nome_arquivo: str, separador: str, decimal: str):
    '''
    Salvar em disco um arquivo .CSV a partir de um DataFrame \n
    Parametros: Um DataFrame, \n
    nome_arquivo: string - Caminho e nome do arquivo .CSV a ser criado, \n
    separador: string - Separador de dados do arquivo .CSV, ex.:  ";" ou ",", \n
    decimal: string - Separador de casas decimais, ex.: "." ou ",".
    '''
    df.to_csv(nome_arquivo, sep=separador, decimal=decimal, index=False)