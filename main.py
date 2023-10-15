from excel_reader import ExcelReader


def main():
    exc = ExcelReader()
    for data in exc.read_rows():
        print(data)


if __name__ == "__main__":
    main()
