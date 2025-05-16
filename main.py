from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.lang import Builder
from kivymd.uix.behaviors import CommonElevationBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.clock import Clock
from plyer import notification

class Interface(MDBoxLayout):
    milli_secs=0
    seconds =0
    minutes =0
    timer_status = False
    def timer(self, *args):
        Interface.milli_secs+=1
        if Interface.milli_secs ==100:
            Interface.milli_secs=0
            Interface.seconds+=1
            if Interface.seconds==60:
                Interface.minutes+=1
        self.ids.timer_placeholder.text = "{0:0=2d}".format(Interface.minutes)+" : "+"{0:0=2d}".format(Interface.seconds)+" : "+"{0:0=2d}".format(Interface.milli_secs)

    def start_timer(self):
        if Interface.timer_status ==False:
            Interface.timer_status=True
            Clock.schedule_interval(self.timer,1/1000)
            self.ids.icon_placeholder.icon = "timer-pause-outline"
            self.ids.progressbar.start()
        else:
            Clock.unschedule(self.timer)
            Interface.timer_status=False
            Interface.milli_secs=0
            Interface.seconds =0
            Interface.minutes =0
            self.ids.progressbar.stop()
            self.ids.icon_placeholder.icon = "timer-play-outline"
            notification.notify(title="Timer Duration",message =str(self.ids.timer_placeholder.text))

class CustomButton(ButtonBehavior,CommonElevationBehavior,MDAnchorLayout):
    pass

class TimerApp(MDApp):
    def change_theme(self,app_bar):
        if self.theme_cls.theme_style =="Light":
            self.theme_cls.theme_style ="Dark"
            self.theme_cls.primary_palette = "Amber"
            app_bar.right_action_items=[["weather-sunny", lambda x: self.change_theme(app_bar)]]
        else:
            self.theme_cls.primary_palette = "Purple"
            self.theme_cls.theme_style = "Light"

    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Light"

TimerApp().run()
