import warnings
import pandas as pd
from sqlalchemy import create_engine

# Suppress warnings
warnings.filterwarnings('ignore')

# MySQL connection configuration
config = {
    'user': 'YOUR USER ID user',          
    'password': 'YOUR PASSWORD',      
    'host': 'YOUR HOST NAME',     
    'database': 'YOUR DATABASEA NAME',      
}

# Use pymysql instead of MySQLdb
engine = create_engine(f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}/{config['database']}")

try:
    # Read CSV file
    file_path = r"YOUR FILE PATH"
    data = pd.read_csv(file_path)

    # Write DataFrame to MySQL table
    data.to_sql('YOUR TABLE NAME', con=engine, index=False, if_exists='replace')

    print("✅ Data successfully written to MySQL table 'YOUR TABLE NAME'.")

except FileNotFoundError:
    print(f"❌ Error: The file '{file_path}' was not found. Check the path.")

except Exception as e:
    print("❌ An error occurred:", e)
