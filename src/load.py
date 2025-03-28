import pandas as pd

def salvarCSV(df: pd.DataFrame, nome_arquivo: str, separador: str, decimal: str):
    df.to_csv(nome_arquivo, sep=separador, decimal=decimal, index=False)