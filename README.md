# Auto Watermark Telegram Bot

This Python script automatically adds watermarks to images sent to your Telegram bot. The watermark is selected based on the brightness of the image's background—using a light watermark for dark images and a dark watermark for light images.

## How It Works? 
- When a user sends a photo to the bot, the image is downloaded.
- If the image width exceeds 1080px, it will be resized to fit within the specified maximum width.
- The script analyzes the brightness of the central region of the image to determine which watermark to apply.
- The selected watermark (either light or dark) is resized and added to the image with reduced opacity for a subtle effect.
- The final watermarked image is sent back to the user.

## Requirements

- Python 3.7+
- [Pillow](https://pillow.readthedocs.io/en/stable/) for image manipulation
- [python-telegram-bot](https://python-telegram-bot.org/) for the Telegram Bot API
- A Telegram bot token (obtainable from [BotFather](https://core.telegram.org/bots#botfather))

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/tinequara/Auto-watermark-for-Telegram.git
cd Auto-watermark-for-Telegram
```
### 2. Instal requirements
````bash
pip install -r requirements.txt
````
### 3. Put files water_dark.png and water_light.png in root folder.
### 4. Create bot with BotFather, and take API token from and put in: 
````bash
TOKEN = "123" ## your api token from BotFather
````
### 5. Start the script 
````bash
py kek.py
````
### 6. Enjoy!
