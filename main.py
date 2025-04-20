# import logging
# import yt_dlp
# import os
# import tempfile
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler
# import asyncio
# import re
# from typing import Dict, Any
# from dotenv import load_dotenv
# from concurrent.futures import ThreadPoolExecutor
# import threading
# from flask import Flask


# # Flask app for Render Web Service
# flask_app = Flask(__name__)

# @flask_app.route('/')
# def home():
#     return "Stream Sage Bot is running!"

# def run_flask():
#     """Run Flask web server in a separate thread"""
#     port = int(os.getenv("PORT", 8080))
#     flask_app.run(host='0.0.0.0', port=port)


# # Load environment variables from .env file
# load_dotenv()

# # Set up logging
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )
# logger = logging.getLogger(__name__)

# # Thread pool for synchronous operations
# executor = ThreadPoolExecutor(max_workers=4)

# # Define constants
# MAX_VIDEO_SIZE = 50 * 1024 * 1024  # 50MB limit for Telegram
# MAX_PREMIUM_SIZE = 100 * 1024 * 1024  # 100MB for premium users
# SUPPORTED_PLATFORMS = ["YouTube", "TikTok", "Twitter", "Instagram", "Facebook", "Twitch", "Reddit"]
# PREMIUM_FEATURES = ["Video Generation", "Image Generation", "Larger File Downloads", "Batch Processing", "Priority Support"]

# async def safe_reply(update: Update, context: CallbackContext, text: str, **kwargs):
#     """Safely send a reply through any update type."""
#     try:
#         if update.message:
#             return await update.message.reply_text(text, **kwargs)
#         elif update.callback_query:
#             try:
#                 return await update.callback_query.message.reply_text(text, **kwargs)
#             except:
#                 return await update.callback_query.edit_message_text(text, **kwargs)
#         elif update.effective_message:
#             return await update.effective_message.reply_text(text, **kwargs)
#     except Exception as e:
#         logger.error(f"Failed to send message: {e}")
#         if update.effective_chat:
#             return await context.bot.send_message(
#                 chat_id=update.effective_chat.id,
#                 text=text,
#                 **kwargs
#             )

# async def start(update: Update, context: CallbackContext):
#     """Send a welcome message when the command /start is issued."""
#     user = update.effective_user
#     welcome_message = (
#         f"🌟 *Welcome {user.first_name} to the Ultimate Media Bot!* 🌟\n\n"
        # "I'm your all-in-one solution for media downloading. Here's what I can do:\n\n"
        # "🎥 *Video Downloader* - Download videos from various platforms\n"
        # "🎵 *Audio Extractor* - Convert videos to high-quality MP3\n"
        # "📊 *Media Info* - Get detailed information about any video\n\n"
        # "💎 *Premium Features Coming Soon*\n"
        # "🔹 *How to use:*\n"
        # "1. Send me a video URL\n"
        # "2. Choose your preferred format\n"
        # "3. Get your media instantly!\n\n"
        # "📌 *Available Commands:*\n"
        # "/start - Show this welcome message\n"
        # "/help - Detailed help and instructions\n"
        # "/about - Bot information and credits\n"
        # "/features - List all available features\n"
        # "/premium - Learn about premium options\n\n"
        # "Try me out by sending a video link now!"
#     )
    
#     keyboard = [
#         [InlineKeyboardButton("📋 Features List", callback_data="features_list"),
#          InlineKeyboardButton("❓ How To Use", callback_data="quick_help")],
#         [InlineKeyboardButton("🔗 Supported Sites", callback_data="supported_sites")]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
    
#     await safe_reply(update, context, welcome_message, reply_markup=reply_markup, parse_mode='Markdown')

# async def help_command(update: Update, context: CallbackContext):
#     """Send a help message when the command /help is issued."""
#     help_text = (
#         "📚 *Complete Help Guide*\n\n"
#         "*Basic Commands:*\n"
#         "/start - Welcome message\n"
#         "/help - This help guide\n"
#         "/about - Bot information\n"
#         "/features - List all features\n"
#         "/premium - Premium subscription info\n\n"
#         "*How to Download Videos:*\n"
#         "1. Send me a video URL from any supported platform\n"
#         "2. I'll detect it automatically and show options\n"
#         "3. Choose to download as video or audio\n"
#         "4. Wait for processing (usually takes a few seconds)\n"
#         "5. Receive your file directly in chat\n\n"
#         "*Supported Platforms:*\n"
#         f"{', '.join(SUPPORTED_PLATFORMS)}\n\n"
#         "*Advanced Features:*\n"
#         "• Multiple quality options (for supported platforms)\n"
#         "• Video information extraction (duration, views, etc.)\n"
#         "• High-quality audio extraction (up to 320kbps)\n\n"
#         "⚠️ *Limitations:*\n"
#         "• Free users: 50MB file size limit\n"
#         "• Some platforms may have restrictions\n\n"
#         "Need more help? Just send me a message!"
#     )
#     await safe_reply(update, context, help_text, parse_mode='Markdown')

# async def about_command(update: Update, context: CallbackContext):
#     """Send information about the bot when the command /about is issued."""
#     about_text = (
#         "🤖 *Ultimate Media Bot*\n\n"
#         "*Version:* 1.0.0\n"
#         "*Last Updated:* April 2025\n\n"
#         "*Core Features:*\n"
#         "• Video downloading from 50+ platforms\n"
#         "• Audio extraction with quality options\n"
#         "• Video information display\n\n"
#         "*Technologies Used:*\n"
#         "• Python 3.10+\n"
#         "• python-telegram-bot\n"
#         "• yt-dlp (video extraction)\n"
#         "• FFmpeg (media processing)\n\n"
#         "*Developer:*\n"
#         "Christian Kusi\n\n"
#         "This bot is actively maintained and updated regularly with new features!"
#     )
#     await safe_reply(update, context, about_text, parse_mode='Markdown')

# async def features_command(update: Update, context: CallbackContext):
#     """List all available features."""
#     features_text = (
#         "✨ *All Available Features*\n\n"
#         "*Current Features:*\n"
#         "• Video downloading from supported platforms\n"
#         "• Audio extraction (MP3 format)\n"
#         "• Video information display\n"
#         "• Quality selection (when available)\n"
#         "• 50MB file size limit\n\n"
#         "*Coming Soon:*\n"
#         f"• {' | '.join(PREMIUM_FEATURES)}\n"
#         "• 100MB file size limit\n"
#         "• Priority processing\n"
#         "• Batch downloads\n\n"
#         "Stay tuned for updates!"
#     )
#     await safe_reply(update, context, features_text, parse_mode='Markdown')

# async def premium_command(update: Update, context: CallbackContext):
#     """Show premium subscription information."""
#     premium_text = (
#         "💎 *Premium Features Coming Soon!*\n\n"
#         "We're working hard to bring you these exciting features:\n\n"
#         f"• {' | '.join(PREMIUM_FEATURES)}\n"
#         "• Larger file downloads (up to 100MB)\n"
#         "• Faster processing times\n"
#         "• Batch processing\n\n"
#         "Check back soon for updates on our premium offerings!\n\n"
#         "For now, enjoy our free features - they're pretty awesome too!"
#     )
#     await safe_reply(update, context, premium_text, parse_mode='Markdown')

# def is_valid_url(url: str) -> bool:
#     """Check if the provided string is a valid URL."""
#     url_pattern = re.compile(
#         r'^(https?://)?'  # http:// or https://
#         r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
#         r'localhost|'  # localhost...
#         r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
#         r'(?::\d+)?'  # optional port
#         r'(?:/?|[/?]\S+)$', re.IGNORECASE
#     )
#     return bool(url_pattern.match(url))

# async def handle_message(update: Update, context: CallbackContext):
#     """Process incoming messages and detect URLs."""
#     message_text = update.message.text
    
#     if is_valid_url(message_text):
#         context.user_data['current_url'] = message_text
        
#         processing_msg = await update.message.reply_text(
#             "🔍 Analyzing the link...",
#             reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="cancel")]])
#         )
#         context.user_data['processing_msg_id'] = processing_msg.message_id
#         context.user_data['chat_id'] = update.message.chat_id
        
