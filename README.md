![Price Prediction](https://github.com/user-attachments/assets/478a0946-5486-4825-9a19-139e3b06ab54)

Gurgaon Real Estate Price Prediction
 
I developed a machine learning application to predict property prices in Gurgaon using a structured data science workflow and full-stack deployment:

1. Data Science Workflow
 
- Performed EDA to understand the dataset and identify patterns
- Cleaned and preprocessed the data (handling missing values, encoding, etc.)
- Applied cross-validation and GridSearchCV for model tuning
- Used Gradient Boosting Regressor, achieving around 94% accuracy

 
2. Backend (Flask API)
 
- Built a Flask API to serve the ML model
- API allows users to: 
  > Fetch available locations and property types
  
  > Submit property details to get a predicted price


3. Frontend (HTML, CSS, JS)

- Created a simple user interface with HTML, CSS, and JavaScript
- Users can input property details through the form
- The frontend makes a request to the Flask API and displays the predicted price

 
4. Deployment (AWS + NGINX)

- Deployed the full project on an Ubuntu-based AWS EC2 instance
- Used NGINX to:
  > Serve the static frontend files
  
  > Reverse-proxy API requests to the Flask backend running on port 5000

 
Final product is accessible via a web browser using the EC2 public IP
