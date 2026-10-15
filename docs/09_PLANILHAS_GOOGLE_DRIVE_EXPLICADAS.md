# Planilhas do Google Drive — inventário explicado

Este documento elimina ambiguidades sobre quais arquivos CSV devem ser convertidos em Google Sheets, em que pasta ficam, por que existem e quando são utilizados.

## Primeiro: upload de CSV não é o mesmo que criar Google Sheets
O ZIP `GeminiLab_SmartWater_Drive_Starter_Kit_v2.zip` contém arquivos CSV de modelo e dados. Se eles foram simplesmente enviados ao Drive, continuam sendo arquivos CSV. Para criar cada planilha Google, abra uma planilha nova e use **Arquivo > Importar > Fazer upload**, escolhendo o CSV. Preserve cabeçalhos e separador por vírgula. Renomeie a planilha com o nome abaixo.

## As seis planilhas previstas

| Nº | Nome da planilha Google | Pasta no Drive | CSV de origem no starter kit | Finalidade | Quando usar |
|---|---|---|---|---|---|
| 1 | `GeminiLab_Telemetria_Sintetica` | `01_DADOS_DE_ENTRADA` | `CSV_PARA_IMPORTAR/telemetry_synthetic_5min.csv` | Cópia de trabalho dos sinais sintéticos (vazão, demanda, pressões, nível e bomba), sem rótulos de eventos. | Auditoria inicial de colunas e contexto dos sinais. |
| 2 | `02_DICIONARIO_DE_DADOS` | `01_DADOS_DE_ENTRADA` | `CSV_PARA_IMPORTAR/data_dictionary.csv` | Define o significado, unidade, papel e ressalvas de cada coluna. | Auditar a interpretação do modelo; comparar cabeçalhos e unidades. |
| 3 | `03_EVENTOS_DE_REFERENCIA_AVALIACAO` | Criar somente depois da primeira auditoria cega, em `01_DADOS_DE_ENTRADA` | `CSV_PARA_IMPORTAR/ground_truth_events.csv` | Contém os rótulos dos seis eventos conhecidos para avaliação offline. | Depois de congelar as previsões iniciais, comparar deteção e ground truth. **Não colocar no alcance do Gemini durante a primeira auditoria cega.** |
| 4 | `01_INDICE_DE_FONTES` | `00_GOVERNANCA_E_INDICE` | `01_INDICE_DE_FONTES.csv` | Registra instituição/autores, URL, tipo de fonte, finalidade e estado da verificação. | Durante a conferência das referências científicas e documentação de produto. |
| 5 | `03_REGISTRO_DE_VIDEOS_YOUTUBE` | `03_PESQUISA_YOUTUBE` | `03_REGISTRO_DE_VIDEOS_YOUTUBE.csv` | Registra títulos e URLs de vídeos realmente encontrados em português e inglês, instituição/canal, data e relevância. | Preencher após realizar as pesquisas; não inventar títulos nem resultados antecipados. |
| 6 | `04_REGISTRO_DE_USO_APPS` | `04_DIARIO_DE_EXECUCAO` | `04_REGISTRO_DE_USO_APPS.csv` | Diário tabular das ações de cada conector, prompt literal, arquivo/resultados, captura, validação e limitações. | Preencher durante cada tentativa de uso de GitHub, Workspace, YouTube e Serviços de pesquisa. |

## Procedimento de importação

1. No Google Drive, abra a pasta de destino especificada.
2. Clique em **Novo > Planilhas Google** para criar uma planilha vazia.
3. Na planilha, selecione **Arquivo > Importar > Fazer upload**.
4. Escolha o CSV de origem no kit descompactado. Se ainda só tiver o ZIP, extraia-o antes.
5. Escolha separador por vírgula e a opção de importar para a planilha atual (ou a opção equivalente disponível).
6. Confirme que a primeira linha virou cabeçalho e que a planilha não colocou todas as colunas em uma única célula.
7. Renomeie a planilha exatamente como a tabela.
8. Confira a contagem de linhas e os cabeçalhos contra o CSV original.

## Ordem crítica para evitar vazamento de rótulo

**Fase 1 — auditoria cega:** disponibilizar apenas `GeminiLab_Telemetria_Sintetica` e `02_DICIONARIO_DE_DADOS` ao Gemini. Não importar nem deixar acessível ao Gemini a planilha de ground truth nesta fase. Os rótulos são verdade-terreno reservada para avaliação.

**Fase 2 — avaliação offline:** após registrar e congelar a primeira previsão do detector, criar/importar `03_EVENTOS_DE_REFERENCIA_AVALIACAO` e calcular métricas localmente. Se os rótulos forem expostos ao modelo antes da previsão, registrar que a análise deixou de ser cega.

## Documentos Google Docs (não são planilhas)

- `00_LEIA-ME_E_PLANO_DE_EXECUCAO` — Google Docs, criado com o conteúdo do modelo Markdown.
- `EXPERIMENT_JOURNAL_SMART_WATER` — Google Docs, diário da sessão real.
- `ARGON_EXECUTION_REPORT` — Google Docs, relatório final preenchido após executar.
- `02_FONTES_CIENTIFICAS` — pasta para links/notas/PDFs cuja procedência foi verificada.
- `06_EVIDENCIAS` — pasta com capturas reais de tela e resultados de testes.

## O que a conexão Workspace deve comprovar
Na primeira consulta, o Gemini deve localizar e, se possível, ler `EXPERIMENT_JOURNAL_SMART_WATER`, `GeminiLab_Telemetria_Sintetica` e `02_DICIONARIO_DE_DADOS`. Ele deve enumerar os cabeçalhos exatos. Achar o título do arquivo não prova que leu a planilha. Compare as colunas retornadas manualmente com o CSV/dicionário do repositório.

## Responsabilidade e origem
Eric Pimentel cria o dossiê e importa cópias de trabalho. Os CSVs de telemetria, dicionário e eventos vêm do repositório deste projeto; a telemetria é gerada por código e inteiramente sintética. Os artigos/benchmarks citados no índice são fontes de fundamentação, não fornecedores dos valores sintéticos. As pesquisas de YouTube só podem ser registradas depois de realizadas.