#         try:
#             loop = asyncio.get_running_loop()
#             with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
#                 info_dict = await loop.run_in_executor(
#                     executor,
#                     lambda: ydl.extract_info(message_text, download=False)
#                 )  # This parenthesis was missing
                
#                 context.user_data['video_info'] = info_dict
                
#                 keyboard = [
#                     [InlineKeyboardButton("🎬 Download Video", callback_data="video"),
#                      InlineKeyboardButton("🎵 Download Audio (MP3)", callback_data="audio")],
#                     [InlineKeyboardButton("ℹ️ Video Info", callback_data="info"),
#                      InlineKeyboardButton("❌ Cancel", callback_data="cancel")]
#                 ]
#                 reply_markup = InlineKeyboardMarkup(keyboard)
                
#                 title = info_dict.get('title', 'Video')
#                 duration = info_dict.get('duration')
#                 duration_str = f"{int(duration // 60)}:{int(duration % 60):02d}" if duration else "Unknown"
                
#                 await context.bot.edit_message_text(
#                     chat_id=update.message.chat_id,
#                     message_id=context.user_data['processing_msg_id'],
#                     text=(
#                         f"📋 *Video Found*\n\n"
#                         f"*Title:* {title}\n"
#                         f"*Duration:* {duration_str}\n"
#                         f"*Source:* {info_dict.get('extractor', 'Unknown')}\n\n"
#                         f"Select an option to continue:"
#                     ),
#                     reply_markup=reply_markup,
#                     parse_mode='Markdown'
#                 )
                
#         except Exception as e:
#             logger.error(f"Error fetching video info: {e}")
#             await context.bot.edit_message_text(
#                 chat_id=update.message.chat_id,
#                 message_id=context.user_data['processing_msg_id'],
#                 text="❌ Sorry, I couldn't process this URL. Make sure it's from a supported platform."
#             )
#     else:
#         await update.message.reply_text(
#             "Please send me a valid video URL from platforms like YouTube, TikTok, Twitter, etc.\n\n"
#             "Use /help for complete instructions."
#         )

# async def button_callback(update: Update, context: CallbackContext):
#     """Handle button presses from inline keyboards."""
#     query = update.callback_query
#     await query.answer()
    
#     if query.data == "cancel":
#         await query.edit_message_text("✅ Operation cancelled.")
#         return
#     elif query.data == "features_list":
#         await features_command(update, context)
#         return
#     elif query.data == "premium_info":
#         await premium_command(update, context)
#         return
#     elif query.data == "quick_help":
#         await help_command(update, context)
#         return
#     elif query.data == "supported_sites":
#         sites_text = "📺 *Supported Platforms:*\n\n" + "\n".join(f"• {site}" for site in SUPPORTED_PLATFORMS)
#         await query.edit_message_text(sites_text, parse_mode='Markdown')
#         return
    
#     video_url = context.user_data.get('current_url')
#     if not video_url:
#         await query.edit_message_text("❌ Session expired. Please send the URL again.")
#         return
    
#     if query.data == "info":
#         await show_video_info(query, context)
#     elif query.data in ["video", "audio"]:
#         await start_download(query, context, format_type=query.data)

# async def show_video_info(query, context: CallbackContext):
#     """Show available video information, even if some fields are missing."""
#     try:
#         info_dict = context.user_data.get('video_info', {})
        
#         # Build information text piece by piece
#         info_parts = ["📑 *Video Information*"]
        
#         # Helper function to safely add fields
#         def add_field(name, value, formatter=None):
#             if value not in [None, 'Unknown', '']:
#                 formatted = formatter(value) if formatter else str(value)
#                 info_parts.append(f"*{name}:* {formatted}")
        
#         # Add available fields
#         add_field("Title", info_dict.get('title'))
        
#         duration = info_dict.get('duration')
#         if duration:
#             duration_str = f"{int(duration // 60)}:{int(duration % 60):02d}"
#             add_field("Duration", duration_str)
        
#         add_field("Channel/Uploader", info_dict.get('uploader'))
        
#         upload_date = info_dict.get('upload_date')
#         if upload_date and len(upload_date) == 8:
#             formatted_date = f"{upload_date[6:8]}/{upload_date[4:6]}/{upload_date[0:4]}"
#             add_field("Upload Date", formatted_date)
        
#         # Add numeric fields with formatting
#         def format_count(count):
#             if isinstance(count, int):
#                 if count >= 1000000:
#                     return f"{count/1000000:.1f}M"
#                 elif count >= 1000:
#                     return f"{count/1000:.1f}K"
#             return str(count)
        
#         add_field("Views", info_dict.get('view_count'), format_count)
#         add_field("Likes", info_dict.get('like_count'), format_count)
        
#         # Add technical info if available
#         add_field("Resolution", info_dict.get('resolution'))
#         add_field("FPS", info_dict.get('fps'))
        
#         filesize = info_dict.get('filesize_approx')
#         if isinstance(filesize, (int, float)):
#             if filesize >= 1000000:
#                 filesize_str = f"{filesize/1000000:.1f} MB"
#             elif filesize >= 1000:
#                 filesize_str = f"{filesize/1000:.1f} KB"
#             else:
#                 filesize_str = f"{filesize} bytes"
#             add_field("Estimated Size", filesize_str)
        
#         # If we couldn't get any info
#         if len(info_parts) == 1:
#             info_parts.append("\n⚠️ Couldn't retrieve detailed information")
#             info_parts.append("You can still try downloading the media")
        
#         # Create keyboard
#         keyboard = [
#             [InlineKeyboardButton("🎬 Download Video", callback_data="video"),
#              InlineKeyboardButton("🎵 Download Audio", callback_data="audio")],
#             [InlineKeyboardButton("❌ Cancel", callback_data="cancel")]
#         ]
        
#         await query.edit_message_text(
#             "\n\n".join(info_parts),
#             reply_markup=InlineKeyboardMarkup(keyboard),
#             parse_mode='Markdown'
#         )
        
#     except Exception as e:
#         logger.error(f"Error showing video info: {e}")
#         keyboard = [
#             [InlineKeyboardButton("Try Download Anyway", callback_data="video")],
#             [InlineKeyboardButton("Cancel", callback_data="cancel")]
#         ]
#         await query.edit_message_text(
#             "⚠️ Limited information available\n\n"
#             "You can still try downloading the media",
#             reply_markup=InlineKeyboardMarkup(keyboard),
#             parse_mode='Markdown'
#         )

# async def start_download(query, context: CallbackContext, format_type: str):
#     """Start downloading the video or audio."""
#     video_url = context.user_data.get('current_url')
#     max_size = MAX_VIDEO_SIZE
    
#     download_msg = await query.edit_message_text(
#         f"⏳ Starting {'audio' if format_type == 'audio' else 'video'} download..."
#     )
    
#     asyncio.create_task(
#         download_and_send_media(
#             video_url,
#             format_type,
#             max_size,
#             context,
#             query.message.chat_id,
#             download_msg.message_id
#         )
#     )

# async def download_and_send_media(url: str, format_type: str, max_size: int, 
#                                  context: CallbackContext, chat_id: int, message_id: int):
#     """Handle the complete download and send process."""
#     try:
#         with tempfile.TemporaryDirectory() as temp_dir:
#             ydl_opts = {
#                 'outtmpl': os.path.join(temp_dir, '%(id)s.%(ext)s'),
#                 'quiet': True,
#                 'noplaylist': True,
#                 'retries': 3,
#             }

#             if format_type == "audio":
#                 ydl_opts.update({
#                     'format': 'bestaudio/best',
#                     'postprocessors': [{
#                         'key': 'FFmpegExtractAudio',
#                         'preferredcodec': 'mp3',
#                         'preferredquality': '192',
#                     }],
#                 })
#                 file_extension = "mp3"
#             else:
#                 ydl_opts.update({
#                     'format': 'bestvideo+bestaudio/best',
#                     'postprocessors': [{
#                         'key': 'FFmpegVideoConvertor',
#                         'preferedformat': 'mp4',
#                     }],
#                 })
#                 file_extension = "mp4"

#             loop = asyncio.get_running_loop()
#             with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#                 info_dict = await loop.run_in_executor(
#                     executor,
#                     lambda: ydl.extract_info(url, download=True)
#                 )
                
