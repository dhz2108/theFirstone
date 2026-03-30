import flet as ft

def main(page: ft.Page):
    page.title = "Meine erste App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    text = ft.Text("Hallo von Python!", size=30)
    text_a=ft.Text("Du Hast mich gedrückt",size=50)
    def button_click(e):
        page.add(ft.Text("Button gedrückt!"))

    page.add(
        ft.Row([text], alignment=ft.MainAxisAlignment.CENTER),
        ft.Button("Klick mich", on_click=button_click)
    )
 

#ft.run(target=main)
ft.run(main)
