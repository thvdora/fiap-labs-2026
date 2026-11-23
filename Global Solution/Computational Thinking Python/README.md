# ♿ Caminho Acessível

Programa em Python para **registrar e monitorar problemas de acessibilidade, mobilidade e infraestrutura urbana**, como ausência de rampas, calçadas irregulares, elevadores quebrados e falta de iluminação.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![ODS 10](https://img.shields.io/badge/ODS-10-DD1367?style=flat-square)
![ODS 11](https://img.shields.io/badge/ODS-11-F99D26?style=flat-square)

## 🎯 Sobre o projeto

O programa classifica **automaticamente a gravidade** de cada ocorrência, organiza os registros por **categoria** e gera **estatísticas** que mostram onde estão as maiores necessidades.

**Quem se beneficia**
- Pessoas com deficiência, idosos e pedestres em geral
- Equipes de manutenção urbana, que passam a ter informações organizadas para priorizar atendimentos

## 👩‍💻 Integrantes

| Nome | RM |
|---|---|
| Isadora Soares Couto | 576852 |

## 🌍 Problema e ODS

**Problema escolhido:** falta de acessibilidade e problemas de infraestrutura urbana.

| ODS | Tema |
|:-:|---|
| **11** | Cidades e Comunidades Sustentáveis |
| **10** | Redução das Desigualdades |

## ▶️ Como executar

1. Instale o Python 3.x
2. Salve o código como `caminho_acessivel.py`
3. Execute no terminal:
   ```bash
   python caminho_acessivel.py
   ```
4. Digite `10` na tela inicial para acessar o sistema
5. Use o menu:

| Opção | Ação |
|:-:|---|
| **1** | Registrar problema (escolher local e tipo de problema) |
| **2** | Consultar problemas registrados |
| **3** | Filtrar problemas por gravidade |
| **4** | Visualizar estatísticas |
| **0** | Sair |

## 📋 Regras de classificação

### Gravidade

Atribuída automaticamente, conforme o tipo de problema.

| Gravidade | Critério |
|:-:|---|
| 🔴 **Alta** | Riscos diretos à segurança ou barreiras que impedem a passagem |
| 🟠 **Média** | Dificultam a locomoção, mas não impedem totalmente |
| 🟢 **Baixa** | Problemas com menor impacto imediato |

> Problemas fora da lista recebem **Média** por padrão.

### Categorias

| Categoria | Problemas |
|---|---|
| **Acessibilidade** | Rampas, elevadores, pisos táteis, banheiros, pontos de ônibus |
| **Mobilidade urbana** | Calçadas, faixas de pedestres, semáforos, alagamentos, vias |
| **Infraestrutura urbana** | Iluminação, lixo, buracos na calçada, pavimentação |

## 📊 Resultados

O programa:
- registra ocorrências com **local**, **problema** e **gravidade**;
- permite **consultar** e **filtrar por gravidade**;
- exibe **estatísticas** com o total de registros e a quantidade por gravidade e por categoria.

Com isso, é possível identificar rapidamente quais tipos de problema são mais frequentes e quais exigem atendimento prioritário.

## 🚧 Limitações e melhorias futuras

- **Limitação:** os dados ficam apenas em memória e são perdidos ao encerrar o programa.
- **Próximas versões:** banco de dados, mapa e estatísticas por região.
