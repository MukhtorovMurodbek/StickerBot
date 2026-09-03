"""Translation strings for StickerBot's end-user-facing text (English,
Uzbek, Russian). Deliberately duplicated per bot -- same "no shared files
between bots" independence as shared_features.py -- but the STRINGS content
here is specific to this bot's own commands and flows.

Admin-only output (/whois, /messageas, /dbdump, /status, /crashtest) is
intentionally NOT translated -- only the bot owner ever sees it, same
reasoning as downloader_bot's i18n.py.

The keys below split into two groups:
  - "Shared" keys (donate flow, sibling-bot blurb) exist under the exact
    same names in every bot's i18n.py, since shared_features.py is
    duplicated byte-identical across the family and calls t() with these
    names regardless of which bot it's running in.
  - Bot-specific keys, everything below the shared block, for this bot's
    own bot.py (plus video_sticker.py/import_utils.py error text) strings
    only.
"""
import asyncio

import db

SUPPORTED_LANGUAGES = ("en", "uz", "ru")
LANGUAGE_LABELS = {"en": "English 🇬🇧", "uz": "O'zbekcha 🇺🇿", "ru": "Русский 🇷🇺"}

# What every /start shows, whether or not the user already has a language.
# Deliberately not part of STRINGS: it is trilingual on purpose, so there
# is no single `lang` to look it up under.
LANGUAGE_PROMPT = (
    "👋 Welcome! / Xush kelibsiz! / Добро пожаловать!\n\n"
    "Please choose your language / Iltimos, tilni tanlang / "
    "Пожалуйста, выберите язык:"
)

