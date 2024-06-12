# 🚀 Projeto: TING (Trybe is not Google)

## Sobre o Projeto

O projeto TING (Trybe is not Google) tem como objetivo desenvolver um programa capaz de simular um algoritmo de indexação de documentos, semelhante ao utilizado pelo Google. O programa será capaz de identificar ocorrências de termos em arquivos TXT, utilizando dois módulos principais: gerenciamento de arquivos e busca.

## 🛠️ Tecnologias e Habilidades

- **Linguagem Utilizada:** Python
- **Estruturas de Dados:** Pilhas, Deque, Nós e Listas Ligadas, Listas Duplamente Ligadas
- **Manipulação de Arquivos TXT**

## 📋 Funcionalidades Implementadas

### 01 - Módulo de Gerenciamento de Arquivos

1. **Implementação da Fila (Queue):** Implementação de uma fila FIFO (First-In, First-Out) para armazenar os arquivos que serão lidos. A fila deve ter métodos de inserção, remoção e busca.

2. **Função txt_importer:** Implementação de uma função capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador. A função lida com casos de arquivo não encontrado e formato inválido.

3. **Função process:** Transformação do conteúdo importado pela função `txt_importer` em um dicionário, que será armazenado na fila implementada. A função ignora arquivos já processados anteriormente.

4. **Função remove:** Implementação de uma função capaz de remover o primeiro arquivo processado da fila.

5. **Função file_metadata:** Implementação de uma função para apresentar as informações superficiais de um arquivo processado.

### 02 - Testes para a Classe PriorityQueue

Implementação de testes para a classe `PriorityQueue`, capaz de armazenar arquivos pequenos com prioridade na fila, de acordo com a quantidade de linhas do arquivo.

## 🔍 Como Editar ou Copiar o Projeto

1. Faça um fork deste repositório para sua conta do GitHub.
2. Clone o fork para sua máquina local usando o comando:
git clone git@github.com:JesusPastorini/Ting-Python.git
3. Navegue até o diretório do projeto:
cd nome_do_projeto
4. Crie um ambiente virtual e instale as dependências:
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r dev-requirements.txt

5. Edite ou utilize o projeto conforme desejado.

## 🚦 Pronto para Rodar

Para executar os testes do projeto, você pode utilizar o seguinte comando:
pytest
