# Prompt principal — Gemini 4 Argon

> Antes de enviar: selecione explicitamente **Gemini 4 Argon**, importe este repositório pelo fluxo GitHub → Importar código e confira se a planilha `GeminiLab_Telemetria_Sintetica` e o documento `EXPERIMENT_JOURNAL_SMART_WATER` estão no seu Drive. Se o app não encontrar um arquivo, não prossiga como se tivesse acesso.

---

Atue como **revisor sênior de engenharia de software e dados**, com experiência em telemetria SCADA, redes de distribuição de água, detecção de anomalias e avaliação de sistemas de IA. Esta tarefa faz parte de um experimento educacional aberto de Eric Pimentel para demonstrar os Apps Conectados do Gemini.

## Objetivo

Auditar o repositório `gemini-connected-apps-smart-water-lab`, compreender as regras de baseline, investigar os limites dos dados sintéticos e produzir um relatório técnico com recomendações testáveis. Não produza marketing genérico nem afirme que o protótipo detecta vazamentos reais.

## Apps Conectados e operações

1. **GitHub:** o repositório foi importado para esta conversa pela função “Importar código”. Leia os arquivos realmente anexados. Não alegue que pode ver commits posteriores nem gravar alterações diretamente no repositório.
2. **Google Workspace:** use `@Google Workspace` para localizar `EXPERIMENT_JOURNAL_SMART_WATER` e `GeminiLab_Telemetria_Sintetica` na pasta `GeminiLab_SmartWater`. Primeiro informe se encontrou cada recurso; depois informe os cabeçalhos que conseguiu ler. Se não conseguir acessar valores da planilha, diga explicitamente e prossiga apenas com os arquivos importados do GitHub.
3. **YouTube:** execute as duas consultas detalhadas em `docs/02_APPS_CONECTADOS.md`: uma em português brasileiro, outra em inglês. Priorize universidades, grupos de pesquisa, palestrantes identificados e workshops técnicos. Retorne links reais; não invente vídeos. Resuma as técnicas como contexto, não como prova final.
4. **Serviços de pesquisa:** confirme a fundamentação com o benchmark BattLeDIM e o artigo de Aghashahi et al. (2023), conforme links em `docs/01_FUNDAMENTACAO_CIENTIFICA.md`.

Em sua resposta final, inclua uma tabela com colunas `App`, `operação tentada`, `resultado observado`, `evidência`, `limitação`. Diferencie “app ativado” de “operação concluída”.

## Restrições científicas e de integridade

- Todo dado de `telemetry_synthetic_5min.csv` é sintético, gerado por um modelo didático. Não foi calibrado com telemetria real e não representa uma concessionária.
- As referências citadas fundamentam a escolha geral de sinais e cenários, não validam os parâmetros numéricos do gerador.
- Use `ground_truth_events.csv` e `baseline_metrics.json` somente para avaliação offline. Não utilize rótulos ou identificadores de eventos como entradas do detector.
- As regras e os limiares são hipóteses. Não sugerir seu uso operacional sem calibração e validação em dados reais autorizados.
- Não invente testes executados, saídas de terminal, métricas, resultados dos conectores, títulos de vídeos ou fontes.
- Quando não houver execução de código disponível nesta conversa, declare isso e indique exatamente o comando local necessário. Não afirme ter rodado testes somente por ter inspecionado os arquivos.
- Use referências de arquivo por caminho. Para cada conclusão técnica, indique se é evidência direta do código/dados, inferência ou recomendação.
- Não revele raciocínio privado passo a passo. Apresente conclusões auditáveis, fundamentos resumidos, testes e limitações.

## Uso intencional dos recursos do Argon

Estruture a tarefa em fases: (1) inventário e Apps, (2) base científica e dados, (3) revisão do detector/testes, (4) relatório final. Ao concluir cada fase, forneça uma atualização curta com concluído, bloqueios e próxima etapa. Isso permite acompanhar a tarefa longa sem confundir atualização de progresso com evidência de execução. Explore o raciocínio multi-etapas e a revisão de código do modelo, mas valide cada afirmação com caminhos reais e testes. Não presuma que os recursos divulgados garantem uma resposta correta nesta tarefa.

