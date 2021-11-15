import csv
import random
import os
from logs.setup_logging import setup_logging
from faker import Faker


logger = setup_logging(__name__)
FILEPATH = os.path.join(".", "data", "data.csv")
RECORD_COUNT = 100000
fake = Faker()


def create_csv_file():
    
    directory = os.path.join("data")
    if not os.path.exists(directory):
        os.mkdir(directory)
        logger.info(f"Created {directory} folder")

    with open(FILEPATH, "w", newline="") as csvfile:
        fieldnames = [
            'first_name',
            'last_name',
            'email',
            'product_id',
            'qty',
            'amount',
            'description',
            'address',
            'city',
            'state',
            'country'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in range(RECORD_COUNT):
            writer.writerow(
                {
                    "first_name": fake.name().split()[0],
                    "last_name": fake.name().split()[1],
                    "email": fake.email(),
                    "product_id": fake.random_int(min=100, max=1000),
                    "qty": fake.random_int(min=1, max=9),
                    "amount": random.randrange(500,1000)/100,
                    "description": fake.sentence(),
                    "address": fake.street_address(),
                    "city": fake.city(),
                    "state": fake.state(),
                    "country": fake.country(),
                }
            )
        logger.info(f"Created csv file with {RECORD_COUNT} rows")
