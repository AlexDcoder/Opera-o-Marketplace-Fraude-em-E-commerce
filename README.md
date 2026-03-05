# Projeto 02 — Operação Marketplace: Fraude em E-commerce

> **Disciplina:** Programação para Ciência de Dados
> **Curso:** MBA em Ciência de Dados — UNIFOR
> **Professor:** Cássio Pinheiro
> **Formato:** Datathon Investigativo
> **Trabalho:** Em duplas ou trios (formação livre)
> **Classificação:** Grupo A — Investigativo (padrões ocultos para descobrir)

---

## Briefing da Operação

A equipe de Trust & Safety de um e-commerce cearense detectou anomalias nas métricas de vendas e avaliações. Há suspeitas de que um **grupo de vendedores esteja manipulando avaliações** com contas falsas e operando um **esquema de vendas fraudulentas** com transações concentradas em horários atípicos. A diretoria precisa saber: quem são os vendedores fraudulentos, qual o impacto financeiro e como detectar esse padrão automaticamente.

Você recebeu acesso a três bases de dados. A fraude está escondida nos detalhes.

---

## Datasets Fornecidos

### 1. `data/projeto_02_ecommerce_vendas.csv`
Registro de 8.000 vendas realizadas em 2 anos.

| Coluna | Descrição |
|--------|-----------|
| `pedido_id` | Identificador único do pedido |
| `data_pedido` | Data do pedido |
| `hora_pedido` | Horário do pedido (HH:MM) |
| `vendedor_id` | Identificador do vendedor |
| `categoria` | Categoria do produto |
| `produto_id` | Identificador do produto |
| `preco_unitario` | Preço unitário (R$) — **atenção: pode conter erros de tipo** |
| `quantidade` | Quantidade comprada |
| `valor_total` | Valor total da venda (R$) |
| `frete` | Valor do frete (R$) |
| `estado_cliente` | Estado do comprador |
| `status_pedido` | Status (Entregue, Cancelado, Devolvido, Em trânsito) |
| `nota_avaliacao` | Nota da avaliação (1-5) |

### 2. `data/projeto_02_vendedores_perfil.csv`
Cadastro dos 120 vendedores da plataforma.

| Coluna | Descrição |
|--------|-----------|
| `vendedor_id` | Identificador do vendedor |
| `nome_loja` | Nome da loja |
| `data_cadastro` | Data de cadastro na plataforma |
| `cidade`, `estado` | Localização |
| `categoria_principal` | Categoria principal de venda |
| `total_vendas` | Total de vendas realizadas |
| `nota_media_loja` | Nota média da loja |
| `reclamacoes` | Número de reclamações |
| `verificado` | Se o vendedor é verificado (True/False) |

### 3. `data/projeto_02_avaliacoes_suspeitas.csv`
3.000 avaliações com metadados de rastreamento.

| Coluna | Descrição |
|--------|-----------|
| `avaliacao_id` | Identificador da avaliação |
| `vendedor_id` | Vendedor avaliado |
| `comprador_id` | Comprador que avaliou |
| `data_avaliacao` | Data da avaliação |
| `data_criacao_conta` | Data de criação da conta do comprador |
| `nota` | Nota atribuída (1-5) |
| `ip_origem` | IP de onde a avaliação foi feita |
| `texto_avaliacao` | Texto da avaliação |

---

## Missão

Investigue os dados e responda:

1. **Existem vendedores com padrão de vendas concentrado em horários atípicos** (madrugada, 2h-5h)? Quem são e qual o volume?
2. **Há avaliações falsas?** Identifique padrões: contas criadas há poucos dias que avaliam com nota 5, IPs repetidos, textos idênticos.
3. **Os vendedores suspeitos compartilham características em comum?** Cruze com o cadastro: data de cadastro próxima, mesma cidade, nomes similares, não verificados.
4. **Qual o impacto financeiro** das vendas dos vendedores suspeitos? Quanto representam do faturamento total?
5. **A taxa de cancelamento/devolução** dos vendedores suspeitos é diferente dos demais?
6. **Construa um "score de risco"** baseado nos indicadores encontrados. Quais critérios compõem esse score?
7. **Proponha regras automáticas** para detectar fraudes futuras baseadas nos padrões descobertos.

---