#                 file_id = info_dict['id']
#                 file_path = os.path.join(temp_dir, f"{file_id}.{file_extension}")
                
#                 if not os.path.exists(file_path):
#                     for file in os.listdir(temp_dir):
#                         if file.startswith(file_id):
#                             file_path = os.path.join(temp_dir, file)
#                             break

#                 file_size = os.path.getsize(file_path)
#                 if file_size > max_size:
#                     await context.bot.edit_message_text(
#                         chat_id=chat_id,
#                         message_id=message_id,
#                         text=(
#                             f"⚠️ File too large ({file_size/1024/1024:.1f}MB > "
#                             f"{max_size/1024/1024:.1f}MB limit)"
#                         )
#                     )
#                     return

#                 await context.bot.edit_message_text(
#                     chat_id=chat_id,
#                     message_id=message_id,
#                     text="✅ Download complete! Now uploading..."
#                 )

#                 with open(file_path, 'rb') as file:
#                     if format_type == "audio":
#                         await context.bot.send_audio(
#                             chat_id=chat_id,
#                             audio=file,
#                             title=info_dict.get('title', 'Audio'),
#                             performer=info_dict.get('uploader', 'Unknown'),
#                             duration=int(info_dict.get('duration', 0)),
#                             caption=f"🎵 {info_dict.get('title', 'Audio')}"
#                         )
#                     else:
#                         await context.bot.send_video(
#                             chat_id=chat_id,
#                             video=file,
#                             caption=f"🎬 {info_dict.get('title', 'Video')}",
#                             duration=int(info_dict.get('duration', 0))
#                         )

#                 await context.bot.delete_message(chat_id=chat_id, message_id=message_id)

#     except Exception as e:
#         logger.error(f"Download failed: {e}")
#         await context.bot.edit_message_text(
#             chat_id=chat_id,
#             message_id=message_id,
#             text=f"❌ Download failed: {str(e)}"
#         )

# async def error_handler(update: Update, context: CallbackContext):
#     """Log errors and send user-friendly messages."""
#     logger.error(f"Update {update} caused error {context.error}")
    
#     if update.effective_chat:
#         await context.bot.send_message(
#             chat_id=update.effective_chat.id,
#             text="❌ An error occurred. Please try again later."
#         )

# async def main():
#     TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
#     if not TOKEN:
#         logger.error("No TELEGRAM_BOT_TOKEN environment variable found!")
#         return
    
#     # Start Flask in a separate thread
#     flask_thread = threading.Thread(target=run_flask, daemon=True)
#     flask_thread.start()
    
#     # Create application
#     application = Application.builder().token(TOKEN).build()
    
#     # Register handlers
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(CommandHandler("help", help_command))
#     application.add_handler(CommandHandler("about", about_command))
#     application.add_handler(CommandHandler("features", features_command))
#     application.add_handler(CommandHandler("premium", premium_command))
#     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
#     application.add_handler(CallbackQueryHandler(button_callback))
#     application.add_error_handler(error_handler)
    
   

    
#     # # Run the bot with proper shutdown handling
#     # try:
#     #     await application.initialize()
#     #     await application.start()
#     #     await application.updater.start_polling()
        
#     #     # Keep the application running until interrupted
#     #     while True:
#     #         await asyncio.sleep(1)
            
#     # except (KeyboardInterrupt, asyncio.CancelledError):
#     #     logger.info("Shutting down bot...")
#     #     await application.updater.stop()
#     #     await application.stop()
#     #     await application.shutdown()
#     # except Exception as e:
#     #     logger.error(f"Fatal error: {e}")
#     #     await application.shutdown()
#     #     raise

#     # Start polling
#     await application.initialize()
#     await application.start()
#     await application.updater.start_polling(
#         drop_pending_updates=True,
#         allowed_updates=Update.ALL_TYPES
#     )
    
#     logger.info("Bot is now running with Flask web service")
    
#     # Keep the application running
#     while True:
#         await asyncio.sleep(3600)  # Sleep for longer periods
        
# # if __name__ == '__main__':
# #     try:
# #         # Windows-specific event loop policy
# #         if os.name == 'nt':
# #             asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
# #         # Create and run event loop
# #         loop = asyncio.new_event_loop()
# #         asyncio.set_event_loop(loop)
        
# #         try:
# #             loop.run_until_complete(main())
# #         finally:
# #             loop.close()
            
# #     except KeyboardInterrupt:
# #         logger.info("Bot stopped by user")
# #     except Exception as e:
# #         logger.error(f"Fatal error: {e}")

# if __name__ == '__main__':
#     try:
#         # Windows-specific event loop policy
#         if os.name == 'nt':
#             asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
#         asyncio.run(main())
#     except KeyboardInterrupt:
#         logger.info("Bot stopped by user")
#     except Exception as e:
#         logger.error(f"Fatal error: {e}")

# import logging
# import yt_dlp
# import os
# import tempfile
# import subprocess
# import requests
# from bs4 import BeautifulSoup
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
# from telegram.error import Conflict
# import asyncio
# import re
# from dotenv import load_dotenv
# from concurrent.futures import ThreadPoolExecutor
# import threading
# from flask import Flask

# # Flask app for Render
# flask_app = Flask(__name__)

# @flask_app.route('/')
# def home():
#     return "Stream Sage Bot is running!"

# def run_flask():
#     port = int(os.getenv("PORT", 8080))
#     flask_app.run(host='0.0.0.0', port=port)

# # Load environment variables
# load_dotenv()

# # Logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Thread pool
# executor = ThreadPoolExecutor(max_workers=4)

# # Constants
# MAX_VIDEO_SIZE = 50 * 1024 * 1024
# MAX_PREMIUM_SIZE = 100 * 1024 * 1024
# SUPPORTED_PLATFORMS = ["TikTok", "Twitter", "Instagram", "Facebook", "Twitch", "Reddit"]
# PREMIUM_FEATURES = ["Video Generation", "Image Generation", "Larger File Downloads", "Batch Processing", "Priority Support"]
# TIKSAVE_URL = "https://tiksave.io/en"

# async def safe_reply(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str, **kwargs):
#     try:
#         if update.message:
#             return await update.message.reply_text(text, **kwargs)
#         elif update.callback_query:
#             try:
#                 return await update.callback_query.message.reply_text(text, **kwargs)
#             except:
#                 return await update.callback_query.edit_message_text(text, **kwargs)
#         elif update.effective_message:
#             return await update.effective_message.reply_text(text, **kwargs)
#     except Exception as e:
#         logger.error(f"Failed to send: {e}")
#         if update.effective_chat:
#             return await context.bot.send_message(chat_id=update.effective_chat.id, text=text, **kwargs)

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user = update.effective_user
#     welcome_message = (
#         f"🌟 *Welcome {user.first_name} to the Ultimate Media Bot!* 🌟\n\n"
#         "I'm your all-in-one solution for media downloading. Here's what I can do:\n\n"
#         "🎥 *Video Downloader* - Download videos from various platforms\n"
#         "🎵 *Audio Extractor* - Convert videos to high-quality MP3\n"
#         "📊 *Media Info* - Get detailed information about any video\n\n"
#         "💎 *Premium Features Coming Soon*\n"
#         "🔹 *How to use:*\n"
#         "1. Send me a video URL\n"
#         "2. Choose your preferred format\n"
#         "3. Get your media instantly!\n\n"
#         "📌 *Available Commands:*\n"
#         "/start - Show this welcome message\n"
#         "/help - Detailed help and instructions\n"
#         "/about - Bot information and credits\n"
#         "/features - List all available features\n"
#         "/premium - Learn about premium options\n\n"
#         "Try me out by sending a video link now!"
#     )
#     keyboard = [
#         [InlineKeyboardButton("📋 Features List", callback_data="features_list"),
#          InlineKeyboardButton("❓ How To Use", callback_data="quick_help")],
#         [InlineKeyboardButton("🔗 Supported Sites", callback_data="supported_sites")]
#     ]
#     await safe_reply(update, context, welcome_message, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     help_text = (
#         "📚 *Complete Help Guide*\n\n"
#         "*Basic Commands:*\n"
#         "/start - Welcome message\n"
#         "/help - This help guide\n"
#         "/about - Bot information\n"
#         "/features - List all features\n"
#         "/premium - Premium subscription info\n\n"
#         "*How to Download Videos:*\n"
#         "1. Send me a video URL from any supported platform\n"
#         "2. I'll detect it automatically and show options\n"
#         "3. Choose to download as video or audio\n"
#         "4. Wait for processing (usually takes a few seconds)\n"
#         "5. Receive your file directly in chat\n\n"
#         "*Supported Platforms:*\n"
#         f"{', '.join(SUPPORTED_PLATFORMS)}\n\n"
#         "*Advanced Features:*\n"
#         "• Multiple quality options (for supported platforms)\n"
#         "• Video information extraction (duration, views, etc.)\n"
#         "• High-quality audio extraction (up to 320kbps)\n\n"
#         "⚠️ *Limitations:*\n"
#         "• Free users: 50MB file size limit\n"
#         "• Some platforms may have restrictions\n\n"
#         "*Authentication for Platforms:*\n"
#         "Some platforms (e.g., Instagram, Twitter) may require login. To enable downloads:\n"
#         "1. Export your browser cookies using a tool like 'Export Cookies' extension.\n"
#         "2. Save the cookies as 'cookies.txt' and upload it to the bot server.\n"
#         "3. The bot will use these cookies to authenticate.\n\n"
#         "Need more help? Just send me a message!"
#     )
#     await safe_reply(update, context, help_text, parse_mode='Markdown')

