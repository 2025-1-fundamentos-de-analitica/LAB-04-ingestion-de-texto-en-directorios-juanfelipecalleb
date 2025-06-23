import os
import zipfile
import pandas as pd

def pregunta_01():
    # Rutas
    zip_path = "files/input.zip"
    extract_dir = "files/input"
    output_dir = "files/output"
    os.makedirs(output_dir, exist_ok=True)

    # Descomprimir zip
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall("files")

    # Procesar datos
    for split in ["train", "test"]:
        frases = []
        etiquetas = []
        split_path = os.path.join(extract_dir, split)

        for sentiment in ["positive", "negative", "neutral"]:
            folder = os.path.join(split_path, sentiment)
            for filename in os.listdir(folder):
                filepath = os.path.join(folder, filename)
                with open(filepath, encoding="utf-8") as f:
                    frases.append(f.read().strip())
                    etiquetas.append(sentiment)

        df = pd.DataFrame({"phrase": frases, "target": etiquetas})
        df.to_csv(os.path.join(output_dir, f"{split}_dataset.csv"), index=False)
