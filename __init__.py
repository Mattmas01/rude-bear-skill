from mycroft import MycroftSkill, intent_file_handler


class RudeBear(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('bear.rude.intent')
    def handle_bear_rude(self, message):
        self.speak_dialog('bear.rude')


def create_skill():
    return RudeBear()

