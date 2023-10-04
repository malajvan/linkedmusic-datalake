import json
try:
   return json.loads(value)['name']
except:
   start_tag = '<title>'
end_tag = '</title>'

start_index = value.find(start_tag)
end_index = value.find(end_tag)

# Extract the content between the <title> tags
if start_index != -1 and end_index != -1:
    title_content = value[start_index + len(start_tag):end_index]

    # Remove leading and trailing whitespace
    title_content = title_content.split('-')[0]
    title_content = title_content.strip()

    # Print the title content
    return title_content
