import pandas as pd


def cargar_csv(csv_path: str) -> list[dict]:
    """
    Carga un archivo CSV y lo convierte en lista de diccionarios.
    """
    df = pd.read_csv(csv_path)
    return df.to_dict(orient="records")

