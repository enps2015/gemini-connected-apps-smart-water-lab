# Especificação do dossiê Google Drive — Smart Water Anomaly Lab

**Responsável por disponibilizar os documentos no Drive:** Eric Pimentel.  
**Repositório fonte:** https://github.com/enps2015/gemini-connected-apps-smart-water-lab  
**Finalidade:** tornar reproduzível a etapa de consulta ao Google Workspace no Gemini Web.  
**Importante:** os arquivos de modelo deste repositório não aparecem automaticamente no Google Drive. Eric precisa criá-los/importá-los conforme estas instruções.

## 1. Pasta raiz e subpastas exatas

No Google Drive > Meu Drive, crie a pasta raiz:

`GeminiLab_SmartWater`

Crie nela as seguintes subpastas:

```text
GeminiLab_SmartWater/
├── 00_GOVERNANCA_E_INDICE/
├── 01_DADOS_DE_ENTRADA/
├── 02_FONTES_CIENTIFICAS/
├── 03_PESQUISA_YOUTUBE/
├── 04_DIARIO_DE_EXECUCAO/
├── 05_RELATORIO_FINAL/
└── 06_EVIDENCIAS/
```

Não disponibilize a pasta inteira por link público. Ela deve permanecer na conta do autor, acessível pelo conector autorizado do Google Workspace.

## 2. Arquivos obrigatórios e origem

| Caminho no Drive | Tipo a criar | Arquivo de origem / como criar | Quem fornece e o que contém |
|---|---|---|---|
| `00_GOVERNANCA_E_INDICE/00_LEIA-ME_E_PLANO_DE_EXECUCAO` | Google Docs | Copiar o conteúdo de `drive_starter_kit/00_LEIA-ME_E_PLANO_DE_EXECUCAO.md` | Eric cria o documento. Define escopo, procedência, sequência e regras de integridade. |
| `00_GOVERNANCA_E_INDICE/01_INDICE_DE_FONTES` | Google Sheets | Importar `drive_starter_kit/01_INDICE_DE_FONTES.csv` | Eric cria a planilha. Registra fontes científicas e documentação de produto. Os estados começam como pendentes; só marcar verificadas depois de abrir as fontes. |
| `01_DADOS_DE_ENTRADA/GeminiLab_Telemetria_Sintetica` | Google Sheets | Importar `data/telemetry_synthetic_5min.csv` do repositório | Eric disponibiliza a cópia de trabalho da telemetria gerada pelo script do projeto. São medições inteiramente sintéticas, 4.032 linhas, sem rótulos de ground truth. |
| `01_DADOS_DE_ENTRADA/02_DICIONARIO_DE_DADOS` | Google Sheets | Importar `data/data_dictionary.csv` | Eric cria a planilha a partir do dicionário incluído no repositório; descreve nomes, unidades, uso e ressalvas das colunas. |
| `01_DADOS_DE_ENTRADA/03_EVENTOS_DE_REFERENCIA_AVALIACAO` | Google Sheets | Importar `data/ground_truth_events.csv` | Eric disponibiliza os rótulos para avaliação offline. Não usar como feature nem como entrada do detector ou da primeira auditoria cega do Argon. |
| `03_PESQUISA_YOUTUBE/03_REGISTRO_DE_VIDEOS_YOUTUBE` | Google Sheets | Importar `drive_starter_kit/03_REGISTRO_DE_VIDEOS_YOUTUBE.csv` | Eric cria a planilha de registro. Completar somente com vídeos que tenham sido encontrados e verificados durante o experimento. |
| `04_DIARIO_DE_EXECUCAO/EXPERIMENT_JOURNAL_SMART_WATER` | Google Docs | Copiar `drive_starter_kit/02_EXPERIMENT_JOURNAL_SMART_WATER.md` | Eric registra data, modelo, prompts, acessos, resultados, falhas, validações e evidências reais. |
| `04_DIARIO_DE_EXECUCAO/04_REGISTRO_DE_USO_APPS` | Google Sheets | Importar `drive_starter_kit/04_REGISTRO_DE_USO_APPS.csv` | Eric mantém uma linha por tentativa/conector, com comando literal, resultado e estado. |
| `05_RELATORIO_FINAL/ARGON_EXECUTION_REPORT` | Google Docs | Usar `drive_starter_kit/05_RELATORIO_FINAL_TEMPLATE.md` só depois da execução | Eric produz o relatório final a partir do que foi realmente observado. Não preencher resultados antecipadamente. |
| `02_FONTES_CIENTIFICAS/` | Docs/PDF/atalhos conforme permitido | Adicionar notas e links às fontes de `docs/01_FUNDAMENTACAO_CIENTIFICA.md` após conferi-las | Eric organiza os registros bibliográficos originais. Não copiar material de terceiros sem necessidade e licença. |
| `06_EVIDENCIAS/` | Pasta com imagens | Capturas de tela produzidas durante a execução real | Eric salva evidências que comprovem o seletor de modelo, importação de código, uso do Workspace, resultados do YouTube e validação local. Ocultar dados pessoais desnecessários. |

