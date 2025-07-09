import os
from PIL import Image, ImageEnhance, ImageStat
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "123" ## your api token from BotFather
MAX_WIDTH = 1080
WATERMARK_SCALE = 0.6
LIGHT_WATERMARK = "water_light.png" ##for dark background
DARK_WATERMARK = "water_dark.png" ##for white background

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file = await context.bot.get_file(photo.file_id)
    image_path = "user_image.jpg"
    await file.download_to_drive(image_path)
    base_image = Image.open(image_path).convert("RGBA")
    if base_image.width > MAX_WIDTH:
        w_percent = MAX_WIDTH / float(base_image.width)
        h_size = int(float(base_image.height) * w_percent)
        base_image = base_image.resize((MAX_WIDTH, h_size), Image.LANCZOS)
    base_width, base_height = base_image.size
    target_wm_width = int(base_width * WATERMARK_SCALE)
    region_size = target_wm_width
    left = (base_width - region_size) // 2
    top = (base_height - region_size) // 2
    right = left + region_size
    bottom = top + region_size
    region = base_image.crop((left, top, right, bottom)).convert("L")
    brightness = ImageStat.Stat(region).mean[0]
    if brightness < 127:
        watermark_path = LIGHT_WATERMARK
    else:
        watermark_path = DARK_WATERMARK
    watermark = Image.open(watermark_path).convert("RGBA")
    scale_ratio = target_wm_width / float(watermark.width)
    target_wm_height = int(float(watermark.height) * scale_ratio)
    watermark = watermark.resize((target_wm_width, target_wm_height), Image.LANCZOS)
    alpha = watermark.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(0.3)
    watermark.putalpha(alpha)
    wm_width, wm_height = watermark.size
    position = ((base_width - wm_width) // 2, (base_height - wm_height) // 2)
    combined = base_image.copy()
    combined.paste(watermark, position, mask=watermark)
    output_path = "watermarked.png" ##ready name
    combined.save(output_path)
    await update.message.reply_photo(photo=open(output_path, 'rb'))
    os.remove(image_path)
    os.remove(output_path)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

print("Auto-watermark for Telegram is started...Send pic your bot and enjoy!")
app.run_polling()
