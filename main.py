from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget

# Import files like
from wtf.tkwexams import TkwExamsApp

class manager(BoxLayout):

    # Add screens to main
    tkw_widget=TkwExamsApp()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Check kv file to understand these lines
        self.ids.TkwExamsApp.add_widget(self.login_widget)

class main(App):
    def build(self):
        return manager()

if __name__ == "__main__":
    main().run()