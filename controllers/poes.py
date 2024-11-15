import xlwings as xw
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from models.seeder import generate_data_with_scipy
import models.solubilidadGas as solubilidadGas
import models.presionBurbujeo as presionBurbujeo
import models.FactorVolumetricoOil as factorVolumetricoOil

def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]

    RS = "Rs"
    T =  "T"
    LPCA = "lpca"
    LPCA_NOB = "lpca_nob"
    LPCA_B = "lpca_b"
    SG_G = "SG_g"
    API = "API"
    RS_STANDING = "Rs_standing"
    RS_VASQUEZ = "Rs_vasquez"
    PB_STANDING = "Pb_standing"
    PB_VASQUEZ = "Pb_vasquez"
    BO_STANDING = "Bo_standing"
    BO_VASQUEZ = "Bo_vasquez"
    DO_STANDING = "Do_standing"
    DO_VASQUEZ = "Do_vasquez"
    CO_VASQUEZ = "Co_Vasquez"
    CO_PETROSKY = "Co_Petrosky"

    rs_values = sheet.range(RS).value
    lpca_values = sheet.range(LPCA).value
    T_values = sheet.range(T).value
    SG_G_values = sheet.range(SG_G).value
    API_values = sheet.range(API).value

    solubilidadGas_standing_values = []
    for lpca, T, SG_g, API in zip(lpca_values, T_values, SG_G_values, API_values):
        Rs = solubilidadGas.correlacion_standing(lpca, T, SG_g, API)
        solubilidadGas_standing_values.append([Rs])

    sheet.range(RS_STANDING).value = solubilidadGas_standing_values

    solubilidadGas_vasquez_values = []
    for lpca, T, SG_g, API in zip(lpca_values, T_values, SG_G_values, API_values):
        Rs = solubilidadGas.correlacion_vasquez_beggs(API, T, lpca, SG_g)
        solubilidadGas_vasquez_values.append([Rs])

    sheet.range(RS_VASQUEZ).value = solubilidadGas_vasquez_values

    chart1 = sheet.charts.add()
    chart1.name = "LPCA vs Solubilidad (Standing)"
    chart1.chart_type = "xy_scatter_lines"

    cell_position_1 = sheet.range("I23")
    chart1.left = cell_position_1.left
    chart1.top = cell_position_1.top
    chart1.width = 400
    chart1.height = 300

    chart1.api[1].SeriesCollection().NewSeries()
    chart1.api[1].SeriesCollection(1).XValues = lpca_values
    chart1.api[1].SeriesCollection(1).Values = solubilidadGas_standing_values
    chart1.api[1].SeriesCollection(1).Name = "Relación LPCA vs Solubilidad (Standing)"

    chart1.api[1].ChartTitle.Text = "Relación entre LPCA y Solubilidad del Gas (Standing)"
    chart1.api[1].Axes(1).HasTitle = True
    chart1.api[1].Axes(1).AxisTitle.Text = "LPCA (Presión)"
    chart1.api[1].Axes(2).HasTitle = True
    chart1.api[1].Axes(2).AxisTitle.Text = "Solubilidad del Gas (Rs) Standing"


    chart2 = sheet.charts.add()
    chart2.name = "LPCA vs Solubilidad (Vásquez)"
    chart2.chart_type = "xy_scatter_lines"

    cell_position_2 = sheet.range("I43")
    chart2.left = cell_position_2.left
    chart2.top = cell_position_2.top
    chart2.width = 400
    chart2.height = 300

    chart2.api[1].SeriesCollection().NewSeries()
    chart2.api[1].SeriesCollection(1).XValues = lpca_values
    chart2.api[1].SeriesCollection(1).Values = solubilidadGas_vasquez_values
    chart2.api[1].SeriesCollection(1).Name = "Relación LPCA vs Solubilidad (Vásquez)"

    chart2.api[1].ChartTitle.Text = "Relación entre LPCA y Solubilidad del Gas (Vásquez)"
    chart2.api[1].Axes(1).HasTitle = True
    chart2.api[1].Axes(1).AxisTitle.Text = "LPCA (Presión)"
    chart2.api[1].Axes(2).HasTitle = True
    chart2.api[1].Axes(2).AxisTitle.Text = "Solubilidad del Gas (Rs) Vásquez"

    presionBurbujeo_standing = []
    for RS, T, API in zip(rs_values, T_values, API_values):
        pb = presionBurbujeo.presion_burbuja_standing(RS, T, API)
        presionBurbujeo_standing.append([pb])

    sheet.range(PB_STANDING).value = presionBurbujeo_standing

    presionBurbujeo_vasquez = []
    for RS, T, SG_g, API in zip(rs_values, T_values, SG_G_values, API_values):
        pb = presionBurbujeo.presion_burbuja_vasquez_beggs(RS, T, SG_g, API)
        presionBurbujeo_vasquez.append([pb])

    sheet.range(PB_VASQUEZ).value = presionBurbujeo_vasquez

    factorVolumetrico_standing = []
    for RS, T, API, SG_g in zip(rs_values, T_values, API_values, SG_G_values):
        bo = factorVolumetricoOil.correlacion_standing(RS, SG_g, T, API)
        factorVolumetrico_standing.append([bo])

    sheet.range(BO_STANDING).value = factorVolumetrico_standing

    factorVolumetrico_vasquez = []
    for RS, T, API, SG_g in zip(rs_values, T_values, API_values, SG_G_values):
        bo = factorVolumetricoOil.correlacion_VasquezyBeggs(RS, T, API, SG_g)
        factorVolumetrico_vasquez.append([bo])

    sheet.range(BO_VASQUEZ).value = factorVolumetrico_vasquez

    chart1 = sheet.charts.add()
    chart1.name = "LPCA vs Factor Volumetrico (Standing)"
    chart1.chart_type = "xy_scatter_lines"

    cell_position_1 = sheet.range("W23")
    chart1.left = cell_position_1.left
    chart1.top = cell_position_1.top
    chart1.width = 400
    chart1.height = 300

    chart1.api[1].SeriesCollection().NewSeries()
    chart1.api[1].SeriesCollection(1).XValues = lpca_values
    chart1.api[1].SeriesCollection(1).Values = factorVolumetrico_standing
    chart1.api[1].SeriesCollection(1).Name = "Relación LPCA vs  Factor Volumetrico (Standing)"

    chart1.api[1].ChartTitle.Text = "Relación entre LPCA y  Factor Volumetrico (Standing)"
    chart1.api[1].Axes(1).HasTitle = True
    chart1.api[1].Axes(1).AxisTitle.Text = "LPCA (Presión)"
    chart1.api[1].Axes(2).HasTitle = True
    chart1.api[1].Axes(2).AxisTitle.Text = " Factor Volumetrico (Bo) Standing"

    chart2 = sheet.charts.add()
    chart2.name = "LPCA vs Factor Volumetrico (Vásquez)"
    chart2.chart_type = "xy_scatter_lines"

    cell_position_2 = sheet.range("W43")
    chart2.left = cell_position_2.left
    chart2.top = cell_position_2.top
    chart2.width = 400
    chart2.height = 300

    chart2.api[1].SeriesCollection().NewSeries()
    chart2.api[1].SeriesCollection(1).XValues = lpca_values
    chart2.api[1].SeriesCollection(1).Values = factorVolumetrico_vasquez
    chart2.api[1].SeriesCollection(1).Name = "Relación LPCA vs Factor Volumetrico (Vásquez)"

    chart2.api[1].ChartTitle.Text = "Relación entre LPCA y Factor Volumetrico (Vásquez)"
    chart2.api[1].Axes(1).HasTitle = True
    chart2.api[1].Axes(1).AxisTitle.Text = "LPCA (Presión)"
    chart2.api[1].Axes(2).HasTitle = True
    chart2.api[1].Axes(2).AxisTitle.Text = " Factor Volumetrico (Bo) Vásquez"

