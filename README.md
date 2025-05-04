<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Heart Disease Prediction Project using Machine Learning">
    <title>Heart Disease Prediction</title>
    <link rel="stylesheet" href="styles.css"> <!-- Optional: If you want to link a custom CSS file -->
</head>
<body>

    <header>
        <h1>Heart Disease Prediction</h1>
        <p>Predicting the likelihood of heart disease based on health features using Machine Learning</p>
    </header>

    <section id="description">
        <h2>Description</h2>
        <p>This project uses machine learning to predict the likelihood of a heart disease diagnosis based on various health parameters. It uses the **Heart Disease dataset** from Cleveland to train a **Random Forest Classifier**.</p>
    </section>

    <section id="installation">
        <h2>Installation</h2>
        <p>To run this project, you will need Python and the following libraries:</p>
        <ul>
            <li>pandas</li>
            <li>matplotlib</li>
            <li>seaborn</li>
            <li>scikit-learn</li>
        </ul>
        <p>Install the dependencies using:</p>
        <pre><code>pip install pandas matplotlib seaborn scikit-learn</code></pre>
    </section>

    <section id="usage">
        <h2>Usage</h2>
        <p>To use this project:</p>
        <ol>
            <li>Clone the repository: <code>git clone https://github.com/yourusername/heart-disease-prediction.git</code></li>
            <li>Navigate to the project folder: <code>cd heart-disease-prediction</code></li>
            <li>Run the Python script: <code>python heart_disease_prediction.py</code></li>
        </ol>
    </section>

    <section id="model-evaluation">
        <h2>Model Evaluation</h2>
        <p>The performance of the model is evaluated using the following metrics:</p>
        <ul>
            <li>Accuracy</li>
            <li>Mean Squared Error</li>
            <li>R2 Score</li>
            <li>Classification Report (Precision, Recall, F1-Score)</li>
            <li>Confusion Matrix</li>
        </ul>
    </section>

    <section id="visualization">
        <h2>Visualization</h2>
        <p>The correlation matrix of different features is displayed using a heatmap.</p>
        <img src="correlation_matrix_image.png" alt="Correlation Heatmap">
    </section>

</body>
</html>
