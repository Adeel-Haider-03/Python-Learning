import numpy as np
import scipy.stats as stats
#mean, median, mode 

data = [1, 2, 3, 4, 5, 5, 6]
mean = np.mean(data)
mode=stats.mode(data)
median=np.median(data)
std_dev=np.std(data)

print("Mean:", mean)

print("Mode:", mode)  #mode returns a ModeResult object, first element is the mode value, second is the count
x,y=mode[0],mode[1]
print("Mode Value:", x, "Count:", y)

print("Median:", median)
print("Standard Deviation:", std_dev)


#percentiles
ages=[23, 45, 31, 35, 22, 28, 40, 29, 33, 27, 30, 26, 24, 38, 32, 36, 34, 37, 39, 41]

# x=np.sort(ages)
# print(x)

percentiles=np.percentile(ages, [25, 50, 75])
print("25th Percentile:", percentiles[0], "50th Percentile (Median):", percentiles[1], "75th Percentile:", percentiles[2])


