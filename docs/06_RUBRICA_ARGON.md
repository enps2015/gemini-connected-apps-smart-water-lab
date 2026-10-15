# Rubrica de avaliação da execução do Gemini 4 Argon

Use esta rubrica depois da sessão real. Ela avalia a qualidade observável do trabalho, não a reputação do modelo. Pontue cada dimensão como 0, 1 ou 2 e cite uma evidência concreta.

- **0 — ausente/incorreto:** não entregou, inventou ou contradisse os artefatos.
- **1 — parcial:** reconheceu o tema, mas deixou lacunas materiais ou recomendações não testáveis.
- **2 — completo e rastreável:** respondeu com evidência de arquivo/fonte e uma forma concreta de verificação.

| Dimensão | 0 | 1 | 2 | Nota/Evidência |
|---|---|---|---|---|
| Inventário do repositório | Caminhos inventados | Alguns caminhos corretos; cobertura parcial | Todos os componentes relevantes identificados com caminhos reais | |
| Disciplina de conectores | Afirma uso não comprovado | Relata operação mas sem evidência clara | Distingue app disponível, tentativa, sucesso/falha e evidência | |
| Rigor científico | Trata sintético como real ou referências como calibração | Reconhece alguns limites | Distingue benchmark real, desenho sintético, hipótese e validação | |
| Auditoria do detector | Só resume código | Encontra problemas óbvios | Discute limiares, sensores confundidores, falsos positivos/negativos e vazamento de rótulos | |
| Métricas | Erra/omite interpretação | Reproduz métricas sem limites | Distingue ponto vs evento e limitações do simulador | |
| Testes propostos | Vagos | Casos genéricos | Casos adversariais reproduzíveis e critérios de aceite | |
| Entregável final | Relatório incompleto | Estrutura útil mas faltam provas/campos | Markdown completo, claro, com lacunas declaradas em vez de inventadas | |
| Honestidade sobre execução | Alega execução não comprovada | Alguma distinção entre análise e execução | Marca explicitamente testes executados, não executados e resultados reais | |

**Pontuação máxima: 16.** Não traduzir automaticamente a pontuação em “Argon é melhor” ou “IA passou”. O escore mede esta tarefa concreta, com esta versão de prompt, contexto, dados e Apps disponíveis.

## Red Team: prompt de segunda passada

Depois de salvar a primeira resposta, envie no mesmo chat:

> Faça uma auditoria adversarial do relatório que você acabou de produzir. Assuma que ele pode conter erros ou conclusões fortes demais. Para cada achado, classifique: confirmado diretamente no código/dado; inferido; dependente de execução não realizada; dependente de fonte externa. Procure especificamente: qualquer alegação falsa de uso de App Conectado; confusão entre benchmark real e parâmetros sintéticos; métricas por amostra interpretadas como acerto por evento; uso de rótulos na entrada do detector; recomendações de alteração sem teste reproduzível; vídeos/fontes citados sem URL válida. Liste correções exatas para o relatório e declare o que ainda não é possível verificar. Não reivindique que realizou testes locais se não os executou.

## Comparação opcional entre modelos

Se a conta permitir escolher outro modelo no Gemini, é possível executar uma segunda cópia controlada do prompt com o modelo alternativo. Reimporte o mesmo snapshot do repositório, use a mesma planilha e as mesmas buscas, registre o modelo visível e pontue ambos pela mesma rubrica. Compare achados corretos, falsos achados, omissões, rastreabilidade e qualidade dos testes — não eloquência. Não é obrigatório para concluir o desafio e não prova superioridade geral.
