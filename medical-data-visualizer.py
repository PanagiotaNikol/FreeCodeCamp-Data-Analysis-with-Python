import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
# Διαβάζουμε το dataset
df = pd.read_csv("medical_examination.csv")


# 2
# Υπολογίζουμε το BMI
# BMI = βάρος / ύψος^2
# Το ύψος μετατρέπεται από cm σε μέτρα
#
# BMI > 25 -> overweight = 1
# BMI <= 25 -> overweight = 0
df['overweight'] = (
    df['weight'] / ((df['height'] / 100) ** 2) > 25
).astype(int)


# 3
# Κανονικοποιούμε cholesterol και gluc:
# 1 = καλό -> 0
# >1 = κακό -> 1

df['cholesterol'] = df['cholesterol'].apply(
    lambda x: 0 if x == 1 else 1
)

df['gluc'] = df['gluc'].apply(
    lambda x: 0 if x == 1 else 1
)


# 4
def draw_cat_plot():

    # 5
    # Μετατρέπουμε τα δεδομένα σε long format
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=[
            'cholesterol',
            'gluc',
            'smoke',
            'alco',
            'active',
            'overweight'
        ]
    )

    # 6
    # Μετράμε πόσοι ασθενείς υπάρχουν
    # για κάθε κατηγορία και κάθε τιμή του cardio
    df_cat = (
        df_cat
        .groupby(['cardio', 'variable', 'value'])
        .size()
        .reset_index(name='total')
    )

    # 7
    # Δημιουργούμε το categorical plot
    sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar'
    )

    # 8
    # Παίρνουμε το figure που δημιουργήθηκε
    fig = plt.gcf()

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():

    # 11
    # Αφαιρούμε λανθασμένα δεδομένα
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    # Υπολογίζουμε τον correlation matrix
    corr = df_heat.corr()

    # 13
    # Δημιουργούμε mask για το πάνω τρίγωνο
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    # Δημιουργούμε το figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15
    # Δημιουργούμε το heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={'shrink': 0.5},
        ax=ax
    )

    # 16
    fig.savefig('heatmap.png')
    return fig