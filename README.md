# Social-Media-Insights-Engine
The project's objective is to analyze and parse user JSON data, carrying out filtering operations.

## Prerequisites

Make sure you have the following installed on your local machine:

- Python (version 3.5 or above)
- pip (Python package installer)
- Virtualenv 

## Setup Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/EshwarThummala/smie-api.git
    cd your-project
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask application:**

    ```bash
    python app.py
    ```

4. **Make a POST request using Postman:**

    - Open Postman and create a new request.
    - Set the request type to POST.
    - Enter the URL `http://localhost:5000` as the request URL.
    - In the request body, select "raw" and choose "JSON (application/json)" as the body type.
    - Paste the following JSON body into the request body:

    ```json
    {
        "follower_filter" : [1000,1200],
        "avgview_filter": 5000,
        "keyword_filter": "k"
    }
    ```

    - Click the "Send" button to make the request to the Flask application.

## Troubleshooting

If you encounter any issues during setup or while running the application, here are a few common troubleshooting steps:

- **Issue:** ImportError: No module named 'flask'
  **Solution:** Make sure Flask is installed in your Python environment. You can install it using pip: `pip install Flask`.

- More troubleshooting tips are on the way...

If you're unable to resolve the issue, please feel free to open an issue on GitHub, and I will be happy to assist you.

