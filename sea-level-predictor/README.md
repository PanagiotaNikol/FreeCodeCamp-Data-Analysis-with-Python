# Sea Level Predictor

## Overview

This project is part of the freeCodeCamp Data Analysis with Python curriculum. It analyzes historical sea level measurements and uses linear regression to estimate future sea level changes through the year 2050.

The project explores long-term trends in sea level data and visualizes both historical measurements and predicted changes.

## Features

- Loads historical sea level data using Pandas.
- Creates a scatter plot of year versus adjusted sea level.
- Calculates a linear regression line using the historical dataset.
- Calculates a second regression line using data from the year 2000 onward.
- Extends the regression lines to estimate sea levels through 2050.
- Displays historical measurements alongside the predictions.

## Technologies Used

- **Python** — Programming language.
- **Pandas** — Data processing and analysis.
- **Matplotlib** — Data visualization.
- **SciPy** — Linear regression using `scipy.stats.linregress`.

## Dataset

The project requires the `epa-sea-level.csv` dataset, which contains historical sea level measurements.

## How to Run

1. Install the required libraries:

   `pip install pandas matplotlib scipy`

2. Place `epa-sea-level.csv` in the appropriate project directory.
3. Run the script:

   `python sea_level_predictor.py`

The script generates a visualization saved as `sea_level_plot.png`.

## Skills Demonstrated

- Historical data analysis.
- Scatter plot creation.
- Linear regression.
- Trend analysis and future estimation.
- Scientific computing with SciPy.

## Project Context

Completed as part of the freeCodeCamp Data Analysis with Python certification curriculum.