@xw.sub
def generar_datos():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    df = generate_data_with_scipy(num_samples=20)

    RS = "Rs"
    T = "T"
    LPCA = "lpca"
    LPCA_NOB = "lpca_nob"
    LPCA_B = "lpca_b"
    SG_G = "SG_g"
    API = "API"
    RS_STANDING = "Rs_standing"
    RS_VASQUEZ = "Rs_vasquez"
    PB_STANDING = "Pb_standing"
    PB_VASQUEZ = "Pb_vasquez"
    BO_STANDING = "Bo_standing"
    BO_VASQUEZ = "Bo_vasquez"
    DO_STANDING = "Do_standing"
    DO_VASQUEZ = "Do_vasquez"
    CO_VASQUEZ = "Co_Vasquez"
    CO_PETROSKY = "Co_Petrosky"

    sheet.range(RS).value = df[["Rs"]].values.tolist()
    sheet.range(T).value = df[["T"]].values.tolist()
    sheet.range(LPCA).value = df[["lpca"]].values.tolist()
    sheet.range(SG_G).value = df[["SG_g"]].values.tolist()
    sheet.range(API).value = df[["API"]].values.tolist()
    sheet.range(LPCA_NOB).value = df[["lpca_nob"]].values.tolist()
    sheet.range(LPCA_B).value = df[["lpca_b"]].values.tolist()

if __name__ == "__main__":
    xw.Book("poes.xlsm").set_mock_caller()
    main()
