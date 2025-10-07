import click
import tomllib
from faker import Faker

import logging
from utils import logging_setup

logging = logging_setup()

from data_generation import generate_p01_01_l01

fake = Faker("pt_PT")  # Portuguese


@click.command()
@click.option(
    "-c",
    "--config",
    type=click.STRING,
    help="config input file",
    required=True,
    default="config_input.toml",
)
def main(config="config_input.toml"):
    logging.info("Starting data generation")

    with open(config, "rb") as f:
        config = tomllib.load(f)

    logging.info("Config file loaded")

    Faker.seed(int(config["key_info"]["seed"]))  # Seed for reproducibility

    logging.info("Seed: %s", config["key_info"]["seed"])
    logging.info("Number of individuals: %d", config["population"]["num_individuals"])

    # generate data
    p01_01_l01_table, p01_01_l01_report = generate_p01_01_l01(config, fake)

    logging.info("P01.01.L01 data generated")

    p01_01_l01_table.to_csv("output/p01_01_l01.csv", index=False)
    p01_01_l01_table.to_excel("output/p01_01_l01.xlsx", index=False)
    p01_01_l01_report.to_excel(
        "output/p01_01_l01_report.xlsx", index=False, header=False
    )

    logging.info("Data saved to 'output/' folder")

    logging.info("Data generation completed")

    # # save as csv

    # df_population = pd.DataFrame(population)
    # df_population.to_csv("population.csv", index=False)

    # df_population.to_excel("population.xlsx", index=False)

    # print(df_population.describe(include='all'))


if __name__ == "__main__":
    main()
