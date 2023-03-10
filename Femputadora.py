"""
FelipedelosH
2023

Chatbot

"""
import re
import random

class Question(object):
    def __init__(self, function, str_response, list_of_words, single_response, required_words) -> None:
        self.function = function
        self.str_response = str_response
        self.list_of_words = list_of_words
        self.single_response = single_response
        self.required_words = required_words

class Femputadora:
    def __init__(self, questions) -> None:
        self.questions = questions
        self.conversation = ""


    def clearText(self, user_input):
        """
        Erase a stranger characters of string
        and return a vector with all words
        ['str', 'str', ...]
        """
        clear_sms = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
        return clear_sms


    def getResponse(self, txt):
        """
        The user enter a txt and femputadora analized
        return a codename of function
        """
        _txt = self.clearText(txt)
        self.update_chat("USER", txt)
        response = self.check_all_messages(_txt)
        return response


    def check_all_messages(self, message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] =  self.message_probability(message, list_of_words, single_response, required_words)

        for i in self.questions:
            response(i.function, i.list_of_words, i.single_response, i.required_words)

        best_match = max(highest_prob, key=highest_prob.get)

        if highest_prob[best_match] < 1:
            return self.unknown()
        else:
            return best_match


    def message_probability(self, clear_user_input, recognized_words, single_response=False, required_word=[]):
        message_certrainty = 0
        has_required_words = True

        for w in clear_user_input:
            if w in recognized_words:
                message_certrainty = message_certrainty + 1

        percentage = message_certrainty / len(recognized_words)


        for w in required_word:
            if w not in clear_user_input:
                has_required_words = False
                break

        if has_required_words or single_response:
            return percentage * 100
        else:
            return 0
        

    # ------------------------------------------------------------
    # ------------------------------------------------------------
    # ------------------------------------------------------------    

    """Chatbot Historial"""
    """Chatbot Historial"""
    """Chatbot Historial"""

    def update_chat(self, user, txt):
        if self.conversation == "":
            self.conversation = user + ":\n" + txt + "\n"
        else:
            self.conversation = self.conversation + "\n" + user + ":\n" + txt + "\n"

    """END Chatbot Historial"""
    """END Chatbot Historial"""
    """END Chatbot Historial"""


    # ------------------------------------------------------------
    # ------------------------------------------------------------
    # ------------------------------------------------------------


    """Response funtions"""
    """Response funtions"""
    """Response funtions"""

    def unknown(self):
        responses = ['Podrias Repetir?', 'No estoy seguro', 'No tengo esa información']
        return responses[random.randint(0, len(responses)-1)]
    
    """END Response funtions"""
    """END Response funtions"""
    """END Response funtions"""
