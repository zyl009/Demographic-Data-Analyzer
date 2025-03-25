import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # Race count
    race_count = df['race'].value_counts()

    # Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Percentage of people with Bachelors
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Higher education and rich percentage
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)

    # Lower education and rich percentage
    lower_education = ~higher_education
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

    # Minimum work hours
    min_work_hours = df['hours-per-week'].min()

    # Rich percentage among minimum workers
    num_min_workers = (df['hours-per-week'] == min_work_hours).sum()
    rich_count = ((df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')).sum()
    rich_percentage = round((rich_count / num_min_workers) * 100, 1) if num_min_workers != 0 else 0.0

    # Country with highest percentage of rich people
    country_stats = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100)
    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = round(country_stats.max(), 1)

    # Top occupation in India for rich
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
