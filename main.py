import controllers.excel as excel
import models.seeder as seeder

if __name__ == '__main__':
    df = seeder.generate_data_with_scipy(20)
    excel.write_to_excel(df)