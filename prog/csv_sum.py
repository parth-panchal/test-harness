import argparse
import csv


def csv_sum(file_path, columns):
    try:
        with open(file_path, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            sums = {column: 0 for column in columns}
            for row in reader:
                for column in columns:
                    sums[column] += float(row[column])
            for column, total in sums.items():
                print(f"Sum of {column}: {total}")
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        exit(1)
    except csv.Error as e:
        print(f"CSV Error: {e}")
        exit(1)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)


def main():
    parser = argparse.ArgumentParser(description="Sum specified columns in a CSV file.")
    parser.add_argument("file", metavar="file", type=str, help="CSV file to process")
    parser.add_argument(
        "columns", metavar="columns", type=str, nargs="+", help="Columns to sum"
    )
    args = parser.parse_args()
    csv_sum(args.file, args.columns)


if __name__ == "__main__":
    main()
