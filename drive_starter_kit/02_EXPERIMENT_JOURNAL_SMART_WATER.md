# EXPERIMENT_JOURNAL_SMART_WATER

> Preencher durante a execução. Não registrar como realizado algo que não aconteceu. Use NÃO EXECUTADO, PARCIAL ou NÃO CONFIRMADO quando aplicável.

## 1. Identificação
- Responsável: Eric Pimentel
- Data/hora local America/Belem:
- Repositório: https://github.com/enps2015/gemini-connected-apps-smart-water-lab
- Branch/commit importado (se visível):
- Modelo exatamente exibido no seletor Gemini:
- Objetivo: auditar o protótipo de detecção de anomalias e documentar o uso real dos Apps Conectados.

## 2. Questão do experimento
O Gemini consegue identificar limitações metodológicas e falhas potenciais no detector baseline, consultando o repositório e o dossiê do Drive, e recomendar testes específicos sem confundir dados sintéticos com telemetria real?

## 3. Inventário do Drive
| Arquivo | Caminho | Quem disponibilizou | Conteúdo | Estado no Gemini |
|---|---|---|---|---|
| GeminiLab_Telemetria_Sintetica | 01_DADOS_DE_ENTRADA | Eric; gerado por script do repo | 4.032 medições sintéticas; sem rótulos de eventos | PENDENTE |
| 02_DICIONARIO_DE_DADOS | 01_DADOS_DE_ENTRADA | Eric; copiado de data/data_dictionary.csv | Descrição, unidade e ressalvas de cada coluna | PENDENTE |
| 03_EVENTOS_DE_REFERENCIA_AVALIACAO | 01_DADOS_DE_ENTRADA | Eric; copiado de data/ground_truth_events.csv | 6 eventos para avaliação offline; proibido como entrada do detector | PENDENTE |
| 00_LEIA-ME_E_PLANO_DE_EXECUCAO | 00_GOVERNANCA_E_INDICE | Eric | Propósito, procedência e regras | PENDENTE |
| 01_INDICE_DE_FONTES | 00_GOVERNANCA_E_INDICE | Eric | Links e proveniência científica/produto | PENDENTE |
| 03_REGISTRO_DE_VIDEOS_YOUTUBE | 03_PESQUISA_YOUTUBE | Eric; preenchido após buscas reais | Resultados reais em pt-BR e inglês | PENDENTE |

## 4. Etapa A — GitHub
- Hora de início/fim:
- Ação da interface executada:
- Repositório/branch:
- Importação confirmada pela interface? SIM/NÃO:
- Arquivos que o Gemini nomeou corretamente:
- Resumo dos achados com caminhos de arquivos:
- Evidência/captura em 06_EVIDENCIAS:
- Limitações ou erros:

## 5. Etapa B — Google Workspace
- Prompt literal utilizado:
- Arquivos encontrados:
- Arquivos abertos/lidos:
- Cabeçalhos de telemetria devolvidos pelo Gemini:
- O modelo leu linhas de dados ou localizou apenas o nome do arquivo?
- Conferência manual contra data/data_dictionary.csv:
- Estado: CONFIRMADO / PARCIAL / NÃO CONFIRMADO / INDISPONÍVEL
- Evidência/captura:
- Erros e limitações:

## 6. Etapa C — YouTube em português
- Consulta literal:
- Título/canal/instituição/palestrante/data/URL:
- Credibilidade conferida? Como:
- Referências científicas citadas:
- Decisão: INCLUIR / REJEITAR / NENHUM RESULTADO ADEQUADO
- Justificativa:

## 7. Etapa D — YouTube em inglês
- Consulta literal:
- Title/channel/institution/speaker/date/URL:
- Credibility check:
- Primary references:
- Decision: INCLUDE / REJECT / NO SUITABLE RESULT
- Reason:

## 8. Etapa E — pesquisa de fontes primárias
- Consultas executadas:
- URLs abertas e verificadas:
- Afirmações confrontadas:
- Evidência encontrada:
- Lacunas:

## 9. Resultado do Gemini 4 Argon
- Nome/versionamento visível:
- Prompt integral usado:
- Resposta salva em:
- Achados por gravidade (CRÍTICO/ALTO/MÉDIO/BAIXO/OBSERVAÇÃO):
- Caminho/função/trecho que sustenta cada achado:
- Achados confirmados pela revisão humana:
- Afirmações não sustentadas/erradas:
- Recomendações aceitas:
- Recomendações rejeitadas e motivo:
- O modelo declarou ter executado tarefas que não foram executadas? Registrar frase e evidência:

## 10. Testes locais antes e depois
- Versão de Python/ambiente:
- Comando de teste:
- Testes antes:
- Métricas baseline:
- Mudanças aplicadas e commit:
- Testes depois:
- Métricas depois:
- Melhora comprovada:
- Regressões ou problemas restantes:

## 11. Conclusão
- O que era esperado:
- O que de fato foi entregue:
- O que foi validado:
- O que não foi validado:
- Limitações da simulação:
- Limitações dos Apps:
- Próximas melhorias priorizadas:

## 12. Evidências
- E01 — seletor do modelo:
- E02 — importação GitHub:
- E03 — análise de caminhos reais:
- E04 — Workspace:
- E05 — YouTube pt-BR:
- E06 — YouTube inglês:
- E07 — pesquisa científica:
- E08 — testes e métricas antes/depois:

## Regra de integridade
Resultados do simulador não são evidência de operação real de rede de água. Distinguir resultados do código local, saídas do Gemini, fontes externas e avaliação humana.