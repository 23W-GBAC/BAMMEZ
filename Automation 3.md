# Week 3 
During this week i wanted to create a simple feeling bot where one would feed in his her feeling then it reponds with an encouragement quote . After the previous weeks of running 
automations which i thought were cool yet they  were against the terms of Git hub ,i had to think outside the box and work on something cool and befinicial to the society this is just 
a simply bot but really nice . 
# First .

i used the get_support_quote  which is a function that takes a feeling as input and returns a corresponding support quote. 
This function uses a dictionary (quotes) to map different feelings to their associated quotes.And just like that i used the quotes i wanted to feed into my system

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
# Second
I had to return the quote incase someone puts in a problem which is not in the system the bot replies I'm here to support you and please remember every situation has an end.

    return quotes.get(feeling.lower(), "I'm here to support you and please remember every situation has an end.")
    
# Third 

I used the interrctive bot interactive_support_bot which is the main function that initiates the interactive conversation by printing a greeting asking the user how they are feeling today.
The code then enters a while loop that will continue until the user types "Thank you."
Inside the loop, it prompts the user for input using input("You: ") and converts the input to lowercase (user_input = input("You: ").lower()).
If the user types "exit," the program prints "Goodbye!" and breaks out of the loop, ending the conversation.
Otherwise, it prints the support bot's response, which is the support quote obtained from the get_support_quote function.

def interactive_support_bot():
    print("Hi there! How are you feeling today?")

    while True:
        user_input = input("You: ").lower()

        break

    print("Support Bot: " + get_support_quote(user_input))
    
# Lastly 
i called the interractive support since the system was supposed to run main

    if __name__ == "__main__":
        interactive_support_bot()
        if user_input == 'Thank you':
            print("Goodbye!")

## Problem

Users may need emotional support and encouragement based on their feelings.

Generating support messages that are sensitive, appropriate, and helpful can be challenging, especially considering the diverse nature of emotions and individuals.

# Context
The need for emotional support is subjective and can vary from person to person.
Providing a human touch to support messages can be challenging in an automated setting.

## Possible Solutions and Errand Attempts
# possible solutions

Collaborate with psychologists, counselors, or mental health specialists to examine and improve replies. Create explicit guidelines for the bot's behavior, and regularly monitor and update responses based on user feedback.

Implement elements that make conversations more interesting, such as asking open-ended inquiries, expressing positive affirmations, and allowing users to express themselves beyond simple phrases. Encourage users to submit comments on the helpfulness of responses.

 # errand attempts
 Use bias detection algorithms to automatically identify potentially biased responses. Perform bias audits with external experts to assure impartiality. 
 Update the dataset on a regular basis to reflect new user interactions. Use data augmentation techniques to simulate various scenarios.  
 ## Advantages
Pre-defined responses ensure consistent support.
Adaptability.Machine learning allows the bot to adapt to user needs over time.
Feedback Loop.User feedback provides insights for refining responses.

## Disadvantages
Fully automating emotional support may lack the personal touch of human interaction.
Complexity in  Model Training. Developing a robust machine learning model requires significant resources and expertise.
Maintenance: Ongoing maintenance for updates, bug fixes, and improvements.
Human Oversight , If using a machine learning model, ongoing human oversight may be necessary.
## solution 
Investing time in assembling a large and diverse dataset. If necessary, supplement data with additional information. Consider working with psychologists or mental health professionals to gain better insights.

## Long-term Savings
Over the next 5 years, the automation could save significant time compared to manual responses, leading to increased efficiency and scalability.

 ## Economic Considerations:

The economic benefit depends on the cost of initial development and maintenance compared to the time saved and user satisfaction achieved. If the bot effectively supports users and requires less human intervention, it can be considered economically beneficial.

            
