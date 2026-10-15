# Gemini Connected Apps × Smart Water Anomaly Lab

**Projeto demonstrativo de Eric Pimentel — Embaixadores Estudantis Google Brasil 2026**  
**Status:** protótipo reproduzível local; experimento com Gemini 4 Argon ainda precisa ser executado e documentado pelo autor.

> Este projeto é independente, educacional e não é um produto oficial do Google nem um projeto oficialmente endossado pela empresa. O dataset é sintético: não representa uma concessionária, não deriva diretamente de telemetria real e não deve ser usado para decisões operacionais.

## Problema

Como usar os Apps Conectados do Gemini para revisar um pequeno projeto de engenharia de dados que sinaliza possíveis anomalias em uma rede fictícia de abastecimento de água, com rastreabilidade, avaliação quantitativa e limitações explícitas?

## O que este repositório contém

- `data/telemetry_synthetic_5min.csv`: 4.032 linhas de telemetria sintética, 14 dias, amostragem de 5 minutos.
- `data/ground_truth_events.csv`: seis eventos conhecidos usados **somente para avaliação offline** (três eventos de vazamento e três cenários não vazamento/confundidores; os rótulos ficam fora das colunas da telemetria de entrada).
- `data/data_dictionary.csv`: descrição das variáveis, unidades, papel analítico e limitações.
- `src/generate_synthetic_data.py`: gerador determinístico, sem bibliotecas externas.
- `src/baseline_detector.py`: baseline transparente baseado em regras e produz previsões/métricas.
- `tests/test_data.py`: testes de integridade temporal, separação dos rótulos e faixas básicas.
- `docs/`: fundamentação científica, protocolo dos Apps Conectados, prompt para Argon e modelo de relatório.
- `outputs/baseline_metrics.json`: resultados do baseline deste dataset sintético; não são resultados de Argon nem desempenho no mundo real.

## Execução local

Requisitos: Python 3.10+; sem dependências Python externas.

```bash
python src/generate_synthetic_data.py
python src/baseline_detector.py
python -m unittest discover -s tests -v
```

O gerador usa uma semente fixa (`20261015`) para que a mesma versão do script produza dados reproduzíveis. O detector grava `outputs/baseline_predictions.csv` e `outputs/baseline_metrics.json`.

## Experimento com Gemini 4 Argon

1. No Gemini Web, escolha **Gemini 4 Argon** no seletor de modelo.
2. Importe este repositório pela interface **Adicionar arquivo → Mais uploads → Importar código**. Colar somente uma URL dentro do prompt não é equivalente a importar o repositório.
3. Use o prompt de `docs/03_PROMPT_GEMINI_ARGON.md`.
4. Para testar o Workspace, crie no seu próprio Google Drive uma Google Sheet a partir de `telemetry_synthetic_5min.csv` e um Google Doc chamado `EXPERIMENT_JOURNAL_SMART_WATER` com o registro do experimento. Não afirme que o Gemini acessou esses arquivos até que ele os encontre e use de fato.
5. Use o app YouTube para pesquisar material técnico institucional conforme as consultas em `docs/02_APPS_CONECTADOS.md`.
6. Salve a resposta integral de Argon como `reports/ARGON_EXECUTION_REPORT.md` (ou cole o resultado no arquivo local). O app GitHub conectado ao Gemini analisa o repositório importado; ele não escreve commits de volta no GitHub.
7. Registre o que ocorreu de fato, incluindo falhas, ferramentas não acionadas, alterações manuais e testes executados.

## Resultado local de referência

O baseline fixo detecta os vazamentos persistentes e o evento de ruptura, mas não detecta o microvazamento e sinaliza falsamente o cenário combinado de viés em dois sensores. A métrica por amostra é melhor que a métrica por evento; esse contraste foi intencional para evitar uma demonstração excessivamente fácil.

Consulte `outputs/baseline_metrics.json` e `docs/04_RELATORIO_EXPERIENCIA_TEMPLATE.md`. Esses resultados são do código local, não de uma execução do Gemini.

## Projeto relacionado

O autor mantém também [`smart-hydrometer-data-simulation`](https://github.com/enps2015/smart-hydrometer-data-simulation), uma iniciativa relacionada de simulação de hidrômetros inteligentes. Este repositório é separado para manter pequeno e reproduzível o estudo sobre pressão/vazão, cenários confundidores, avaliação de regras e Apps Conectados do Gemini.

## Limitações científicas

- Os padrões de variáveis e amostragem foram inspirados por literatura/benchmarks reais de monitoramento de redes de distribuição de água.
- As equações, amplitudes de eventos e limites usados no gerador são hipóteses didáticas criadas para produzir casos analisáveis. **Não foram calibradas com dados reais**, não aplicam as equações hidráulicas de EPANET e não representam parâmetros reais de uma rede.
- Métricas calculadas no dataset sintético medem apenas o comportamento neste simulador.
- O `ground_truth_events.csv` e os rótulos criados para avaliação não devem ser entradas do detector na inferência.

## Fontes primárias e referências

Veja [`docs/01_FUNDAMENTACAO_CIENTIFICA.md`](docs/01_FUNDAMENTACAO_CIENTIFICA.md) para contextualização e ligações para BattLeDIM, o dataset laboratorial de Aghashahi et al. (2023), documentação oficial do Gemini e instruções do conector GitHub.

## Licença e uso

O código e materiais deste repositório são disponibilizados sob MIT, exceto quando explicitamente indicado. Referências e conteúdos de terceiros permanecem sujeitos às respetivas licenças. A atribuição e os links das fontes devem ser mantidos. O dataset sintético é liberado para fins de ensino, com a advertência de que não é telemetria real.
