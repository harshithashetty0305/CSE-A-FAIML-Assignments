
# LOAN APPROVAL PREDICTION - LOGISTIC REGRESSION
# ==========================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pymongo import MongoClient
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import roc_curve, auc

# ==========================================
# STEP 1: Connect to MongoDB
# ==========================================

client = MongoClient("mongodb://localhost:27017/")
db = client["bank_loan_prediction_db"]
collection = db["loan_application_records"]

print("Connected to MongoDB")

# ==========================================
# STEP 2: Load CSV and Insert into MongoDB
# ==========================================

data = pd.read_csv(r"C:\Users\vijay\Downloads\Loan_Approval_High_Accuracy_600.csv")

collection.delete_many({})
collection.insert_many(data.to_dict("records"))

print("CSV Data Inserted into MongoDB")

# ==========================================
# STEP 3: Fetch Data from MongoDB
# ==========================================

mongo_data = list(collection.find({}, {"_id": 0}))
df = pd.DataFrame(mongo_data)

print("Data Retrieved from MongoDB")

# ==========================================
# STEP 4: Data Preprocessing
# ==========================================

df = df.ffill()

label_encoder = LabelEncoder()

categorical_columns = [
    'Gender', 'Married', 'Education',
    'Self_Employed', 'Property_Area', 'Loan_Status'
]

for col in categorical_columns:
    df[col] = label_encoder.fit_transform(df[col])

# ==========================================
# STEP 5: Feature & Target
# ==========================================

X = df.drop("Loan_Status", axis=1)
y = df["Loan_Status"]

# Feature Scaling (Important for Logistic Regression)
scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==========================================
# STEP 6: Train Logistic Regression Model
# ==========================================

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("Logistic Regression Model Trained")

# ==========================================
# STEP 7: Evaluation
# ==========================================

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("\nAccuracy:", accuracy)
print("\nConfusion Matrix:\n", cm)
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# ==========================================
# GRAPH 1: Confusion Matrix
# ==========================================

plt.figure()
plt.imshow(cm)
plt.title("Confusion Matrix - Logistic Regression")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.colorbar()

for i in range(len(cm)):
    for j in range(len(cm)):
        plt.text(j, i, cm[i][j], ha='center', va='center')

plt.show()

# ==========================================
# GRAPH 2: Accuracy Graph
# ==========================================

plt.figure()
plt.bar(["Accuracy"], [accuracy])
plt.title("Model Accuracy - Logistic Regression")
plt.ylabel("Score")
plt.ylim(0, 1)
plt.show()

# ==========================================
# GRAPH 3: ROC Curve
# ==========================================

y_prob = model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr)
plt.plot([0, 1], [0, 1])
plt.title("ROC Curve (AUC = {:.2f})".format(roc_auc))
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.show()

# ==========================================
# STEP 8: Predict New Applicant
# ==========================================

sample_input = [[
    1,      # Gender
    1,      # Married
    0,      # Dependents
    1,      # Education
    0,      # Self_Employed
    8000,   # ApplicantIncome
    2000,   # CoapplicantIncome
    150,    # LoanAmount
    360,    # Loan_Amount_Term
    1,      # Credit_History
    2       # Property_Area
]]

sample_input = scaler.transform(sample_input)
prediction = model.predict(sample_input)

if prediction[0] == 1:
    print("\nLoan Approved")
else:
    print("\nLoan Rejected")

# ==========================================
# END OF PROJECT
# ==========================================
