
# Telegram Bot with Webhook on Render

This project sets up a Telegram bot using Flask and deploys it on Render using a webhook.

## 1. Create a Telegram Bot
- Open Telegram and search for `@BotFather`
- Use `/newbot` to create a bot and get your bot token
- Save the token for later use

## 2. Project Structure

- `app.py`: Flask app that handles Telegram webhook
- `requirements.txt`: Python dependencies
- `Procfile`: Render deployment process

## 3. Deploy to Render

1. Push your code to a GitHub repository.
2. Go to https://render.com and create a new Web Service.
3. Connect your GitHub repo.
4. Set the environment variable:
   - `BOT_TOKEN`: your Telegram bot token
5. Choose the **Free** plan and deploy.

## 4. Set the Webhook

After deployment, get your Render app URL (e.g., `https://your-bot.onrender.com`) and run:

```bash
curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook" \
     -d "url=https://your-bot.onrender.com/<YOUR_BOT_TOKEN>"
