from sqlalchemy import create_engine

def load_to_postgres(datetime_dim, passenger_dim, payment_dim, fact_table):

    engine = create_engine("postgresql://postgres:admin123@127.0.0.1:5432/uber_db")

    datetime_dim.to_sql("datetime_dim", engine, if_exists='replace', index=False)
    passenger_dim.to_sql("passenger_dim", engine, if_exists='replace', index=False)
    payment_dim.to_sql("payment_dim", engine, if_exists='replace', index=False)
    fact_table.to_sql("fact_table", engine, if_exists='replace', index=False)

    print("Data loaded to PostgreSQL ✅")