## Pistas Iniciais

- Filtre vendas entre **2h e 5h da manhã** — quem vende nesse horário?
- No dataset de avaliações, calcule os **dias entre criação da conta e a avaliação** — contas muito novas são suspeitas
- Procure **IPs repetidos** em avaliações de um mesmo vendedor
- No cadastro de vendedores, ordene por **data_cadastro** — há um cluster de cadastros na mesma semana?
- Atenção com a coluna `preco_unitario` — ela pode ter problemas de tipo

---

## Desafio de Dados Reais

Enriqueça sua investigação com dados públicos reais:

| Fonte | URL | O que buscar |
|-------|-----|-------------|
| **Dados Olist (Kaggle)** | https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce | Referência de padrões reais de e-commerce brasileiro |
| **Reclame Aqui** | https://www.reclameaqui.com.br/ | Padrões reais de reclamações em marketplaces |

**Perguntas de cruzamento:**
- O padrão de horário de compra do dataset é compatível com o comportamento real de consumidores brasileiros?
- A taxa de cancelamento encontrada está dentro da faixa normal do mercado?

---

## Técnicas Esperadas

| Módulo | Técnicas |
|--------|----------|
| **M1 — Python** | Conversão de tipos (`preco_unitario` com strings), manipulação de datas e horários, funções para scoring |
| **M2 — Pandas/NumPy** | `merge` entre 3 datasets, `crosstab`, `value_counts` normalizado, análise temporal com extração de hora, detecção de duplicatas por múltiplas colunas |
| **M3 — Visualização** | Histograma de horários de venda, scatter com regressão, barplots de comparação, heatmaps de concentração, subplots organizados |

---

## Estrutura do Projeto

```
projeto_02/
├── README.md          ← Este arquivo
├── data/              ← 3 datasets do projeto
├── notebooks/         ← Notebook(s) Jupyter com a investigação
├── scripts/           ← Scripts Python auxiliares (se necessário)
└── docs/              ← Documentação adicional, apresentação
```

## Entregáveis

1. **Notebook Python (.ipynb)** em `notebooks/` contendo:
   - Importação e inspeção dos 3 datasets
   - Limpeza e transformação (nulos, tipos, duplicatas, outliers)
   - Cruzamento entre datasets (merge/join)
   - Análise investigativa com estatísticas descritivas
   - Mínimo de **8 visualizações** (mix de Matplotlib e Seaborn)
   - Respostas à missão com **evidências nos dados**
   - Células Markdown narrando a investigação (storytelling)
   - Conclusões: quais vendedores são fraudulentos e como detectar

2. **Apresentação oral** (5-7 minutos) — arquivo em `docs/`

## Critérios de Avaliação

| Critério | Peso | O que será observado |
|----------|------|----------------------|
| **Limpeza e transformação dos dados** | 20% | Tratamento de nulos, duplicatas, tipos incorretos, outliers. Justificativa das decisões. |
| **Profundidade da investigação** | 25% | Cruzamento entre os 3 datasets. Respostas fundamentadas à missão. Descoberta de padrões ocultos. |
| **Qualidade e variedade das visualizações** | 20% | Mínimo 8 gráficos. Pelo menos 3 tipos diferentes. Títulos, rótulos, legendas. |
| **Storytelling investigativo** | 20% | Narrativa coerente. Evidências visuais. Conclusões defendidas com dados. Apresentação oral. |
| **Organização do código e boas práticas** | 15% | Código limpo. Funções quando apropriado. Notebook autoexplicativo. |

### Bonificações
- **Enriquecimento com dados reais** (integração de fonte pública): **+1.0 ponto**
- Uso criativo de feature engineering: **+0.5 ponto**
- Visualização avançada além do esperado: **+0.5 ponto**
- Análise adicional não solicitada com insights valiosos: **+0.5 ponto**

### Penalizações
- Notebook sem células Markdown explicativas: **-1.0 ponto**
- Gráficos sem título, rótulos ou legendas: **-0.5 ponto por gráfico**
- Código copiado sem adaptação (entre grupos): **nota zero para ambos**
- Entrega após o prazo: **-2.0 pontos por dia**

---

*Prof. Cássio Pinheiro — MBA Ciência de Dados — UNIFOR — 2026*
