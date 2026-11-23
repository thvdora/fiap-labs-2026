# 🤖 Machine Learning

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C)
![FIAP](https://img.shields.io/badge/FIAP-Faculdade-ED145B)

Atividades da disciplina de **Machine Learning**, com foco na base que sustenta qualquer modelo: **dados**. O repositório reúne o Checkpoint 1 (teoria e prática com Python, NumPy e Pandas) e exercícios de **estatística descritiva** e **visualização de dados**.

> **Aluna:** Isadora Soares Couto · **RM:** 576852
> **Curso:** _preencher_ · **Semestre:** _preencher_

---

## 📑 Sumário

- [Estrutura](#-estrutura)
- [Checkpoint 1](#-checkpoint-1)
- [Estatística descritiva](#-estatística-descritiva)
- [Visualização de dados](#-visualização-de-dados)
- [Como executar](#️-como-executar)

---

## 📂 Estrutura

```
Machine Learning/
├── Checkpoint 1/
│   ├── checkpoint_1_machine_learning.pdf
│   ├── total_com_desconto.py
│   ├── analise_temperaturas_numpy.py
│   └── analise_alunos_pandas.py
├── Estatistica/
│   └── estatistica.py
├── Visualizacao de dados/
│   ├── Grafico_de_linhas.py
│   ├── Grafico_de_barras.py
│   └── Grafico_de_dispersao.py
└── README.md
```

| Pasta | Tipo | Foco |
|---|---|---|
| Checkpoint 1 | 📝 Checkpoint | Conceitos de ML, listas e funções, NumPy e Pandas |
| Estatistica | Exercícios | Média, mediana, moda, variância e desvio padrão |
| Visualizacao de dados | Exercícios | Gráficos de linha, barras e dispersão com Matplotlib |

---

## 📝 Checkpoint 1

Avaliação com **6 questões**: três teóricas sobre os fundamentos de Machine Learning e três práticas em Python. A resolução completa, com as respostas escritas, está em `checkpoint_1_machine_learning.pdf`.

| # | Tipo | Tema | Arquivo |
|:---:|:---:|---|---|
| 1 | 📖 Teórica | O que é Machine Learning? | PDF |
| 2 | 💻 Prática | Listas e funções: manipulação de dados de vendas | `total_com_desconto.py` |
| 3 | 📖 Teórica | O papel dos dados no Machine Learning | PDF |
| 4 | 💻 Prática | NumPy: análise de dados numéricos | `analise_temperaturas_numpy.py` |
| 5 | 📖 Teórica | Tipos de aprendizado | PDF |
| 6 | 💻 Prática | Pandas: análise de dados de alunos | `analise_alunos_pandas.py` |

### 📖 Resumo da parte teórica

- **O que é Machine Learning:** prática de desenvolver programas em que o algoritmo analisa dados e **aprende padrões** com eles, para fazer previsões, classificações ou encontrar padrões. Na programação tradicional, é o programador quem define as regras.
- **O papel dos dados:** é a partir dos dados que o modelo aprende. A **quantidade** e a **qualidade** deles influenciam diretamente os resultados.
- **Tipos de aprendizado:**

| Tipo | Dados | Como aprende | Usos comuns |
|---|---|---|---|
| **Supervisionado** | Rotulados (já têm a resposta correta) | Compara as previsões com as respostas e se ajusta para errar menos | Classificação e regressão |
| **Não supervisionado** | Sem rótulos | Encontra padrões sozinho, sem resposta de referência | Agrupamento, descoberta de estruturas e relações |

### 💻 Parte prática

**Q2 — Total com desconto** (`total_com_desconto.py`)
Percorre uma lista de preços, aplica um desconto percentual a cada item e soma o total em uma função reutilizável.

```
Total com 20% de desconto: R$ 79.60
```

**Q4 — Temperaturas com NumPy** (`analise_temperaturas_numpy.py`)
Cria um array de 10 temperaturas e calcula a média (`np.mean`), o máximo (`np.max`) e quantos dias passaram de 25 °C, usando uma comparação booleana somada com `np.sum`.

```
Temperatura média: 24.5
Temperatura máxima: 29
Dias com temperatura superior a 25°C: 4
```

**Q6 — Alunos com Pandas** (`analise_alunos_pandas.py`)
Monta um `DataFrame` a partir de um dicionário, calcula a média de idade e filtra os alunos com nota maior ou igual a 8,0.

```
Média de idade: 21.2
   Nome  Idade  Nota
0   Ana     20   8.5
2 Carla     21   9.2
```

**Conceitos:** listas · funções com parâmetros e retorno · laço `for` · arrays NumPy e operações vetorizadas · `DataFrame` · filtragem booleana · f-strings com `:.2f`.

---

## 📊 Estatística descritiva

**Arquivo:** `estatistica.py`

Implementa as medidas estatísticas **do zero**, sem bibliotecas, em três exercícios.

| Exercício | Tema | Funções |
|:---:|---|---|
| 1 | Tempos de atendimento: tendência central | `calcular_media`, `calcular_mediana`, `calcular_moda` |
| 2 | Variância e desvio padrão | `calcular_variancia`, `calcular_desvio` |
| 3 | Comparação de desempenho entre a Turma A e a Turma B | reutiliza as funções acima |

| Medida | O que mostra |
|---|---|
| Média | Valor central da soma dos dados |
| Mediana | Valor do meio dos dados ordenados |
| Moda | Valor mais frequente |
| Variância | Média dos quadrados dos desvios em relação à média |
| Desvio padrão | Raiz da variância, que indica o quanto os dados se espalham |

**Ideia do Exercício 3:** duas turmas podem ter a **mesma média** e comportamentos muito diferentes. O desvio padrão revela quem é mais homogênea e quem é mais dispersa, e é por isso que a média sozinha não basta para descrever um conjunto de dados.

---

## 📈 Visualização de dados

Três desafios de um **dashboard de equipe de desenvolvimento**, feitos com **Matplotlib**, cada um usando um tipo de gráfico diferente.

| Desafio | Arquivo | Gráfico | Dados | O que mostra |
|:---:|---|---|---|---|
| 1 | `Grafico_de_linhas.py` | 📈 Linha | Deploys por mês em 2023 | Evolução ao longo do ano (de 12 em janeiro a 52 em dezembro) |
| 2 | `Grafico_de_barras.py` | 📊 Barras | Bugs resolvidos por tecnologia | Comparação entre Python, JavaScript, Java, TypeScript e Go, com o valor sobre cada barra |
| 3 | `Grafico_de_dispersao.py` | 🔴 Dispersão | Pontos de complexidade × horas gastas | Relação entre a complexidade e o tempo de refatoração de 10 tarefas (T1 a T10) |

**Recursos de Matplotlib praticados:**

- `plt.plot`, `plt.bar` e `plt.scatter`
- Personalização de cor, `alpha`, estilo de linha e marcadores
- `plt.text` para escrever os valores sobre as barras
- `plt.annotate` para rotular cada ponto do gráfico de dispersão
- `plt.grid`, `plt.xticks(rotation=45)` e `plt.ylim` para ajustar a leitura

---

## ▶️ Como executar

**Pré-requisito:** Python 3 e as bibliotecas usadas.

```bash
pip install numpy pandas matplotlib

# execute qualquer arquivo
python total_com_desconto.py
python Grafico_de_barras.py
```

> Os arquivos de `Visualizacao de dados` abrem uma janela com o gráfico (`plt.show()`).

---

<p align="center">Feito com 💜 durante a graduação na FIAP</p>
