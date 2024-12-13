##Project: Salary Visualization for Top Earners at Queen's University##

##Description##:
##This project uses data obtained from the Sumerlee List of Top Earners at Queen's University. The dataset includes  information about the top 100 earners, their position, salary, and year. Using OpenPyXL, we visualize these earnings  through various types of charts (Bar, Line, Scatter, Pie) and perform basic statistical analysis.##

##The project highlights the importance of data cleaning, as several charts are not easy to interpret in their current  state. The aim is to improve this aspect in future iterations by properly transforming the dataset.##




import openpyxl

# Step 1: Load the workbook and set the active sheet##
input_file_path = "Excel/Top Earners with this Employer since 1996.xlsx"
wb = openpyxl.load_workbook(input_file_path)

# Set the active sheet
sheet = wb.active

# Create references to the data columns for chart creation
# Columns: A to D, Rows: 1 to 101
# Row 1 contains headers: NAME, POSITION, SALARY, YEAR
refObj = openpyxl.chart.Reference(sheet, min_col=1, min_row=2, max_col=4, max_row=101) 
# Reference data from columns A to D, excluding headers

# Step 2: Create a Bar Chart, Top 10 Salaries by Employee##
bar_chart = openpyxl.chart.BarChart()
bar_chart.title = "Salary by Employee"
salary_data = openpyxl.chart.Reference(sheet, min_col=3, min_row=2, max_row=11)  # SALARY as data
name_data = openpyxl.chart.Reference(sheet, min_col=1, min_row=2, max_row=11)  # NAME as categories
bar_chart.add_data(salary_data, titles_from_data=False)
bar_chart.set_categories(name_data)
bar_chart.y_axis.title = "Salary"
bar_chart.x_axis.title = "Employee"
sheet.add_chart(bar_chart, "E5")


### Step 3: Create a Line Chart, Yearly Salary Trend##
line_chart = openpyxl.chart.LineChart()
line_chart.title = "Yearly Salary Trend"
salary_data = openpyxl.chart.Reference(sheet, min_col=3, min_row=2, max_row=11)
year_data = openpyxl.chart.Reference(sheet, min_col=4, min_row=2, max_row=11)
line_chart.add_data(salary_data, titles_from_data=False)
line_chart.set_categories(year_data)
line_chart.y_axis.title = "Salary"
line_chart.x_axis.title = "Year"
sheet.add_chart(line_chart, "E20")

### Step 4: Create a Scatter Chart, Year vs Salary##
scatter_chart = openpyxl.chart.ScatterChart()
scatter_chart.title = "Year vs Salary Scatter Chart"
year_data = openpyxl.chart.Reference(sheet, min_col=3, min_row=2, max_row=101)   # YEAR (X-axis)
salary_data = openpyxl.chart.Reference(sheet, min_col=4, min_row=2, max_row=101)  # SALARY (Y-axis)
series = openpyxl.chart.Series(values=salary_data, xvalues=year_data, title="Salaries")
scatter_chart.series.append(series)
scatter_chart.x_axis.title = "Year"
scatter_chart.y_axis.title = "Salary"
sheet.add_chart(scatter_chart, "E35")

# Step 5: Create a Pie Chart, Total Salary by Position##3
##The PieChart contains many categories (positions), leading to slices that are too small to interpret meaningfully. Future work could involve grouping similar positions.##
pie_chart = openpyxl.chart.PieChart()
pie_chart.title = "Total Salary by Position"
position_data = openpyxl.chart.Reference(sheet, min_col=2, min_row=2, max_row=101)  # POSITION as categories
pie_chart_data = openpyxl.chart.Reference(sheet, min_col=3, min_row=2, max_row=101)  # SALARY as data
pie_chart.add_data(pie_chart_data, titles_from_data=False)
pie_chart.set_categories(position_data)
sheet.add_chart(pie_chart, "E50")

##Despite the effort to visualize the data, some charts did not work as expected. The scatter plot, in particular, appeared more like a line chart because the dataset wasn’t properly aggregated, and repeating values distorted the visualization. This issue highlights the importance of data cleaning and transformation before visualization.##


## Step 6: Basic Data Analysis (Mean, Median, Standard Deviation, etc.)##3
##The workbook includes basic data analysis with mean, median, standard deviation, minimum, and maximum calculations. This provides a basic summary of the data and helps to understand the distribution of salaries among top earners in the cells outlined below##
sheet["G2"] = "Salary Statistics"
sheet.merge_cells("G2:H2")
sheet["G3"] = "Mean Salary"
sheet["H3"] = "=AVERAGE(C2:C101)"
sheet["G4"] = "Median Salary"
sheet["H4"] = "=MEDIAN(C2:C101)"
sheet["G5"] = "Standard Deviation"
sheet["H5"] = "=STDEV(C2:C101)"



# Save the workbook
output_file_path = "Excel/Top_Earners_Charts_Analysis.xlsx"
wb.save(output_file_path)
print("Excel file with charts and analysis saved successfully.")

##This project provided experience in data analysis and visualization using OpenPyXL. Challenges with the raw data limited the effectiveness of the visualizations. In particular, the scatter chart appeared more like a line chart, and the pie chart was difficult to interpret due to small slices from many categories.##
##In the next iteration, data cleaning and transformation will be prioritized to ensure clearer and more insightful visual outputs. Specifically, future improvements will include grouping similar positions, aggregating data by year, and using histograms to depict salary distributions effectively.##