![Price Prediction](https://github.com/user-attachments/assets/478a0946-5486-4825-9a19-139e3b06ab54)

# Gurgaon Real Estate Price Prediction
 
I developed a machine learning application to predict property prices in Gurgaon using a structured data science workflow and full-stack deployment:

### 1. Data Science Workflow
 
- Performed EDA to understand the dataset and identify patterns
- Cleaned and preprocessed the data (handling missing values, encoding, etc.)
- Applied cross-validation and GridSearchCV for model tuning
- Used Gradient Boosting Regressor, achieving around 94% accuracy

 
### 2. Backend (Flask API)
 
- Built a Flask API to serve the ML model
- API allows users to: 
  > Fetch available locations and property types
  
  > Submit property details to get a predicted price


### 3. Frontend (HTML, CSS, JS)

- Created a simple user interface with HTML, CSS, and JavaScript
- Users can input property details through the form
- The frontend makes a request to the Flask API and displays the predicted price

 
### 4. Deployment (AWS + NGINX)

- Deployed the full project on an Ubuntu-based AWS EC2 instance
- Used NGINX to:
  > Serve the static frontend files
  
  > Reverse-proxy API requests to the Flask backend running on port 5000

 
Final product is accessible via a web browser using the EC2 public IP

## Dataset Usage

This Project uses the [Indian Real Estate - 99acres.com](https://www.kaggle.com/datasets/arvanshul/gurgaon-real-estate-99acres-com) from kaggle.

The Gurgaon Real Estate dataset (licensed under [CDLA-Sharing 1.0](https://cdla.dev/sharing-1-0/)) can be used for various real estate related tasks, including:
- Property price prediction.
- Market analysis to identify trends and patterns.
- Identifying popular property types and locations.
- Evaluating the impact of property attributes on price

  **Note**: This dataset is not included in this repository. Please download it directly from the Kaggle link above.

> *The background image shown here is used only for demonstration purposes in the app UI and is not redistributed. Please replace it with a properly licensed image if using this project.*

> Note: The trained model weights are not included in this repository. You can train train the model yourself using the provided notebook and the linked dataset.
