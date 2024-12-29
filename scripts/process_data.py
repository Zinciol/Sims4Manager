import os
import json
import zipfile

# Paths
data_file = "data.json"
output_dir = "output"

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_html_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def create_zip_file(zip_path, folder_path):
    with zipfile.ZipFile(zip_path, 'w') as zf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, folder_path)
                zf.write(full_path, relative_path)

def main():
    # Load data.json
    with open(data_file, 'r') as f:
        data = json.load(f)

    # Ensure output directory exists
    create_directory(output_dir)

    for mod_id, mod_data in data["mods"].items():
        mod_name = mod_data["name"]

        for variation_id, variation_data in mod_data["variations"].items():
            variation_name = variation_data["name"]

            for version_id, version_data in variation_data["versions"].items():
                version_name = version_data["name"]

                # Create folder structure
                folder_path = os.path.join(output_dir, mod_id, variation_id, version_id)
                create_directory(folder_path)

                # Generate HTML file
                html_content = f"""
                <html>
                <head><title>{mod_name} - {variation_name} - {version_name}</title></head>
                <body>
                    <h1>{mod_name}</h1>
                    <h2>{variation_name}</h2>
                    <h3>{version_name}</h3>
                </body>
                </html>
                """
                html_path = os.path.join(folder_path, "index.html")
                create_html_file(html_path, html_content)

                # Generate ZIP file
                zip_name = f"{mod_id}-{variation_id}-{version_id}.zip"
                zip_path = os.path.join(output_dir, zip_name)
                create_zip_file(zip_path, folder_path)

if __name__ == "__main__":
    main()
