###################### Statistical Functions ##########################
import numpy as np;
import statistics as stats;

# Wap to perform Central Tendency(mean,median,mode) in python.
data = [10, 12, 12, 13, 15, 100] 

print(f"Mean: {np.mean(data)}")     
print(f"Median: {np.median(data)}") 
print(f"Mode: {stats.mode(data)}") 


# Wap to perform Dispersion(Variance and Standard Deviation) in python.
prices = [20, 22, 19, 21, 20]

variance = np.var(prices)
std_dev = np.std(prices)

print(f"Variance: {variance:.2f}")  
print(f"Std Dev: {std_dev:.2f}")    



# Wap to perform Study hours vs Exam scores. As CoRelation
hours = [1, 2, 3, 4, 5]
scores = [40, 55, 65, 80, 90]

correlation_matrix = np.corrcoef(hours, scores)
correlation = correlation_matrix[0, 1]

print(f"Correlation: {correlation}") 