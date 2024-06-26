import pandas as pd
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset and select the relevant columns
columns_to_normalize = ['mean_ghgs', 'mean_ghgs_ch4', 'mean_ghgs_n2o', 'mean_bio', 'mean_land', 'mean_watscar', 'mean_watuse', 'mean_eut', 'mean_acid', 'age_group']

data = pd.read_csv('Results_21Mar2022.csv')[columns_to_normalize]

# Normalize the data and create a DataFrame
scaler = StandardScaler()

normalized_data = scaler.fit_transform(data.iloc[:, :-1])  # The last column is age_group, which does not need to be standardized
normalized_df = pd.DataFrame(normalized_data, columns=columns_to_normalize[:-1])
normalized_df['age_group'] = data['age_group']

# Aggregate data by age_group for plotting
grouped_data = normalized_df.groupby('age_group').mean()

# Creating a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(grouped_data.T, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Between Age and Environmental Influences')
plt.xlabel('Age Group')
plt.ylabel('Variables')
plt.xticks(rotation=45)  # Rotate the x-axis label
plt.yticks(rotation=0)   
plt.show()
