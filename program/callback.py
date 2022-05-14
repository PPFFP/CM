# Copyright (C) 2022 By Shadow

from driver.queues import QUEUE
from pyrogram import Client, filters
from program.utils.inline import menu_markup
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    BOT_PHOTO,
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.answer("الصفحه الرئيسيه")
    await query.edit_message_text(
        f"""⥁⁞ **مرحبا ضلعي: »「 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 」!**\n**⥁⁞ انا بوت «**روبلڪس**» استطيع**
**⥁⁞  تشغيل الموسيقى والفيديوات في محادثات المرئية**
**⥁⁞  لتعلم طريقة تشغيلي في مجموعة اضغط على »« طريقة التفعيل »**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•𝗺𝗥.𝗕𝗮𝗞𝗥⁴⁰ᴷ•", url="https://t.me/PPFFP",
                    )
                ],
                [InlineKeyboardButton("", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 الاوامر", callback_data="cbcmdsu"),
                    InlineKeyboardButton("𝗺𝗥.𝗕𝗮𝗞𝗥⁴⁰ᴷ", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "قناة التحديثات ", url=f"https://t.me/TEAMROBLX"
                    ),
                    InlineKeyboardButton(
                        "📣 قناه السورس ", url=f"https://t.me/EUUUJ"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "ضيـف البـوت لمجمـوعتـك ✅",
                        url=f"https://t.me/USDDBOT?startgroup=true"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("طريقة الاستخدام")
    await query.edit_message_text(
        f"" الدليل الأساسي لاستخدام هذا البوت:

 1 ↤ أولاً ، أضفني إلى مجموعتك
**ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉**
 2 ↤ بعد ذلك ، قم برفعي كمشرف ومنح جميع الصلاحيات باستثناء الوضع الخفي
**ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉**
 3 ↤ بعد رفعي مشرف ، اكتب **« تحديث »** مجموعة لتحديث بيانات المشرفين
**ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉**
 4 ↤ أضف @{ASSISTANT_NAME} إلى مجموعتك أو اكتب **« تع روبلكس »** لدعوة حساب المساعد
**ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉**
 5 ↤ قم بتشغيل المكالمة  أولاً قبل البدء في تشغيل الفيديو / الموسيقى
**ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉**
 6 ↤ في بعض الأحيان ، يمكن أن تساعدك إعادة تحميل البوت باستخدام الأمر **« تحديث»** في إصلاح بعض المشكلات
 📌 إذا لم ينضم البوت إلى المكالمة ، فتأكد من تشغيل المكالمة  بالفعل ، أو اكتب **« غادر روبلكس»** ثم اكتب « تع روبلكس»  مرة أخرى
**ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉**
 💡 إذا كانت لديك أسئلة حول هذا البوت ، فيمكنك إخبارنا من خلال الدعم الفني، 

• [الدعم الفني](t.me/PPFPBOT) ➖ •[تحديثات البوت](t.me/TEAMROBLX)
🏵 [ اضغط هنا لمتابعه جديدنا](t.me/EUUUJ)
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbstart")]]
        ),
    )



@Client.on_callback_query(filters.regex("cbcmdsu"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("ختيار لغة")
    await query.edit_message_text(
        f"""» **قم بالضغط على الزر اللغة الذي تريدها لمعرفه الاوامر لكل لغة منها !**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🇬🇧 English ", callback_data="cbcmds"),
                    InlineKeyboardButton("🇮🇶العربية ", callback_data="cbcmdsar"),
                ],[
                    InlineKeyboardButton("قناة التحديثات", url=f"https://t.me/TEAMROBLX")
                ],[
                    InlineKeyboardButton("🔙 رجوع", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("قائمة الاوامر")
    await query.edit_message_text(
        f"""» **قم بالضغط علي الزر الذي تريده لمعرفه الاوامر لكل فئه منهم !**

⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 اوامر الادمنيه", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 اوامر المطور", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 اوامر اساسيه", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 رجوع", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("الاوامر الاساسيه")
    await query.edit_message_text(
        f"""🏮 الاوامر الاساسيه:

» /play +「اسم الأغنية / رابط」لتشغيل اغنيه في المحادثه الصوتيه
» /vplay +「اسم الفيديو / رابط 」 لتشغيل الفيديو داخل المكالمة
» /vstream 「رابط」 تشغيل فيديو مباشر من اليوتيوب
» /playlist 「تظهر لك قائمة التشغيل」
» /end「لإنهاء الموسيقى / الفيديو في الكول」
» /song + 「الاسم تنزيل صوت من youtube」
»/vsong + 「الاسم  تنزيل فيديو من youtube」
» /skip「للتخطي إلى التالي」
» /ping 「إظهار حالة البوت بينغ」
» /uptime 「لعرض مده التشغيل للبوت」
» /alive「اظهار معلومات البوت(في المجموعه)」
⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )



@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("اوامر الادمنيه")
    await query.edit_message_text(
        f"""🏮 هنا أوامر الادمنيه:

» /pause 「ايقاف التشغيل موقتآ」
» /resume 「استئناف التشغيل」
» /stop「لإيقاف التشغيل」
» /vmute 「لكتم البوت」
» /vunmute 「لرفع الكتم عن البوت」
» /volume 「ضبط مستوئ الصوت」
» /reload「لتحديث البوت و قائمة المشرفين」
» /userbotjoin「لاستدعاء الحساب المساعد」
» /userbotleave「لطرد الحساب المساعد」
⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("اوامر المطور")
    await query.edit_message_text(
        f"""🏮 هنا اوامر المطور:

» /rmw「لحذف جميع الملفات 」
» /rmd「حذف جميع الملفات المحمله」
» /sysinfo「لمعرفه معلومات السيرفر」
» /update「لتحديث بوتك لاخر نسخه」
» /restart「اعاده تشغيل البوت」
» /leaveall「خروج الحساب المساعد من جميع المجموعات」

⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )
    
    
@Client.on_callback_query(filters.regex("cbcmdsar"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("قائمة الاوامر العربية")
    await query.edit_message_text(
        f"""» **قم بالضغط علي الزر الذي تريده لمعرفه الاوامر لكل فئه منهم !**

⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 اوامر الادمنيه", callback_data="cbadminar"),
                    InlineKeyboardButton("🧙🏻 اوامر المطور", callback_data="cbsudoar"),
                ],[
                    InlineKeyboardButton("📚 اوامر اساسيه", callback_data="cbbasicar")
                ],[
                    InlineKeyboardButton("🔙 رجوع", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasicar"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("الاوامر الاساسيه العربية")
    await query.edit_message_text(
        f"""🏮 الاوامر الاساسيه:

⥁⁞ يجب عليك وضع «/ او! » استخدام الاوامر 
ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
⥁⁞ » تشغيل  +「اسم الأغنية / رابط」لتشغيل اغنيه في المحادثه الصوتيه
ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
⥁⁞ » فيديو +「اسم الفيديو / رابط 」 لتشغيل الفيديو داخل المكالمة
ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
⥁⁞ » مباشر「رابط」 تشغيل فيديو مباشر من اليوتيوب
ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
⥁⁞ » قائمة التشغيل 「تظهر لك قائمة التشغيل」
ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
⥁⁞ » ايقاف او انهاء 「لإنهاء الموسيقى / الفيديو في الاتصال」
ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
⥁⁞ » تحميل  + 「الاسم تنزيل صوت من youtube」
ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
⥁⁞ »تحميل فيديو + 「الاسم  تنزيل فيديو من youtube」
ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
⥁⁞ » تخطي「للتخطي إلى التالي」
ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
⥁⁞ » بينج「إظهار حالة البوت بينغ」
ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
⥁⁞ » الوقت 「لعرض مده التشغيل للبوت」
ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
⥁⁞ » المجموعة「اظهار معلومات البوت(في المجموعه)」
ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
🏵 [ اضغط هنا لمتابعه جديدنا](t.me/EUUUJ)""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmdsar")]]
        ),
    )



@Client.on_callback_query(filters.regex("cbadminar"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("اوامر الادمنيه بالعربي")
    await query.edit_message_text(
        f"""🏮 هنا أوامر الادمنيه:

⥁⁞ يجب عليك وضع «/ او! » استخدام الاوامر 
**ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉**
⥁⁞ » توقف「ايقاف التشغيل موقتآ 
**ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉**
⥁⁞ » استئناف「استئناف التشغيل」
**ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉**
⥁⁞ » ايقاف او انهاء「لإيقاف التشغيل」
**ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉**
⥁⁞ » كتم 「لكتم البوت」
**ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉**
⥁⁞ » الغاء كتم「لرفع الكتم عن البوت」
**ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉**
⥁⁞ » الصوت 「ضبط مستوئ الصوت」
**ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉**
⥁⁞ » تحديث「لتحديث البوت و قائمة
**ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉** المشرفين」
⥁⁞ » تع روبلكس「لاستدعاء الحساب المساعد」
**ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉**
⥁⁞ » غادر روبلكس「لطرد الحساب المساعد」
**ء┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉**
🏵 [ اضغط هنا لمتابعه جديدنا](t.me/EUUUJ)""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmdsar")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudoar"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("اوامر المطور بالعربي")
    await query.edit_message_text(
        f"""🏮 هنا اوامر المطور:

» /rmw「لحذف جميع الملفات 」
» /rmd「حذف جميع الملفات المحمله」
» /sysinfo「لمعرفه معلومات السيرفر」
» /update「لتحديث بوتك لاخر نسخه」
» /restart「اعاده تشغيل البوت」
» /leaveall「خروج الحساب المساعد من جميع المجموعات」

⚡ قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("⥁⁞  المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    chat = query.message.chat.title
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **الإعدادات** {query.message.chat.title}\n\n⏸ : ايقاف التشغيل موقتآ\n▶️ : استئناف التشغيل\n🔇 : كتم الصوت\n🔊 : الغاء كتم الصوت\n⏹ : ايقاف التشغيل",
              reply_markup=InlineKeyboardMarkup(buttons),
          )
    else:
        await query.answer("**⥁⁞  قائمة التشغيل فارغه**", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("⥁⁞  المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    await query.message.delete()
