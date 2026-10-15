# Relatório da experiência — Gemini Connected Apps × Smart Water Anomaly Lab

**Status inicial: A EXECUÇÃO DO GEMINI AINDA NÃO FOI REALIZADA.** Preencher após a sessão real no Gemini Web. Não transformar os resultados do baseline local em resultados do Gemini Argon.

## 1. Identificação

- Autor: Eric Pimentel
- Programa: Embaixadores Estudantis Google Brasil 2026
- Projeto: Gemini Connected Apps × Smart Water Anomaly Lab
- Data/hora da sessão:
- Modelo selecionado na interface:
- Link do repositório:
- Branch/estado importado:
- Sistema/ambiente onde foram executados os testes locais:

## 2. O que era esperado

1. O Gemini importaria e analisaria o código do repositório pelo app GitHub.
2. O Gemini localizaria e utilizaria o diário e a Google Sheet no Workspace, ou reportaria a limitação real.
3. O app YouTube retornaria conteúdo técnico pertinente, identificável e acessível; links seriam verificados manualmente.
4. Os Serviços de pesquisa permitiriam rastrear as referências científicas primárias.
5. Argon produziria um relatório Markdown auditável com achados, referências, recomendações, limitações e plano de testes.
6. O relatório separaria resultados locais do código de resultados realmente obtidos na interface Gemini.

## 3. O que foi efetivamente entregue

| Item esperado | Resultado real | Evidência (link/captura/caminho) | Status | Observação |
|---|---|---|---|---|
| Importação GitHub | [preencher] | [preencher] | [preencher] | |
| Leitura do Workspace | [preencher] | [preencher] | [preencher] | |
| Busca YouTube em português | [preencher] | [preencher] | [preencher] | |
| Busca YouTube em inglês | [preencher] | [preencher] | [preencher] | |
| Conferência das fontes | [preencher] | [preencher] | [preencher] | |
| Relatório Argon | [preencher] | [preencher] | [preencher] | |
| Testes locais | [preencher] | [preencher] | [preencher] | |

## 4. Baseline local de referência (já executado antes da sessão Argon)

O baseline usa regras de limiar fixas sobre `inlet_flow_m3h`, `demand_proxy_m3h` e pressões P01/P03. Os números registrados em `outputs/baseline_metrics.json` pertencem exclusivamente ao dataset sintético e ao detector local.

| Métrica | Resultado local | Interpretação correta |
|---|---:|---|
| Precisão por amostra | 0,9649 | Proporção de amostras sinalizadas como vazamento que eram vazamento no rótulo sintético. |
| Recall por amostra | 0,9483 | Proporção de amostras rotuladas como vazamento que foram sinalizadas. |
| F1 por amostra | 0,9565 | Resumo de precisão e recall por amostra; não mede diretamente se cada evento foi encontrado. |
| Recall por evento de vazamento | 0,6667 (2/3) | O detector encontra dois eventos, mas perde completamente o microvazamento sintético. |
| Recall de amostras de deriva do sensor | 0,9083 | Detecção do rótulo sintético de deriva; não é desempenho em campo. |

O cenário combinado de viés em vazão e pressão produz alarmes falsos. Esse resultado foi incluído intencionalmente para mostrar que a mesma assinatura observável pode ter mais de uma causa.

## 5. Inventário dos Apps Conectados

| App | Operação real executada? | Resultado observado | Evidência | Limitação |
|---|---|---|---|---|
| GitHub | [sim/não] | | | |
| Google Workspace | [sim/não] | | | |
| YouTube | [sim/não] | | | |
| Serviços de pesquisa | [sim/não] | | | |

## 6. Achados do Argon

| ID | Achado | Gravidade | Caminho de arquivo | Evidência | Ação tomada |
|---|---|---|---|---|---|
| A-01 | [preencher] | | | | |

## 7. Testes e validações depois da sessão

- Comando de geração executado:
- Comando de teste executado:
- Resultado real de `python -m unittest discover -s tests -v`:
- Arquivos modificados manualmente após a resposta do modelo:
- Testes adicionais adicionados:
- Falhas que permanecem:

## 8. O que o experimento demonstrou

[Preencher com evidências observadas. Não afirmar que Argon foi superior a outro modelo sem um desenho comparativo consistente.]

## 9. O que não demonstrou

- Não demonstrou performance em dados reais de concessionárias.
- Não demonstrou que o modelo ou o detector pode tomar decisões operacionais sem validação.
- Não demonstrou superioridade geral do Argon, a menos que um comparador e um protocolo de avaliação tenham sido utilizados.

## 10. Melhorias futuras priorizadas

| Prioridade | Melhoria | Benefício | Esforço | Critério de aceite |
|---|---|---|---|---|
| P1 | Acrescentar casos adversariais e teste de evento, não só ponto | Reduzir falsos negativos e avaliações enganosas | Médio | Cenários identificados no relatório e testes passando |
| P2 | Comparar regras com métodos estatísticos/ML em divisão temporal | Estabelecer um baseline mais robusto | Médio/alto | Avaliação sem vazamento de dados e métricas por evento |
| P3 | Avaliar em benchmark público real com licença e documentação | Aproximar a avaliação de condições reais | Alto | Protocolo de calibração e validação documentado |
| P4 | Modelar rede no EPANET e gerar cenários hidráulicos | Ampliar a plausibilidade física | Alto | Parâmetros/fonte/calibração publicados |
| P5 | Melhorar auditoria de Apps Conectados e comparar modelos | Avaliar utilidade dos conectores/modelo, sem marketing | Médio | Matriz de evidências e rubric consistente |

## 11. Capturas e artefatos da experiência

- `evidence/argon_model_selected.png`
- `evidence/github_import.png`
- `evidence/workspace_access.png`
- `evidence/youtube_results_pt.png`
- `evidence/youtube_results_en.png`
- `reports/ARGON_EXECUTION_REPORT.md`
- `outputs/baseline_metrics.json`

Remover ou ocultar e-mails, informações de perfil, arquivos privados e identificadores desnecessários nas capturas.
