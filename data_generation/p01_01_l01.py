import pandas as pd
import random
from faker import Faker
from utils import logging_setup

logging = logging_setup()


def generate_p01_01_l01(config, fake):
    logging.info("Generating P01.01.L01 data...")

    pop_cfg = config["population"]
    key_info = config["key_info"]
    unit_info = config["unit"]
    random.seed(key_info["seed"])
    num_individuals = pop_cfg["num_individuals"]
    age_min, age_max = pop_cfg["age_range"]
    sex_ratio = pop_cfg["sex_ratio"]  # Probability of male (e.g., 0.5)

    population = []
    for _ in range(num_individuals):
        nop = random.randint(10000000, 99999999)
        n_utente = random.randint(2000000000, 9999999999)
        sex = "Homem" if random.random() < sex_ratio else "Mulher"
        random_name = fake.name_male() if sex == "Homem" else fake.name_female()
        idade = random.randint(age_min, age_max)
        idade_string = "1 Ano" if idade == 1 else f"{idade} Anos"
        data_nascimento = fake.date_of_birth(minimum_age=idade, maximum_age=idade)
        # freguesia_habitação = fake.address().split("\n")[1]
        freguesia_habitação = "Cascos de Rolha"

        individual = {
            "NOP": nop,
            "Utente": n_utente,
            "": random_name,
            "Sexo": sex,
            "Idade": idade_string,
            "Data Nascimento": data_nascimento.strftime("%d/%m/%Y"),
            "Freguesia Habitação": freguesia_habitação,
            " ": "",
        }
        population.append(individual)

        report_metadata = [
            "P01.01.L01. Inscritos &gt; Utente" "",
            "Filtro do relatório",
            f"(Mês = {key_info['year']}-{key_info['month']:02d}) E ({{Unidade Funcional / Polo Hospitalar}} = {unit_info['unit_name']})",
            "",
            "Páginas:",
            f"Mês: {key_info['year']}-{key_info['month']:02d}",
            f"Unidade Funcional / Polo Hospitalar: {unit_info['unit_name']}",
            "Frequentador: Total",
            "Grupo etário: Total",
            "",
            "",
        ]

        df_table = pd.DataFrame(population)
        df_report = pd.DataFrame(report_metadata, columns=["Relatório"])

        df_table_simple = df_table.copy()
        # make a header row right below the report
        df_table_simple.columns = df_table_simple.columns.astype(str)
        df_table_simple = pd.DataFrame(
            [df_table_simple.columns.tolist()], columns=df_table_simple.columns
        )._append(df_table_simple, ignore_index=True)

        # Concatenate: report, header row, table data
        df_final = pd.concat([df_report, df_table_simple], ignore_index=True)
        df_final.columns = [""] * len(df_final.columns)  # Remove all column headers
        # df_final.columns = [""] * len(df_final.columns)

    return df_table, df_final
