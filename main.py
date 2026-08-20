from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class TodoApp(App):
    def build(self):
        # Layout Utama (Vertikal)
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Form Input + Tombol Tambah (Horizontal)
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=5)
        self.task_input = TextInput(hint_text='Ketik tugas baru...', multiline=False)
        add_button = Button(text='Tambah', size_hint_x=0.3, background_color=(0.2, 0.6, 1, 1))
        add_button.bind(on_press=self.add_task)
        
        input_layout.add_widget(self.task_input)
        input_layout.add_widget(add_button)
        self.main_layout.add_widget(input_layout)

        # Area Daftar Tugas dengan Scroll View
        self.scroll = ScrollView()
        self.task_list = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        self.task_list.bind(minimum_height=self.task_list.setter('height'))
        self.scroll.add_widget(self.task_list)
        
        self.main_layout.add_widget(self.scroll)

        return self.main_layout

    def add_task(self, instance):
        task_text = self.task_input.text.strip()
        if task_text:
            # Layout untuk setiap baris tugas
            task_row = BoxLayout(orientation='horizontal', size_hint_y=None, height=40, spacing=5)
            
            label = Label(text=task_text, halign='left', valign='middle')
            label.bind(size=label.setter('text_size'))
            
            delete_btn = Button(text='Hapus', size_hint_x=0.25, background_color=(1, 0.3, 0.3, 1))
            delete_btn.bind(on_press=lambda btn: self.remove_task(task_row))
            
            task_row.add_widget(label)
            task_row.add_widget(delete_btn)
            
            self.task_list.add_widget(task_row)
            self.task_input.text = ''

    def remove_task(self, task_row):
        self.task_list.remove_widget(task_row)

if __name__ == '__main__':
    TodoApp().run()
