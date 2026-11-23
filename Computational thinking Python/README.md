# 📝 Checkpoints — Pensamento Computacional com Python

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![FIAP](https://img.shields.io/badge/FIAP-Faculdade-ED145B)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success)

Resolução dos **Checkpoints** da disciplina, avaliações contínuas aplicadas ao longo do semestre. Os exercícios cobrem, de forma progressiva, entrada e saída de dados, operadores aritméticos, estruturas condicionais, funções, listas, matrizes e laços de repetição.

> **Curso:** _preencher_ · **Semestre:** _preencher_ · **Autor(a):** _preencher_ · **RM:** _preencher_

---

## 📑 Sumário

- [Estrutura de pastas](#-estrutura-de-pastas)
- [Visão geral](#-visão-geral)
- [Checkpoint 1](#-checkpoint-1--fundamentos)
- [Checkpoint 2](#-checkpoint-2--condicionais-e-funções)
- [Checkpoint 3](#-checkpoint-3--listas-matrizes-e-laços)
- [Como executar](#-como-executar)

---

## 📂 Estrutura de pastas

```
checkpoints/
├── checkpoint-1/
│   ├── pcp_checkpoint1_ex01.py
│   ├── pcp_checkpoint1_ex02.py
│   ├── pcp_checkpoint1_ex03.py
│   └── pcp_checkpoint1_ex04.py
├── checkpoint-2/
│   ├── pcp_checkpoint_ex01.py
│   └── pcp_checkpoint_ex02.py
├── checkpoint-3/
│   ├── cp3_q1.py
│   ├── cp3_q2.py
│   └── cp3_q3.py
└── README.md
```

## 🗺️ Visão geral

| Checkpoint | Exercícios | Conceitos principais |
|:---:|:---:|---|
| **1** | 4 | `input`, tipos de dados, operadores `/` `//` `%`, f-strings |
| **2** | 2 | `if / elif / else`, funções, strings, cálculos financeiros |
| **3** | 3 | listas, matrizes, `for`, `while`, `enumerate` |

---

## 🟢 Checkpoint 1 — Fundamentos

Foco em entrada de dados, conversões e operações aritméticas básicas.

| Arquivo | Exercício | O que faz |
|---|---|---|
| `pcp_checkpoint1_ex01.py` | 💱 Conversor de moedas | Recebe um valor em reais e converte para dólar, euro, peso argentino, libra e iene |
| `pcp_checkpoint1_ex02.py` | 🔢 Decomposição de número | Separa um inteiro de 0 a 999 em centena, dezena e unidade |
| `pcp_checkpoint1_ex03.py` | 📅 Idade em dias | Converte anos, meses e dias em total de dias |
| `pcp_checkpoint1_ex04.py` | 🔄 Dias em anos, meses e dias | Operação inversa: transforma dias em anos, meses e dias restantes |

**Destaques**

- **Ex. 1:** cada moeda é convertida dividindo o valor em reais pela cotação, com saída formatada em duas casas decimais (`:.2f`).
- **Ex. 2:** usa `%` para isolar a unidade e `//` para extrair dezenas e centenas.
- **Ex. 3 e 4:** adotam a simplificação de **1 ano = 365 dias** e **1 mês = 30 dias**. O ex. 4 combina `//` e `%` para encadear as divisões.

---

## 🟡 Checkpoint 2 — Condicionais e funções

Aplicação de decisões e modularização em problemas com regras de negócio.

| Arquivo | Exercício | O que faz |
|---|---|---|
| `pcp_checkpoint_ex01.py` | 🚚 Preço de frete por carga | Calcula o preço da carga e o imposto conforme o código da carga e o estado de origem |
| `pcp_checkpoint_ex02.py` | 💼 Resumo salarial | Calcula salário bruto, acréscimos, descontos e salário final de um funcionário |

### 🚚 Ex. 1 — Preço de carga e imposto

O peso é informado em toneladas e convertido para quilogramas. O preço por kg depende do código da carga:

| Código da carga | Preço por kg |
|:---:|:---:|
| 10 a 20 | R$ 100 |
| 21 a 30 | R$ 250 |
| 31 a 40 | R$ 340 |

O imposto incide sobre o preço da carga, de acordo com o estado de origem:

| Estado | 1 | 2 | 3 | 4 | 5 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Imposto** | 35% | 25% | 15% | 5% | isento |

**Saída:** preço da carga, imposto e preço total.

### 💼 Ex. 2 — Resumo salarial

Dividido em três funções, cada uma com uma responsabilidade:

| Função | Regra |
|---|---|
| `calcular_horas_extras` | 1,5% do salário base por hora extra |
| `calcular_descontos_faltas` | 2% do salário base por falta |
| `calcular_bonus` | Só se o funcionário recebeu bônus: Gerente R$ 1.000 · Analista R$ 500 · Assistente R$ 300 · Estagiário R$ 100 |

**Saída:** nome, salário bruto, total de acréscimos, total de descontos e salário final.

---

## 🔵 Checkpoint 3 — Listas, matrizes e laços

Manipulação de estruturas de dados e estruturas de repetição.

| Arquivo | Exercício | O que faz |
|---|---|---|
| `cp3_q1.py` | 📊 Notas da turma | Analisa listas de nomes e notas |
| `cp3_q2.py` | 🌡️ Temperaturas | Lê uma matriz 3×4 e calcula médias e extremos |
| `cp3_q3.py` | ➕ Ímpares e múltiplos | Soma ímpares e conta múltiplos até N |

### 📊 Q1 — Notas da turma

Com duas listas paralelas (`nomes` e `notas`), o programa exibe:

- média da turma;
- maior nota e o aluno correspondente;
- menor nota e o aluno correspondente;
- lista dos alunos com nota acima da média.

### 🌡️ Q2 — Matriz de temperaturas

O usuário digita 12 temperaturas, organizadas em uma matriz de **3 linhas (semanas) × 4 colunas**.

- A função `media_semanal` retorna a média de cada linha.
- Percorre a matriz com laços aninhados para achar a **maior** e a **menor** temperatura.
- Usa `enumerate` para exibir a média de cada semana.

### ➕ Q3 — Ímpares e múltiplos

Dado um número `N`:

1. Usa `while` para somar todos os **ímpares** de 1 até N.
2. Usa `for` para contar quantos números de 1 a N são **múltiplos de 2 e de 3** ao mesmo tempo (ou seja, múltiplos de 6).

---

## ▶️ Como executar

**Pré-requisito:** [Python 3](https://www.python.org/downloads/) instalado.

```bash
# clone o repositório
git clone <url-do-repositorio>
cd checkpoints

# execute qualquer exercício
python checkpoint-1/pcp_checkpoint1_ex01.py
```

Os programas pedem os dados pelo terminal, então basta seguir as instruções na tela.

---
