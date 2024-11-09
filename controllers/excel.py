import xlwings as xw
import os



def write_to_excel(dataframe, file_name="data.xlsm", sheet_name="Data"):
    """
    Abre un archivo Excel existente y escribe un DataFrame en una hoja.

    Parámetros:
    - dataframe: DataFrame con los datos a escribir.
    - file_name: Nombre del archivo Excel existente.
    - sheet_name: Nombre de la hoja dentro del archivo Excel.

    Retorna:
    - Escribe los datos en el archivo Excel existente.
    """
    try:
        folder = os.path.join(os.getcwd(),"controllers")
        file_name = os.path.join(folder, file_name)
        print(file_name)
        wb = xw.Book(file_name)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"El archivo '{file_name}' no existe. Por favor, verifica el nombre o crea el archivo primero.")

    if sheet_name in [sheet.name for sheet in wb.sheets]:
        sheet = wb.sheets[sheet_name]
    else:
        sheet = wb.sheets.add(sheet_name)

    sheet.range("A1").value = dataframe

    wb.save()
    wb.close()
