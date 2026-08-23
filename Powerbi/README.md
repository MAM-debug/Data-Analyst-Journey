# HR Department & Employee Data Analysis

## Project Overview

**HR Department & Employee Data Analysis** is a Power BI project focused on preparing employee records and converting them into a clear view of departmental headcount and role distribution.

The report demonstrates a practical data analysis workflow: raw employee data is cleaned and reshaped in Power Query, employee names and identifiers are standardized, and the resulting dataset is used to analyze the operational structure of the organization. Key fields include employee names, unique employee codes, departments, and position titles.

## Dashboard Preview

The primary dashboard visualizes employee headcount by department and supports a quick assessment of how staff are distributed across the organization.

![HR Department and Employee Data Analysis dashboard](./chart.jpeg)

## Data Transformation Steps

Data preparation was completed in **Power Query Editor** using the following steps:

1. **Raw data cleanup**
   - Imported the employee records into Power BI.
   - Reviewed column names, data types, and record quality.
   - Standardized the table structure for analysis.

2. **Employee name transformation**
   - Applied custom text delimiter splits to the full-name column.
   - Extracted separate `First Name` and `Last Name` fields.
   - Preserved the individual name components for easier filtering and reporting.

3. **Identifier and missing-value handling**
   - Cleaned and standardized unique employee codes.
   - Checked identifiers for inconsistent formatting and incomplete values.
   - Handled missing values to improve the reliability of employee counts and report filters.

4. **Analysis-ready fields**
   - Prepared `Department` and `Position Title` fields for grouping and comparison.
   - Confirmed that the transformed data supported accurate headcount analysis.

## Key Insights & Visualizations

### Headcount by Department

The primary bar chart shows the distribution of staff across departments. **Sales** has the highest headcount, followed by **Procurement** and **Finance**.

This view helps identify the relative scale of each functional area and provides a concise picture of the organization’s operational structure. Comparing departments also highlights how employee roles are distributed across business functions and creates a foundation for workforce planning, capacity reviews, and future HR reporting.

### Operational Structure and Role Distribution

The combination of department and position-title fields supports analysis beyond total headcount. It can be used to examine:

- How roles are distributed within each department.
- Which departments have the broadest range of position titles.
- Whether staffing patterns suggest distinct operational priorities.
- How cleaned employee-level records can support future HR metrics and drill-through analysis.

## Project Structure

```text
Powerbi/
|-- Project.pbix   # Power BI Desktop report file
|-- chart.jpeg     # Visual export of the primary chart
|-- README.md      # Project documentation
```

- `Powerbi/Project.pbix`: Power BI Desktop report file.
- `Powerbi/chart.jpeg`: Visual export of the primary chart.

## How to Run

1. Install and open **Power BI Desktop**.
2. Open `Powerbi/Project.pbix` to view the report or edit its data transformations and visualizations.

If the source data is not embedded in the report, use Power BI Desktop’s **Refresh** option after opening the file and confirm that any required source paths are available.
