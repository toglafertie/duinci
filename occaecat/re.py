import pandas as pd
from sqlalchemy import create_engine

# Create an engine
engine = create_engine('connection_string')

# Read the table into a DataFrame
df = pd.read_sql_table('table_name', con=engine)
