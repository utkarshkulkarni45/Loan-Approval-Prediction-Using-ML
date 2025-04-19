# Loan Approval Prediction Web Application

This web application predicts the likelihood of loan approval based on various applicant features. It utilizes a machine learning model trained on a historical loan application dataset.

## Overview

This project consists of the following main components:

* **`app.py`:** The Flask application that serves the web interface and handles prediction requests.
* **`templates/`:** Contains the HTML templates for the user input form (`index.html`) and the prediction result display (`result.html`).
* **`static/`:** Stores static files such as the main stylesheet (`style.css`) and any images used.
* **`loan_approval_model.pkl`:** The serialized (saved) machine learning model, trained to predict loan approval.
* **`loan_approval_encoders.pkl`:** Contains the serialized `LabelEncoder` objects used to transform categorical input features during model training.
* **`loan_approval_dataset.csv`:** The dataset used to train the machine learning model.
* **`train_model.py`:** The Python script responsible for loading the dataset, training the machine learning model, saving the trained model, and saving the label encoders.
* **`requirements.txt`:** A list of Python packages and their versions required to run the application. This is used by pip for installing dependencies.
* `.gitignore`: Specifies files and directories that Git should ignore and not track in the repository.

## How to Use the Web Application

1.  **Access the Application:**
    * Once the application is deployed and running (e.g., on Render), open the provided URL in your web browser.
    * You will see a user-friendly form to input loan application details.

2.  **Enter Applicant Information:**
    * Carefully fill in the details for each field:
        * **Number of Dependents:** The number of individuals financially dependent on the applicant.
        * **Education:** The highest level of education attained by the applicant (Graduate or Not Graduate).
        * **Self Employed:** Indicates if the applicant is self-employed (Yes or No).
        * **Annual Income:** The applicant's total annual income.
        * **Loan Amount:** The amount of loan requested by the applicant.
        * **Loan Term (months):** The duration for which the loan is required, in months.
        * **CIBIL Score:** A credit score reflecting the applicant's creditworthiness.
        * **Residential Assets Value:** The current value of the applicant's residential properties.
        * **Commercial Assets Value:** The current value of the applicant's commercial properties.
        * **Luxury Assets Value:** The current value of the applicant's luxury assets.
        * **Bank Asset Value:** The total value of the applicant's assets held in bank accounts.
    * Informative tooltips appear when you hover over the labels of each input field, providing a brief explanation of the required information.

3.  **Get the Prediction:**
    * After filling in all the required details, click the "Predict Loan Approval" button.
    * The application will process your input, feed it to the trained machine learning model, and display the prediction on the next page.
    * The result will indicate whether the loan is predicted to be "Approved" or "Rejected".

## Development and Deployment

### Local Development

1.  **Clone the Repository:**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Set Up a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS and Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask Application:**
    ```bash
    python app.py
    ```
    Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application locally.

5.  **Train the Machine Learning Model (If Necessary):**
    If the `loan_approval_model.pkl` or `loan_approval_encoders.pkl` files are missing or you want to retrain the model:
    ```bash
    python train_model.py
    ```
    This script will train the model and save the necessary files. Ensure the `loan_approval_dataset.csv` file is present in the same directory.

### Deployment on Render

This application is designed to be easily deployed on platforms like Render.

1.  **Push to GitHub:** Ensure your entire project codebase is pushed to a GitHub repository.

2.  **Create a New Web Service on Render:**
    * Sign up or log in to [Render](https://render.com/).
    * Click on "+ New" and select "Web Service".
    * Connect your GitHub account and choose your repository.

3.  **Configure Deployment Settings:**
    * **Name:** Choose a name for your web service.
    * **Region:** Select a deployment region.
    * **Branch:** Set to `main` (or your primary branch).
    * **Root Directory:** Leave blank.
    * **Environment:** Choose "Python 3".
    * **Build command:** `pip install -r requirements.txt`
    * **Start command:** `gunicorn app:app`

4.  **Deploy:** Click "Create Web Service". Render will automatically build and deploy your application. Once the deployment is successful, you will receive a live URL to access your loan prediction web application.

## Credits

This web application was developed by Your Name.

## License

[Optional: Add your license information here, e.g., MIT License]