STRINGS = {
    "en": {
        # ---- shared keys (same name in every bot's i18n.py) ----
        "sibling_blurb": "Also part of this bot family, see below \U0001f447",
        "donation_nudge": (
            "💙 If this bot's been useful: hosting/API costs are covered by whoever's "
            "running it, and /donate is a totally optional way to help keep it alive. "
            "No pressure either way!"
        ),
        "donate_unknown_currency": 'Unknown currency "{currency}" -- try xtr or usd.',
        "donate_currency_not_configured": "{currency} donations aren't set up on this bot yet -- try Stars instead.",
        "donate_invalid_amount": "That's not a valid amount -- try e.g. /donate 500 or /donate 5 usd.",
        "donate_prompt": (
            "Thank you for contributing -- it goes directly toward this bot's "
            "hosting and API costs. Choose an amount below, or Custom to enter "
            "your own (you can also send /donate <number> [usd] directly)."
        ),
        "donate_custom_button": "✏️ Custom {symbol}",
        "donate_too_many_stars": "That's a lot of stars! Keep it under {max} ⭐ per donation.",
        "donate_out_of_range": "{currency} donations need to be between {lo} and {hi} {symbol}.",
        "donate_invoice_title": "Buy the bot a coffee ☕",
        "donate_invoice_description": "A one-time voluntary donation towards hosting costs. Thank you!",
        "donate_invoice_label": "Donation",
        "donate_invoice_error": "⚠️ Telegram wouldn't create that invoice: {error}",
        "stars_unit": "Stars",
        "donate_custom_ask": "How many {unit} would you like to donate? Reply with a number.",
        "donate_invalid_amount_retry": "That's not a valid amount -- send /donate to try again.",
        "donate_thanks": "🙏 Thank you for the {amount} ⭐ — genuinely appreciated!",
        "language_set_confirmation": "✅ Language set to English.",
        "cancel_header": "\u274c Cancelled:",
        "cancel_nothing": "Nothing to cancel -- I wasn't waiting on anything from you.",
        "cancel_ask": "What should I stop? Here's what I'm waiting on:",
        "cancel_kept": "Alright -- nothing cancelled.",
        "cancel_reply_box_freed": "Your reply box is free again.",
        "cancel_button_all": "❌ All of it",
        "cancel_button_none": "↩️ Nothing, keep going",
        "cancel_button_donation": "💸 Donation amount",
        "cancel_item_donation": "the donation amount I asked you for",
        "cancel_item_stale_prompt": "a leftover prompt that was still waiting on an answer",
        "cancel_item_new_pack": "the new pack you were naming",
        "cancel_button_new_pack": "🆕 Naming a new pack",
        "cancel_item_rename": "renaming \"{title}\"",
        "cancel_button_rename": "✏️ Renaming a pack",
        "cancel_item_editing": "editing \"{title}\"",
        "cancel_button_editing": "📦 Editing a pack",
        # ---- stickerbot-specific keys ----
        "start_intro": (
            "Hey! I turn your images/GIFs/videos/stickers into Telegram sticker "
            "packs, and I can grab videos from Instagram/TikTok links.\n\n"
        ),
        "help_text": (
            "Commands:\n"
            "/newpack - start a new sticker pack\n"
            "/addsticker - add stickers to an existing pack\n"
            "/mypacks - list your packs\n"
            "/import <pack link/name> - (while editing) bulk-copy stickers from another "
            "Telegram pack, or send a WhatsApp sticker pack .zip/.wastickers file\n"
            "/done - finish editing a pack\n"
            "/cancel - stop something I'm waiting on you for (I'll ask which)\n"
            "/whomade <pack link/name> - see who created a pack (if made through this bot)\n"
            "/donate - chip in for hosting costs (totally optional)\n"
            "/en, /uz, /rus - switch language (or /language, which asks)\n\n"
            "While editing a pack: send images, GIFs, videos, or static/video "
            "stickers to add them.\n"
            "Send emoji after one to tag it with that emoji.\n\n"
            "Tap a pack from /mypacks to rename it, set up co-editing so someone else "
            "can add stickers to it too, or delete it for good (owner-only, asks "
            "twice before it actually happens).\n\n"
            "Want to grab a video from Instagram/TikTok, or convert a file to another "
            "format? Those live in the sibling bots below now.\n\n"
            "This bot is still being developed and hosted temporarily. If its not responding, "
            "wait for it to respond, it will automatically respond when I start hosting it again most of the time.\n\n"
        ),
        "whomade_usage": "Usage: /whomade <pack name or t.me/addstickers link>",
        "whomade_not_found": (
            "I don't have a record of that pack -- either it wasn't created "
            "through this bot, or the name/link isn't right."
        ),
        "whomade_result": "📦 \"{title}\"\nCreated by {creator} on {date} (via this bot).",
        "coedit_link_invalid": "That co-editing link isn't valid -- it may have been reset by the pack owner.",
        "coedit_pack_gone": "That pack doesn't seem to exist anymore.",
        "coedit_own_pack": "That's your own pack -- use /mypacks to manage it.",
        "coedit_joined_intro": (
            "You've been added as a co-editor on \"{title}\"! Send images, GIFs, "
            "videos, or static/video stickers to add them -- default emoji is 😭, "
            "send emoji right after to retag the last one. /done when finished."
        ),
        "btn_new_pack": "➕ New pack",
        "btn_my_packs": "📁 My packs",
        "btn_help": "❓ Help",
        "btn_back": "⬅️ Back",
        "no_packs_yet": "No packs yet -- tap New pack or use /newpack.",
        "your_packs": "Your packs:",
        "not_your_pack": "That's not your pack.",
        "pack_detail_title": "📦 {title}",
        "btn_open_pack": "🔗 Open pack",
        "btn_add_stickers": "➕ Add stickers",
        "btn_rename": "✏️ Rename",
        "btn_coedit": "👥 Co-edit",
        "btn_delete_pack": "🗑️ Delete pack",
        "coedit_count_some": "{count} co-editor(s) so far.",
        "coedit_count_none": "No co-editors yet.",
        "coedit_message": (
            "👥 Co-editing \"{title}\"\n\n"
            "Link: {link}\n\n"
            "Share it -- anyone who opens it can add stickers to this pack "
            "through the bot (they still get added under your ownership).\n\n"
            "{editors_line}\n\n"
            "Reset the link to stop it from granting access to anyone new."
        ),
        "btn_reset_link": "🔄 Reset link",
        "only_owner_coedit": "Only the pack owner can manage co-editing.",
        "link_reset_confirm": "Link reset -- the old one no longer works.",
        "only_owner_rename": "Only the pack owner can rename it.",
        "rename_prompt": "Send the new title for \"{title}\".",
        "rename_broken_state": "Something went wrong -- try Rename again from /mypacks.",
        "btn_back_to_pack": "⬅️ Back to pack",
        "renamed_success": "Renamed to \"{title}\".",
        "renamed_failed": "Couldn't rename it: {error}",
        "only_owner_delete": "Only the pack owner can delete it.",
        "btn_delete": "🗑️ Delete",
        "btn_cancel_inline": "⬅️ Cancel",
        "delete_confirm1": (
            "⚠️ Delete \"{title}\"? This removes it from Telegram for everyone who "
            "has it, including any co-editors, and can't be undone."
        ),
        "btn_delete_confirm": "🗑️ Yes, permanently delete it",
        "delete_confirm2": "❗ Last check -- permanently delete \"{title}\"? There's no undo after this.",
        "delete_failed": "⚠️ Couldn't delete it: {error}",
        "btn_my_packs_back": "⬅️ My packs",
        "delete_success": "🗑️ \"{title}\" has been permanently deleted.",
        "newpack_title_prompt": "What should the pack title be?",
        "title_empty": "That's empty -- send an actual title for the pack.",
        "title_truncated": "Telegram caps pack titles at 64 characters -- using \"{title}\".",
        "editing_intro_new": (
            "Send images, GIFs, videos, or static/video stickers -- each one "
            "is added with the default 😭 emoji. Send emoji right after to retag "
            "the last one. /done when finished."
        ),
        "no_packs_for_add": "You don't have any packs yet. Use /newpack first.",
        "pick_pack_prompt": "Which pack? Tap it, then \"➕ Add stickers\".",
        "editing_intro_add": (
            "Send images, GIFs, videos, or static/video stickers to add -- default "
            "emoji is 😭, send emoji right after to retag the last one. /done when finished.\n\n"
            "Tip: sending a sticker that's already in this pack removes it instead of "
            "adding a duplicate."
        ),
        "status_verb_creating": "Creating",
        "status_verb_editing": "Editing",
        "status_line": "📝 {verb} \"{title}\" — {count} sticker(s) added this session",
        "status_default_title": "this pack",
        "btn_delete_pack_yes": "🗑️ Yes, delete the pack",
        "btn_cancel": "Cancel",
        "remove_last_confirm": (
            "That's the only sticker left in this pack -- removing it deletes the "
            "*whole pack* from Telegram, since packs can't be empty. Are you sure?"
        ),
        "remove_failed": "⚠️ Couldn't remove that sticker: {error}",
        "remove_success": "🗑️ That sticker was already in this pack -- removed it.",
        "keep_pack": "Okay, kept the pack as-is.",
        "pack_deleted_empty": "🗑️ Pack deleted (it had no stickers left).",
        "pack_deleted_note": "❌ Pack deleted.",
        "image_process_failed": "Couldn't process that image: {error}",
        "added_default_emoji": "Added {emoji} — send an emoji to retag it.",
        "last_attempt_failed": "⚠️ Last attempt failed -- send another item to retry, or /cancel.",
        "converting_video": "Converting to a video sticker...",
        "video_convert_failed_redirect": (
            "{error}\n\nCan't turn this into a sticker, but if you just want the "
            "file in a normal format, @ConvertBot can do that -- just send the "
            "same file over there 👇"
        ),
        "video_convert_generic_failed": "Couldn't convert that: {error}",
        "added_video_default_emoji": (
            "Added as a video sticker with default {emoji}. Send emoji "
            "now to retag it, another image/GIF/video to keep going, or /done to finish."
        ),
        "animated_not_supported": (
            "Animated (Lottie/.tgs) stickers aren't supported -- send a static "
            "image, a GIF/video, or a static/video sticker instead."
        ),
        "import_usage": (
            "Send /import <telegram pack link or name> to copy stickers from "
            "another public Telegram pack into this one -- or just send a "
            "WhatsApp sticker pack .zip/.wastickers file directly."
        ),
        "import_invalid_source": "That doesn't look like a valid pack name or t.me/addstickers link.",
        "import_fetching": "Fetching stickers from \"{source}\"...",
        "import_summary_head": "Imported {added} sticker(s) from \"{source}\"",
        "import_summary_skipped": ", skipped {skipped} unsupported (animated/Lottie)",
        "import_summary_failed": ", {failed} failed",
        "import_summary_tail": ". Keep sending more, or /done to finish.",
        "done_standalone_hint": (
            "Nothing to finish -- you aren't editing a pack right now. Start one "
            "with /newpack, or tap Add stickers on a pack from /mypacks."
        ),
        "import_standalone_hint": (
            "Start or open a pack first (/newpack, or tap Add stickers on a pack from "
            "/mypacks), then use /import <link> inside that session."
        ),
        "whatsapp_reading": "Reading the WhatsApp sticker pack...",
        "whatsapp_summary_head": "Imported {added} sticker(s) from the WhatsApp pack",
        "not_emoji_message": "Send an image/GIF/video/sticker to add, emoji to retag the last one, or /done.",
        "no_sticker_to_tag": "Add a sticker first, then send emoji to tag it.",
        "retagged_success": "Retagged as {emojis}.",
        "retag_failed": "Couldn't update the emoji: {error}",
        "nothing_added_yet": "You haven't added anything yet. Send an image first.",
        "done_success": (
            "✅ Finished \"{title}\" — {count} sticker(s) added this session.\n\n"
            "All set: https://t.me/addstickers/{pack_name}"
        ),
        "convert_redirect": (
            "File conversion (images/video/audio, not sticker-specific) moved to "
            "@ConvertBot -- tap below to open it."
        ),
        "cancelled_status_note": "❌ Cancelled.",
        "unrecognized": "Not sure what that's for -- try /newpack, /mypacks, or /help.",
        "unknown_command": "I don't recognize that command. Send /help to see what I can do.",
        "err_invalid_name": (
            "⚠️ Telegram rejected the pack's internal name -- this usually happens when the "
            "title starts with a number or symbol. Send /cancel, then /newpack again with a "
            "title that starts with a letter (e.g. \"My 2007\" instead of \"2007\")."
        ),
        "err_name_occupied": (
            "⚠️ That pack's internal name collided with an existing one (rare, just bad luck). "
            "Send /cancel, then /newpack again to get a fresh one."
        ),
        "err_too_many_stickers": "⚠️ This pack is already at Telegram's sticker limit (120) -- start a new pack with /newpack instead.",
        "err_bad_format": "⚠️ Telegram didn't accept that file's format for this pack -- try a different image.",
        "err_generic": "⚠️ Telegram rejected that: {msg}\n\nYou can try again, or /cancel to stop.",
        "err_timed_out": (
            "⚠️ Telegram didn't confirm in time -- it may have gone through anyway, "
            "so check the pack before retrying to avoid a duplicate. You can try "
            "again, or /cancel to stop."
        ),
        "restarting_send_again": "🔄 I'm being updated right now — give me a few seconds and send that again.",
        "update_soon_try_later": "🔧 I'm being updated in a moment, so I can't start anything new right now — please try again in about {minutes} minute(s). I'll message you when I'm back.",
        "update_soon_try_later_soon": "🔧 I'm being updated right now, so I can't start anything new — please try again shortly. I'll message you when I'm back.",
        "update_will_reset": "🔧 Heads up: I'm about to be updated, and what you have going right now will be reset. You'll be able to start it again in a few minutes.",
        "update_done_try_now": '✅ The update is done — go ahead and try again now.',
        "video_convert_ffmpeg_missing": (
            "ffmpeg isn't installed on this host, so GIF/video stickers can't "
            "be converted. Install it with 'apt install ffmpeg' (Linux), "
            "'brew install ffmpeg' (Mac), or add a Windows build to PATH."
        ),
        "video_convert_empty_file": "That file came through empty -- try sending it again.",
        "video_convert_too_big": (
            "Couldn't compress this clip under Telegram's 256 KB video-sticker "
            "limit ({note}). Try a shorter or visually simpler clip."
        ),
        "import_pack_not_found": (
            "Couldn't find a sticker pack called \"{source}\" -- double-check "
            "the link/name (it must be public)."
        ),
        "import_bad_zip": "That doesn't look like a valid .zip/.wastickers file.",
        "import_zip_no_images": "No usable images found inside that zip.",
    },
    "uz": {
        "sibling_blurb": "Bu bot oilasining bir qismi, pastda ko'ring \U0001f447",
        "donation_nudge": (
            "💙 Agar bu bot foydali bo'lgan bo'lsa: hosting/API xarajatlarini uni ishga "
            "tushirgan kishi qoplaydi, /donate esa uni tirik saqlashga yordam berishning "
            "ixtiyoriy usuli. Bosim yo'q, xohlasangiz ham, xohlamasangiz ham!"
        ),
        "donate_unknown_currency": '"{currency}" — noma\'lum valyuta. xtr yoki usd dan foydalaning.',
        "donate_currency_not_configured": "{currency} orqali xayriya bu botda hali sozlanmagan — Stars dan foydalaning.",
        "donate_invalid_amount": "Bu noto'g'ri miqdor — masalan, /donate 500 yoki /donate 5 usd deb yozing.",
        "donate_prompt": (
            "Hissa qo'shganingiz uchun rahmat — bu mablag' to'g'ridan-to'g'ri "
            "botning hosting va API xarajatlariga sarflanadi. Quyidan miqdorni "
            "tanlang yoki o'zingiz kiritish uchun \"Boshqa\"ni bosing (shuningdek, "
            "to'g'ridan-to'g'ri /donate <son> [usd] deb yuborishingiz mumkin)."
        ),
        "donate_custom_button": "✏️ Boshqa {symbol}",
        "donate_too_many_stars": "Bu juda ko'p yulduzcha! Har bir xayriya {max} ⭐ dan kam bo'lsin.",
        "donate_out_of_range": "{currency} xayriyalar {lo} va {hi} {symbol} oralig'ida bo'lishi kerak.",
        "donate_invoice_title": "Botga bir chashka qahva sotib oling ☕",
        "donate_invoice_description": "Hosting xarajatlariga bir martalik ixtiyoriy xayriya. Rahmat!",
        "donate_invoice_label": "Xayriya",
        "donate_invoice_error": "⚠️ Telegram bu hisob-fakturani yarata olmadi: {error}",
        "stars_unit": "Stars (yulduzcha)",
        "donate_custom_ask": "Nechta {unit} xayriya qilmoqchisiz? Raqam bilan javob bering.",
        "donate_invalid_amount_retry": "Bu noto'g'ri miqdor — qayta urinish uchun /donate yuboring.",
        "donate_thanks": "🙏 {amount} ⭐ uchun rahmat — bu chindan ham qadrlanadi!",
        "language_set_confirmation": "✅ Til o'zbekchaga o'zgartirildi.",
        "cancel_header": "\u274c Bekor qilindi:",
        "cancel_nothing": "Bekor qiladigan narsa yo'q -- men sizdan hech narsa kutmayotgan edim.",
        "cancel_ask": "Nimani to'xtatay? Mana, men nimalarni kutyapman:",
        "cancel_kept": "Yaxshi -- hech narsa bekor qilinmadi.",
        "cancel_reply_box_freed": "Javob yozish oynasi yana bo'sh.",
        "cancel_button_all": "❌ Hammasini",
        "cancel_button_none": "↩️ Hech narsani, davom etamiz",
        "cancel_button_donation": "💸 Xayriya miqdori",
        "cancel_item_donation": "men so'ragan xayriya miqdori",
        "cancel_item_stale_prompt": "javob kutib qolgan eski so'rov",
        "cancel_item_new_pack": "siz nom qo'yayotgan yangi to'plam",
        "cancel_button_new_pack": "🆕 Yangi to'plamga nom berish",
        "cancel_item_rename": "\"{title}\" nomini o'zgartirish",
        "cancel_button_rename": "✏️ To'plam nomini o'zgartirish",
        "cancel_item_editing": "\"{title}\" ni tahrirlash",
        "cancel_button_editing": "📦 To'plamni tahrirlash",
        "start_intro": (
            "Salom! Men sizning rasm/GIF/video/stikerlaringizni Telegram stiker "
            "to'plamlariga aylantiraman, shuningdek Instagram/TikTok havolalaridan "
            "video ham olib bera olaman.\n\n"
        ),
        "help_text": (
            "Buyruqlar:\n"
            "/newpack - yangi stiker to'plamini boshlash\n"
            "/addsticker - mavjud to'plamga stiker qo'shish\n"
            "/mypacks - o'z to'plamlaringizni ko'rish\n"
            "/import <to'plam havolasi/nomi> - (tahrirlash paytida) boshqa Telegram "
            "to'plamidan stikerlarni ommaviy nusxalash, yoki WhatsApp stiker to'plami "
            ".zip/.wastickers faylini yuborish\n"
            "/done - to'plamni tahrirlashni tugatish\n"
            "/cancel - men sizdan kutayotgan ishni to'xtatish (qaysinisini so'rayman)\n"
            "/whomade <to'plam havolasi/nomi> - to'plamni kim yaratganini bilish "
            "(agar shu bot orqali yaratilgan bo'lsa)\n"
            "/donate - hosting xarajatlariga hissa qo'shish (butunlay ixtiyoriy)\n"
            "/en, /uz, /rus - tilni almashtirish (yoki /language — u so\'raydi)\n\n"
            "To'plamni tahrirlash paytida: rasm, GIF, video yoki statik/video "
            "stikerlarni yuboring — ular qo'shiladi.\n"
            "Ulardan biridan keyin emoji yuborsangiz, o'sha stikerga shu emoji belgilanadi.\n\n"
            "/mypacks dan to'plamni bosib, uni qayta nomlashingiz, boshqa birov ham "
            "stiker qo'sha olishi uchun hamtahrirlashni sozlashingiz yoki uni butunlay "
            "o'chirishingiz mumkin (faqat egasi uchun, amalga oshirishdan oldin ikki "
            "marta so'raladi).\n\n"
            "Instagram/TikTok'dan video olishni yoki faylni boshqa formatga aylantirishni "
            "xohlaysizmi? Ular endi quyidagi qarindosh botlarda joylashgan.\n\n"
            "Bu bot hali ishlab chiqilmoqda va vaqtinchalik joylashtirilgan. Agar javob "
            "bermasa, biroz kuting — men uni qayta ishga tushirganimda odatda o'zi qaytadi.\n\n"
        ),
        "whomade_usage": "Foydalanish: /whomade <to'plam nomi yoki t.me/addstickers havolasi>",
        "whomade_not_found": (
            "Bu to'plam haqida ma'lumotim yo'q — u shu bot orqali yaratilmagan "
            "yoki nom/havola noto'g'ri."
        ),
        "whomade_result": "📦 \"{title}\"\nUni {creator} {date} sanada yaratgan (shu bot orqali).",
        "coedit_link_invalid": "Bu hamtahrirlash havolasi yaroqsiz — ehtimol, to'plam egasi uni qayta tikladi (reset qildi).",
        "coedit_pack_gone": "Bu to'plam endi mavjud emasga o'xshaydi.",
        "coedit_own_pack": "Bu sizning o'z to'plamingiz — uni boshqarish uchun /mypacks dan foydalaning.",
        "coedit_joined_intro": (
            "Siz \"{title}\" to'plamiga hammuallif sifatida qo'shildingiz! Rasm, GIF, "
            "video yoki statik/video stikerlarni yuboring — ular qo'shiladi, standart "
            "emoji 😭, oxirgisini qayta belgilash uchun darhol keyin emoji yuboring. "
            "Tugatgach /done ni bosing."
        ),
        "btn_new_pack": "➕ Yangi to'plam",
        "btn_my_packs": "📁 Mening to'plamlarim",
        "btn_help": "❓ Yordam",
        "btn_back": "⬅️ Orqaga",
        "no_packs_yet": "Hali to'plamlar yo'q — \"Yangi to'plam\"ni bosing yoki /newpack dan foydalaning.",
        "your_packs": "Sizning to'plamlaringiz:",
        "not_your_pack": "Bu sizning to'plamingiz emas.",
        "pack_detail_title": "📦 {title}",
        "btn_open_pack": "🔗 To'plamni ochish",
        "btn_add_stickers": "➕ Stiker qo'shish",
        "btn_rename": "✏️ Nomini o'zgartirish",
        "btn_coedit": "👥 Hamtahrirlash",
        "btn_delete_pack": "🗑️ To'plamni o'chirish",
        "coedit_count_some": "Hozircha {count} ta hammuallif bor.",
        "coedit_count_none": "Hali hammualliflar yo'q.",
        "coedit_message": (
            "👥 \"{title}\" uchun hamtahrirlash\n\n"
            "Havola: {link}\n\n"
            "Uni ulashing — uni ochgan har bir kishi bot orqali shu to'plamga stiker "
            "qo'sha oladi (ular baribir sizning nomingiz ostida qo'shiladi).\n\n"
            "{editors_line}\n\n"
            "Havolani yangilang, shunda u yangi kishilarga kirish huquqini bermaydi."
        ),
        "btn_reset_link": "🔄 Havolani yangilash",
        "only_owner_coedit": "Hamtahrirlashni faqat to'plam egasi boshqara oladi.",
        "link_reset_confirm": "Havola yangilandi — eskisi endi ishlamaydi.",
        "only_owner_rename": "To'plamni faqat egasi qayta nomlay oladi.",
        "rename_prompt": "\"{title}\" uchun yangi nom yuboring.",
        "rename_broken_state": "Nimadir xato ketdi — /mypacks dan qayta \"Nomini o'zgartirish\"ni sinab ko'ring.",
        "btn_back_to_pack": "⬅️ To'plamga qaytish",
        "renamed_success": "\"{title}\" deb qayta nomlandi.",
        "renamed_failed": "Nomini o'zgartirib bo'lmadi: {error}",
        "only_owner_delete": "To'plamni faqat egasi o'chira oladi.",
        "btn_delete": "🗑️ O'chirish",
        "btn_cancel_inline": "⬅️ Bekor qilish",
        "delete_confirm1": (
            "⚠️ \"{title}\" o'chirilsinmi? Bu uni Telegram'da unga ega bo'lgan hamma "
            "uchun, jumladan hammualliflar uchun ham o'chiradi va buni ortga qaytarib "
            "bo'lmaydi."
        ),
        "btn_delete_confirm": "🗑️ Ha, butunlay o'chirilsin",
        "delete_confirm2": "❗ Oxirgi tekshiruv — \"{title}\" butunlay o'chirilsinmi? Bundan keyin ortga qaytarib bo'lmaydi.",
        "delete_failed": "⚠️ O'chirib bo'lmadi: {error}",
        "btn_my_packs_back": "⬅️ Mening to'plamlarim",
        "delete_success": "🗑️ \"{title}\" butunlay o'chirildi.",
        "newpack_title_prompt": "To'plamning nomi qanday bo'lsin?",
        "title_empty": "Bu bo'sh — to'plam uchun haqiqiy nom yuboring.",
        "title_truncated": "Telegram to'plam nomini 64 belgigacha cheklaydi — \"{title}\" ishlatiladi.",
        "editing_intro_new": (
            "Rasm, GIF, video yoki statik/video stikerlarni yuboring — har biri "
            "standart 😭 emojisi bilan qo'shiladi. Oxirgisini qayta belgilash uchun "
            "darhol keyin emoji yuboring. Tugatgach /done ni bosing."
        ),
        "no_packs_for_add": "Sizda hali to'plamlar yo'q. Avval /newpack dan foydalaning.",
        "pick_pack_prompt": "Qaysi to'plam? Uni bosing, keyin \"➕ Stiker qo'shish\"ni tanlang.",
        "editing_intro_add": (
            "Qo'shish uchun rasm, GIF, video yoki statik/video stikerlarni yuboring — "
            "standart emoji 😭, oxirgisini qayta belgilash uchun darhol keyin emoji "
            "yuboring. Tugatgach /done ni bosing.\n\n"
            "Maslahat: shu to'plamda allaqachon bor stikerni yuborsangiz, u dublikat "
            "sifatida qo'shilmaydi, aksincha olib tashlanadi."
        ),
        "status_verb_creating": "Yaratilmoqda",
        "status_verb_editing": "Tahrirlanmoqda",
        "status_line": "📝 \"{title}\" {verb} — shu seansda {count} ta stiker qo'shildi",
        "status_default_title": "bu to'plam",
        "btn_delete_pack_yes": "🗑️ Ha, to'plam o'chirilsin",
        "btn_cancel": "Bekor qilish",
        "remove_last_confirm": (
            "Bu to'plamda qolgan yagona stiker — uni olib tashlash *butun to'plamni* "
            "Telegram'dan o'chirib yuboradi, chunki to'plamlar bo'sh bo'lishi mumkin "
            "emas. Ishonchingiz komilmi?"
        ),
        "remove_failed": "⚠️ Bu stikerni olib tashlab bo'lmadi: {error}",
        "remove_success": "🗑️ Bu stiker allaqachon shu to'plamda bor edi — uni olib tashladim.",
        "keep_pack": "Yaxshi, to'plam o'zgarishsiz qoldirildi.",
        "pack_deleted_empty": "🗑️ To'plam o'chirildi (unda stiker qolmagan edi).",
        "pack_deleted_note": "❌ To'plam o'chirildi.",
        "image_process_failed": "Bu rasmni qayta ishlab bo'lmadi: {error}",
        "added_default_emoji": "{emoji} bilan qo'shildi — qayta belgilash uchun emoji yuboring.",
        "last_attempt_failed": "⚠️ Oxirgi urinish muvaffaqiyatsiz tugadi — qayta urinish uchun boshqa narsa yuboring yoki /cancel qiling.",
        "converting_video": "Video stikerga aylantirilmoqda...",
        "video_convert_failed_redirect": (
            "{error}\n\nBuni stikerga aylantirib bo'lmaydi, lekin agar sizga shunchaki "
            "oddiy formatdagi fayl kerak bo'lsa, buni @ConvertBot qila oladi — shu "
            "faylni o'sha yerga yuboring 👇"
        ),
        "video_convert_generic_failed": "Buni aylantirib bo'lmadi: {error}",
        "added_video_default_emoji": (
            "Standart {emoji} bilan video stiker sifatida qo'shildi. Uni qayta "
            "belgilash uchun hozir emoji yuboring, davom etish uchun yana "
            "rasm/GIF/video yuboring yoki tugatish uchun /done ni bosing."
        ),
        "animated_not_supported": (
            "Animatsion (Lottie/.tgs) stikerlar qo'llab-quvvatlanmaydi — buning "
            "o'rniga statik rasm, GIF/video yoki statik/video stiker yuboring."
        ),
        "import_usage": (
            "Boshqa ochiq Telegram to'plamidan stikerlarni shu to'plamga nusxalash "
            "uchun /import <telegram to'plam havolasi yoki nomi> yuboring — yoki "
            "shunchaki WhatsApp stiker to'plami .zip/.wastickers faylini "
            "to'g'ridan-to'g'ri yuboring."
        ),
        "import_invalid_source": "Bu haqiqiy to'plam nomi yoki t.me/addstickers havolasiga o'xshamayapti.",
        "import_fetching": "\"{source}\" dan stikerlar olinmoqda...",
        "import_summary_head": "\"{source}\" dan {added} ta stiker import qilindi",
        "import_summary_skipped": ", {skipped} ta qo'llab-quvvatlanmaydigani (animatsion/Lottie) o'tkazib yuborildi",
        "import_summary_failed": ", {failed} tasi muvaffaqiyatsiz tugadi",
        "import_summary_tail": ". Davom etish uchun yana yuboraversangiz bo'ladi, yoki tugatish uchun /done ni bosing.",
        "done_standalone_hint": (
            "Tugatadigan narsa yo'q -- hozir hech qanday to'plamni tahrirlamayapsiz. "
            "/newpack bilan yangisini boshlang yoki /mypacks dagi to'plamda "
            "\"Stiker qo'shish\"ni bosing."
        ),
        "import_standalone_hint": (
            "Avval to'plamni boshlang yoki oching (/newpack, yoki /mypacks dan biror "
            "to'plamda \"Stiker qo'shish\"ni bosing), so'ng o'sha seans ichida "
            "/import <havola> dan foydalaning."
        ),
        "whatsapp_reading": "WhatsApp stiker to'plami o'qilmoqda...",
        "whatsapp_summary_head": "WhatsApp to'plamidan {added} ta stiker import qilindi",
        "not_emoji_message": "Qo'shish uchun rasm/GIF/video/stiker yuboring, oxirgisini qayta belgilash uchun emoji yuboring, yoki /done ni bosing.",
        "no_sticker_to_tag": "Avval stiker qo'shing, keyin uni belgilash uchun emoji yuboring.",
        "retagged_success": "{emojis} sifatida qayta belgilandi.",
        "retag_failed": "Emojini yangilab bo'lmadi: {error}",
        "nothing_added_yet": "Siz hali hech narsa qo'shmadingiz. Avval rasm yuboring.",
        "done_success": (
            "✅ \"{title}\" tugallandi — shu seansda {count} ta stiker qo'shildi.\n\n"
            "Tayyor: https://t.me/addstickers/{pack_name}"
        ),
        "convert_redirect": (
            "Fayl konvertatsiyasi (rasm/video/audio, faqat stikerga xos bo'lmagan) "
            "endi @ConvertBot ga ko'chirildi — ochish uchun quyidagini bosing."
        ),
        "cancelled_status_note": "❌ Bekor qilindi.",
        "unrecognized": "Bu nima uchunligini tushunmadim — /newpack, /mypacks yoki /help ni sinab ko'ring.",
        "unknown_command": "Bu buyruqni tanimadim. Nima qila olishimni bilish uchun /help yuboring.",
        "err_invalid_name": (
            "⚠️ Telegram to'plamning ichki nomini rad etdi — bu odatda nom raqam yoki "
            "belgidan boshlanganda yuz beradi. /cancel yuboring, so'ng harfdan "
            "boshlanadigan nom bilan yana /newpack qiling (masalan, \"2007\" o'rniga "
            "\"My 2007\")."
        ),
        "err_name_occupied": (
            "⚠️ Bu to'plamning ichki nomi mavjud nom bilan to'qnashdi (kamdan-kam "
            "uchraydi, shunchaki omadsizlik). /cancel yuboring, so'ng yangisini olish "
            "uchun yana /newpack qiling."
        ),
        "err_too_many_stickers": "⚠️ Bu to'plam Telegram'ning stiker chegarasiga (120) allaqachon yetgan — buning o'rniga /newpack bilan yangi to'plam boshlang.",
        "err_bad_format": "⚠️ Telegram bu fayl formatini shu to'plam uchun qabul qilmadi — boshqa rasmni sinab ko'ring.",
        "err_generic": "⚠️ Telegram buni rad etdi: {msg}\n\nQayta urinib ko'rishingiz mumkin, yoki to'xtatish uchun /cancel qiling.",
        "err_timed_out": (
            "⚠️ Telegram vaqtida tasdiqlamadi — baribir amalga oshgan bo'lishi mumkin, "
            "shuning uchun qayta urinishdan oldin to'plamni tekshiring. Qayta urinib "
            "ko'rishingiz mumkin, yoki to'xtatish uchun /cancel qiling."
        ),
        "restarting_send_again": "🔄 Hozir yangilanmoqdaman — bir necha soniyadan so'ng buni qaytadan yuboring.",
        "update_soon_try_later": "🔧 Hozir yangilanaman, shuning uchun yangi ish boshlay olmayman — taxminan {minutes} daqiqadan so'ng qaytadan urinib ko'ring. Qaytganimda o'zim xabar beraman.",
        "update_soon_try_later_soon": "🔧 Hozir yangilanmoqdaman, shuning uchun yangi ish boshlay olmayman — birozdan so'ng qaytadan urinib ko'ring. Qaytganimda o'zim xabar beraman.",
        "update_will_reset": "🔧 Diqqat: men yangilanmoqchiman va hozir boshlagan ishingiz bekor qilinadi. Bir necha daqiqadan so'ng qaytadan boshlashingiz mumkin.",
        "update_done_try_now": "✅ Yangilanish tugadi — endi qaytadan urinib ko'rishingiz mumkin.",
        "video_convert_ffmpeg_missing": (
            "Bu serverda ffmpeg o'rnatilmagan, shuning uchun GIF/video stikerlarni "
            "aylantirib bo'lmaydi. Uni 'apt install ffmpeg' (Linux), 'brew install "
            "ffmpeg' (Mac) orqali o'rnating, yoki Windows uchun build'ni PATH'ga qo'shing."
        ),
        "video_convert_empty_file": "Bu fayl bo'sh holda keldi — uni qayta yuborishga urinib ko'ring.",
        "video_convert_too_big": (
            "Bu klipni Telegram'ning 256 KB video-stiker chegarasidan pastga siqib "
            "bo'lmadi ({note}). Qisqaroq yoki vizual jihatdan soddaroq klipni sinab ko'ring."
        ),
        "import_pack_not_found": (
            "\"{source}\" nomli stiker to'plami topilmadi — havola/nomni qayta "
            "tekshiring (u ochiq bo'lishi kerak)."
        ),
        "import_bad_zip": "Bu haqiqiy .zip/.wastickers fayliga o'xshamayapti.",
        "import_zip_no_images": "Bu zip ichida ishlatsa bo'ladigan rasm topilmadi.",
    },
    "ru": {
        "sibling_blurb": "Тоже часть этой семьи ботов, смотри ниже \U0001f447",
        "donation_nudge": (
            "💙 Если этот бот оказался полезным: расходы на хостинг/API покрывает тот, "
            "кто его запустил, а /donate — это совершенно необязательный способ помочь "
            "ему остаться на плаву. Никакого давления в любом случае!"
        ),
        "donate_unknown_currency": 'Неизвестная валюта "{currency}" — попробуйте xtr или usd.',
        "donate_currency_not_configured": "Пожертвования в {currency} на этом боте пока не настроены — попробуйте Stars.",
        "donate_invalid_amount": "Это некорректная сумма — попробуйте, например, /donate 500 или /donate 5 usd.",
        "donate_prompt": (
            "Спасибо за вклад — эти средства идут прямо на хостинг и API этого "
            "бота. Выберите сумму ниже или нажмите «Другое», чтобы ввести свою "
            "(также можно сразу отправить /donate <число> [usd])."
        ),
        "donate_custom_button": "✏️ Другое {symbol}",
        "donate_too_many_stars": "Это очень много звёзд! Пусть будет меньше {max} ⭐ за одно пожертвование.",
        "donate_out_of_range": "Пожертвования в {currency} должны быть в диапазоне от {lo} до {hi} {symbol}.",
        "donate_invoice_title": "Угостите бота кофе ☕",
        "donate_invoice_description": "Разовое добровольное пожертвование на хостинг. Спасибо!",
        "donate_invoice_label": "Пожертвование",
        "donate_invoice_error": "⚠️ Telegram не смог создать этот счёт: {error}",
        "stars_unit": "Stars (звёзды)",
        "donate_custom_ask": "Сколько {unit} вы хотите пожертвовать? Ответьте числом.",
        "donate_invalid_amount_retry": "Это некорректная сумма — отправьте /donate, чтобы попробовать снова.",
        "donate_thanks": "🙏 Спасибо за {amount} ⭐ — это по-настоящему ценно!",
        "language_set_confirmation": "✅ Язык изменён на русский.",
        "cancel_header": "\u274c \u041e\u0442\u043c\u0435\u043d\u0435\u043d\u043e:",
        "cancel_nothing": "\u041e\u0442\u043c\u0435\u043d\u044f\u0442\u044c \u043d\u0435\u0447\u0435\u0433\u043e -- \u044f \u043d\u0438\u0447\u0435\u0433\u043e \u043e\u0442 \u0432\u0430\u0441 \u043d\u0435 \u0436\u0434\u0430\u043b.",
        "cancel_ask": "Что остановить? Вот что я жду:",
        "cancel_kept": "Хорошо -- ничего не отменено.",
        "cancel_reply_box_freed": "Поле ответа снова свободно.",
        "cancel_button_all": "❌ Всё",
        "cancel_button_none": "↩️ Ничего, продолжаем",
        "cancel_button_donation": "💸 Сумма пожертвования",
        "cancel_item_donation": "\u0441\u0443\u043c\u043c\u0430 \u043f\u043e\u0436\u0435\u0440\u0442\u0432\u043e\u0432\u0430\u043d\u0438\u044f, \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u044f \u0437\u0430\u043f\u0440\u043e\u0441\u0438\u043b",
        "cancel_item_stale_prompt": "старый запрос, который всё ещё ждал ответа",
        "cancel_item_new_pack": "\u043d\u043e\u0432\u044b\u0439 \u043d\u0430\u0431\u043e\u0440, \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u0432\u044b \u0434\u0430\u0432\u0430\u043b\u0438 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435",
        "cancel_button_new_pack": "🆕 Название нового набора",
        "cancel_item_rename": "\u043f\u0435\u0440\u0435\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u00ab{title}\u00bb",
        "cancel_button_rename": "✏️ Переименование набора",
        "cancel_item_editing": "\u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u00ab{title}\u00bb",
        "cancel_button_editing": "📦 Редактирование набора",
        "start_intro": (
            "Привет! Я превращаю ваши изображения/GIF/видео/стикеры в наборы "
            "стикеров Telegram, а также могу скачать видео по ссылке из "
            "Instagram/TikTok.\n\n"
        ),
        "help_text": (
            "Команды:\n"
            "/newpack - начать новый набор стикеров\n"
            "/addsticker - добавить стикеры в существующий набор\n"
            "/mypacks - показать ваши наборы\n"
            "/import <ссылка/имя набора> - (во время редактирования) массово "
            "скопировать стикеры из другого набора Telegram, или отправить файл "
            "экспорта набора стикеров WhatsApp .zip/.wastickers\n"
            "/done - закончить редактирование набора\n"
            "/cancel - остановить то, чего я от вас жду (спрошу, что именно)\n"
            "/whomade <ссылка/имя набора> - узнать, кто создал набор (если он был "
            "создан через этого бота)\n"
            "/donate - помочь с расходами на хостинг (совершенно необязательно)\n"
            "/en, /uz, /rus - сменить язык (или /language — он спрашивает)\n\n"
            "Во время редактирования набора: отправляйте изображения, GIF, видео "
            "или статические/видео-стикеры, чтобы добавить их.\n"
            "Отправьте эмодзи сразу после стикера, чтобы пометить его этим эмодзи.\n\n"
            "Нажмите на набор в /mypacks, чтобы переименовать его, настроить "
            "совместное редактирование, чтобы кто-то ещё мог добавлять стикеры, или "
            "удалить его насовсем (только для владельца, дважды спрашивает перед этим).\n\n"
            "Хотите скачать видео из Instagram/TikTok или сконвертировать файл в "
            "другой формат? Теперь это делают соседние боты ниже.\n\n"
            "Этот бот всё ещё находится в разработке и размещён временно. Если он не "
            "отвечает, подождите — обычно он снова заработает, когда я запущу его в "
            "следующий раз.\n\n"
        ),
        "whomade_usage": "Использование: /whomade <имя набора или ссылка t.me/addstickers>",
        "whomade_not_found": (
            "У меня нет записи об этом наборе — либо он не был создан через этого "
            "бота, либо имя/ссылка неверны."
        ),
        "whomade_result": "📦 «{title}»\nСоздал(а) {creator} {date} (через этого бота).",
        "coedit_link_invalid": "Эта ссылка для совместного редактирования недействительна — возможно, владелец набора сбросил её.",
        "coedit_pack_gone": "Похоже, этого набора больше не существует.",
        "coedit_own_pack": "Это ваш собственный набор — используйте /mypacks, чтобы им управлять.",
        "coedit_joined_intro": (
            "Вас добавили как соредактора набора «{title}»! Отправляйте изображения, "
            "GIF, видео или статические/видео-стикеры, чтобы добавить их — эмодзи по "
            "умолчанию 😭, отправьте эмодзи сразу после, чтобы переметить последний. "
            "По завершении — /done."
        ),
        "btn_new_pack": "➕ Новый набор",
        "btn_my_packs": "📁 Мои наборы",
        "btn_help": "❓ Помощь",
        "btn_back": "⬅️ Назад",
        "no_packs_yet": "Пока нет наборов — нажмите «Новый набор» или используйте /newpack.",
        "your_packs": "Ваши наборы:",
        "not_your_pack": "Это не ваш набор.",
        "pack_detail_title": "📦 {title}",
        "btn_open_pack": "🔗 Открыть набор",
        "btn_add_stickers": "➕ Добавить стикеры",
        "btn_rename": "✏️ Переименовать",
        "btn_coedit": "👥 Совместное редактирование",
        "btn_delete_pack": "🗑️ Удалить набор",
        "coedit_count_some": "Пока {count} соредактор(ов).",
        "coedit_count_none": "Пока нет соредакторов.",
        "coedit_message": (
            "👥 Совместное редактирование «{title}»\n\n"
            "Ссылка: {link}\n\n"
            "Поделитесь ей — любой, кто её откроет, сможет добавлять стикеры в этот "
            "набор через бота (они всё равно будут добавляться от вашего имени).\n\n"
            "{editors_line}\n\n"
            "Сбросьте ссылку, чтобы она больше не давала доступ новым людям."
        ),
        "btn_reset_link": "🔄 Сбросить ссылку",
        "only_owner_coedit": "Совместным редактированием может управлять только владелец набора.",
        "link_reset_confirm": "Ссылка сброшена — старая больше не работает.",
        "only_owner_rename": "Переименовать набор может только его владелец.",
        "rename_prompt": "Отправьте новое название для «{title}».",
        "rename_broken_state": "Что-то пошло не так — попробуйте снова переименовать через /mypacks.",
        "btn_back_to_pack": "⬅️ Назад к набору",
        "renamed_success": "Переименовано в «{title}».",
        "renamed_failed": "Не удалось переименовать: {error}",
        "only_owner_delete": "Удалить набор может только его владелец.",
        "btn_delete": "🗑️ Удалить",
        "btn_cancel_inline": "⬅️ Отмена",
        "delete_confirm1": (
            "⚠️ Удалить «{title}»? Это удалит набор из Telegram у всех, у кого он "
            "есть, включая соредакторов, и отменить это будет нельзя."
        ),
        "btn_delete_confirm": "🗑️ Да, удалить навсегда",
        "delete_confirm2": "❗ Последняя проверка — удалить «{title}» навсегда? После этого отменить будет нельзя.",
        "delete_failed": "⚠️ Не удалось удалить: {error}",
        "btn_my_packs_back": "⬅️ Мои наборы",
        "delete_success": "🗑️ «{title}» удалён(а) навсегда.",
        "newpack_title_prompt": "Каким будет название набора?",
        "title_empty": "Это пусто — отправьте настоящее название для набора.",
        "title_truncated": "Telegram ограничивает название набора 64 символами — используется «{title}».",
        "editing_intro_new": (
            "Отправляйте изображения, GIF, видео или статические/видео-стикеры — "
            "каждый добавляется с эмодзи по умолчанию 😭. Отправьте эмодзи сразу "
            "после, чтобы переметить последний. По завершении — /done."
        ),
        "no_packs_for_add": "У вас пока нет наборов. Сначала используйте /newpack.",
        "pick_pack_prompt": "Какой набор? Нажмите на него, затем «➕ Добавить стикеры».",
        "editing_intro_add": (
            "Отправляйте изображения, GIF, видео или статические/видео-стикеры, "
            "чтобы добавить их — эмодзи по умолчанию 😭, отправьте эмодзи сразу "
            "после, чтобы переметить последний. По завершении — /done.\n\n"
            "Совет: если отправить стикер, который уже есть в этом наборе, он будет "
            "удалён, а не добавлен повторно."
        ),
        "status_verb_creating": "Создание",
        "status_verb_editing": "Редактирование",
        "status_line": "📝 {verb} «{title}» — за эту сессию добавлено {count} стикер(ов)",
        "status_default_title": "этот набор",
        "btn_delete_pack_yes": "🗑️ Да, удалить набор",
        "btn_cancel": "Отмена",
        "remove_last_confirm": (
            "Это последний стикер, оставшийся в наборе — его удаление удалит *весь "
            "набор* из Telegram, так как наборы не могут быть пустыми. Вы уверены?"
        ),
        "remove_failed": "⚠️ Не удалось удалить этот стикер: {error}",
        "remove_success": "🗑️ Этот стикер уже был в наборе — я его удалил.",
        "keep_pack": "Хорошо, набор оставлен как есть.",
        "pack_deleted_empty": "🗑️ Набор удалён (в нём не осталось стикеров).",
        "pack_deleted_note": "❌ Набор удалён.",
        "image_process_failed": "Не удалось обработать это изображение: {error}",
        "added_default_emoji": "Добавлено {emoji} — отправьте эмодзи, чтобы переметить.",
        "last_attempt_failed": "⚠️ Последняя попытка не удалась — отправьте другой файл, чтобы попробовать снова, или /cancel.",
        "converting_video": "Преобразование в видео-стикер...",
        "video_convert_failed_redirect": (
            "{error}\n\nПревратить это в стикер нельзя, но если вам просто нужен "
            "файл в обычном формате, это может сделать @ConvertBot — просто "
            "отправьте тот же файл туда 👇"
        ),
        "video_convert_generic_failed": "Не удалось это преобразовать: {error}",
        "added_video_default_emoji": (
            "Добавлено как видео-стикер с эмодзи {emoji} по умолчанию. Отправьте "
            "эмодзи сейчас, чтобы переметить, ещё одно изображение/GIF/видео, чтобы "
            "продолжить, или /done, чтобы закончить."
        ),
        "animated_not_supported": (
            "Анимированные (Lottie/.tgs) стикеры не поддерживаются — отправьте "
            "вместо этого статичное изображение, GIF/видео или "
            "статический/видео-стикер."
        ),
        "import_usage": (
            "Отправьте /import <ссылка или имя набора Telegram>, чтобы скопировать "
            "стикеры из другого публичного набора Telegram в этот — или просто "
            "отправьте файл набора стикеров WhatsApp .zip/.wastickers напрямую."
        ),
        "import_invalid_source": "Это не похоже на настоящее имя набора или ссылку t.me/addstickers.",
        "import_fetching": "Загрузка стикеров из «{source}»...",
        "import_summary_head": "Импортировано {added} стикер(ов) из «{source}»",
        "import_summary_skipped": ", пропущено {skipped} неподдерживаемых (анимированные/Lottie)",
        "import_summary_failed": ", {failed} не удалось",
        "import_summary_tail": ". Можете отправлять ещё, или /done, чтобы закончить.",
        "done_standalone_hint": (
            "Нечего завершать -- сейчас вы не редактируете набор. "
            "Начните новый через /newpack или нажмите «Добавить стикеры» "
            "на наборе из /mypacks."
        ),
        "import_standalone_hint": (
            "Сначала начните или откройте набор (/newpack, или нажмите «Добавить "
            "стикеры» на наборе из /mypacks), затем используйте /import <ссылка> "
            "внутри этой сессии."
        ),
        "whatsapp_reading": "Чтение набора стикеров WhatsApp...",
        "whatsapp_summary_head": "Импортировано {added} стикер(ов) из набора WhatsApp",
        "not_emoji_message": "Отправьте изображение/GIF/видео/стикер, чтобы добавить, эмодзи, чтобы переметить последний, или /done.",
        "no_sticker_to_tag": "Сначала добавьте стикер, затем отправьте эмодзи, чтобы его пометить.",
        "retagged_success": "Переметено как {emojis}.",
        "retag_failed": "Не удалось обновить эмодзи: {error}",
        "nothing_added_yet": "Вы ещё ничего не добавили. Сначала отправьте изображение.",
        "done_success": (
            "✅ «{title}» завершён — за эту сессию добавлено {count} стикер(ов).\n\n"
            "Готово: https://t.me/addstickers/{pack_name}"
        ),
        "convert_redirect": (
            "Конвертация файлов (изображения/видео/аудио, не только стикеры) теперь "
            "в @ConvertBot — нажмите ниже, чтобы открыть."
        ),
        "cancelled_status_note": "❌ Отменено.",
        "unrecognized": "Не понял, для чего это — попробуйте /newpack, /mypacks или /help.",
        "unknown_command": "Я не знаю такую команду. Отправь /help, чтобы увидеть, что я умею.",
        "err_invalid_name": (
            "⚠️ Telegram отклонил внутреннее имя набора — обычно это происходит, "
            "когда название начинается с цифры или символа. Отправьте /cancel, затем "
            "снова /newpack с названием, начинающимся с буквы (например, «My 2007» "
            "вместо «2007»)."
        ),
        "err_name_occupied": (
            "⚠️ Внутреннее имя набора совпало с уже существующим (редкость, просто "
            "не повезло). Отправьте /cancel, затем снова /newpack, чтобы получить новое."
        ),
        "err_too_many_stickers": "⚠️ Этот набор уже достиг лимита Telegram по стикерам (120) — вместо этого начните новый набор через /newpack.",
        "err_bad_format": "⚠️ Telegram не принял формат этого файла для этого набора — попробуйте другое изображение.",
        "err_generic": "⚠️ Telegram отклонил это: {msg}\n\nВы можете попробовать снова, или /cancel, чтобы остановиться.",
        "err_timed_out": (
            "⚠️ Telegram не подтвердил вовремя — возможно, всё же прошло, поэтому "
            "проверьте набор перед повторной попыткой, чтобы не задвоить. Можете "
            "попробовать снова, или /cancel, чтобы остановиться."
        ),
        "restarting_send_again": "🔄 Сейчас обновляюсь — подождите несколько секунд и отправьте ещё раз.",
        "update_soon_try_later": '🔧 Сейчас меня обновляют, поэтому я не могу начать ничего нового — попробуйте снова примерно через {minutes} мин. Я напишу, когда вернусь.',
        "update_soon_try_later_soon": '🔧 Сейчас меня обновляют, поэтому я не могу начать ничего нового — попробуйте снова чуть позже. Я напишу, когда вернусь.',
        "update_will_reset": '🔧 Внимание: меня скоро обновят, и то, что вы сейчас начали, будет сброшено. Через несколько минут сможете начать заново.',
        "update_done_try_now": '✅ Обновление завершено — можете пробовать снова.',
        "video_convert_ffmpeg_missing": (
            "На этом сервере не установлен ffmpeg, поэтому GIF/видео-стикеры нельзя "
            "преобразовать. Установите его через 'apt install ffmpeg' (Linux), "
            "'brew install ffmpeg' (Mac), либо добавьте сборку для Windows в PATH."
        ),
        "video_convert_empty_file": "Этот файл пришёл пустым — попробуйте отправить его ещё раз.",
        "video_convert_too_big": (
            "Не удалось сжать этот клип до лимита Telegram в 256 КБ для "
            "видео-стикера ({note}). Попробуйте более короткий или визуально более "
            "простой клип."
        ),
        "import_pack_not_found": (
            "Не удалось найти набор стикеров с именем «{source}» — перепроверьте "
            "ссылку/имя (он должен быть публичным)."
        ),
        "import_bad_zip": "Это не похоже на настоящий файл .zip/.wastickers.",
        "import_zip_no_images": "Внутри этого zip-файла не найдено пригодных изображений.",
    },
}


def t(lang: str | None, key: str, **kwargs) -> str:
    table = STRINGS.get(lang) or STRINGS["en"]
    template = table.get(key) or STRINGS["en"].get(key, key)
    return template.format(**kwargs) if kwargs else template


async def get_lang(user_id: int, context) -> str:
    """Cached in context.user_data to avoid a DB round-trip on every handler
    call. Falls back to "en" for a user who hasn't chosen a language yet
    (only reachable outside /start's first-run gate, e.g. someone who sends
    a sticker before ever running /start)."""
    cached = context.user_data.get("lang")
    if cached:
        return cached
    lang = await asyncio.to_thread(db.get_user_language, user_id) or "en"
    context.user_data["lang"] = lang
    return lang
