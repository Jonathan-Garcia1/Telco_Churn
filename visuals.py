import matplotlib.pyplot as plt
import seaborn as sns

def plot_churn_distribution(df):
    plt.figure(figsize=(6, 4))
    
    total_count = len(df)
    churn_counts = df['churn'].value_counts()
    
    sns.countplot(data=df, x='churn', palette=["#149911", "#D00000"])
    plt.title('Churn Distribution')
    plt.xlabel('Churn')
    plt.ylabel('Count')
    
    for i, count in enumerate(churn_counts):
        percentage = (count / total_count) * 100
        plt.text(i, count + 50, f'{percentage:.2f}%', ha='center', weight='bold')






def plot_churn_by_internet_service(df):
    # Calculate churn ratios for internet service types
    churn_ratio_fiber_optic = (df[df['internet_service_type'] == 'Fiber optic']['churn'].value_counts()['Yes'] / 
                               (df[df['internet_service_type'] == 'Fiber optic']['churn'].value_counts()['Yes'] +
                                df[df['internet_service_type'] == 'Fiber optic']['churn'].value_counts()['No'])) * 100

    churn_ratio_dsl = (df[df['internet_service_type'] == 'DSL']['churn'].value_counts()['Yes'] /
                       (df[df['internet_service_type'] == 'DSL']['churn'].value_counts()['Yes'] +
                        df[df['internet_service_type'] == 'DSL']['churn'].value_counts()['No'])) * 100

    churn_ratio_none = (df[df['internet_service_type'] == 'No internet service']['churn'].value_counts()['Yes'] /
                        (df[df['internet_service_type'] == 'No internet service']['churn'].value_counts()['Yes'] +
                         df[df['internet_service_type'] == 'No internet service']['churn'].value_counts()['No'])) * 100

    # Chart settings
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 4))

    # Map index values to labels
    churn_counts = df['churn'].value_counts()
    churn_counts.index = churn_counts.index.map({'Yes': "Churned", 'No': "Non-Churned"})

    # Create a bar plot for internet service types and churn rates
    ax = sns.countplot(x='internet_service_type', hue='churn', data=df, palette=["#149911", "#D00000"], order=['Fiber optic', 'DSL', 'No internet service'])

    # Set new labels for x-axis
    ax.set_xticklabels(['Fiber Optic', 'DSL', 'No Internet'])

    plt.title("Churn vs. Internet Service Type")
    plt.xlabel("Internet Service Type")
    plt.ylabel("Number of Customers")

    # Annotate the churned columns with the churn ratio
    ax.annotate(f"{churn_ratio_fiber_optic:.2f}%", xy=(0, churn_ratio_fiber_optic), xytext=(32, 135),
                textcoords="offset points", ha='center', va='bottom', color='black', weight='bold')

    ax.annotate(f"{churn_ratio_dsl:.2f}%", xy=(1, churn_ratio_dsl), xytext=(32, 46),
                textcoords="offset points", ha='center', va='bottom', color='black', weight='bold')

    ax.annotate(f"{churn_ratio_none:.2f}%", xy=(2, churn_ratio_none), xytext=(32, 12),
                textcoords="offset points", ha='center', va='bottom', color='black', weight='bold')

    plt.show()







def plot_churn_vs_payment_method(df):
    # Calculate churn ratios for payment methods
    churn_ratio_mailed_check = (df[df['payment_method'] == 'Mailed check']['churn'].value_counts()['Yes'] /
                                 (df[df['payment_method'] == 'Mailed check']['churn'].value_counts()['Yes'] +
                                  df[df['payment_method'] == 'Mailed check']['churn'].value_counts()['No'])) * 100
    
    churn_ratio_electronic_check = (df[df['payment_method'] == 'Electronic check']['churn'].value_counts()['Yes'] /
                                    (df[df['payment_method'] == 'Electronic check']['churn'].value_counts()['Yes'] +
                                     df[df['payment_method'] == 'Electronic check']['churn'].value_counts()['No'])) * 100
    
    churn_ratio_credit_card = (df[df['payment_method'] == 'Credit card']['churn'].value_counts()['Yes'] /
                               (df[df['payment_method'] == 'Credit card']['churn'].value_counts()['Yes'] +
                                df[df['payment_method'] == 'Credit card']['churn'].value_counts()['No'])) * 100
    
    churn_ratio_bank_transfer = (df[df['payment_method'] == 'Bank transfer']['churn'].value_counts()['Yes'] /
                                 (df[df['payment_method'] == 'Bank transfer']['churn'].value_counts()['Yes'] +
                                  df[df['payment_method'] == 'Bank transfer']['churn'].value_counts()['No'])) * 100
    
    # Chart settings
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 4))

    # Create a bar plot for payment methods and churn rates
    ax = sns.countplot(x='payment_method', hue='churn', data=df, palette=["#149911", "#D00000"], order=['Electronic check', 'Mailed check', 'Credit card', 'Bank transfer'])

    plt.title("Churn vs Payment Method")
    plt.xlabel("Payment Method")
    plt.ylabel("Number of Customers")

    # Annotate the churned columns with the churn ratio
    ax.annotate(f"{churn_ratio_electronic_check:.2f}%", xy=(0, churn_ratio_electronic_check), xytext=(28, 165),
                textcoords="offset points", ha='center', va='bottom', color='black', weight='bold')

    ax.annotate(f"{churn_ratio_mailed_check:.2f}%", xy=(1, churn_ratio_mailed_check), xytext=(28, 46),
                textcoords="offset points", ha='center', va='bottom', color='black', weight='bold')

    ax.annotate(f"{churn_ratio_credit_card:.2f}%", xy=(2, churn_ratio_credit_card), xytext=(28, 34),
                textcoords="offset points", ha='center', va='bottom', color='black', weight='bold')

    ax.annotate(f"{churn_ratio_bank_transfer:.2f}%", xy=(3, churn_ratio_bank_transfer), xytext=(28, 38),
                textcoords="offset points", ha='center', va='bottom', color='black', weight='bold')

    plt.show()




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