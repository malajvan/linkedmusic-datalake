import psycopg2
from psycopg2 import sql
import csv
import re

db_params = {
    'dbname': 'simssadb',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost'
}

query = """
    SELECT file_id, {}
    FROM (SELECT file_id, feature_name, value
        FROM (SELECT
        f.id AS file_id,
        e.id AS extracted_id,
        fe.name AS feature_name,
        e.value AS value
    FROM 
    files f
    JOIN extracted_feature e ON e.feature_of_id = f.id
    JOIN
    feature fe ON fe.id = e.instance_of_feature_id
    )d 
    AS SourceTable
    PIVOT (
        MAX(value) FOR feature_name IN ({})
    ) AS PivotTable
    GROUP BY file_id
    

"""


# Connect to the database
conn = psycopg2.connect(**db_params)
cur = conn.cursor()


######get distinct feature name:
cur.execute("""SELECT DISTINCT feature_name FROM 
            (SELECT
        f.id AS file_id,
        e.id AS extracted_id,
        fe.name AS feature_name,
        e.value AS value
    FROM 
    files f
    JOIN extracted_feature e ON e.feature_of_id = f.id
    JOIN
    feature fe ON fe.id = e.instance_of_feature_id)d""")

feature_names = [row[0] for row in cur.fetchall()]
print(feature_names)
cur.close()
conn.close()

# for renaming feature names for column compatibility
def sanitize_column_name(name):
    return re.sub(r'[^a-zA-Z0-9]', '_', name)

# Create feature columns
feature_columns = ", ".join(
    f"MAX(CASE WHEN feature_name = '{name}' THEN value ELSE NULL END) AS  \"{sanitize_column_name(name)}\""
    for name in feature_names
)

feature_query = f"""
    SELECT file_id, {feature_columns}
    FROM (SELECT
        f.id AS file_id,
        e.id AS extracted_id,
        fe.name AS feature_name,
        e.value AS value
    FROM 
    files f
    JOIN extracted_feature e ON e.feature_of_id = f.id
    JOIN
    feature fe ON fe.id = e.instance_of_feature_id)d
    GROUP BY file_id
"""

# Execute the query
conn = psycopg2.connect(**db_params)
cur = conn.cursor()
cur.execute(feature_query)

# Retrieve data
results = cur.fetchall()

# Export data to TSV
with open('feature2.csv', 'w') as f:
    writer = csv.writer(f)

    # write the column names
    writer.writerow([col[0] for col in cur.description])

    # write the query results
    writer.writerows(results)

# Clean up
cur.close()
conn.close()