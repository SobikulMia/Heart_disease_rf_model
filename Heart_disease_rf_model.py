#Importing necessary librarics

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error,r2_score,classification_report,confusion_matrix,accuracy_score

# Load the dataset from Excel file
data_set =pd.read_excel("heart_cleveland_upload.xlsx")
print(data_set.head()) # Display the first 5 rows of the dataset

# Check for missing values in each columns
check_miss_value =data_set.isnull().sum()
print(check_miss_value)

# Calculate correlation between numeric features
corr = data_set.corr(numeric_only=True)
print(corr)
# Separate features (X) and target label (Y) 
x = data_set.drop("condition",axis=1)
y = data_set["condition"]

# Split the dataset into training and testing sets (60% train 40% test) 
x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.4,random_state=42)

# Create and train a Random Forest classifier
model = RandomForestClassifier()
model.fit(x_train,y_train)
# Predict using the test set
y_pre =model.predict(x_test)

# Evaluate model performance using different metrics
print("Accuracy scroe:",accuracy_score(y_test,y_pre)) # Overall accuracy
print("Mean squer error:",mean_squared_error(y_test,y_pre)) # Regression metrics, not ideal for classification
print("R2_scroe",r2_score(y_test,y_pre)) # Also a regression metric,less useful here
print("Classification Matrixe:\n",classification_report(y_test,y_pre)) #  Precision recall, F1_socre
print("confusion matrics:\n",confusion_matrix(y_test,y_pre)) # Actual vs Prediction values

#Visualize correlation matrix using heatmap
sns.heatmap(data_set.corr(),annot=True,cmap="coolwarm")
plt.title("Correlation Matrixe")
plt.show()
