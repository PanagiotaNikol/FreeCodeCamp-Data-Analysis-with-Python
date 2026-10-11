# Page View Time Series Visualizer

## Overview

This project is part of the freeCodeCamp Data Analysis with Python curriculum. It analyzes daily page views on the freeCodeCamp forum from May 2016 to December 2019.

The objective is to identify trends in website traffic over time and visualize changes in page views across different periods.

## Features

- Loads and processes time series data using Pandas.
- Removes extreme values using percentile-based filtering.
- Creates a line plot to display daily page views over time.
- Creates a bar plot to compare average monthly page views across years.
- Creates box plots to examine yearly trends and monthly seasonality.

## Technologies Used

- **Python** — Programming language.
- **Pandas** — Data manipulation and time series analysis.
- **Matplotlib** — Plotting and visualization.
- **Seaborn** — Statistical visualization.

## Dataset

The project requires the `fcc-forum-pageviews.csv` dataset, which contains daily page view counts.

## How to Run

1. Install the required libraries:

   `pip install pandas matplotlib seaborn`

2. Place `fcc-forum-pageviews.csv` in the appropriate project directory.
3. Run the script:

   `python time_series_visualizer.py`

The script generates three visualizations: `line_plot.png`, `bar_plot.png`, and `box_plot.png`.

## Skills Demonstrated

- Time series data analysis.
- Data cleaning and outlier removal.
- Grouping data by year and month.
- Trend and seasonality analysis.
- Data visualization.

## Project Context

Completed as part of the freeCodeCamp Data Analysis with Python certification curriculum.
