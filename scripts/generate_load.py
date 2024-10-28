import random
import datetime

# Definir o intervalo de datas
start_date = datetime.date(1900, 1, 1)
end_date = datetime.date(2024, 12, 31)
date_range = (end_date - start_date).days + 1  # Adicionar 1 para incluir o end_date

total_records = 40000
fund_id = 5

# Verificar se o intervalo é suficiente
if total_records > date_range:
    raise ValueError("O intervalo de datas é insuficiente para gerar datas únicas.")

# Gerar lista de todas as datas no intervalo
all_dates = [start_date + datetime.timedelta(days=i) for i in range(date_range)]

# Selecionar as primeiras 40.000 datas únicas
selected_dates = all_dates[:total_records]

with open("inserts.sql", "w") as f:
    for i, date in enumerate(selected_dates):
        calculation_at = date.strftime("%Y-%m-%d")
        comparison_dt = calculation_at

        # Gerar um timestamp único para created_at
        random_time = datetime.datetime.combine(
            date, datetime.time.min
        ) + datetime.timedelta(
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59),
            seconds=random.randint(0, 59),
            microseconds=random.randint(0, 999999),
        )
        created_at = random_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3] + "+00"

        identificator = 140000 + i

        insert_statement = f"""INSERT INTO "calculated_indicators" ("calculation_at", "comparison_dt", "created_at", "fifth_set", "first_set", "fourth_set", "fund_id", "id", "indicator_base_source_id", "indicator_id", "ingestion_source", "is_alert_active", "is_nonconformity_active", "second_set", "sixth_set", "third_set", "value") VALUES ('{calculation_at}', '{comparison_dt}', '{created_at}', '', '', '', {fund_id}, '{identificator}', '1', '641', NULL, TRUE, FALSE, '', '', '', '1000.5678');\n"""
        f.write(insert_statement)