# async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     about_text = (
#         "🤖 *Ultimate Media Bot*\n\n"
#         "*Version:* 1.0.0\n"
#         "*Last Updated:* April 2025\n\n"
#         "*Core Features:*\n"
#         "• Video downloading from 50+ platforms\n"
#         "• Audio extraction with quality options\n"
#         "• Video information display\n\n"
#         "*Technologies Used:*\n"
#         "• Python 3.10+\n"
#         "• python-telegram-bot\n"
#         "• yt-dlp (video Wextraction)\n"
#         "• FFmpeg (media processing)\n\n"
#         "*Developer:*\n"
#         "Christian Kusi\n\n"
#         "This bot is actively maintained and updated regularly with new features!"
#     )
#     await safe_reply(update, context, about_text, parse_mode='Markdown')

# async def features_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     features_text = (
#         "✨ *All Available Features*\n\n"
#         "*Current Features:*\n"
#         "• Video downloading from supported platforms\n"
#         "• Audio extraction (MP3 format)\n"
#         "• Video information display\n"
#         "• Quality selection (when available)\n"
#         "• 50MB file size limit\n\n"
#         "*Coming Soon:*\n"
#         f"• {' | '.join(PREMIUM_FEATURES)}\n"
#         "• 100MB file size limit\n"
#         "• Priority processing\n"
#         "• Batch downloads\n\n"
#         "Stay tuned for updates!"
#     )
#     await safe_reply(update, context, features_text, parse_mode='Markdown')

# async def premium_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     premium_text = (
#         "💎 *Premium Features Coming Soon!*\n\n"
#         "We're working hard to bring you these exciting features:\n\n"
#         f"• {' | '.join(PREMIUM_FEATURES)}\n"
#         "• Larger file downloads (up to 100MB)\n"
#         "• Faster processing times\n"
#         "• Batch processing\n\n"
#         "Check back soon for updates on our premium offerings!\n\n"
#         "For now, enjoy our free features - they're pretty awesome too!"
#     )
#     await safe_reply(update, context, premium_text, parse_mode='Markdown')

# def is_valid_url(url: str) -> bool:
#     url_pattern = re.compile(r'^(https?://)?([A-Z0-9-]+\.)+[A-Z]{2,6}(:\d+)?(/.*)?$', re.IGNORECASE)
#     return bool(url_pattern.match(url))

# async def get_tiksave_download_url(tiktok_url: str) -> str:
#     """Fetch TikTok video URL from TikSave."""
#     try:
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
#             'Referer': TIKSAVE_URL,
#             'Origin': TIKSAVE_URL
#         }
#         data = {'url': tiktok_url}
        
#         response = await asyncio.get_event_loop().run_in_executor(
#             executor, 
#             lambda: requests.post(TIKSAVE_URL, data=data, headers=headers, timeout=30)
#         )
        
#         if response.status_code != 200:
#             raise Exception(f"TikSave request failed with status {response.status_code}")
            
#         soup = BeautifulSoup(response.text, 'html.parser')
#         download_button = soup.find('a', string=re.compile('Download MP4 \\[1\\]'))
        
#         if not download_button or 'href' not in download_button.attrs:
#             raise Exception("No MP4 [1] download link found in TikSave response")
            
#         return download_button['href']
#     except Exception as e:
#         logger.error(f"TikSave failed: {e}")
#         return None

# async def convert_video(input_path: str, output_path: str) -> bool:
#     """Convert video to WhatsApp-compatible format using FFmpeg. Returns True if successful, False if failed."""
#     try:
#         if not os.path.exists(input_path) or os.path.getsize(input_path) == 0:
#             raise Exception("Input video file is empty or missing")

#         # WhatsApp-compatible settings: H.264 video, AAC audio, MP4 container
#         process = subprocess.run([
#             'ffmpeg', '-i', input_path,
#             '-c:v', 'libx264', '-profile:v', 'baseline', '-level', '3.0',
#             '-b:v', '1000k',  # Lower bitrate for compatibility
#             '-vf', 'scale=640:-2',  # Scale to 640 width, maintain aspect ratio
#             '-c:a', 'aac', '-b:a', '128k',
#             '-f', 'mp4', '-movflags', '+faststart',
#             '-y', output_path
#         ], capture_output=True, text=True, timeout=120)  # Increased timeout to 120 seconds

#         if process.returncode != 0:
#             logger.error(f"FFmpeg conversion error: {process.stderr}")
#             return False

#         if not os.path.exists(output_path) or os.path.getsize(output_path) == 0:
#             logger.error("Converted video file is empty or missing")
#             return False

#         return True

#     except subprocess.TimeoutExpired:
#         logger.error("FFmpeg conversion timed out after 120 seconds")
#         return False
#     except Exception as e:
#         logger.error(f"Video conversion failed: {e}")
#         return False

# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     message_text = update.message.text
#     if not is_valid_url(message_text):
#         await update.message.reply_text(
#             "Please send me a valid video URL from platforms like TikTok, Twitter, etc.\n\n"
#             "Use /help for complete instructions."
#         )
#         return
    
#     context.user_data['current_url'] = message_text
#     processing_msg = await update.message.reply_text("🔍 Analyzing...", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="cancel")]]))
#     context.user_data['processing_msg_id'] = processing_msg.message_id
#     context.user_data['chat_id'] = update.message.chat_id
    
#     try:
#         loop = asyncio.get_running_loop()
#         info_dict = {}
#         platform = next((p for p in SUPPORTED_PLATFORMS if p.lower() in message_text.lower()), "Other")
        
#         # yt-dlp options with cookie support
#         ydl_opts = {
#             'quiet': True,
#             'cookiefile': 'cookies.txt'  # Assumes cookies.txt is in the project root
#         }
        
#         if platform == "TikTok":
#             download_url = await get_tiksave_download_url(message_text)
#             if download_url:
#                 info_dict = {
#                     'title': 'TikTok Video',
#                     'duration': 0,
#                     'extractor': 'TikTok',
#                     'download_url': download_url
#                 }
#             else:
#                 logger.info("TikSave failed, falling back to yt-dlp for TikTok")
#                 try:
#                     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#                         info_dict = await loop.run_in_executor(executor, lambda: ydl.extract_info(message_text, download=False))
#                 except Exception as e:
#                     logger.error(f"yt-dlp fallback for TikTok failed: {e}")
#                     raise Exception("Failed to process TikTok URL with both TikSave and yt-dlp")
#         else:
#             try:
#                 with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#                     info_dict = await loop.run_in_executor(executor, lambda: ydl.extract_info(message_text, download=False))
#             except Exception as e:
#                 logger.error(f"yt-dlp failed for {platform}: {e}")
#                 if "login required" in str(e).lower() or "rate-limit" in str(e).lower():
#                     raise Exception(f"{platform} requires login or hit rate limit. Please add cookies.txt as described in /help.")
#                 raise Exception(f"Failed to process {platform} URL: {str(e)}")
        
