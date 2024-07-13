import asyncio
import flet as ft
import subprocess

def main(page: ft.Page) -> None:
    page.title = "Hello $Meow"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#4197e4"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {"SALongBeach": "fonts/SALongBeach.ttf"}
    page.theme = ft.Theme(font_family="SALongBeach")
    
    def open_other_file(event: ft.ContainerTapEvent) -> None:
        subprocess.Popen(["python", "C:/Users/HONOR/Desktop/mandarinclicer/АААА.py"])

   

    page.add(
         ft.Text(value="ты пока не пригласил ни одного друга :(", size=30),
    )
    page.title = "Basic elevated buttons"
    page.add(
        ft.CupertinoFilledButton(text="next", on_click=open_other_file),
    )
if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER)  