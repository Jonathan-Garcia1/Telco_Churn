import matplotlib.pyplot as plt
import seaborn as sns


# posible colors 
# Greens: 1E3888 
# Reds: F46036 DF2935 721817 FB5012 F8333C 93032E C03221 E53D00 BF211E D00000


def plot_churn_distribution(df):
    plt.figure(figsize=(3, 4))

    # Count the churned and non-churned customers
    churn_counts = df['churn'].value_counts()

    # Calculate churned percentage
    churn_percentage = churn_counts['Yes'] / churn_counts['No'] * 100

    # Map index values to labels
    churn_counts.index = churn_counts.index.map({'Yes': "Churned", 'No': "Un-Churned"})

    # Create a bar plot
    sns.barplot(x=churn_counts.index, y=churn_counts.values, palette=["#149911", "#D00000"])
    plt.title("Ratio of Churned vs. Un-Churned Customers")
    plt.xlabel("Churn")
    plt.ylabel("Number of Customers")

    # Annotate only the churned bar with the churned percentage
    for index, value in enumerate(churn_counts):
        if churn_counts.index[index] == "Churned":
            plt.text(index, value, f"{churn_percentage:.1f}%", ha='center', va='bottom',  color='black', weight='bold')

    sns.despine()
    plt.show()


'''    # Annotate the churned columns with the churn ratio
    ax.annotate(f"{churn_ratio_internet_yes:.2f}%", xy=(0, churn_ratio_internet_yes), xytext=(52, 92),
                textcoords="offset points", ha='center', va='bottom', color='black', weight='bold')

    ax.annotate(f"{churn_ratio_internet_no:.2f}%", xy=(1, churn_ratio_internet_no), xytext=(52, 7),
                textcoords="offset points", ha='center', va='bottom', color='black', weight='bold')

    plt.tight_layout()
    plt.show()'''
    


def plot_churn_by_internet_service(df):
    # Calculate churn counts
    churn_counts = df['churn'].value_counts()

    # Calculate churn ratios for internet service types
    churn_ratios = {}
    internet_service_types = ['Fiber optic', 'DSL', 'No internet service']
    
    for service_type in internet_service_types:
        churned_count = df[(df['internet_service_type'] == service_type) & (df['churn'] == 'Yes')]['churn'].count()
        unchurned_count = df[(df['internet_service_type'] == service_type) & (df['churn'] == 'No')]['churn'].count()
        
        churn_ratio = (churned_count / (churned_count + unchurned_count)) * 100
        churn_ratios[service_type] = churn_ratio
    
    # Chart settings
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 4))

    # Map index values to labels
    churn_counts.index = churn_counts.index.map({'Yes': "Churned", 'No': "Non-Churned"})

    # Create a bar plot for internet service types and churn rates
    ax = sns.countplot(x='internet_service_type', hue='churn', data=df, palette=["#149911", "#D00000"],
                       order=['Fiber optic', 'DSL', 'No internet service'])

    # Set new labels for x-axis
    ax.set_xticklabels(['Fiber Optic', 'DSL', 'No Internet'])

    plt.title("Churn vs. Internet Service Type")
    plt.xlabel("Internet Service Type")
    plt.ylabel("Number of Customers")

    # Semi-annotate the churned columns with the churn ratio
    ax.annotate(f"{churn_ratios['Fiber optic']:.2f}%", xy=(0, churn_ratios['Fiber optic']), xytext=(32, 136),
                textcoords="offset points", ha='center', va='bottom', color='black', weight='bold')
    
    ax.annotate(f"{churn_ratios['DSL']:.2f}%", xy=(1, churn_ratios['DSL']), xytext=(32, 47),
                textcoords="offset points", ha='center', va='bottom', color='black', weight='bold')
    
    ax.annotate(f"{churn_ratios['No internet service']:.2f}%", xy=(2, churn_ratios['No internet service']), xytext=(32, 12),
                textcoords="offset points", ha='center', va='bottom', color='black', weight='bold')

    plt.show()







    