#         context.user_data['video_info'] = info_dict
#         keyboard = [
#             [InlineKeyboardButton("🎬 Download Video", callback_data="video"),
#              InlineKeyboardButton("🎵 Download Audio (MP3)", callback_data="audio")],
#             [InlineKeyboardButton("ℹ️ Video Info", callback_data="info"),
#              InlineKeyboardButton("❌ Cancel", callback_data="cancel")]
#         ]
#         duration = info_dict.get('duration')
#         duration_str = f"{int(duration // 60)}:{int(duration % 60):02d}" if duration else "Unknown"
        
#         await context.bot.edit_message_text(
#             chat_id=update.message.chat_id,
#             message_id=processing_msg.message_id,
#             text=f"📋 *Video Found*\n\n*Title:* {info_dict.get('title', 'Video')}\n*Duration:* {duration_str}\n*Source:* {info_dict.get('extractor', platform)}\n\nSelect an option to continue:",
#             reply_markup=InlineKeyboardMarkup(keyboard),
#             parse_mode='Markdown'
#         )
        
#     except Exception as e:
#         logger.error(f"Processing error: {e}")
#         error_msg = str(e)
#         if "login required" in error_msg.lower() or "rate-limit" in error_msg.lower():
#             error_msg = f"❌ {platform} requires authentication or hit rate limit. Please add cookies.txt as described in /help."
#         else:
#             error_msg = f"❌ Failed to process URL: {error_msg}"
#         await context.bot.edit_message_text(chat_id=update.message.chat_id, message_id=processing_msg.message_id, text=error_msg)

# async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()
    
#     if query.data == "cancel":
#         await query.edit_message_text("✅ Operation cancelled.")
#         return
#     elif query.data == "features_list":
#         await features_command(update, context)
#         return
#     elif query.data == "quick_help":
#         await help_command(update, context)
#         return
#     elif query.data == "supported_sites":
#         sites_text = "📺 *Supported Platforms:*\n\n" + "\n".join(f"• {site}" for site in SUPPORTED_PLATFORMS)
#         await query.edit_message_text(sites_text, parse_mode='Markdown')
#         return
    
#     url = context.user_data.get('current_url')
#     if not url:
#         await query.edit_message_text("❌ Session expired. Please send the URL again.")
#         return
    
#     if query.data == "info":
#         await show_media_info(query, context)
#     elif query.data in ["video", "audio"]:
#         await start_download(query, context, query.data)

# async def show_media_info(query, context: ContextTypes.DEFAULT_TYPE):
#     info_dict = context.user_data.get('video_info', {})
#     info_parts = ["📑 *Video Information*"]
    
#     def add_field(name, value, formatter=None):
#         if value not in [None, 'Unknown', '']:
#             formatted = formatter(value) if formatter else str(value)
#             info_parts.append(f"*{name}:* {formatted}")
    
#     add_field("Title", info_dict.get('title'))
#     duration = info_dict.get('duration')
#     if duration:
#         add_field("Duration", f"{int(duration // 60)}:{int(duration % 60):02d}")
#     add_field("Channel/Uploader", info_dict.get('uploader'))
    
#     upload_date = info_dict.get('upload_date')
#     if upload_date and len(upload_date) == 8:
#         add_field("Upload Date", f"{upload_date[6:8]}/{upload_date[4:6]}/{upload_date[0:4]}")
    
#     def format_count(count):
#         if isinstance(count, int):
#             return f"{count/1000000:.1f}M" if count >= 1000000 else f"{count/1000:.1f}K" if count >= 1000 else str(count)
#         return str(count)
    
#     add_field("Views", info_dict.get('view_count'), format_count)
#     add_field("Likes", info_dict.get('like_count'), format_count)
#     add_field("Resolution", info_dict.get('resolution'))
#     add_field("FPS", info_dict.get('fps'))
    
#     filesize = info_dict.get('filesize_approx')
#     if isinstance(filesize, (int, float)):
#         filesize_str = f"{filesize/1000000:.1f} MB" if filesize >= 1000000 else f"{filesize/1000:.1f} KB" if filesize >= 1000 else f"{filesize} bytes"
#         add_field("Estimated Size", filesize_str)
    
#     if len(info_parts) == 1:
#         info_parts.append("\n⚠️ Couldn't retrieve detailed information")
#         info_parts.append("You can still try downloading the media")
    
#     keyboard = [
#         [InlineKeyboardButton("🎬 Download Video", callback_data="video"),
#          InlineKeyboardButton("🎵 Download Audio", callback_data="audio")],
#         [InlineKeyboardButton("❌ Cancel", callback_data="cancel")]
#     ]
    
#     await query.edit_message_text("\n\n".join(info_parts), reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

# async def start_download(query, context: ContextTypes.DEFAULT_TYPE, format_type: str):
#     url = context.user_data.get('current_url')
#     download_msg = await query.edit_message_text(f"⏳ Starting {'audio' if format_type == 'audio' else 'video'} download...")
#     asyncio.create_task(download_and_send_media(url, format_type, MAX_VIDEO_SIZE, context, query.message.chat_id, download_msg.message_id))

# async def download_and_send_media(url: str, format_type: str, max_size: int, 
#                                 context: ContextTypes.DEFAULT_TYPE, chat_id: int, message_id: int):
#     try:
#         with tempfile.TemporaryDirectory() as temp_dir:
#             platform = next((p for p in SUPPORTED_PLATFORMS if p.lower() in url.lower()), "Other")
#             raw_file_path = os.path.join(temp_dir, f"raw_media.{format_type}")
#             final_file_path = os.path.join(temp_dir, f"final_media.{format_type if format_type == 'audio' else 'mp4'}")
#             info_dict = context.user_data.get('video_info', {})
            
#             # Step 1: Download the media
#             if platform == "TikTok" and 'download_url' in info_dict and format_type == "video":
#                 response = await asyncio.get_event_loop().run_in_executor(
#                     executor, lambda: requests.get(info_dict['download_url'], stream=True, timeout=30)
#                 )
#                 response.raise_for_status()
#                 with open(raw_file_path, 'wb') as f:
#                     for chunk in response.iter_content(1024):
#                         f.write(chunk)
#             else:
#                 ydl_opts = {
#                     'outtmpl': raw_file_path,
#                     'quiet': True,
#                     'format': 'bestvideo+bestaudio/best' if format_type == "video" else 'bestaudio/best',
#                     'cookiefile': 'cookies.txt'  # Use cookies for authentication
#                 }
#                 if format_type == "audio":
#                     ydl_opts['postprocessors'] = [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]
#                 try:
#                     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#                         await asyncio.get_event_loop().run_in_executor(executor, lambda: ydl.download([url]))
#                 except Exception as e:
#                     if "login required" in str(e).lower() or "rate-limit" in str(e).lower():
#                         raise Exception(f"{platform} requires login or hit rate limit. Please add cookies.txt as described in /help.")
#                     raise

#             # Step 2: Convert the media if it's a video
#             if format_type == "video":
#                 conversion_success = await convert_video(raw_file_path, final_file_path)
#                 if not conversion_success:
#                     logger.info("Conversion failed, falling back to raw file")
#                     final_file_path = raw_file_path
#             else:
#                 # For audio, just use the raw file (already in MP3 format)
#                 final_file_path = raw_file_path

#             # Step 3: Check file size
#             file_size = os.path.getsize(final_file_path)
#             if file_size > max_size:
#                 await context.bot.edit_message_text(chat_id=chat_id, message_id=message_id, 
#                                                   text=f"⚠️ File too large ({file_size/1024/1024:.1f}MB > {max_size/1024/1024:.1f}MB limit)")
#                 return

