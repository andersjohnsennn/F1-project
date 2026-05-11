import seaborn as sns
import matplotlib.pyplot as plt

def hist(df, str):

    sns.histplot(df[str], kde=True)

    plt.title("Distribution of " + str)

    plt.show()