import pylab

pylab.title('Queries per lookup')
pylab.xlabel('Queries')
pylab.ylabel('CDF')

lines_to_plot = (
    ('ut-50.lookup_queries.cdf', 'ut-50', 'ks-'),
    #('test1', 'l1', 'rs-'),
    #('test2', 'l2', 'bs-'),
    )
#    (filename, label, style)


plots = []
for line_to_plot in lines_to_plot:
    filename, label, style = line_to_plot
    x = []
    y = []
    for line in open(filename):
        cum_str, value_str = line.split()
        y.append(float(cum_str))
        x.append(float(value_str))
    plots.append(pylab.plot(x, y, style, label=label))

pylab.legend(loc='lower right')
pylab.show()

