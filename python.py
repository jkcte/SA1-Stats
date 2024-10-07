import json

# Replace 'your_file.json' with the path to your JSON file
with open('dataset.json', 'r') as file:
    data = json.load(file)

print(len(data["mean_time_using_phone"]['male']))