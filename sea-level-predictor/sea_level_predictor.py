import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Διαβάζουμε το dataset
    df = pd.read_csv("epa-sea-level.csv")

    # Δημιουργούμε scatter plot
    plt.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # --------------------------------------------------
    # ΠΡΩΤΗ ΓΡΑΜΜΗ ΠΡΟΒΛΕΨΗΣ
    # Χρησιμοποιούμε όλα τα διαθέσιμα δεδομένα
    # --------------------------------------------------

    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Δημιουργούμε τα έτη από το πρώτο έτος μέχρι το 2050
    years_extended = pd.Series(
        range(df["Year"].min(), 2051)
    )

    # Υπολογίζουμε τις προβλεπόμενες τιμές sea level
    sea_level_predicted = slope * years_extended + intercept

    # Σχεδιάζουμε την πρώτη γραμμή
    plt.plot(
        years_extended,
        sea_level_predicted
    )

    # --------------------------------------------------
    # ΔΕΥΤΕΡΗ ΓΡΑΜΜΗ ΠΡΟΒΛΕΨΗΣ
    # Χρησιμοποιούμε μόνο δεδομένα από το 2000 και μετά
    # --------------------------------------------------

    df_recent = df[df["Year"] >= 2000]

    # Νέο linear regression μόνο για τα δεδομένα από το 2000
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    # Δημιουργούμε έτη από το 2000 μέχρι το 2050
    years_recent = pd.Series(
        range(2000, 2051)
    )

    # Υπολογίζουμε τις προβλεπόμενες τιμές
    sea_level_predicted_recent = (
        slope_recent * years_recent + intercept_recent
    )

    # Σχεδιάζουμε τη δεύτερη γραμμή
    plt.plot(
        years_recent,
        sea_level_predicted_recent
    )

    # --------------------------------------------------
    # Labels και τίτλος
    # --------------------------------------------------

    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
