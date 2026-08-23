# Data Analyst Journey

## Analytics Portfolio in Progress

A practical data analytics portfolio documenting progression from Python fundamentals to exploratory analysis, data preparation, and business intelligence reporting. The repository combines focused practice scripts, interactive Jupyter notebooks, Pandas workflows, and Power BI dashboards built around real analysis tasks.

## Repository Structure

| Status | Directory | Focus |
| --- | --- | --- |
| [x] Done | [`Basic-python-revision/`](Basic-python-revision/) | Python fundamentals, core data structures such as dictionaries and lists, and practice scripts. |
| [x] Done | [`Data-Analytics-Jupyter/`](Data-Analytics-Jupyter/) | Interactive exploratory data analysis notebooks for investigation, visualization, and communicating findings. |
| [ ] In progress | [`Data-Analytics-pandas/`](Data-Analytics-pandas/) | Data manipulation, cleaning, and aggregation workflows using Pandas. |
| [x] Done | [`Powerbi/`](Powerbi/) | End-to-end business intelligence projects, Power Query transformations, data modeling, and dashboard visualizations. Includes `Project.pbix` and `chart.jpeg`. |

## Completed Work

- [x] Python revision scripts and core data structure practice
- [x] Exploratory analysis notebooks in Jupyter
- [x] HR employee data cleaning and headcount dashboard in Power BI
- [ ] Pandas data manipulation and aggregation workflows

## Featured Project: HR Headcount Analysis

### Power BI Department & Employee Analysis

This Power BI project transforms employee records into a clear view of departmental staffing. The workflow uses Power Query to clean raw data, split full names into `First Name` and `Last Name`, standardize unique employee IDs, and prepare the dataset for analysis.

The dashboard visualizes headcount by department, with **Sales** leading the distribution, followed by **Procurement** and **Finance**. The result provides a direct view of the organization’s operational structure and supports role and workforce analysis.

![HR Department and Employee Data Analysis dashboard](./Powerbi/chart.jpeg)

See the detailed project documentation in [`Powerbi/README.md`](Powerbi/README.md).

## Tech Stack & Tools

| Category | Technologies |
| --- | --- |
| Languages | Python, M (Power Query) |
| Libraries and environments | Pandas, Jupyter |
| Development and BI tools | Power BI Desktop, VS Code, Git |

## How to Run and Navigate

### Python Scripts

1. Open a terminal in the relevant directory.
2. Run a script with:

	```bash
	python script_name.py
	```

	Example:

	```bash
	python Basic-python-revision/dictionaries.py
	```

### Jupyter Notebooks

1. Open `Data-Analytics-Jupyter/Explore.ipynb` or another `.ipynb` file in VS Code with the Jupyter extension installed, or launch Jupyter from the repository root:

	```bash
	jupyter notebook
	```

2. Select a Python kernel and run the notebook cells interactively.

### Power BI Reports

1. Install and open Power BI Desktop.
2. Open [`Powerbi/Project.pbix`](Powerbi/Project.pbix) to view or edit the report, Power Query steps, data model, and visualizations.

## Progression

```text
Python fundamentals -> Pandas workflows -> Jupyter analysis -> Power BI reporting
```
