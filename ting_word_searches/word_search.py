def exists_word(word, instance):
    result = []

    for item in instance.items:
        filename = item["nome_do_arquivo"]
        lines = item["linhas_do_arquivo"]

        occurrences = []
        for line_num, line in enumerate(lines, start=1):
            if word.lower() in line.lower():  # busca case insensitive
                occurrences.append({"linha": line_num})

        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": filename,
                "ocorrencias": occurrences
            })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