'''def plot_churn_vs_internet_service_type_ratio(df):
    # Calculate churn counts
    churn_counts = df['churn'].value_counts()

    # Calculate churn ratios for internet service types
    churn_ratio_fiber_optic = (df[df['internet_service_type'] == 'Fiber optic']['churn'].value_counts()['Yes'] / df[df['internet_service_type'] == 'Fiber optic']['churn'].value_counts()['No']) * 100
    churn_ratio_dsl = (df[df['internet_service_type'] == 'DSL']['churn'].value_counts()['Yes'] / df[df['internet_service_type'] == 'DSL']['churn'].value_counts()['No']) * 100
    churn_ratio_none = (df[df['internet_service_type'] == 'No internet service']['churn'].value_counts()['Yes'] / df[df['internet_service_type'] == 'No internet service']['churn'].value_counts()['No']) * 100

    # Chart settings
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 4))

    # Map index values to labels
    churn_counts.index = churn_counts.index.map({'Yes': "Churned", 'No': "Non-Churned"})

    # Create a bar plot for internet service types and churn rates
    ax = sns.countplot(x='internet_service_type', hue='churn', data=df, palette=["#149911", "#D00000"], order=['Fiber optic', 'DSL', 'No internet service'])

    # Set new labels for x-axis
    ax.set_xticklabels(['Fiber Optic', 'DSL', 'No Internet'])

    plt.title("Churn vs. Internet Service Type")
    plt.xlabel("Internet Service Type")
    plt.ylabel("Number of Customers")

    # Annotate the churned columns with the churn ratio
    ax.annotate(f"{churn_ratio_fiber_optic:.2f}%", xy=(0, churn_ratio_fiber_optic), xytext=(32, 132),
                textcoords="offset points", ha='center', va='bottom', color='black', weight='bold')

    ax.annotate(f"{churn_ratio_dsl:.2f}%", xy=(1, churn_ratio_dsl), xytext=(32, 46),
                textcoords="offset points", ha='center', va='bottom', color='black', weight='bold')

    ax.annotate(f"{churn_ratio_none:.2f}%", xy=(2, churn_ratio_none), xytext=(32, 12),
                textcoords="offset points", ha='center', va='bottom', color='black', weight='bold')

    #plt.tight_layout()
    plt.show()'''


'''def plot_churn_vs_payment_method(df):
    # Calculate churn counts
    churn_counts = df['churn'].value_counts()

    # Calculate churn ratios for payment methods
    churn_ratio_mailed_check = (df[df['payment_method'] == 'Mailed check']['churn'].value_counts()['Yes'] / df[df['payment_method'] == 'Mailed check']['churn'].value_counts()['No']) * 100
    churn_ratio_electronic_check = (df[df['payment_method'] == 'Electronic check']['churn'].value_counts()['Yes'] / df[df['payment_method'] == 'Electronic check']['churn'].value_counts()['No']) * 100
    churn_ratio_credit_card = (df[df['payment_method'] == 'Credit card']['churn'].value_counts()['Yes'] / df[df['payment_method'] == 'Credit card']['churn'].value_counts()['No']) * 100
    churn_ratio_bank_transfer = (df[df['payment_method'] == 'Bank transfer']['churn'].value_counts()['Yes'] / df[df['payment_method'] == 'Bank transfer']['churn'].value_counts()['No']) * 100

    # Chart settings
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 4))

    # Map index values to labels
    churn_counts.index = churn_counts.index.map({'Yes': "Churned", 'No': "Non-Churned"})

    # Create a bar plot for payment methods and churn rates
    ax = sns.countplot(x='payment_method', hue='churn', data=df, palette=["#149911", "#D00000"], order=['Electronic check', 'Mailed check', 'Credit card', 'Bank transfer'])

    # Set new labels for x-axis
    ax.set_xticklabels(['Electronic check', 'Mailed check', 'Credit card', 'Bank transfer'])

    plt.title("Churn vs Payment Method")
    plt.xlabel("Payment Method")
    plt.ylabel("Number of Customers")

    # Annotate the churned columns with the churn ratio
    
    ax.annotate(f"{churn_ratio_electronic_check:.2f}%", xy=(0, churn_ratio_electronic_check), xytext=(28, 160),
                textcoords="offset points", ha='center', va='bottom', color='black', weight='bold')

    ax.annotate(f"{churn_ratio_mailed_check:.2f}%", xy=(1, churn_ratio_mailed_check), xytext=(28, 46),
                textcoords="offset points", ha='center', va='bottom', color='black', weight='bold')

    ax.annotate(f"{churn_ratio_credit_card:.2f}%", xy=(2, churn_ratio_credit_card), xytext=(28, 34),
                textcoords="offset points", ha='center', va='bottom', color='black', weight='bold')

    ax.annotate(f"{churn_ratio_bank_transfer:.2f}%", xy=(3, churn_ratio_bank_transfer), xytext=(28, 38),
                textcoords="offset points", ha='center', va='bottom', color='black', weight='bold')

    #plt.tight_layout()
    plt.show()'''

