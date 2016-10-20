### Import Excel file with Pandas

xls_file = pd.ExcelFile('path')
sheets = xls_file.sheet_names
df = xls_file.parse(sheets[0])


### Transform double index in 2 variables

table["var1"] = (table.index.levels[0])[table.index.labels[0]]
table["var2"] = (table.index.levels[1])[table.index.labels[1]]


### Plots

# Boxplot
df.boxplot(column="var_to_plot", by="group_var")
# Histogram
plt.hist(df.variable) # also works with df.groupby(...).variable.grouper()
plt.title("Title")
plt.xlabel("Label for x-axis")
plt.ylabel("Label for y-axis")

### Draw a dendrogram

from sklearn.metrics.pairwise import euclidean_distances
from scipy.cluster import hierarchy
Z = hierarchy.linkage(euclidean_distances(mileage), 'ward') # Can also use 'average', 'single', 'complete'...
hierarchy.dendrogram(Z)

##### test
