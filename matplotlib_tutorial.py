from matplotlib import pyplot

def line_plot():
  x = (4, 8, 13, 17, 20)
  y = (54, 67, 98, 78, 45)

  pyplot.plot(x, y, 'g--d')
  pyplot.show()

def scatter_plot():
  x = [2,4,6,7,9,13,19,26,29,31,36,40,48,51,57,67,69,71,78,88]
  y = [54,72,43,2,8,98,109,5,35,28,48,83,94,84,73,11,464,75,200,54]

  pyplot.scatter(x, y)
  pyplot.show()

def histogram_plot():
  x = [2,4,6,5,42,543,5,3,73,64,42,97,63,76,63,8,73,97,23,45,56,89,45,3,23,2,5,78,23,56,67,78,8,3,78,34,67,23,324,234,43,544,54,33,223,443,444,234,76,432,233,23,232,243,222,221,254,222,276,300,353,354,387,364,309]

  num_bins = 6
  n, bins, patches = pyplot.hist(x, num_bins, facecolor = 'green')
  pyplot.show()


histogram_plot()
