import psycopg2
import csv

db_params = {
    'dbname': 'simssadb',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost'
}

query = """
    SELECT
        musical_work.id AS musical_work_id,
        musical_work.variant_titles AS musical_work_variant_titles,
        musical_work.sacred_or_secular AS sacred_or_secular,
        person.given_name AS contributor_given_name,
        person.surname AS contributor_sur_name,
        contribution_musical_work.id AS contribution_id,
        contribution_musical_work.role AS contributor_role,
        contribution_musical_work.certainty_of_attribution AS contributor_certainty_of_attribution,
        source_instantiation.portion AS source_instantiation_portion,
        source.title AS source_title,
        source.source_type AS source_type,
        source.url AS source_url,
        files.file_type AS file_type,
        files.file_format AS file_format,
        files.version AS file_version,
        'https://db.simssa.ca/files/' || files.id AS url_to_file
        -- extracted_feature.value AS extracted_feature_value,
        -- feature.name AS feature_name
    FROM
        musical_work
    FULL OUTER JOIN
        contribution_musical_work ON contribution_musical_work.contributed_to_work_id = musical_work.id
    FULL OUTER JOIN
        source_instantiation ON musical_work.id = source_instantiation.work_id
    FULL OUTER JOIN
        source ON source_instantiation.source_id = source.id
    FULL OUTER JOIN
        files ON files.instantiates_id = source_instantiation.id
    -- FULL OUTER JOIN
    --     extracted_feature ON files.id = extracted_feature.feature_of_id
    -- FULL OUTER JOIN
    --     feature ON extracted_feature.instance_of_feature_id = feature.id
    FULL OUTER JOIN
        person ON contribution_musical_work.person_id = person.id

    -- WHERE files.id=1460
    
 
"""


# Connect to the database
conn = psycopg2.connect(**db_params)
cur = conn.cursor()

# Execute the query
cur.execute(query)

# Retrieve data
results = cur.fetchall()

# Export data to TSV
with open('output.csv', 'w') as f:
    writer = csv.writer(f)

    # write the column names
    writer.writerow([col[0] for col in cur.description])

    # write the query results
    writer.writerows(results)

# Clean up
cur.close()
conn.close()