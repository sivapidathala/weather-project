# Weather Data Collection System


##  Features

- Fetches real-time weather for **multiple cities**
- Shows **temperature, humidity, weather conditions**
- Automatically uploads data to **AWS S3**
- Maintains **timestamps** for historical tracking
- Uses a **.env** file for secure configuration
- Clean Python project structure with modular code

---

## Technical Stack

- **Python 3.x**
- **OpenWeather API**
- **AWS S3** (via boto3 SDK)
- **requests**, **python-dotenv**
- Optional: Terraform (Infrastructure as Code)

---

## Architecture Diagram (Mermaid)

```mermaid
flowchart TD
  A[User / Scheduler] --> B[Python Script]
  B --> C[OpenWeather API]
  B --> D[AWS S3 Upload]
  C --> B
  D --> S3Bucket[(S3 Weather Bucket)]
Project Structure
weather-project/
├── src/
│   ├── main.py
│   ├── weather_client.py
│   ├── s3_uploader.py
│   └── utils.py
├── .env.example
├── requirements.txt
├── README.md
└── .gitignore
⚙️ Prerequisites

Make sure you have:
Python 3.8+
pip installed
AWS credentials (Access key + Secret key)
OpenWeather API key
Setup Instructions (Step by Step)
1️⃣ Clone Repository
git clone https://github.com/<your-username>/weather-data-project.git
cd weather-data-project
2️⃣ Create & Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
# OR
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Configure Environment Variables
OPENWEATHER_API_KEY=your_api_key

AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_REGION=us-east-1
S3_BUCKET_NAME=your-bucket-name

CITIES=Hyderabad,Chennai,Mumbai,Bangalore
AWS S3 Setup
Log in to AWS console
Create an S3 bucket
Give your IAM user permissions:
s3:PutObject
s3:GetObject
Ensure region matches your .env
How to Run the Project
python src/main.py
Testing
pytest
Pushing to GitHub
git add .
git commit -m "Initial commit"
git push -u origin main
👤 Author

Your Name : PIDATHALA SIVA
GitHub: https://github.com/sivapidathala/weather-project.git