def plot_churn_vs_tenure_histogram(df):
    # Chart settings
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))

    # Calculate the number of churned and non-churned customers for each tenure
    churned_tenure = df[df['churn'] == 'Yes']['tenure']
    non_churned_tenure = df[df['churn'] == 'No']['tenure']

    # Create histogram for non-churned customers
    plt.hist(non_churned_tenure, bins=range(0, 74, 3), rwidth=1, color='green', label='Non-Churned')

    # Define custom data range to shift the churned histogram to the left
    custom_range = [x - 0.3 for x in range(0, 74, 3)]
    plt.hist(churned_tenure, bins=custom_range, rwidth=0.8, color='red', alpha=0.8, label='Churned')

    plt.title("Shifted Churn vs Tenure Histogram")
    plt.xlabel("Tenure (Months)")
    plt.ylabel("Number of Customers")
    plt.legend()

    # Set x-axis tick marks every 6 months
    plt.xticks(range(0, 74, 6))

    plt.tight_layout()
    plt.show()


def plot_churn_vs_monthly_charges_histogram(df):
    # Chart settings
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))

    # Calculate the common bin edges for both datasets
    #bin_edges = range(15, 125, 5)  # Define bin edges

    # Create histograms for churn vs monthly charges with shared bins
    plt.hist(df[df['churn'] == 'No']['monthly_charges'], bins=range(15, 125, 5) , color='green', alpha=1, label='Non-Churned')
    
    custom_range = [x - 0.4 for x in range(15, 130, 5)]
    plt.hist(df[df['churn'] == 'Yes']['monthly_charges'], bins=custom_range, rwidth=0.8, color='red', alpha=0.8, label='Churned')

    plt.title("Aligned Churn vs Monthly Charges Histogram")
    plt.xlabel("Monthly Charges")
    plt.ylabel("Number of Customers")
    plt.legend()

    plt.tight_layout()
    plt.show()
    
    
'''def plot_churn_vs_internet_service_ratio(df):
    # Chart settings
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 4))

    # Calculate churn ratios for internet service types
    churn_ratio_internet_yes = (df[df['internet_service'] == 'Yes']['churn'].value_counts()['Yes'] /
                                df[df['internet_service'] == 'Yes']['churn'].value_counts()['No']) * 100

    churn_ratio_internet_no = (df[df['internet_service'] == 'No']['churn'].value_counts()['Yes'] /
                            df[df['internet_service'] == 'No']['churn'].value_counts()['No']) * 100

    # Create a bar plot for internet service types and churn rates
    ax = sns.countplot(x='internet_service', hue='churn', data=df, palette=["#149911", "#D00000"])

    # Set new labels for x-axis
    ax.set_xticklabels(['With Internet', 'Without Internet'])

    plt.title("Churn vs. Internet Service")
    plt.xlabel("Internet Service")
    plt.ylabel("Number of Customers")'''