import pandas as pd
import matplotlib.pyplot as plt

# Full path to your CSV file
file_path = r"C:\Users\dell\Desktop\internshipprojects\archive\population_by_age_group.csv"

# Load the dataset into a DataFrame
df = pd.read_csv(file_path)

# Display the first few rows to understand its structure
print("Dataset loaded successfully. First few rows:")
print(df.head())

# Clean the column names
df.columns = df.columns.str.strip()

# Display the columns to ensure they are clean
print("Cleaned column names:")
print(df.columns)

# Check if 'Country' is a valid column
if 'Country' in df.columns:
    # Filter data for a specific country (e.g., India)
    country_data = df[df['Country'] == 'India']

    if country_data.empty:
        print("No data found for the country 'India'. Please check the dataset.")
    else:
        # Display the filtered data
        print("Filtered data for India:")
        print(country_data.head())

        # Drop unnecessary columns and keep age group columns
        country_data = country_data.drop(['Country', 'Total'], axis=1)

        # Melt the DataFrame to long format
        country_data_melted = country_data.melt(var_name='Age Group', value_name='Population')

        # Check the reshaped data
        print("Reshaped data:")
        print(country_data_melted.head())

        # Extract the age groups and population values
        age_groups = country_data_melted['Age Group']
        population = country_data_melted['Population']

        # Create a bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(age_groups, population, color='IndianRed')
        plt.title('Population Distribution by Age Group (India)')
        plt.xlabel('Age Group')
        plt.ylabel('Population')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
else:
    print("Column 'Country' does not exist in the DataFrame.")
