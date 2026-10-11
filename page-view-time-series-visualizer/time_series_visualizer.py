import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()


# Import data
# Διαβάζουμε το CSV, μετατρέπουμε τη στήλη date σε ημερομηνία
# και τη χρησιμοποιούμε ως index.
df = pd.read_csv(
    "fcc-forum-pageviews.csv",
    parse_dates=["date"],
    index_col="date"
)


# Clean data
# Αφαιρούμε τις ακραίες τιμές:
# κάτω από το 2.5% και πάνω από το 97.5%.
df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
    # Κάνουμε αντίγραφο των δεδομένων
    df_line = df.copy()

    # Δημιουργούμε το line plot
    fig, ax = plt.subplots(figsize=(15, 5))

    ax.plot(
        df_line.index,
        df_line["value"]
    )

    # Τίτλος και labels
    ax.set_title(
        "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
    )
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image and return fig
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    # Δημιουργούμε στήλες για year και month
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month

    # Υπολογίζουμε τον μέσο όρο των page views
    # για κάθε μήνα κάθε έτους
    df_bar = (
        df_bar
        .groupby(["year", "month"])["value"]
        .mean()
        .unstack()
    )

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(15, 8))

    df_bar.plot(
        kind="bar",
        ax=ax
    )

    # Labels
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    # Ονόματα μηνών
    month_names = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    # Legend
    ax.legend(
        title="Months",
        labels=month_names
    )

    # Save image and return fig
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()

    df_box.reset_index(inplace=True)

    df_box['year'] = [
        d.year for d in df_box.date
    ]

    df_box['month'] = [
        d.strftime('%b') for d in df_box.date
    ]

    # Σειρά μηνών από January μέχρι December
    month_order = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    # Δημιουργούμε δύο box plots δίπλα-δίπλα
    fig, axes = plt.subplots(
        1,
        2,
        figsize=(15, 6)
    )

    # Year-wise Box Plot
    sns.boxplot(
        x="year",
        y="value",
        data=df_box,
        ax=axes[0]
    )

    axes[0].set_title(
        "Year-wise Box Plot (Trend)"
    )
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise Box Plot
    sns.boxplot(
        x="month",
        y="value",
        data=df_box,
        order=month_order,
        ax=axes[1]
    )

    axes[1].set_title(
        "Month-wise Box Plot (Seasonality)"
    )
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Save image and return fig
    fig.savefig('box_plot.png')
    return fig
