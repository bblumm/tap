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

    async def score_up(event: ft.ContainerTapEvent) -> None:
        score.data += 1
        score.value = str(score.data)

        image.scale = 0.95

        progress_bar.value += (1 / 100)
        if score.data % 100 == 0:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value="+100",
                    size=20,
                    color="#ff8b1f",
                    text_align=ft.TextAlign.CENTER
                ),
                bgcolor="#25223a"
            )
            page.snack_bar.open = True 
            progress_bar.value = 0
        page.add(score, image, score_counter, progress_bar)

        await asyncio.sleep(0.1)
        image.scale = 1
        score_counter.opacity = 0
        page.add(image, score_counter)
        page.update()

    def open_other_file(event: ft.ContainerTapEvent) -> None:
        subprocess.Popen(["python", "C:/Users/HONOR/Desktop/mandarinclicer/ИСПЫТАНИЕ2.py"])

    score = ft.Text(value="0", size=100, data=0)
    score_counter = ft.Text(
        size=50,
        animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN)
    )

    image = ft.Image(
        src='surok.png',
        fit=ft.ImageFit.CONTAIN,
        animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE)
    )

    page.title = "Basic elevated buttons"
    page.add(
        ft.CupertinoFilledButton(text="CONNECT WALLETS"),
        ft.CupertinoFilledButton(text="friends", on_click=open_other_file),
    )

    progress_bar = ft.ProgressBar(
        value=0,
        width=page.width - 100,
        bar_height=20,
        color="#E0FFFF",
        bgcolor="#00FFFF"
    )

    page.add(
        score,
        ft.Container(
            content=ft.Stack(controls=[image, score_counter]),
            on_click=score_up,
            margin=ft.Margin(0, 0, 0, 30)
        ),
        ft.Container(
            content=progress_bar,
            border_radius=ft.BorderRadius(10, 10, 10, 18)
        ),
         ft.Text(value="МЕНЮ", size=20),
                       
    )

if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER)