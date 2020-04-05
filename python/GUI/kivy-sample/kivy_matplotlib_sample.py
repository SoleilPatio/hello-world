
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg #[CLS]:似乎是要Python3才有，但是Kivy安裝不起來
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import matplotlib.pyplot as plt

plt.plot([1, 23, 2, 4])
plt.ylabel('some numbers')

class MyApp(App):

    def build(self):
        box = BoxLayout()
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        return box

MyApp().run()