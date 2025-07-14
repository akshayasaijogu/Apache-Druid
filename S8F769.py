import requests
import json

# Define the Druid Query API endpoint
query_url = 'http://localhost:8082/druid/v2/sql'

# Define your SQL query with the correct datasource name
query = 'SELECT * FROM "8F769_TOP"'

# Send the query to Druid and retrieve the result
response = requests.post(query_url, json={'query': query})
if response.status_code == 200:
    result = response.json()

    # Process the result
    rows_by_roll_number = {}  # Dictionary to hold rows by roll number
    for row in result:
        roll_number = row['ROLL NUMBER']
        if roll_number not in rows_by_roll_number:
            rows_by_roll_number[roll_number] = []
        rows_by_roll_number[roll_number].append(row)

    # Convert the dictionary to JSON
    json_output = json.dumps(rows_by_roll_number, indent=2)

    # Export JSON data to a file
    with open('output_8F769.json', 'w') as outfile:
        outfile.write(json_output)

    print('JSON data exported to output.json.')
else:
    print('Error:', response.text)