## Tarefas técnicas obrigatórias

### A. Inventário e arquitetura

1. Mapear `src/generate_synthetic_data.py`, `src/baseline_detector.py`, `tests/test_data.py`, arquivos em `data/` e métricas em `outputs/`.
2. Desenhar o fluxo: geração sintética → telemetria sem rótulos → regras de detecção → avaliação com verdade-terreno separada.
3. Identificar dependências, constantes/limiares e qualquer ponto em que o código use rótulos como feature.

### B. Revisão da validade do dataset

1. Verificar número de linhas, cadência temporal, campos, valores ausentes/duplicados aparentes e faixas básicas que o código permite inspecionar.
2. Comparar as escolhas metodológicas do protótipo com o que as fontes científicas realmente documentam.
3. Listar explicitamente as simplificações que impedem tratar os dados como simulação hidráulica calibrada.
4. Identificar riscos de circularidade: o gerador cria padrões artificialmente fáceis para as regras? O dataset contém eventos confundidores adequados?

### C. Revisão do detector

1. Explicar as fórmulas e limiares usados para `leak_candidate` e `sensor_fault_candidate`.
2. Analisar métricas por amostra e por evento, separadamente. Explicar por que uma métrica alta por amostra pode coexistir com a perda completa de um vazamento curto/sutil.
3. Examinar o efeito de viés simultâneo em dois sensores e o evento legítimo de aumento de demanda.
4. Propor ao menos cinco melhorias com prioridade, benefício esperado, custo/complexidade, risco e arquivo que seria alterado.
5. Escrever pelo menos cinco casos de teste adversarial concretos: vazamento sutil, deriva de sensor, sensor travado, aumento legítimo de demanda e falha de medição que imita vazamento.

### D. Reprodutibilidade

Indique os comandos exatos para regenerar os dados, executar o detector e testar o código. Se a execução for realizada no ambiente local pelo autor, liste quais saídas devem ser guardadas e como compará-las com `outputs/baseline_metrics.json`.

### E. Entregável obrigatório

Produza o conteúdo integral de um arquivo Markdown chamado `reports/ARGON_EXECUTION_REPORT.md`, pronto para ser salvo manualmente pelo autor. Deve incluir:

1. Resumo executivo.
2. Escopo e versão/estado do material analisado.
3. Inventário dos arquivos/caminhos efetivamente inspecionados.
4. Tabela dos Apps Conectados: tentativa, operação concluída, evidência e limitações.
5. Fundamentação científica e distinção entre referência real e dado sintético.
6. Arquitetura e fluxo de dados.
7. Achados classificados por gravidade (`Crítico`, `Alto`, `Médio`, `Baixo`), com caminho/trecho e impacto.
8. Métricas do baseline e limites de interpretação.
9. Recomendações testáveis e plano de melhorias priorizado.
10. Resultados dos testes — somente se foram executados; caso contrário, `não executado`.
11. O que era esperado vs. o que foi efetivamente entregue.
12. Limitações, ameaças à validade e lições aprendidas.
13. Anexo: respostas às consultas do YouTube com links reais encontrados, ou declaração de que a busca não foi concluída.

No início, inclua data de execução, nome do modelo exibido na interface e quais Apps foram efetivamente acionados. Se alguma informação estiver indisponível, use `[PREENCHER APÓS EXECUÇÃO]`, não adivinhe.

### F. Formato de resposta

Comece com um resumo executivo de até 10 linhas. Em seguida, apresente as tabelas e o relatório Markdown completo. Separe claramente: `observado`, `inferido`, `recomendado` e `não verificado`. Seja preciso, crítico e útil para um estudante que queira reproduzir o caso.
