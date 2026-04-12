import pandas as pd

def transform_data(df):

    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    df = df.drop_duplicates().reset_index(drop=True)

    # Datetime Dimension
    datetime_dim = df[['tpep_pickup_datetime','tpep_dropoff_datetime']].drop_duplicates().reset_index(drop=True)
    datetime_dim['datetime_id'] = datetime_dim.index
    datetime_dim['pick_hour'] = datetime_dim['tpep_pickup_datetime'].dt.hour
    datetime_dim['pick_day'] = datetime_dim['tpep_pickup_datetime'].dt.day
    datetime_dim['pick_month'] = datetime_dim['tpep_pickup_datetime'].dt.month
    datetime_dim['pick_year'] = datetime_dim['tpep_pickup_datetime'].dt.year

    # Passenger Dimension
    passenger_dim = df[['passenger_count']].drop_duplicates().reset_index(drop=True)
    passenger_dim['passenger_id'] = passenger_dim.index

    # Payment Dimension
    payment_map = {
        1:"Card", 2:"Cash", 3:"No Charge", 4:"Dispute"
    }
    payment_dim = df[['payment_type']].drop_duplicates().reset_index(drop=True)
    payment_dim['payment_id'] = payment_dim.index
    payment_dim['payment_name'] = payment_dim['payment_type'].map(payment_map)

    # FACT TABLE
    fact_table = df.merge(datetime_dim, on=['tpep_pickup_datetime','tpep_dropoff_datetime']) \
                   .merge(passenger_dim, on='passenger_count') \
                   .merge(payment_dim, on='payment_type')

    print("Transformation Complete ✅")

    return datetime_dim, passenger_dim, payment_dim, fact_table