BoxLayout:
    orientation: "vertical"
    padding: 20
    spacing: 10

    Label:
        text: app.message
        font_size: 24
        size_hint_y: None
        height: 40

    TextInput:
        id: name_input
        hint_text: "Type a name..."
        multiline: False
        font_size: 20
        size_hint_y: None
        height: 50
        on_text_validate: app.add_name()

    BoxLayout:
        size_hint_y: None
        height: 50
        spacing: 10

        Button:
            text: "Add"
            font_size: 20
            on_press: app.add_name()

        Button:
            text: "Clear"
            font_size: 20
            on_press: app.clear_list()

    Label:
        text: "List:"
        font_size: 22
        size_hint_y: None
        height: 40

    ScrollView:
        GridLayout:
            id: list_box
            cols: 1
            size_hint_y: None
            height: self.minimum_height
            spacing: 10
