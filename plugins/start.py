# Copyright (c) 2025 devgagan : https://github.com/devgaganin.
# Licensed under the GNU General Public License v3.0.

from shared_client import app
from pyrogram import filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
from config import FORCE_SUB, OWNER_ID

# ✅ Force Subscribe Check
async def subscribe(client, message):
    if FORCE_SUB:
        try:
            user = await client.get_chat_member(FORCE_SUB, message.from_user.id)
            if str(user.status) == "ChatMemberStatus.BANNED":
                await message.reply_text("🚫 आप इस चैनल से प्रतिबंधित हैं। कृपया टीम SPY से संपर्क करें।")
                return 1
        except UserNotParticipant:
            await message.reply_photo(
                photo="https://graph.org/file/d44f024a08ded19452152.jpg",
                caption="🔒 इस बॉट का उपयोग करने के लिए कृपया हमारे चैनल से जुड़ें।",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/quiz_zone_new")]
                ])
            )
            return 1
        except Exception as e:
            await message.reply_text(f"❌ कुछ गलत हो गया: `{e}`")
            return 1
    return 0

# ✅ /start command
@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    join = await subscribe(client, message)
    if join == 1:
        return

    await message.reply_text(
        "**👋 Welcome to Save Restricted Bot!**\n\n"
        "मैं आपकी मदद कर सकता हूँ विभिन्न प्लेटफार्म से वीडियो और मीडिया डाउनलोड करने में।\n\n"
        "📌 कमांड देखने के लिए /help भेजें।\n\n"
        "__Developed by Team SPY__",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📋 Help", callback_data="help_next_0")],
            [InlineKeyboardButton("📢 Channel", url="https://t.me/quiz_zone_new")],
        ])
    )

# ✅ /help pages
help_pages = [
    (
        "**📘 Help Menu (1/2):**\n\n"
        "• /start - बॉट शुरू करें\n"
        "• /help - सभी कमांड्स देखें\n"
        "• /login - लॉगिन करें\n"
        "• /batch - बैच में लिंक एक्सट्रैक्ट करें\n"
        "• /adl - ऑडियो डाउनलोड करें\n"
        "• /dl - वीडियो डाउनलोड करें\n"
        "• /logout - लॉगआउट करें\n"
        "• /cancel - किसी भी प्रक्रिया को रद्द करें"
    ),
    (
        "**📘 Help Menu (2/2):**\n\n"
        "• /add user_id - प्रीमियम यूज़र जोड़ें\n"
        "• /rem user_id - प्रीमियम से हटाएँ\n"
        "• /transfer user_id - प्रीमियम ट्रांसफर करें\n"
        "• /status - पेमेंट स्टेटस देखें\n"
        "• /plan - प्रीमियम प्लान्स देखें\n"
        "• /terms - नियम व शर्तें देखें\n"
        "__⚙️ Settings & Customization available using `/settings`__"
    )
]

# ✅ Help Navigation
async def send_or_edit_help_page(_, message, page_number):
    if page_number < 0 or page_number >= len(help_pages):
        return

    buttons = []
    if page_number > 0:
        buttons.append(InlineKeyboardButton("◀️ Previous", callback_data=f"help_prev_{page_number}"))
    if page_number < len(help_pages) - 1:
        buttons.append(InlineKeyboardButton("Next ▶️", callback_data=f"help_next_{page_number}"))

    keyboard = InlineKeyboardMarkup([buttons]) if buttons else None

    await message.reply_text(help_pages[page_number], reply_markup=keyboard)

@app.on_message(filters.command("help") & filters.private)
async def help(client, message):
    join = await subscribe(client, message)
    if join == 1:
        return
    await send_or_edit_help_page(client, message, 0)

@app.on_callback_query(filters.regex(r"help_(prev|next)_(\d+)"))
async def help_callback(client, callback_query):
    action, page_number = callback_query.data.split("_")[1:]
    page_number = int(page_number) - 1 if action == "prev" else int(page_number) + 1
    await send_or_edit_help_page(client, callback_query.message, page_number)
    await callback_query.answer()

# ✅ /terms command
@app.on_message(filters.command("terms") & filters.private)
async def terms(client, message):
    await message.reply_text(
        "**📜 Terms and Conditions:**\n\n"
        "• हम किसी भी कॉपीराइटेड कंटेंट के लिए ज़िम्मेदार नहीं हैं।\n"
        "• पेमेंट करने से बॉट की सेवाएं निश्चित नहीं होतीं।\n"
        "• हमारी मर्जी से हम किसी भी यूज़र को रोक या चालू कर सकते हैं।",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📋 See Plans", callback_data="see_plan")],
            [InlineKeyboardButton("💬 Contact Admin", url="https://t.me/kingofpatal")]
        ])
    )

# ✅ /plan command
@app.on_message(filters.command("plan") & filters.private)
async def plan(client, message):
    await message.reply_text(
        "**💰 Premium Plans:**\n\n"
        "• ₹200 या $2 से शुरुआत\n"
        "• 1 लाख फाइलें प्रति बैच डाउनलोड\n"
        "• मोड्स: /batch और /bulk\n",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📜 Terms", callback_data="see_terms")],
            [InlineKeyboardButton("💬 Contact Admin", url="https://t.me/kingofpatal")]
        ])
    )

# ✅ Callback for plans and terms
@app.on_callback_query(filters.regex("see_plan"))
async def see_plan(client, callback_query):
    await callback_query.message.edit_text(
        "**💰 Premium Plans:**\n\n"
        "• ₹200 या $2 से शुरुआत\n"
        "• 1 लाख फाइलें प्रति बैच डाउनलोड\n"
        "• /batch और /bulk मोड्स\n"
        "• और जानने के लिए नीचे क्लिक करें...",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📜 Terms", callback_data="see_terms")],
            [InlineKeyboardButton("💬 Contact Admin", url="https://t.me/kingofpatal")]
        ])
    )
    await callback_query.answer()

@app.on_callback_query(filters.regex("see_terms"))
async def see_terms(client, callback_query):
    await callback_query.message.edit_text(
        "**📜 Terms and Conditions:**\n\n"
        "• किसी भी प्रकार की कॉपीराइट उल्लंघन की जिम्मेदारी यूज़र की होगी।\n"
        "• पेमेंट से सेवा की गारंटी नहीं होती।\n"
        "• बैन / अप्रूवल हमारी मर्जी पर निर्भर करता है।",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📋 See Plans", callback_data="see_plan")],
            [InlineKeyboardButton("💬 Contact Admin", url="https://t.me/kingofpatal")]
        ])
    )
    await callback_query.answer()
