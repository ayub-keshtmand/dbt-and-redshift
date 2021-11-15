from logs.setup_logging import setup_logging
from create_csv_file import create_csv_file
from load_data import load_data


logger = setup_logging(__name__)


if __name__ == "__main__":
    create_csv_file()
    load_data()
