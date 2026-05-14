"""
Gera uma imagem de exemplo da tabela do report, com dados ficticios,
para ilustrar o README sem precisar conectar ao banco/Slack reais.

Uso:
    python docs/gerar_exemplo.py
"""
import matplotlib.pyplot as plt
import pandas as pd

COR_VERDE = '#2EA407'
COR_VERMELHO = '#E46B6B'
COR_LARANJA = '#F3A07D'
COR_VERDE_CLARO = '#9AC09A'
COR_AZUL_CLARO = 'lightblue'


def ajustar_celula(celula, valor):
    if valor < 0:
        celula.set_facecolor(COR_VERDE)
        celula.set_text_props(text=f"{round(valor, 2)}%", color='white')
    elif valor > 0:
        celula.set_facecolor(COR_VERMELHO)
        celula.set_text_props(text=f"{round(valor, 2)}%", color='white')
    else:
        celula.set_facecolor('white')
        celula.set_text_props(text="-", color='black')


tabela = {
    "": [
        "Padrão Média dia Útil Ago/Out 2025",
        "WhatsApp D-7 Quarta-Feira|07/05",
        "Chat D-7 Quarta-Feira|07/05",
        "Telefone D-7 Quarta-Feira|07/05",
        "Consolidado D-7 Quarta-Feira|07/05",
        "WhatsApp Quarta-Feira | 14/05",
        "Chat Quarta-Feira | 14/05",
        "Telefone Quarta-Feira | 14/05",
        "Consolidado Quarta-Feira | 14/05",
        "% Comparado ao Padrão",
        "% Comparado a Semana Anterior",
    ],
    "00:00 as 10:00": [320, 142, 88, 41, 271, 138, 84, 39, 261, 0, 0],
    "00:00 as 14:00": [510, 228, 141, 64, 433, 235, 152, 71, 458, 0, 0],
    "00:00 as 18:00": [780, 352, 217, 98, 667, 368, 234, 105, 707, 0, 0],
}

percentual_padrao = [
    (261 - 320) / 320 * 100,
    (458 - 510) / 510 * 100,
    (707 - 780) / 780 * 100,
]
percentual_semana = [
    (261 - 271) / 271 * 100,
    (458 - 433) / 433 * 100,
    (707 - 667) / 667 * 100,
]

df = pd.DataFrame(tabela)

plt.figure(figsize=(10, 5))
plt.axis('tight')
plt.axis('off')

col_widths = [0.3, 0.1, 0.1, 0.1]
table = plt.table(
    cellText=df.values,
    colLabels=df.columns,
    cellLoc='center',
    loc='center',
    colWidths=col_widths,
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.7, 1.7)

table[0, 0].set_text_props(text="Suporte (exemplo)")
for col in range(4):
    table[0, col].set_facecolor(COR_AZUL_CLARO)

for col in range(4):
    table[1, col].set_facecolor('white')

for linha in (2, 3, 4, 5):
    for col in range(4):
        table[linha, col].set_facecolor(COR_LARANJA)

for linha in (6, 7, 8, 9):
    for col in range(4):
        table[linha, col].set_facecolor(COR_VERDE_CLARO)

table[10, 0].set_facecolor('white')
ajustar_celula(table[10, 1], percentual_padrao[0])
ajustar_celula(table[10, 2], percentual_padrao[1])
ajustar_celula(table[10, 3], percentual_padrao[2])

table[11, 0].set_facecolor('white')
ajustar_celula(table[11, 1], percentual_semana[0])
ajustar_celula(table[11, 2], percentual_semana[1])
ajustar_celula(table[11, 3], percentual_semana[2])

plt.title("Report Diário Suporte (exemplo) | 14/05 | 18:00", fontsize=14)

saida = "docs/exemplo.png"
plt.savefig(saida, format='png', bbox_inches='tight', dpi=200)
plt.close()
print(f"Imagem salva em: {saida}")
