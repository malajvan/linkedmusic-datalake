import json

# Read the JSON data
with open('data/open.json', 'r') as file:
    data = json.load(file)

def grouping(data, property):
# Create a dictionary to store grouped data
    grouped_data = {}

    # Group the data by "id"
    for item in data:
        id_value = item['@id']
        if id_value not in grouped_data:
            grouped_data[id_value] = {'@id': id_value, property: []}
        grouped_data[id_value][property].append(item[property])

    # Convert the grouped data back to a list
    return list(grouped_data.values())

fin = []
for i in ['track']:
    fin.append(grouping(data,i))


# Save the result as JSON
with open('grouped_data.json', 'w') as output_file:
    json.dump(fin, output_file, indent=2)
