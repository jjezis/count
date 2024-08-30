import numpy as np 
import matplotlib.pyplot as plt

names = np.array(['John krasinski','Rainn Wilson',' Angela Kinsey','Brian Baumgartner','Leslie David Baker',' Phyllis Smith','Steve Carell','B.J Novak','Creed Bratton','Jenna fischer'])

x = np.vectorize(lambda s: s[0])(names)=='J'
print(x)

# Define the list of head sizes
head_sizes = [4,5,3,1,2]

# Sort the list of head sizes
sorted_head_sizes = np.sort(head_sizes)

# Define the head size we're interested in
head_size_to_check = 1.5

# Calculate the percentile of the head size within the sorted list
percentile_of_head_size = np.percentile(sorted_head_sizes, np.arange(0, 101, 1))  # Percentiles from 0 to 100

# Find the closest percentile value
percentile_value = np.searchsorted(sorted_head_sizes, head_size_to_check, side='right')


# Compute the percentile value based on the position in the sorted list
percentile = (percentile_value / len(sorted_head_sizes)) * 100

print(f"The head size of {head_size_to_check} inches is approximately at the {percentile:.2f} percentile.")