#             # Step 4: Upload the media
#             await context.bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="✅ Download complete! Now uploading...")
#             with open(final_file_path, 'rb') as file:
#                 if format_type == "audio":
#                     await context.bot.send_audio(chat_id=chat_id, audio=file, 
#                                                title=info_dict.get('title', 'Audio'),
#                                                performer=info_dict.get('uploader', 'Unknown'),
#                                                duration=int(info_dict.get('duration', 0)))
#                 else:
#                     await context.bot.send_video(chat_id=chat_id, video=file, 
#                                                caption=f"🎬 {info_dict.get('title', 'Video')}",
#                                                duration=int(info_dict.get('duration', 0)), 
#                                                supports_streaming=True)
            
#             await context.bot.delete_message(chat_id=chat_id, message_id=message_id)

#     except Exception as e:
#         logger.error(f"Download failed: {e}")
#         error_msg = str(e)
#         if "login required" in error_msg.lower() or "rate-limit" in error_msg.lower():
#             error_msg = f"❌ {platform} requires authentication or hit rate limit. Please add cookies.txt as described in /help."
#         await context.bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=error_msg)

# async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     logger.error(f"Error: {context.error}")
#     if isinstance(context.error, Conflict):
#         logger.warning("Conflict detected, retrying in 5 seconds...")
#         await asyncio.sleep(5)
#         return
#     if update.effective_chat:
#         await context.bot.send_message(chat_id=update.effective_chat.id, text="❌ An error occurred. Please try again later or see /help.")

# async def main():
#     TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
#     if not TOKEN:
#         logger.error("No TOKEN!")
#         return
    
#     flask_thread = threading.Thread(target=run_flask, daemon=True)
#     flask_thread.start()
    
#     application = Application.builder().token(TOKEN).build()
    
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(CommandHandler("help", help_command))
#     application.add_handler(CommandHandler("about", about_command))
#     application.add_handler(CommandHandler("features", features_command))
#     application.add_handler(CommandHandler("premium", premium_command))
#     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
#     application.add_handler(CallbackQueryHandler(button_callback))
#     application.add_error_handler(error_handler)
    
#     max_retries = 5
#     retry_delay = 10
    
#     for attempt in range(max_retries):
#         try:
#             await application.initialize()
#             await application.start()
#             await application.updater.start_polling(drop_pending_updates=True, allowed_updates=Update.ALL_TYPES)
#             logger.info("Bot running successfully")
#             while True:
#                 await asyncio.sleep(3600)
#         except Conflict as e:
#             logger.error(f"Conflict {attempt + 1}/{max_retries}: {e}")
#             if attempt < max_retries - 1:
#                 logger.info(f"Retrying in {retry_delay} seconds...")
#                 await asyncio.sleep(retry_delay)
#                 continue
#             logger.error("Max retries reached, shutting down")
#             break
#         except Exception as e:
#             logger.error(f"Unexpected error: {e}")
#             break
#         finally:
#             try:
#                 await application.updater.stop()
#                 await application.stop()
#                 await application.shutdown()
#             except Exception as e:
#                 logger.error(f"Shutdown error: {e}")

# if __name__ == '__main__':
#     try:
#         if os.name == 'nt':
#             asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#         asyncio.run(main())
#     except KeyboardInterrupt:
#         logger.info("Stopped by user")
#     except Exception as e:
#         logger.error(f"Fatal error: {e}")


import logging
import os
import tempfile
import subprocess
import requests
from bs4 import BeautifulSoup
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from telegram.error import Conflict
import asyncio
import re
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor
import threading
from flask import Flask

# Flask app for Render
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Stream Sage Bot is running!"

def run_flask():
    port = int(os.getenv("PORT", 8080))
    flask_app.run(host='0.0.0.0', port=port)

# Load environment variables
load_dotenv()

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Thread pool
executor = ThreadPoolExecutor(max_workers=4)

# Constants
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB limit for free users
MAX_PREMIUM_SIZE = 100 * 1024 * 1024
SUPPORTED_PLATFORMS = ["TikTok", "YouTube", "Twitter", "Instagram", "Facebook"]
PREMIUM_FEATURES = ["Video Generation", "Image Generation", "Larger File Downloads", "Batch Processing", "Priority Support"]
TIKTOK_URL = "https://downloader.bot/en"
YOUTUBE_URL = "https://www.y2mate.com/en949"
TWITTER_URL = "https://x-downloader.com/"
INSTAGRAM_URL = "https://fastdl.app/en"
FACEBOOK_URL = "https://fdown.net/"

async def safe_reply(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str, **kwargs):
    try:
        if update.message:
            return await update.message.reply_text(text, **kwargs)
        elif update.callback_query:
            try:
                return await update.callback_query.message.reply_text(text, **kwargs)
            except:
                return await update.callback_query.edit_message_text(text, **kwargs)
        elif update.effective_message:
            return await update.effective_message.reply_text(text, **kwargs)
    except Exception as e:
        logger.error(f"Failed to send: {e}")
        if update.effective_chat:
            return await context.bot.send_message(chat_id=update.effective_chat.id, text=text, **kwargs)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_message = (
        f"🌟 *Welcome {user.first_name} to the Ultimate Media Bot!* 🌟\n\n"
        "I'm your all-in-one solution for media downloading. Here's what I can do:\n\n"
        "🎥 *Video Downloader* - Download videos from various platforms\n"
        "🎵 *Audio Extractor* - Convert videos to high-quality MP3\n"
        "📊 *Media Info* - Get detailed information about any video\n\n"
        "💎 *Premium Features Coming Soon*\n"
        "🔹 *How to use:*\n"
        "1. Send me a video URL\n"
        "2. Choose your preferred format\n"
        "3. Get your media instantly!\n\n"
        "📌 *Available Commands:*\n"
        "/start - Show this welcome message\n"
        "/help - Detailed help and instructions\n"
        "/about - Bot information and credits\n"
        "/features - List all available features\n"
        "/premium - Learn about premium options\n\n"
        "Try me out by sending a video link now!"
    )
    keyboard = [
        [InlineKeyboardButton("📋 Features List", callback_data="features_list"),
         InlineKeyboardButton("❓ How To Use", callback_data="quick_help")],
        [InlineKeyboardButton("🔗 Supported Sites", callback_data="supported_sites")]
    ]
    await safe_reply(update, context, welcome_message, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "📚 *Complete Help Guide*\n\n"
        "*Basic Commands:*\n"
        "/start - Welcome message\n"
        "/help - This help guide\n"
        "/about - Bot information\n"
        "/features - List all features\n"
        "/premium - Premium subscription info\n\n"
        "*How to Download Videos:*\n"
        "1. Send me a video URL from any supported platform\n"
        "2. I'll detect it automatically and show options\n"
        "3. Choose to download as video, audio, or images\n"
        "4. For videos, select quality if available\n"
        "5. Receive your file directly in chat\n\n"
        "*Supported Platforms:*\n"
        f"{', '.join(SUPPORTED_PLATFORMS)}\n\n"
        "*Advanced Features:*\n"
        "• Multiple quality options for YouTube\n"
        "• Image downloads from TikTok and Instagram\n"
        "• High-quality audio extraction\n\n"
        "⚠️ *Limitations:*\n"
        "• Free users: 50MB file size limit\n"
        "• Some platforms may have restrictions\n\n"
        "Need more help? Just send me a message!"
    )
    await safe_reply(update, context, help_text, parse_mode='Markdown')

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = (
        "🤖 *Ultimate Media Bot*\n\n"
        "*Version:* 1.0.1\n"
        "*Last Updated:* April 2025\n\n"
        "*Core Features:*\n"
        "• Video downloading from supported platforms\n"
        "• Audio extraction with quality options\n"
        "• Image downloading\n\n"
        "*Technologies Used:*\n"
        "• Python 3.10+\n"
        "• python-telegram-bot\n"
        "• FFmpeg (media processing)\n\n"
        "*Developer:*\n"
        "Christian Kusi\n\n"
        "This bot is actively maintained and updated regularly with new features!"
    )
    await safe_reply(update, context, about_text, parse_mode='Markdown')

async def features_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    features_text = (
        "✨ *All Available Features*\n\n"
        "*Current Features:*\n"
        "• Video downloading from supported platforms\n"
        "• Audio extraction (MP3 format)\n"
        "• Image downloading (TikTok, Instagram)\n"
        "• Quality selection for YouTube\n"
        "• 50MB file size limit\n\n"
        "*Coming Soon:*\n"
        f"• {' | '.join(PREMIUM_FEATURES)}\n"
        "• 100MB file size limit\n"
        "• Priority processing\n"
        "• Batch downloads\n\n"
        "Stay tuned for updates!"
    )
    await safe_reply(update, context, features_text, parse_mode='Markdown')

