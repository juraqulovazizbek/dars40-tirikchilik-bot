from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import Config
from callbacks import (
    start,                     # /start - asosiy menyu
    send_about,                # ℹ️ Ma'lumot - kompaniya yoki bot haqida
    change_language,           # 🌐 Tilni tanlash - tilni o'zgartirish
    sendFeedback,              # ✍️ Izoh qoldirish - foydalanuvchi fikri
    send_cart,                 # 📥 Savat - foydalanuvchi savati
    send_partnership_info,     # 💼 Hamkorlik - kompaniya bilan hamkorlik
    send_feedback_response5,   # 😊 Menga hamma narsa yoqdi, 5 ❤️
    send_feedback_response4,   # ☺️ Yaxshi, 4 ⭐️⭐️⭐️⭐️
    send_feedback_response3,   # 😐 Qo'niqarli, 3 ⭐️⭐️⭐️
    send_feedback_response2,   # ☹️ Yoqmadi, 2 ⭐️⭐️
    send_feedback_response1,   # 😤 Men shikoyat qilmoqchiman 👎🏻
    send_delivery_terms,       # 🚀 Yetkazib berish shartlari
    send_contacts              # ☎️ Kontaktlar
)


def main():
    updater = Updater(Config.TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler(
            command='start',
            callback=start
        )
    )

    dispatcher.add_handler(
        MessageHandler(
            Filters.text('📥 Savat'),
            callback=send_cart
        )
    )

    dispatcher.add_handler(
        MessageHandler(
            Filters.text('💼 Hamkorlik'),
            callback=send_partnership_info
        )
    )

    dispatcher.add_handler(
        MessageHandler(
            Filters.text("ℹ️ Ma'lumot"),
            callback=send_about
        )
    )

    dispatcher.add_handler(
        MessageHandler(
            Filters.text("🌐 Tilni tanlash"),
            callback=change_language
        )
    )

    dispatcher.add_handler(
        MessageHandler(
            Filters.text('🏠 Bosh menyu'),
            callback=start
        )
    )

    dispatcher.add_handler(
        MessageHandler(
            Filters.text('✍️ Izoh qoldirish'),
            callback=sendFeedback
        )
    )

    dispatcher.add_handler(
        MessageHandler(
            Filters.text('🚀 Yetkazib berish shartlari'),
            callback=send_delivery_terms
        )
    )

    dispatcher.add_handler(
        MessageHandler(
            Filters.text('☎️ Kontaktlar'),
            callback=send_contacts
        )
    )

    dispatcher.add_handler(
        MessageHandler(
            Filters.text('😊 Menga hamma narsa yoqdi, 5 ❤️'),
            callback=send_feedback_response5
        )
    )

    dispatcher.add_handler(
        MessageHandler(
            Filters.text('☺️ Yaxshi, 4 ⭐️⭐️⭐️⭐️'),
            callback=send_feedback_response4
        )
    )

    dispatcher.add_handler(
        MessageHandler(
            Filters.text("😐 Qo'niqarli, 3⭐️⭐️⭐️"),
            callback=send_feedback_response3
        )
    )

    dispatcher.add_handler(
        MessageHandler(
            Filters.text('☹️ Yoqmadi, 2 ⭐️⭐️'),
            callback=send_feedback_response2
        )
    )

    dispatcher.add_handler(
        MessageHandler(
            Filters.text('😤 Men shikoyat qilmoqchiman 👎🏻'),
            callback=send_feedback_response1
        )
    )

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
