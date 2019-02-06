from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout

Builder.load_string("""
#:import MDLabel kivymd.label.MDLabel


<OverviewComponent>:
    canvas.before:
        Color:
            rgb: root.bg_color
        Rectangle:
            pos: self.pos
            size: self.size
            
    canvas:
        
    
        Color:
            rgb: 1, 0, 0
        # Line:
        #     width: 3
        #     cap: 'none'
        #     circle: (self.center_x, self.center_y, 150, 0, 90, 20)
        Ellipse:
            pos: self.pos
            size: self.size[0], self.size[0]
            angle_start: 0
            angle_end: 90
            
        Color:
            rgb: 0, 1, 0
        # Line:
        #     joint: 'none'
        #     # dash_length: 5
        #     width: 3
        #     cap: 'none'
        #     circle: (self.center_x, self.center_y, 150, 90, 360, 100)
        Ellipse:
            pos: self.pos
            size: self.size[0], self.size[0]
            angle_start: 90
            angle_end: 360
            
        
    MDLabel:
        font_style: 'Caption'
        theme_text_color: 'Custom'
        text_color: root.text_color
        text: root.text
        
        pos_hint: {'center_x': 0.5, 'center_y':0.5}
        size_hint: 1, None
        size: self.texture_size
        halign: 'center'
        markup:True
""")


class OverviewComponent(FloatLayout):
    bg_color = ListProperty()
    text_color = ListProperty()

    text = StringProperty()
    data = ListProperty()

    def __init__(self, **kwargs):
        self.bg_color = kwargs.pop('bg_color', [1, 1, 1, 1])
        self.text_color = kwargs.pop('text_color', [0, 0, 0, 1])
        self.data = kwargs.pop('data', [0, 0, 0])
        super(OverviewComponent, self).__init__(**kwargs)

    def on_data(self, *args):
        self.text = (f"[b]Carteira[/b]:\t\tR${self.data[0]:10.2f}\n"
                     f"[b]Receitas[/b]:\t\tR${self.data[0]:10.2f}\n"
                     f"[b]Despesas[/b]:\t\tR${self.data[2]:10.2f}\n"
                     f"[b]Total[/b]:\t\tR${(self.data[0]+self.data[1] -self.data[2]):10.2f}")
