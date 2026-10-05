# Cadastro de Produtos Automatizado

Automação desenvolvida em Python para realizar o cadastro de produtos em um sistema web a partir de dados armazenados em um arquivo CSV.

O projeto utiliza **PyAutoGUI** para controlar o navegador e **Pandas** para ler e manipular os dados da planilha.

## 🚀 Funcionalidades

* Abre o Google Chrome automaticamente.
* Acessa o sistema de cadastro.
* Realiza o login automaticamente.
* Lê os produtos armazenados em `produtos.csv`.
* Percorre os produtos da tabela.
* Preenche automaticamente os campos do formulário.
* Cadastra cada produto.
* Retorna ao início da página para continuar o processo.

## 🛠️ Tecnologias utilizadas

* **Python**
* **PyAutoGUI** — automação de teclado e mouse.
* **Pandas** — leitura e manipulação dos dados do CSV.

## 📁 Estrutura do projeto

```text
Cadastro de Produtos Automatizado/
│
├── produtos.csv
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 📋 Formato do CSV

O arquivo `produtos.csv` deve possuir as seguintes colunas:

```text
codigo
marca
tipo
categoria
preco_unitario
custo
obs
```

Exemplo:

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
123,Apple,Eletrônico,Informática,5000,4000,Produto novo
456,Samsung,Eletrônico,Telefonia,2500,2000,
```

## ⚙️ Instalação

Clone o repositório:

```bash
git clone SEU_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd "Cadastro de Produtos Automatizado"
```

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## ▶️ Execução

Com o ambiente virtual ativado, execute:

```bash
python main.py
```

A automação irá abrir o navegador, acessar o sistema e iniciar o cadastro dos produtos presentes no arquivo `produtos.csv`.

## ⚠️ Observações

Este projeto utiliza coordenadas fixas de mouse, por exemplo:

```python
pyautogui.click(x=595, y=400)
```

Por isso, a automação depende da posição dos elementos na tela e pode precisar de ajustes caso:

* A resolução da tela seja alterada.
* O tamanho da janela do navegador seja diferente.
* O layout do site seja modificado.
* O navegador não esteja na posição esperada.

Além disso, o projeto foi desenvolvido com finalidade **educacional**, para praticar automação de tarefas, manipulação de arquivos CSV e utilização de bibliotecas Python.

## 📚 Objetivo do projeto

Este projeto foi desenvolvido como prática de:

* Automação de tarefas com Python.
* Manipulação de dados com Pandas.
* Leitura de arquivos CSV.
* Estruturas de repetição (`for`).
* Condicionais (`if`).
* Utilização de ambientes virtuais.
* Organização de projetos Python.
* Automação de interfaces gráficas com PyAutoGUI.

## 👨‍💻 Autor

**Cássio Rodrigues**

Desenvolvedor Backend Júnior
Python | Java | APIs REST | SQL | Docker
