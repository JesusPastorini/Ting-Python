from pathlib import Path
import sys


def txt_importer(path_file):
    # Verifica se o arquivo existe
    file_path = Path(path_file)
    if not file_path.exists():
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        return []
    
    # Verifica a extensão do arquivo
    file_extension = file_path.suffix.lower()
    if file_extension != ".txt":
        sys.stderr.write("Formato inválido\n")
        return []
    
    # Lê o conteúdo do arquivo e retorna as linhas
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')
        return lines
