import flet as ft
import os
import services.lectura_fichero as lf
class vista:
    def __init__(self,page:ft.Page) -> None:
        self.page = page
        # self.text = ft.TextField(width=200,height=200,multiline=True)
        # self.table = ft.DataTable(columns=[ft.Text("1"),ft.Text("2")])
        #Botones : 
        self.btn_dec_asig = ft.ElevatedButton(text="Declaración y asignación",width=250,on_click=self.action_btn_dec_asig)
        self.btn_io= ft.ElevatedButton("IO",width=250,on_click=self.action_btn_io)
        self.btn_lexico = ft.ElevatedButton("Analisis Lexico",width=250,on_click=self.action_analisis_lexico)
        self.btn_borrar = ft.ElevatedButton("Borrar",width=250,on_click=self.action_borrar)
        self.btn_archivo = ft.ElevatedButton("Cargar archivo",width=250,on_click=self.action_carga_archivo)


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
        self.main()
    
    def main(self) -> None:
        self.page.window_resizable = False
        self.page.window_height = 700
        self.page.window_width = 1500
        self.page.add(self.c_buttons)
        self.page.add(
            ft.Row(
                [
                self.c_text_input,
                self.c_text_output
                ]
            )
        )
        self.page.title = "Analizador lexico"
        self.page.update()
    
    #funciones de eventos ----------------------------------------------------------
        
    def action_btn_dec_asig(self,e)->None:
        res = lf.leer_fichero("src/resources/prueba2.txt")
        self.text_input.value = res
        self.page.update()
    def action_btn_io(self,e)->None:
        print("IO")

    def action_analisis_lexico(self,e)->None:
        print("analisis lexico")
    
    def action_borrar(self,e)->None:
        print("borrar")

    def action_carga_archivo(self,e)->None:
        print("carga archivo")
    #fin fucniones de eventos ------------------------------------------------------------

        