## 3. Importação de CSV para Google Sheets

Repetir este procedimento para os quatro CSVs:

1. Baixe o arquivo no GitHub (botão **Raw** ou opção de download) ou use o arquivo dentro do ZIP do projeto.
2. Abra Google Drive > **Novo > Upload de arquivo** e envie o CSV; alternativamente, abra uma planilha vazia e use **Arquivo > Importar > Fazer upload**.
3. Selecione separador por vírgula. Mantenha a primeira linha como cabeçalho.
4. Preserve os nomes de coluna; não traduza nem renomeie campos nesta fase.
5. Confirme a contagem de linhas:
   - Telemetria: 4.032 linhas de dados, além do cabeçalho.
   - Eventos de referência: 6 eventos (além do cabeçalho).
   - Dicionário: 9 variáveis descritas (além do cabeçalho).
6. Confira manualmente as colunas e uma pequena amostra de linhas contra o CSV original no GitHub.
7. Renomeie a planilha exatamente conforme a tabela de arquivos obrigatórios.

**Separação dos dados:** a planilha de telemetria é a única planilha de medições que pode ser apresentada na etapa inicial de análise. Os rótulos de `ground_truth_events.csv` só entram na avaliação offline, após fixar as previsões, para reduzir risco de vazamento de rótulo.

## 4. Conteúdo exato do diário Google Docs

Use o modelo `02_EXPERIMENT_JOURNAL_SMART_WATER.md`. No mínimo, o diário precisa registrar:

- modelo exatamente exibido pelo seletor do Gemini;
- data e hora local;
- URL e branch do repositório importado e SHA do commit se for exibido;
- prompt literal usado;
- cada app tentado;
- cada arquivo que o Gemini alegou localizar e que conteúdo demonstrou ler;
- títulos, canais, palestrantes, datas e URLs reais dos vídeos;
- referências científicas abertas e afirmações que foram conferidas;
- achados do Argon, com caminhos de arquivo e evidência;
- quais recomendações foram aceitas/rejeitadas e por quê;
- comandos locais, resultados de testes e métricas antes/depois;
- limitações e etapas não concluídas.

## 5. Prompt de recuperação do Workspace

No Gemini Web, selecione o app Google Workspace pelo seletor ou use `@Google Workspace` se esse comando estiver disponível na interface:

> Localize no meu Google Drive a pasta GeminiLab_SmartWater. Dentro dela, localize os documentos 00_LEIA-ME_E_PLANO_DE_EXECUCAO e EXPERIMENT_JOURNAL_SMART_WATER, a planilha GeminiLab_Telemetria_Sintetica e a planilha 02_DICIONARIO_DE_DADOS. Informe separadamente quais arquivos encontrou e quais conseguiu abrir/ler. Para a planilha de telemetria, enumere os nomes das colunas exatamente como aparecem e informe se consegue acessar linhas de dados além do cabeçalho. Não estime nem invente conteúdo que não tenha lido. Não use a planilha 03_EVENTOS_DE_REFERENCIA_AVALIACAO para inferir/analisar eventos nesta primeira etapa. Se localizar o arquivo mas não conseguir ler o conteúdo, declare essa distinção expressamente.

Depois compare manualmente os cabeçalhos com `data/data_dictionary.csv`. Se o Gemini apenas localizar o título do arquivo, o uso do Workspace é **parcial**, não uma análise de dados confirmada.

## 6. Registro e validação do YouTube

Para as consultas exatas em pt-BR e inglês, consulte `docs/02_APPS_CONECTADOS.md`. Não inventar vídeos nem preencher os campos antecipadamente. Selecionar até dois vídeos somente após conferir o canal, instituição/autor, data, relevância e referências. Se nenhuma opção satisfizer os critérios, registrar que não foi encontrado material adequado na busca executada.

## 7. Política de verdade e limitações

- A pasta e os documentos operacionais do Drive são preparados por Eric.
- A telemetria é sintética e gerada pelo código do repositório; nenhum serviço do Google ou instituição de saneamento a forneceu.
- Artigos e benchmarks são de seus autores/instituições e servem de fundamentação metodológica, não de origem direta dos valores sintéticos.
- Ativação de app não prova uso. Localizar nome de arquivo não prova acesso ao conteúdo.
- O GitHub conectado ao Gemini analisa o snapshot de código importado; não assume que modifica ou sincroniza o repositório.
- Resultados só devem ser publicados depois de verificados. Não expor materiais privados nem dados operacionais de concessionárias.
