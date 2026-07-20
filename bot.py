import os

from dotenv import load_dotenv

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

from calculator import calculate



load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")



expressions = {}





def calculator_keyboard():

    return InlineKeyboardMarkup(

        [
            [
                InlineKeyboardButton("7", callback_data="7"),
                InlineKeyboardButton("8", callback_data="8"),
                InlineKeyboardButton("9", callback_data="9"),
                InlineKeyboardButton("÷", callback_data="/")
            ],

            [
                InlineKeyboardButton("4", callback_data="4"),
                InlineKeyboardButton("5", callback_data="5"),
                InlineKeyboardButton("6", callback_data="6"),
                InlineKeyboardButton("×", callback_data="*")
            ],

            [
                InlineKeyboardButton("1", callback_data="1"),
                InlineKeyboardButton("2", callback_data="2"),
                InlineKeyboardButton("3", callback_data="3"),
                InlineKeyboardButton("-", callback_data="-")
            ],

            [
                InlineKeyboardButton("0", callback_data="0"),
                InlineKeyboardButton(".", callback_data="."),
                InlineKeyboardButton("=", callback_data="="),
                InlineKeyboardButton("+", callback_data="+")
            ],

            [
                InlineKeyboardButton("(", callback_data="("),
                InlineKeyboardButton(")", callback_data=")"),
                InlineKeyboardButton("%", callback_data="%"),
                InlineKeyboardButton("C", callback_data="C")
            ]
        ]

    )








async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id


    expressions[user_id] = ""



    await update.message.reply_text(

        "🧮 Astra Calculator\n\n"
        "محاسبه را شروع کن:",

        reply_markup=calculator_keyboard()

    )









async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):


    query = update.callback_query

    await query.answer()


    user_id = query.from_user.id


    if user_id not in expressions:

        expressions[user_id] = ""



    value = query.data





    if value == "C":

        expressions[user_id] = ""





    elif value == "=":


        result = calculate(
            expressions[user_id]
        )


        expressions[user_id] = str(result)




    else:


        expressions[user_id] += value





    await query.edit_message_text(

        f"🧮 {expressions[user_id]}",

        reply_markup=calculator_keyboard()

    )








def main():


    app = Application.builder().token(TOKEN).build()



    app.add_handler(

        CommandHandler(
            "start",
            start
        )

    )



    app.add_handler(

        CallbackQueryHandler(button)

    )



    print("Astra Calculator Started 🧮")



    app.run_polling()






if __name__ == "__main__":

    main()