async def premium_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    premium_text = (
        "💎 *Premium Features Coming Soon!*\n\n"
        "We're working hard to bring you these exciting features:\n\n"
        f"• {' | '.join(PREMIUM_FEATURES)}\n"
        "• Larger file downloads (up to 100MB)\n"
        "• Faster processing times\n"
        "• Batch processing\n\n"
        "Check back soon for updates on our premium offerings!\n\n"
        "For now, enjoy our free features - they're pretty awesome too!"
    )
    await safe_reply(update, context, premium_text, parse_mode='Markdown')

def is_valid_url(url: str) -> bool:
    url_pattern = re.compile(r'^(https?://)?([A-Z0-9-]+\.)+[A-Z]{2,6}(:\d+)?(/.*)?$', re.IGNORECASE)
    return bool(url_pattern.match(url))

async def fetch_html(url: str, post_url: str) -> str:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    data = {'url': url}
    response = await asyncio.get_event_loop().run_in_executor(
        executor, lambda: requests.post(post_url, data=data, headers=headers, timeout=30)
    )
    return response.text if response.status_code == 200 else None

async def get_tiktok_options(url: str) -> dict:
    html = await fetch_html(url, TIKTOK_URL)
    if not html:
        return {}
    soup = BeautifulSoup(html, 'html.parser')
    options = {}
    for button in soup.find_all('a', class_='block-flex-btn'):
        href = button.get('href', '')
        if href != "javascript:void(0);":  # Check if link is populated
            text = button.find('span', class_='md-font').text.lower()
            if 'video' in text:
                options['video'] = href
            elif 'music' in text:
                options['audio'] = href
    # Placeholder for images (since snippet wasn't provided for images)
    images = [img.get('src', '') for img in soup.find_all('img', class_='downloadable-image') if img.get('src')]
    if images:
        options['images'] = images
    return options

async def get_youtube_options(url: str) -> dict:
    html = await fetch_html(url, YOUTUBE_URL)
    if not html:
        return {}
    soup = BeautifulSoup(html, 'html.parser')
    options = {'qualities': []}
    for row in soup.select('tbody tr'):
        cells = row.find_all('td')
        if len(cells) >= 3:
            button = cells[2].find('button', onclick=True)
            if button:
                onclick = button['onclick']
                match = re.search(r"startConvert\('(.*?)','(.*?)'\)", onclick)
                if match:
                    fmt, dl_url = match.groups()
                    if fmt == 'mp4':
                        resolution = cells[0].text.strip().split()[0]  # e.g., "360p"
                        options['qualities'].append({'resolution': resolution, 'url': dl_url})
                    elif fmt == 'mp3':
                        options['audio'] = dl_url
    return options

async def get_twitter_options(url: str) -> dict:
    html = await fetch_html(url, TWITTER_URL)
    if not html:
        return {}
    soup = BeautifulSoup(html, 'html.parser')
    options = {}
    for link in soup.find_all('a', class_='btn btn-primary btn-download-file'):
        href = link['href']
        if '.mp4' in href:
            options['video'] = href
        elif '.mp3' in href:
            options['audio'] = href
    return options

async def get_instagram_options(url: str) -> dict:
    html = await fetch_html(url, INSTAGRAM_URL)
    if not html:
        return {}
    soup = BeautifulSoup(html, 'html.parser')
    options = {'videos': [], 'images': []}
    for link in soup.find_all('a', class_='button--filled'):
        href = link['href']
        if '.mp4' in href:
            options['videos'].append(href)
        elif '.jpg' in href or '.jpeg' in href:
            options['images'].append(href)
    return options

async def get_facebook_options(url: str) -> dict:
    html = await fetch_html(url, FACEBOOK_URL)
    if not html:
        return {}
    soup = BeautifulSoup(html, 'html.parser')
    options = {'qualities': []}
    for link in soup.find_all('a', class_='btn btn-primary btn-sm'):
        href = link['href']
        link_id = link.get('id', '')
        resolution = 'Normal' if link_id == 'sdlink' else 'HD' if link_id == 'hdlink' else 'Unknown'
        options['qualities'].append({'resolution': resolution, 'url': href})
    return options

