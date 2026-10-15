# 00 — LEIA-ME E PLANO DE EXECUÇÃO

**Autor e responsável pelo dossiê:** Eric Pimentel  
**Projeto:** Gemini Connected Apps × Smart Water Anomaly Lab  
**Repositório fonte:** https://github.com/enps2015/gemini-connected-apps-smart-water-lab

## Por que esta pasta do Drive existe?
Esta pasta reúne os documentos e cópias de trabalho que o Gemini deverá localizar através do Google Workspace. Os arquivos no GitHub **não aparecem automaticamente** no Google Drive. Eric é responsável por criar/importar os documentos descritos aqui.

## Estrutura exata a criar
No Google Drive > Meu Drive, crie a pasta raiz `GeminiLab_SmartWater` e dentro dela:
- `00_GOVERNANCA_E_INDICE`
- `01_DADOS_DE_ENTRADA`
- `02_FONTES_CIENTIFICAS`
- `03_PESQUISA_YOUTUBE`
- `04_DIARIO_DE_EXECUCAO`
- `05_RELATORIO_FINAL`
- `06_EVIDENCIAS`

## Inventário obrigatório
1. `00_GOVERNANCA_E_INDICE/00_LEIA-ME_E_PLANO_DE_EXECUCAO` — este conteúdo, convertido em Google Docs.
2. `00_GOVERNANCA_E_INDICE/01_INDICE_DE_FONTES` — Google Sheets a partir de `01_INDICE_DE_FONTES.csv`.
3. `01_DADOS_DE_ENTRADA/GeminiLab_Telemetria_Sintetica` — Google Sheets importada de `data/telemetry_synthetic_5min.csv` no GitHub.
4. `01_DADOS_DE_ENTRADA/02_DICIONARIO_DE_DADOS` — Google Sheets importada de `data/data_dictionary.csv`.
5. `01_DADOS_DE_ENTRADA/03_EVENTOS_DE_REFERENCIA_AVALIACAO` — Google Sheets importada de `data/ground_truth_events.csv`. **Apenas avaliação offline; não usar na primeira análise cega do Argon nem como entrada do detector.**
6. `03_PESQUISA_YOUTUBE/03_REGISTRO_DE_VIDEOS_YOUTUBE` — Google Sheets a partir de `03_REGISTRO_DE_VIDEOS_YOUTUBE.csv`, preenchida depois das buscas reais.
7. `04_DIARIO_DE_EXECUCAO/EXPERIMENT_JOURNAL_SMART_WATER` — Google Docs a partir de `02_EXPERIMENT_JOURNAL_SMART_WATER.md`.
8. `04_DIARIO_DE_EXECUCAO/04_REGISTRO_DE_USO_APPS` — Google Sheets a partir de `04_REGISTRO_DE_USO_APPS.csv`.
9. `05_RELATORIO_FINAL/ARGON_EXECUTION_REPORT` — Google Docs a partir de `05_RELATORIO_FINAL_TEMPLATE.md`, **somente após executar o experimento**.
10. `02_FONTES_CIENTIFICAS/` — links/notas dos estudos e documentação de produto citados em `docs/01_FUNDAMENTACAO_CIENTIFICA.md`, após abrir e conferir as fontes.
11. `06_EVIDENCIAS/` — capturas de tela produzidas durante a execução real.

## Origem e responsabilidade
- Eric disponibiliza no Drive as cópias de trabalho da telemetria, dicionário e eventos de referência, e cria o diário e os registros.
- A telemetria é sintética e gerada por `src/generate_synthetic_data.py`; não vem de uma companhia de saneamento.
- BattLeDIM e o estudo de Aghashahi et al. são fontes de fundamentação metodológica; não são a origem direta dos valores sintéticos.
- Vídeos só serão adicionados ao índice depois de localizados e conferidos; não inserir exemplos fictícios.
- Não expor documentos pessoais, dados internos da concessionária nem a pasta inteira por link público.

## Procedimento para CSVs
1. Baixe o arquivo CSV do GitHub.
2. No Drive, use Novo > Upload de arquivo ou, no Sheets, Arquivo > Importar > Fazer upload.
3. Use vírgula como separador, mantenha a primeira linha como cabeçalho e preserve os nomes das colunas.
4. Confira contagens: telemetria = 4.032 linhas de dados; eventos = 6; dicionário = 9 variáveis.
5. Confira uma amostra de linhas contra o CSV original.
6. Renomeie a planilha conforme o inventário acima.

## Teste real do Workspace
No Gemini Web, selecione Google Workspace no seletor de apps ou use `@Google Workspace` se o comando estiver disponível. Peça para localizar `GeminiLab_SmartWater`, `EXPERIMENT_JOURNAL_SMART_WATER`, `GeminiLab_Telemetria_Sintetica` e `02_DICIONARIO_DE_DADOS`. Exija que liste os arquivos encontrados e os cabeçalhos que conseguiu ler. Compare os cabeçalhos com `data/data_dictionary.csv`. Encontrar o título não prova que o conteúdo foi lido.

## Ordem de execução
1. Verificar fontes e preencher o índice.
2. Importar e conferir os CSVs.
3. Importar o repositório GitHub no Gemini (não basta colar uma URL no prompt).
4. Testar acesso a documentos e planilha pelo Google Workspace.
5. Executar as consultas do YouTube em português e inglês; registrar resultados reais, ou ausência de resultado adequado.
6. Rodar o prompt de `docs/03_PROMPT_GEMINI_ARGON.md`.
7. Guardar evidências e a resposta integral.
8. Executar localmente os testes antes/depois das mudanças aceitas.
9. Preencher o relatório final sem antecipar resultados.

## Estados obrigatórios por conector
- `CONFIRMADO`: o app foi acionado e o resultado retornado foi conferido.
- `PARCIAL`: app acionado, mas conteúdo ou operação incompleta.
- `NÃO CONFIRMADO`: não existe evidência que comprove uso.
- `INDISPONÍVEL`: operação não oferecida ou acesso negado.

## Nota de integridade
O app estar ativado não significa que foi utilizado. Uma sugestão do Argon não é uma alteração executada. Métricas de dados sintéticos não estimam desempenho em rede real.