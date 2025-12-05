from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import Config
from callbacks import (
    start,                     
    send_about,                
    change_language,           
    sendFeedback,              
    send_cart,                 
    send_partnership_info,     
    send_feedback_response5,   
    send_feedback_response4,   
    send_feedback_response3,   
    send_feedback_response2,   
    send_feedback_response1,   
    send_delivery_terms,       
    send_contacts              
)

def main():
    application = Application.builder().token(Config.TOKEN).build()

    application.add_handler(
        CommandHandler(
            command='start',
            callback=start
        )
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex('^📥 Savat$'),
            callback=send_cart
        )
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex('^💼 Hamkorlik$'),
            callback=send_partnership_info
        )
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex('^ℹ️ Ma\'lumot$'),
            callback=send_about
        )
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex('^🌐 Tilni tanlash$'),
            callback=change_language
        )
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex('^🏠 Bosh menyu$'),
            callback=start
        )
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex('^✍️ Izoh qoldirish$'),
            callback=sendFeedback
        )
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex('^🚀 Yetkazib berish shartlari$'),
            callback=send_delivery_terms
        )
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex('^☎️ Kontaktlar$'),
            callback=send_contacts
        )
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex('^😊 Menga hamma narsa yoqdi, 5 ❤️$'),
            callback=send_feedback_response5
        )
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex('^☺️ Yaxshi, 4 ⭐️⭐️⭐️⭐️$'),
            callback=send_feedback_response4
        )
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex('^😐 Qo\'niqarli, 3⭐️⭐️⭐️$'),
            callback=send_feedback_response3
        )
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex('^☹️ Yoqmadi, 2 ⭐️⭐️$'),
            callback=send_feedback_response2
        )
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex('^😤 Men shikoyat qilmoqchiman 👎🏻$'),
            callback=send_feedback_response1
        )
    )

    application.run_polling()

if __name__ == '__main__':
    main()
