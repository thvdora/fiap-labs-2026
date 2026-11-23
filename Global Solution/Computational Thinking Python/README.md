# Caminho Acessível introdução:
O Caminho Acessível é um programa em Python que permite registrar e monitorar problemas de acessibilidade, mobilidade e 
infraestrutura urbana, como ausência de rampas, calçadas irregulares, elevadores quebrados e falta de iluminação. O programa 
beneficia principalmente pessoas com deficiência, idosos e pedestres em geral, além das equipes de manutenção urbana, 
que passam a ter informações organizadas para priorizar atendimentos. O objetivo é classificar automaticamente a gravidade de 
cada ocorrência, organizá-las por categoria e gerar estatísticas que mostrem onde estão as maiores necessidades.

# Integrantes
- Nome: Isadora Soares Couto
- RM: 576852

## Problema escolhido
Falta de acessibilidade e problemas de infraestrutura urbana.

## ODS relacionados
- ODS 11 – Cidades e Comunidades Sustentáveis
- ODS 10 – Redução das Desigualdades

## Instruções de execução
1. Instalar o Python 3.x
2. Salvar o código como `caminho_acessivel.py`
3. Executar no terminal: `python caminho_acessivel.py`
4. Digitar `10` na tela inicial para acessar o sistema
5. Usar o menu:
   - 1 – Registrar problema (escolher local e tipo de problema)
   - 2 – Consultar problemas registrados
   - 3 – Filtrar problemas por gravidade
   - 4 – Visualizar estatísticas
   - 0 – Sair

## Regras de classificação

### Gravidade (automática, conforme o tipo de problema)
- Alta: riscos diretos à segurança ou barreiras que impedem a passagem.
- Média: dificultam a locomoção, mas não impedem totalmente.
- Baixa: problemas com menor impacto imediato.
- Problemas fora da lista recebem Média por padrão.

### Categorias
- Acessibilidade: rampas, elevadores, pisos táteis, banheiros, pontos de ônibus
- Mobilidade urbana: calçadas, faixas de pedestres, semáforos, alagamentos, vias
- Infraestrutura urbana: iluminação, lixo, buracos na calçada, pavimentação

## Resultados
O programa registra ocorrências com local, problema e gravidade, permite
consultá-las e filtrá-las por gravidade, e exibe estatísticas com o total
de registros, a quantidade por gravidade e por categoria. Isso permite
identificar rapidamente quais tipos de problema são mais frequentes e quais
exigem atendimento prioritário.

## Limitações e melhorias futuras
- Os dados ficam apenas em memória (são perdidos ao encerrar o programa)
- Futuras versões podem incluir banco de dados, mapa e estatísticas por região