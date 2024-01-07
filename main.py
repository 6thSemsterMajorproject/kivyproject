from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import wikipedia

class WikipediaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.search_input = TextInput(hint_text='Enter search term', multiline=False)
        search_button = Button(text='Search', on_press=self.search_wikipedia)
        self.result_label = Label(text='Search results will appear here')

        layout.add_widget(self.search_input)
        layout.add_widget(search_button)
        layout.add_widget(self.result_label)

        return layout

    def search_wikipedia(self, instance):
        search_term = self.search_input.text
        try:
            result = wikipedia.summary(search_term)
            self.result_label.text = result
        except wikipedia.exceptions.DisambiguationError as e:
            self.result_label.text = f"Ambiguous search term. Choose a specific topic: {e.options}"
        except wikipedia.exceptions.PageError:
            self.result_label.text = "No results found."

if _name_ == '_main_':
    WikipediaApp().run()
