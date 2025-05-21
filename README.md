Solar Data Challenge - Week 0
Project Overview
This repository, solar-challenge-week1, contains the deliverables for the Week 0 challenge of the 10 Academy training program. The project focuses on analyzing solar radiation data from Benin, Sierra Leone, and Togo to support MoonLight Energy Solutions' strategic investment decisions for solar farm installations. The analysis aims to maximize operational efficiency, sustainability, and long-term return on investment.
The project includes:

Task 1: Git and environment setup with a reproducible workflow.
Task 2: Data profiling, cleaning, and exploratory data analysis (EDA) for each country's dataset.
Task 3: Cross-country comparison of solar potential.
Bonus: An interactive Streamlit dashboard to visualize insights.

Repository Structure
├── .github/workflows/ci.yml      # GitHub Actions workflow for CI
├── .gitignore                    # Excludes data/, .ipynb_checkpoints/, etc.
├── requirements.txt              # Project dependencies
├── README.md                     # Project documentation
├── final_report.md               # Final report summarizing all tasks
├── notebooks/                    # Jupyter notebooks for analysis
│   ├── benin_eda.ipynb           # EDA for Benin dataset
│   ├── sierraleone_eda.ipynb     # EDA for Sierra Leone dataset
│   ├── togo_eda.ipynb            # EDA for Togo dataset
│   ├── compare_countries.ipynb   # Cross-country comparison
├── app/                          # Streamlit dashboard
│   ├── __init__.py
│   ├── main.py                   # Main dashboard script
│   ├── utils.py                  # Utility functions for plotting
├── figures/                      # Saved plots from EDA and comparison
├── dashboard_screenshots/        # Dashboard screenshot
├── scripts/                      # Additional scripts (if any)
│   ├── __init__.py
│   ├── README.md
├── tests/                        # Test scripts (if any)
│   ├── __init__.py

Environment Setup
To reproduce the environment locally, follow these steps:

Clone the Repository:
git clone https://github.com/<your-username>/solar-challenge-week1.git
cd solar-challenge-week1


Set Up a Python Virtual Environment:
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate


Install Dependencies:
pip install -r requirements.txt

Dependencies include pandas, numpy, matplotlib, seaborn, scipy, windrose, and streamlit.

Verify CI Workflow:

The .github/workflows/ci.yml file runs pip install -r requirements.txt and checks the Python version on push or pull request.



Running the Streamlit Dashboard
The interactive dashboard visualizes solar data insights for Benin, Sierra Leone, and Togo.

Run Locally:
streamlit run app/main.py


Select a country from the dropdown to view GHI boxplots.
View the cross-country summary table.


Deployed URL:

Access the dashboard at: [Insert Streamlit Community Cloud URL here]
Note: Replace with the actual URL after deployment.


Screenshot:

A screenshot of the dashboard is available in dashboard_screenshots/dashboard.png.



Key Deliverables

Task 1: Git repository with .gitignore, requirements.txt, CI workflow, and organized folder structure.
Task 2: EDA notebooks (benin_eda.ipynb, sierraleone_eda.ipynb, togo_eda.ipynb) with:
Summary statistics, missing value reports, and outlier handling.
Time series, cleaning impact, wind rose, histograms, temperature-humidity scatter plots, and bubble charts.
Cleaned datasets saved to data/<country>_clean.csv (not committed, per .gitignore).


Task 3: compare_countries.ipynb with boxplots, summary table, ANOVA test, and GHI ranking bar chart.
Bonus: Streamlit dashboard with interactive country selection and visualizations.
Final Report: final_report.md summarizing all tasks with actionable insights and embedded figures.

Usage Instructions

Explore EDA:

Open notebooks/<country>_eda.ipynb to view data profiling and visualizations for each country.
Plots are saved in figures/.


Cross-Country Comparison:

Open notebooks/compare_countries.ipynb to see GHI, DNI, and DHI comparisons and statistical analysis.


Run the Dashboard:

Follow the instructions above to run locally or access the deployed version.



Notes

The data/ directory is excluded from version control (see .gitignore). Ensure you have the raw datasets (benin-malanville.csv, sierraleone-bumbuna.csv, togo-dapaong.csv) in data/ before running notebooks.
The project adheres to best practices for modular code, error handling, and Git hygiene with descriptive commit messages.

References

Pandas: https://pandas.pydata.org/docs/
Streamlit: https://docs.streamlit.io/
Windrose: https://windrose.readthedocs.io/
Seaborn: https://seaborn.pydata.org/

Prepared by: Oliyad Mulugeta
