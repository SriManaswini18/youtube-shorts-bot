# 🤖 YouTube Shorts Daily Content Bot

An automated Python pipeline that tracks hot topics and generates 3 ready-to-use YouTube Shorts scripts every single day.

## 🚀 How It Works
This project uses **GitHub Actions** to run a "headless" agent every morning. The agent performs the following steps:
1. **Scrapes Trending Data:** Connects to the News API to find the most discussed stories.
2. **Generates Scripts:** Formats the data into a high-retention "Shorts" structure (Hook, Body, CTA).
3. **Self-Updates:** Commits the fresh scripts directly into this repository.



---

## 🛠️ Tech Stack
* **Language:** Python 3.9
* **Automation:** GitHub Actions (Cron Scheduling)
* **Data Source:** NewsAPI
* **Storage:** Markdown files inside this Repo

---

## 📂 Project Structure
* `agent.py`: The core logic that fetches and processes news.
* `.github/workflows/main.yml`: The automation engine that schedules the daily run.
* `shorts_scripts.md`: **Where the magic happens.** Open this file to find your daily content!
* `requirements.txt`: Lists the necessary Python libraries.

---

## 🔧 Setup Instructions
If you want to fork this and run it yourself:
1. **Get an API Key:** Sign up at [NewsAPI.org](https://newsapi.org/).
2. **Add Secrets:** Go to `Settings > Secrets > Actions` and add your key as `NEWS_API_KEY`.
3. **Enable Permissions:** Go to `Settings > Actions > General` and set **Workflow permissions** to `Read and write`.
4. **Manual Trigger:** Go to the `Actions` tab and click **Run workflow** to see it in action immediately.

---

## 📈 Future Goals
- [ ] Add AI-powered rewriting for even more "attractive" scripts.
- [ ] Auto-generate image prompts for AI video tools.
- [ ] Support for multiple languages.

---
*Generated automatically by [SriManaswini18]'s Automation Bot.*
