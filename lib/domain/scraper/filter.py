import json

# Load the JSON file
input_file = "results.json"  # Replace with your actual file name
output_file = "filtered_results.json"

# Read JSON data
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Filter out entries where "movie_download_links" is missing
filtered_data = [entry for entry in data if "movie_download_links" in entry and entry["movie_download_links"]]

# Save filtered data to a new JSON file
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(filtered_data, f, indent=2)

print(f"Filtered results saved to {output_file}")