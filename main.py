from src.excel_reader import ExcelReader
from src.service import Service


def main():
    exc = ExcelReader()
    service = Service()

    print("Начало работы скрипта.")

    for data in exc.read_rows():
        service.inserting_to_db(data)

    print("----------------------")
    print("Скрипт завершил работу.")


if __name__ == "__main__":
    main()
