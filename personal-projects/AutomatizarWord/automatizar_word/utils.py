import pandas as pd


COLUMNAS_OBLIGATORIAS = {
    "name",
    "address",
    "phone_number",
    "email",
    "job",
    "company",
}


def cargar_csv(csv_path: str) -> list[dict]:
    """
    Carga un archivo CSV, valida columnas obligatorias
    y lo convierte en lista de diccionarios.
    """
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        raise RuntimeError(f"No se pudo leer el CSV: {e}")

    columnas_csv = set(df.columns)

    columnas_faltantes = COLUMNAS_OBLIGATORIAS - columnas_csv

    if columnas_faltantes:
        raise ValueError(
            f"El CSV no contiene las columnas obligatorias: {', '.join(columnas_faltantes)}"
        )

    return df.to_dict(orient="records")
