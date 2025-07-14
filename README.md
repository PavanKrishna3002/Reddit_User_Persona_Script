🧠 Reddit User Persona Generator

This project takes a Reddit username, scrapes their recent posts and comments, and generates a user persona using OpenAI's GPT model — with source citations.

---

📁 Project Structure

reddit_user_persona/

├── main.py # Main entry point

├── requirements.txt # Project dependencies

├── .env # Stores API keys (not checked into version control)

├── README.md # You're reading it!

├── src/

│ ├── scraper.py # Handles Reddit scraping via PRAW

│ ├── llm.py # Sends content to OpenAI and gets persona

│ └── utils.py # Utility to save persona to a text file

✅ Features

- 🔍 Scrapes up to **50 posts** and **100 comments** from a given Reddit user
- 
- 🧠 Uses **GPT-4 or GPT-3.5** to generate a persona
- 
- 📎 Cites sources (URLs) for each persona trait
- 
- 💾 Outputs result to a `.txt` file

---

🚀 Setup Instructions

1. 📥 Clone or Download the Project

Unzip the project folder or clone it from your GitHub (if applicable):

cd reddit_user_persona

2. 🧪 Create Virtual Environment (Recommended)
# Windows
python -m venv venv

venv\\Scripts\\activate

# macOS/Linux
python3 -m venv venv

source venv/bin/activate

3. 📦 Install Dependencies

pip install -r requirements.txt

🔐 API Key Setup

1. Create .env file in the root directory with the following content:

REDDIT_CLIENT_ID=your_client_id_here

REDDIT_CLIENT_SECRET=your_client_secret_here

OPENAI_API_KEY=your_openai_api_key_here

USER_AGENT=RedditPersonaScript by /u/your_reddit_username

🔒 Keep this file private and never commit it to GitHub.

🔑 How to Get These Keys

🟠 Reddit API Credentials

Visit: https://www.reddit.com/prefs/apps

Scroll to Developed Applications → Click “Create App”

Fill:

Name: RedditPersonaApp

App type: script

Redirect URI: http://localhost:8080

After creating:

Client ID: under app name

Client Secret: labeled as secret

🔵 OpenAI API Key

Visit: https://platform.openai.com/account/api-keys

Click “Create new secret key”

Paste into .env under OPENAI_API_KEY

▶️ Run the Script

python main.py

You'll be prompted to enter a Reddit username (e.g., kojied).

After execution, the script will generate:

kojied_persona.txt

🧾 Example Output Format

Name: Unknown

Age Range: 25-34 (Comment: “...during my college days...” - [URL])

Occupation: Software Engineer (Post: “...at work we use Python...” - [URL])

Interests: Gaming, Psychology, Fitness (Posts & Comments: [URL])

Personality: Thoughtful, Analytical (Based on tone and content)

🧼 Optional Enhancements

1.Streamlit or Gradio UI for non-technical users

2.Output in PDF, JSON, or Markdown formats

3.Pushshift fallback if Reddit API limits are hit

4.Persona comparison between multiple users

📜 License

This project is for educational and personal use only. Use responsibly and in compliance with Reddit and OpenAI's usage policies.

🛠️ Credits

Built with ❤️ by Python, PRAW, and OpenAI GPT.
