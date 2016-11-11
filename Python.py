### Import Excel file with Pandas

xls_file = pd.ExcelFile('path')
sheets = xls_file.sheet_names
df = xls_file.parse(sheets[0])


### Transform double index in 2 variables

table["var1"] = (table.index.levels[0])[table.index.labels[0]]
table["var2"] = (table.index.levels[1])[table.index.labels[1]]


### Select columns starting with "Work_" from a df

cols = [ x for x in table.columns if x.startswith("Work_")]
sub_table = table[cols]


### Print the variables which are not float

dtypes = table.dtypes
for i in range(len(dtypes)):
    if dtypes[i] != 'float64':
        print (dtypes.index[i])
        
    

### PLOTS

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

## Draw the trendline on a scatterplot
plt.plot(x,y,'o')# plot the data itself
z = numpy.polyfit(x, data.sales, 3) # calc the trendline
f = numpy.poly1d(z)
x_new = numpy.linspace(x[0], x[len(x)-1], 50)
y_new = f(x_new)
plt.plot(x_new,y_new,"-")

### Draw a tree into a pdf (works with jpg, png)
with open("tree.dot", 'w') as f:
    f = tree.export_graphviz(reg_tree, feature_names=x.columns, impurity=False, out_file=f)
Then type the cmd line:
    dot -Tpdf iris.dot -o iris.pdf
