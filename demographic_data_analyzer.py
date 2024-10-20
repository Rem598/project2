import pandas as pd

def demographic_data_analyzer():
    # Define the column names based on the dataset's structure
    column_names = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race', 
        'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 
        'native-country', 'salary'
    ]
    
    # Load the dataset without headers and assign the defined column names
    df = pd.read_csv('adult.data.csv', header=None, names=column_names)

    # Print the first few rows and the columns to confirm the load
    print(df.head())  # Print first few rows to check data
    print(df.columns)  # Print column names to verify
    
    # Count the number of people of each race
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    total_people = len(df)
    bachelors_count = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = (bachelors_count / total_people) * 100 if total_people > 0 else 0

    # What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    if len(advanced_education) > 0:
        percentage_advanced_education_rich = (len(advanced_education[advanced_education['salary'] == '>50K']) / len(advanced_education)) * 100
    else:
        percentage_advanced_education_rich = 0

    # What percentage of people without advanced education make more than 50K?
    non_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    if len(non_advanced_education) > 0:
        percentage_non_advanced_education_rich = (len(non_advanced_education[non_advanced_education['salary'] == '>50K']) / len(non_advanced_education)) * 100
    else:
        percentage_non_advanced_education_rich = 0

    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    if len(num_min_workers) > 0:
        rich_percentage_min_hours = (len(num_min_workers[num_min_workers['salary'] == '>50K']) / len(num_min_workers)) * 100
    else:
        rich_percentage_min_hours = 0

    # What country has the highest percentage of people that earn >50K?
    countries_earning_over_50k = df[df['salary'] == '>50K']['native-country'].value_counts()
    total_people_per_country = df['native-country'].value_counts()
    
    if not total_people_per_country.empty:
        highest_earning_country = (countries_earning_over_50k / total_people_per_country).idxmax()
        highest_earning_country_percentage = round((countries_earning_over_50k / total_people_per_country).max() * 100, 1)
    else:
        highest_earning_country = None
        highest_earning_country_percentage = 0

    # Identify the most popular occupation for those who earn >50K in India.
    india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    if not india_high_earners.empty:
        top_occupation_india = india_high_earners['occupation'].value_counts().idxmax()
    else:
        top_occupation_india = None

    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'percentage_advanced_education_rich': round(percentage_advanced_education_rich, 1),
        'percentage_non_advanced_education_rich': round(percentage_non_advanced_education_rich, 1),
        'min_work_hours': min_work_hours,
        'rich_percentage_min_hours': round(rich_percentage_min_hours, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_occupation_india': top_occupation_india
    }

# Example of calling the function
if __name__ == "__main__":
    print(demographic_data_analyzer())
