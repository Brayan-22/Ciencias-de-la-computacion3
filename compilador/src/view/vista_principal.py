import flet as ft
import os
import services.lectura_fichero as lf
import services.analizador_lexico.lexico as al

class vista:
    def __init__(self,page:ft.Page) -> None:
        self.page = page
        # self.text = ft.TextField(width=200,height=200,multiline=True)
        # self.table = ft.DataTable(columns=[ft.Text("1"),ft.Text("2")])
        #ventanas emergentes:
        self.pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)
        self.selected_files = ft.Text("hola")
        #Botones : 
        self.btn_dec_asig = ft.ElevatedButton(text="Declaración y asignación",width=250,on_click=self.action_btn_dec_asig)
        self.btn_io= ft.ElevatedButton("IO",width=250,on_click=self.action_btn_io)
        self.btn_lexico = ft.ElevatedButton("Analisis Lexico",width=250,on_click=self.action_analisis_lexico)
        self.btn_borrar = ft.ElevatedButton("Borrar",width=250,on_click=self.action_borrar)
        self.btn_archivo = ft.ElevatedButton("Cargar archivo",width=250,icon=ft.icons.UPLOAD_FILE,on_click=lambda _:self.pick_files_dialog.pick_files(allow_multiple=False))


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
        self.page.overlay.append(self.pick_files_dialog)
        self.page.add(self.selected_files)
        self.page.update()

    #funciones de eventos ----------------------------------------------------------
    def pick_files_result(self,e: ft.FilePickerResultEvent):
        nuevo_archivo = ("".join(map(lambda f: f.path,e.files)) if e.files else "No hay archivo")
        self.action_carga_archivo(nuevo_archivo)
    
    def action_btn_dec_asig(self,e)->None:
        res = lf.leer_fichero("src/resources/prueba.java")
        self.text_input.value = res
        self.page.update()
        
    def action_btn_io(self,e)->None:
        res = lf.leer_fichero("src/resources/prueba2.java")
        self.text_input.value = res
        self.page.update()
        print("IO")

    def action_analisis_lexico(self,e)->None:
        print("analisis lexico")
        self.text_output.value = al.analizador_lexico(self.text_input.value)
        self.page.update()
    
    def action_borrar(self,e)->None:
        self.text_input.value = ""
        self.text_output.value = ""
        self.page.update()
        print("borrar")

    def action_carga_archivo(self,path:str)->None:
        print("carga archivo")
        self.text_input.value = lf.leer_fichero(path)
        self.page.update()
    #fin fucniones de eventos ------------------------------------------------------------

        