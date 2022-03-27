from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


from tkwcards import TkwCards

# Another example: https://gist.github.com/Kovak/5977673

class TkwMainWindow(Screen):
    def __init__(self, **kwargs):
        super(TkwMainWindow, self).__init__(**kwargs)

    def login(self):
        pass

    def show_techniques(self):
        self.manager.transition.direction = "left"
        self.manager.belt = "all"
        self.manager.ids.topics.ids.start_topic.visible(False)
        self.manager.current = "exam"

class TkwExamBelts(Screen):
    def __init__(self, **kwargs):
        super(TkwExamBelts, self).__init__(**kwargs)

    def set_belt(self, belt):
        self.manager.belt = belt
        self.manager.transition.direction = "left"
        self.manager.current = "exam"

class TkwExamWindow(Screen):

    def __init__(self, **kwargs):
        super(TkwExamWindow, self).__init__(**kwargs)

    def back(self):
        current_belt = self.manager.belt
        self.manager.belt = ""
        self.manager.transition.direction = "right"
        if current_belt == "all": self.manager.current = "main"
        else: self.manager.current = "belt_list"

    def set_topic(self, topic):
        self.manager.topic = topic
        self.manager.transition.direction = "right"
        self.manager.current = "topics"

    def start_test(self):
        belt = self.manager.belt
        print("Test all topics for " + belt)
        # TODO: Check database for list of techniques of this belt and show them randomly per topic

class TkwTopicWindow(Screen):
    def __init__(self, **kwargs):
        super(TkwTopicWindow, self).__init__(**kwargs)

    def list_test(self):
        belt = self.manager.belt
        self.manager.transition.direction = "right"
        self.manager.current = "topic_list"

    def start_topic(self):
        topic = self.manager.topic
        belt = self.manager.belt
        print("Test topic " + topic + " for belt " + belt)

class TkwTopicList(Screen):
    def __init__(self, **kwargs):
        super(TkwTopicList, self).__init__(**kwargs)

    def on_enter(self, *args):
        topic_list = self.manager.get_topic_techniques()
        print(self.ids)
        self.ids.grid_topic_list.clear_widgets()
        for tec in topic_list:
            label = Label(text=tec["name"],
                          size_hint=(.5, .5),
                          pos_hint={'center_x': .5, 'center_y': .5})
            self.ids.grid_topic_list.add_widget(label)
        btn = Button(text='Back', size_hint_y=None, height=70)
        btn.bind(on_release=self.back)
        self.ids.grid_topic_list.add_widget(btn)

    def back(self):
        self.manager.current = "topics"

class WindowManager(ScreenManager):

    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        self.belt = ""
        self.topic = ""
        self.cards = TkwCards()

    def get_belt_techniques(self):
        if not self.belt: return []
        return self.cards.get_belt_techniques(self.belt)

    def get_topic_techniques(self):
        if not self.belt or not self.topic: return []
        return self.cards.get_topic_techniques(self.belt, self.topic)

class TkwExamsApp(App):
    def build(self):
        pass

if __name__ == '__main__':
    TkwExamsApp().run()