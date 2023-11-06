from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    # Verifica se o arquivo já foi processado anteriormente
    if not instance.is_empty() and \
            path_file in [item["nome_do_arquivo"] for item in instance.items]:
        print(f"Arquivo {path_file} já foi processado anteriormente.")
        return
    
    noticias = txt_importer(path_file)

    if noticias:
        # Cria um dicionário com informações do arquivo
        file_info = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(noticias),
            "linhas_do_arquivo": noticias
        }

        # Adiciona o dicionário à fila
        instance.enqueue(file_info)

        # Mostra as informações processadas
        print(file_info)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