async def convert_video(input_path: str, output_path: str) -> bool:
    try:
        if not os.path.exists(input_path) or os.path.getsize(input_path) == 0:
            raise Exception("Input video file is empty or missing")
        process = subprocess.run([
            'ffmpeg', '-i', input_path,
            '-c:v', 'libx264', '-profile:v', 'baseline', '-level', '3.0',
            '-b:v', '1000k',
            '-vf', 'scale=640:-2',
            '-c:a', 'aac', '-b:a', '128k',
            '-f', 'mp4', '-movflags', '+faststart',
            '-y', output_path
        ], capture_output=True, text=True, timeout=120)
        if process.returncode != 0:
            logger.error(f"FFmpeg conversion error: {process.stderr}")
            return False
        if not os.path.exists(output_path) or os.path.getsize(output_path) == 0:
            logger.error("Converted video file is empty or missing")
            return False
        return True
    except subprocess.TimeoutExpired:
        logger.error("FFmpeg conversion timed out after 120 seconds")
        return False
    except Exception as e:
        logger.error(f"Video conversion failed: {e}")
        return False

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text
    if not is_valid_url(message_text):
        await update.message.reply_text(
            "Please send me a valid video URL from platforms like TikTok, YouTube, etc.\n\n"
            "Use /help for complete instructions."
        )
        return
    
    context.user_data['current_url'] = message_text
    processing_msg = await update.message.reply_text("🔍 Analyzing...", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="cancel")]]))
    context.user_data['processing_msg_id'] = processing_msg.message_id
    context.user_data['chat_id'] = update.message.chat_id
    
    try:
        platform = next((p for p in SUPPORTED_PLATFORMS if p.lower() in message_text.lower()), "Other")
        fetchers = {
            'TikTok': get_tiktok_options,
            'YouTube': get_youtube_options,
            'Twitter': get_twitter_options,
            'Instagram': get_instagram_options,
            'Facebook': get_facebook_options
        }
        if platform == "Other":
            raise Exception(f"Unsupported platform")
        
        options = await fetchers[platform](message_text)
        if not options:
            raise Exception(f"Failed to fetch download options for {platform}")
        
        context.user_data['download_options'] = options
        context.user_data['platform'] = platform.lower()
        
        keyboard = []
        if 'video' in options:
            keyboard.append([InlineKeyboardButton("🎬 Download Video", callback_data=f"{platform.lower()}_video")])
        if 'audio' in options:
            keyboard.append([InlineKeyboardButton("🎵 Download Audio", callback_data=f"{platform.lower()}_audio")])
        if 'images' in options and options['images']:
            keyboard.append([InlineKeyboardButton("🖼️ Download Images", callback_data=f"{platform.lower()}_images")])
        if 'qualities' in options:
            keyboard.append([InlineKeyboardButton("🎬 Select Video Quality", callback_data=f"{platform.lower()}_select_quality")])
        if platform.lower() == 'instagram' and (options.get('videos') or options.get('images')):
            keyboard.append([InlineKeyboardButton("📦 Download All Media", callback_data=f"{platform.lower()}_all_media")])
        keyboard.append([InlineKeyboardButton("❌ Cancel", callback_data="cancel")])
        
        await context.bot.edit_message_text(
            chat_id=update.message.chat_id,
            message_id=processing_msg.message_id,
            text=f"📋 *{platform} Content Found*\n\nSelect an option to continue:",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
        
    except Exception as e:
        logger.error(f"Processing error: {e}")
        error_msg = f"❌ Failed to process URL: {str(e)}"
        await context.bot.edit_message_text(chat_id=update.message.chat_id, message_id=processing_msg.message_id, text=error_msg)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "cancel":
        await query.edit_message_text("✅ Operation cancelled.")
        return
    elif query.data == "features_list":
        await features_command(update, context)
        return
    elif query.data == "quick_help":
        await help_command(update, context)
        return
    elif query.data == "supported_sites":
        sites_text = "📺 *Supported Platforms:*\n\n" + "\n".join(f"• {site}" for site in SUPPORTED_PLATFORMS)
        await query.edit_message_text(sites_text, parse_mode='Markdown')
        return
    
    url = context.user_data.get('current_url')
    if not url:
        await query.edit_message_text("❌ Session expired. Please send the URL again.")
        return
    
    options = context.user_data.get('download_options', {})
    platform = context.user_data.get('platform', '')
    
    if query.data == f"{platform}_video":
        await start_download(query, context, options['video'], 'video')
    elif query.data == f"{platform}_audio":
        await start_download(query, context, options['audio'], 'audio')
    elif query.data == f"{platform}_images":
        await download_and_send_images(query, context, options['images'])
    elif query.data == f"{platform}_select_quality" and 'qualities' in options:
        qualities = options['qualities']
        keyboard = [[InlineKeyboardButton(q['resolution'], callback_data=f"{platform}_quality_{i}")] for i, q in enumerate(qualities)]
        keyboard.append([InlineKeyboardButton("❌ Cancel", callback_data="cancel")])
        await query.edit_message_text("Select video quality:", reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data.startswith(f"{platform}_quality_"):
        index = int(query.data.split('_')[-1])
        if 'qualities' in options and 0 <= index < len(options['qualities']):
            await start_download(query, context, options['qualities'][index]['url'], 'video')
        else:
            await query.edit_message_text("❌ Invalid quality selected.")
    elif query.data == f"{platform}_all_media" and ('videos' in options or 'images' in options):
        await download_and_send_media_group(query, context, options)

async def start_download(query, context: ContextTypes.DEFAULT_TYPE, download_url: str, format_type: str):
    download_msg = await query.edit_message_text(f"⏳ Starting {'audio' if format_type == 'audio' else 'video'} download...")
    asyncio.create_task(download_and_send_media(download_url, format_type, MAX_FILE_SIZE, context, query.message.chat_id, download_msg.message_id))

async def download_and_send_images(query, context: ContextTypes.DEFAULT_TYPE, image_urls: list):
    download_msg = await query.edit_message_text("⏳ Downloading images...")
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            image_paths = []
            for i, url in enumerate(image_urls):
                response = await asyncio.get_event_loop().run_in_executor(
                    executor, lambda: requests.get(url, stream=True, timeout=30)
                )
                response.raise_for_status()
                path = os.path.join(temp_dir, f"image_{i}.jpg")
                with open(path, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                if os.path.getsize(path) > MAX_FILE_SIZE:
                    await context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=download_msg.message_id,
                                                      text=f"⚠️ Image {i+1} too large ({os.path.getsize(path)/1024/1024:.1f}MB)")
                    continue
                image_paths.append(path)
            
            media_group = [InputMediaPhoto(open(path, 'rb')) for path in image_paths]
            await context.bot.send_media_group(chat_id=query.message.chat_id, media=media_group)
            await context.bot.delete_message(chat_id=query.message.chat_id, message_id=download_msg.message_id)
    except Exception as e:
        logger.error(f"Image download failed: {e}")
        await context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=download_msg.message_id,
                                          text=f"❌ Failed to download images: {str(e)}")

async def download_and_send_media_group(query, context: ContextTypes.DEFAULT_TYPE, options: dict):
    download_msg = await query.edit_message_text("⏳ Downloading media group...")
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            media_paths = []
            for i, url in enumerate(options.get('videos', []) + options.get('images', [])):
                response = await asyncio.get_event_loop().run_in_executor(
                    executor, lambda: requests.get(url, stream=True, timeout=30)
                )
                response.raise_for_status()
                ext = '.mp4' if '.mp4' in url else '.jpg'
                raw_path = os.path.join(temp_dir, f"media_{i}_raw{ext}")
                final_path = os.path.join(temp_dir, f"media_{i}{ext}")
                with open(raw_path, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                if ext == '.mp4':
                    if not await convert_video(raw_path, final_path):
                        final_path = raw_path
                else:
                    final_path = raw_path
                if os.path.getsize(final_path) > MAX_FILE_SIZE:
                    await context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=download_msg.message_id,
                                                      text=f"⚠️ Media {i+1} too large ({os.path.getsize(final_path)/1024/1024:.1f}MB)")
                    continue
                media_paths.append((final_path, ext))
            
            media_group = []
            for path, ext in media_paths:
                with open(path, 'rb') as f:
                    if ext == '.mp4':
                        media_group.append(InputMediaVideo(f, supports_streaming=True))
                    else:
                        media_group.append(InputMediaPhoto(f))
            await context.bot.send_media_group(chat_id=query.message.chat_id, media=media_group)
            await context.bot.delete_message(chat_id=query.message.chat_id, message_id=download_msg.message_id)
    except Exception as e:
        logger.error(f"Media group download failed: {e}")
        await context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=download_msg.message_id,
                                          text=f"❌ Failed to download media group: {str(e)}")

async def download_and_send_media(download_url: str, format_type: str, max_size: int, 
                                context: ContextTypes.DEFAULT_TYPE, chat_id: int, message_id: int):
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            raw_file_path = os.path.join(temp_dir, f"raw_media.{format_type if format_type == 'audio' else 'video'}")
            final_file_path = os.path.join(temp_dir, f"final_media.{format_type if format_type == 'audio' else 'mp4'}")
            
            response = await asyncio.get_event_loop().run_in_executor(
                executor, lambda: requests.get(download_url, stream=True, timeout=30)
            )
            response.raise_for_status()
            with open(raw_file_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            
            if format_type == "video":
                conversion_success = await convert_video(raw_file_path, final_file_path)
                if not conversion_success:
                    logger.info("Conversion failed, falling back to raw file")
                    final_file_path = raw_file_path
            else:
                final_file_path = raw_file_path
            
            if not os.path.exists(final_file_path):
                raise Exception("Downloaded file is missing")
            file_size = os.path.getsize(final_file_path)
            if file_size > max_size:
                await context.bot.edit_message_text(chat_id=chat_id, message_id=message_id, 
                                                  text=f"⚠️ File too large ({file_size/1024/1024:.1f}MB > {max_size/1024/1024:.1f}MB limit)")
                return
            
            await context.bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="✅ Download complete! Now uploading...")
            with open(final_file_path, 'rb') as file:
                if format_type == "audio":
                    await context.bot.send_audio(chat_id=chat_id, audio=file, title="Audio")
                else:
                    await context.bot.send_video(chat_id=chat_id, video=file, caption="🎬 Video", supports_streaming=True)
            
            await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    except Exception as e:
        logger.error(f"Download failed: {e}")
        error_msg = f"❌ Failed to process URL: {str(e)}"
        await context.bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=error_msg)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Error: {context.error}")
    if isinstance(context.error, Conflict):
        logger.warning("Conflict detected, retrying in 5 seconds...")
        await asyncio.sleep(5)
        return
    if update.effective_chat:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="❌ An error occurred. Please try again later or see /help.")

async def main():
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    if not TOKEN:
        logger.error("No TOKEN!")
        return
    
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))
    application.add_handler(CommandHandler("features", features_command))
    application.add_handler(CommandHandler("premium", premium_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_error_handler(error_handler)
    
    max_retries = 5
    retry_delay = 10
    
    for attempt in range(max_retries):
        try:
            await application.initialize()
            await application.start()
            await application.updater.start_polling(drop_pending_updates=True, allowed_updates=Update.ALL_TYPES)
            logger.info("Bot running successfully")
            while True:
                await asyncio.sleep(3600)
        except Conflict as e:
            logger.error(f"Conflict {attempt + 1}/{max_retries}: {e}")
            if attempt < max_retries - 1:
                logger.info(f"Retrying in {retry_delay} seconds...")
                await asyncio.sleep(retry_delay)
                continue
            logger.error("Max retries reached, shutting down")
            break
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            break
        finally:
            try:
                await application.updater.stop()
                await application.stop()
                await application.shutdown()
            except Exception as e:
                logger.error(f"Shutdown error: {e}")

if __name__ == '__main__':
    try:
        if os.name == 'nt':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")