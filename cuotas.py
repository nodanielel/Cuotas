import flet as ft

def main(page: ft.Page):
    page.title = "Quote Translator"
    page.theme_mode = ft.ThemeMode.LIGHT

    quotes = {"original": "Un gran poder conlleva una gran responsabilidad","english": "With great power comes great responsibility","criollo haitiano": "Avèk gwo pouvwa vini gwo responsablite"}

    quoteText = ft.Text(value=quotes["original"],text_align=ft.TextAlign.CENTER)

    def changeLanguage(e):
        if radioGroup.value == "original":
            quoteText.value = quotes["original"]
        elif radioGroup.value == "english":
            quoteText.value = quotes["english"]
        elif radioGroup.value == "criollo haitiano":
            quoteText.value = quotes["criollo haitiano"]

        page.update()

    radioGroup = ft.RadioGroup(value="original",on_change=changeLanguage,content=ft.Column([ft.Radio(value="original", label="Original"),ft.Radio(value="english", label="English"),ft.Radio(value="criollo haitiano", label="Criollo Haitiano"),]))

    image = ft.Image(src="https://upload.wikimedia.org/wikipedia/en/f/f3/Spider-Man2002Poster.jpg",width=200,height=300)
    page.add(ft.Column([ft.Text("Quote Translator"),image,quoteText,radioGroup],horizontal_alignment=ft.CrossAxisAlignment.CENTER))

ft.run(main)