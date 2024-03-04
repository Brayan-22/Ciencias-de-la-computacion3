import flet as ft
class vista:


    def __init__(self) -> None:
        # self.text = ft.TextField(width=200,height=200,multiline=True)
        # self.table = ft.DataTable(columns=[ft.Text("1"),ft.Text("2")])
        #Botones : 
        self.btn_dec_asig = ft.ElevatedButton(text="Declaración y asignación",width=250,on_click=self.hola)
        self.btn_io= ft.ElevatedButton("IO",width=250)
        self.btn_lexico = ft.ElevatedButton("Analisis Lexico",width=250)
        self.btn_borrar = ft.ElevatedButton("Borrar",width=250)
        self.btn_archivo = ft.ElevatedButton("Cargar archivo",width=250)


        #TextAreas
        self.text_input = ft.TextField(multiline=True,width="100%",height="100%",content_padding=10,label="Input",text_size=12)
        self.text_output = ft.TextField(multiline=True,width="100%",height="100%",content_padding=10,label="Analisis Lexico")

        #Contenedores
        self.c_buttons = ft.Container(
            content= ft.Row(
                [
                    self.btn_dec_asig,
                    self.btn_io,
                    self.btn_lexico,
                    self.btn_borrar,
                    self.btn_archivo
                ],
                scroll=True,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            ),alignment=ft.alignment.center
        )
        self.c_text_input = ft.Container(
            content= ft.Column(
                [
                    self.text_input,
                ],
                scroll=ft.ScrollMode.ALWAYS
            ),
            width=450,
            height=600,
            margin=5,
            padding=5
        )
        self.c_text_output=ft.Container(
            content=self.text_output,
            width=450,
            height=600,
            margin=5,
            padding=5
        )
        ft.app(self.main)

    
    def main(self,page:ft.Page) -> None:
        page.window_resizable = False
        page.window_height = 700
        page.window_width = 1500
        page.add(self.c_buttons)
        page.add(
            ft.Row(
                [
                self.c_text_input,
                self.c_text_output
                ]
            )
        )
        page.title = "Analizador lexico"
        page.update()
    
    #funciones de eventos
    def hola(self,e)->None:
        print("hola")