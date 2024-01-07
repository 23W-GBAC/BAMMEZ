def get_support_quote(feeling):
    
    quotes = {
        'happy': "Every day may not be good, but there's something good in every day.",
        'sad': "Tough times never last, but tough people do, so please know the storm will come to pass.",
        'stressed': "In the middle of difficulty lies opportunity just look for the opportunity and you will realise that even in the worst state you are a winner .",
        'excited': "Your attitude determines your direction .",
        'angry': "Don't let the behavior of others destroy your inner peace and remember anger comes with regretable results.",
        'horny':"No solution is permanet try to think ",
        'heart broken':'Do not let someone who is not worth your love make you forget how much you are worth.',
        'suicidal':'Do not let pain you hid inside overtake you like the darkness overtakes the sun. But rather comfort yourself in knowing that even on the darkest night, stars still shine.',
        'hopeless':" If you lose hope your dreams will not come true TRY HARDER MY GEE ",
        'anxious': "Worrying does not take away tomorrow's troubles; it takes away today's peace so worry not MY GEE it is just a matter of time everything will come to pass."

        
    }

    
    return quotes.get(feeling.lower(), "I'm here to support you and please remember every situation has an end.")


def interactive_support_bot():
    print("Hi there! How are you feeling today?")

    while True:
        user_input = input("You: ").lower()

        break

    print("Support Bot: " + get_support_quote(user_input))

    if __name__ == "__main__":
        interactive_support_bot()
        if user_input == 'Thank you':
            print("Goodbye!")



