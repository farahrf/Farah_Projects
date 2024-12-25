# Customer Segmentation Project

This project focuses on customer segmentation using various data analysis and visualization techniques. The main notebook in this project is **customer segmentation.ipynb**.

## customer segmentation.ipynb

This notebook explores customer data to segment them into different groups based on their attributes. The following steps and tools are used:

### Data Overview

The dataset contains several features including:

- **ID**: Unique identifier for each customer.
- **Year_Birth**: Year of birth of the customer.
- **Income**: Annual income of the customer.
- **Kidhome**: Number of children at home.


### Data Visualization

Several visualizations are created to understand the distribution and relationships in the data:

- **Pie Charts**: Display the distribution of categorical features such as `Kidhome`.
- **Age Distribution**: Histogram or bar chart showing the distribution of customers' ages derived from `Year_Birth`.

### Segmentation Analysis

The analysis involves clustering customers into different segments based on their attributes such as age and income. Techniques used may include:

- **K-Means Clustering**
- **Hierarchical Clustering**

These techniques help in identifying distinct groups of customers with similar characteristics, which can be useful for targeted marketing strategies.

### Tools and Libraries

The following tools and libraries are used in this project:

- **NumPy**: For numerical operations.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib** and **Matplotlib.pyplot**: For data visualization.
- **Seaborn**: For statistical data visualization.
- **Datetime**: For handling date and time data.
- **Scikit-Learn**: For machine learning tasks such as preprocessing, clustering, and metrics.
  - **LabelEncoder**: For encoding categorical features.
  - **StandardScaler**: For feature scaling.
  - **PCA (Principal Component Analysis)**: For dimensionality reduction.
  - **K-Means Clustering**: For segmenting the data.
  - **Agglomerative Clustering**: For hierarchical clustering.
- **Yellowbrick**: For visualizing the elbow method in K-Means clustering.
- **ListedColormap**: For custom color maps in visualizations.

## Conclusion

The Customer Segmentation project provides insights into different customer groups based on their demographic and behavioral attributes. The segmentation helps in understanding the customer base better and enables more effective marketing and business strategies.
