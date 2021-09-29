from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout


class Wid(App):
  def build(self):
    box = BoxLayout()
    def haga(instancia, valor):
      print("Asi se oprime el boton")

    la = Label(text = "Esto es Kivy", font_size=50)
    bt = Button(text = "Esto es un boton")
    bt.bind(state = haga)
    sl = Slider(orientation="horizontal",min = -5, max =5, value_track="True", value_track_color = (1,1,0,1))
    box.add_widget(la)
    box.add_widget(bt)
    box.add_widget(sl)
    
    
    return box

if __name__ == "__main__":
  Wid().run()