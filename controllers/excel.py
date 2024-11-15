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
        folder = os.path.join(os.getcwd(), "controllers")
        file_name = os.path.join(folder, file_name)
        wb = xw.Book(file_name)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"El archivo '{file_name}' no existe. Por favor, verifica el nombre o crea el archivo primero.")

    if sheet_name in [sheet.name for sheet in wb.sheets]:
        sheet = wb.sheets[sheet_name]
    else:
        sheet = wb.sheets.add(sheet_name)

    # Escribir el DataFrame en la hoja
    sheet.range("A1").value = dataframe

    # Insertar un botón de formulario
    cell = sheet.range("A25")
    cell_top = cell.api.Top
    cell_left = cell.api.Left
    cell_width = cell.api.Width
    cell_height = cell.api.Height

    # Insertar un botón de formulario en la celda
    button = sheet.api.Shapes.AddFormControl(
        Type=0,
        Left=cell_left,
        Top=cell_top,
        Width=cell_width,
        Height=cell_height
    )
    # Configurar propiedades del botón
    button.Name = "CustomButton"  # Cambiar el nombre del botón
    button.TextFrame.Characters.Text = "¡Haz clic aquí!"

    # Vincular el botón a la macro
    macro_name = "say_hello"
    button.OnAction = macro_name

    wb.save()
    #wb.close()


@xw.sub
def say_hello():
    """
    Esta función será llamada desde un botón en Excel.
    """
    wb = xw.Book.caller()  # Conecta el script al archivo abierto en Excel
    sheet = wb.sheets.active
    sheet.range("A1").value = "¡Hola desde Python!"
