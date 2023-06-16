## Check the weather app

### Coding challenge description
Here is the coding challenge :)

Create an application:
• Prompt user for zipcode
• Call this service to get the weather:
[Weatherstack API URL](http://api.weatherstack.com/current?access_key=<ACCESS_KEY>&query=<ZIPCODE>)


Here are the answers to your questions:

- Should I go outside?
  - If it's not raining, then yes, you can go outside.

- Should I wear sunscreen?
  - If the UV index is above 3, it is recommended to wear sunscreen.

- Can I fly my kite?
  - Yes, you can fly your kite if it's not raining and the wind speed is over 15.


### Prerequisites

- Python 3.9 or higher
- Docker (if running inside a container)

### Local Development

1. Clone the repository:

   ```bash
   git clone https://github.com/nandor-frenteria/challenge_fpt
   cd challenge_fpt
   ```

2. Set up a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set environment variables:

   - Create a `.env` file in the project directory.
   - Define any required environment variables in the `.env` file.

   ```
   ACCESS_KEY=<ACCESS_KEY_PROVIDED>

   ```

5. Run the Flask application:

   ```bash
   python app.py
   ```

6. Access the application in a web browser at `http://localhost:5000`.

### Running Inside a Docker Container

1. Build the Docker image:

   ```bash
   docker build -t my-flask-app .
   ```

2. Run the Docker container:

   ```bash
   docker run -d -p 5000:5000 --env-file .env my-flask-app
   ```

   Make sure to replace `my-flask-app` with the appropriate image name.

3. Access the application in a web browser at `http://localhost:5000`.
