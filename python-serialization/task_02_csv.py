import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convertit un fichier CSV en fichier JSON (data.json).

    Args:
        csv_filename (str): Le nom du fichier CSV à lire.

    Returns:
        bool: True si la conversion a réussi, False sinon.
    """
    try:
        # Lire le contenu CSV et le convertir en liste de dictionnaires
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        # Écrire les données dans un fichier JSON
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
