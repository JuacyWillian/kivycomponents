from kivy.app import App
from kivy.properties import ObjectProperty

from kivymd.theming import ThemeManager

from .screens import SCREENS, SCREEN_TYPE


class KivycomponentsApp(App):
    """Basic kivy app

    Edit kivycomponents.kv to get started.
    """
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'DeepPurple'
    title = "Kivy Components"

    manager = ObjectProperty(None)

    def build(self):
        self.manager = self.root.ids.manager
        return self.root
    
    def on_start(self, ):
        self.goto(SCREEN_TYPE.HOME)

    def goto(self, screenType, **kwargs):
        if isinstance(screenType, SCREEN_TYPE):
            screen = SCREENS[screenType](self, **kwargs)
            self.manager.switch_to(screen)
        else:
            raise(TypeError("'screenType' arg must be instance of 'SCREEN_TYPE'"))
