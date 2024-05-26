import flet as ft
import services.lectura_fichero as lf
import json
# import services.analizador_lexico.lexico as al
from services.myAnalizador.MyLexer import MyLexer
from services.myAnalizador.MyParser import MyParser
from services.myAnalizador.MyParser import visitor
class vista:##### if switch doWhile while for inicio 
    def __init__(self,page:ft.Page) -> None:
        self.tamButtons = 130
        self.page = page
        # self.text = ft.TextField(width=200,height=200,multiline=True)
        # self.table = ft.DataTable(columns=[ft.Text("1"),ft.Text("2")])
        #ventanas emergentes:
        self.input = ""
        self.pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)
        self.selected_files = ft.Text("")
        #Botones : 
        self.btn_dec_asig = ft.ElevatedButton(text="Declaración y asignación",width=self.tamButtons,on_click=self.action_btn_dec_asig)
        self.btn_io= ft.ElevatedButton("IO",width=self.tamButtons,on_click=self.action_btn_io)
        self.btn_borrar = ft.ElevatedButton("Borrar",width=self.tamButtons,on_click=self.action_borrar)
        self.btn_archivo = ft.ElevatedButton("Cargar archivo",width=self.tamButtons,icon=ft.icons.UPLOAD_FILE,on_click=lambda _:self.pick_files_dialog.pick_files(allow_multiple=False))
        self.btn_if = ft.ElevatedButton("If",width=self.tamButtons,on_click=self.action_btn_if)
        self.btn_switch = ft.ElevatedButton("Switch",width=self.tamButtons,on_click=self.action_btn_switch)
        self.btn_dowhile = ft.ElevatedButton("doWhile",width=self.tamButtons,on_click=self.action_btn_dowhile)
        self.btn_while = ft.ElevatedButton("while",width=self.tamButtons,on_click=self.action_btn_while)
        self.btn_for = ft.ElevatedButton("For",width=self.tamButtons,on_click=self.action_btn_for)
        self.btn_inicio = ft.ElevatedButton("Inicio",width=self.tamButtons,on_click=self.action_btn_inicio)
        self.btn_lexico = ft.ElevatedButton("Analisis Lexico",width=self.tamButtons,on_click=self.action_analisis_lexico)
        self.btn_sintax = ft.ElevatedButton("Analisis Sintactico",width=self.tamButtons,on_click=self.action_analisis_sintax)
        #TextAreas
        self.text_input = ft.TextField(multiline=True,width="100%",height="100%",content_padding=10,label="Input",text_size=12)
        self.text_output = ft.TextField(multiline=True,width="100%",height="100%",content_padding=10,label="Analisis Lexico")
        self.text_output2 = ft.TextField(multiline=True,width="100%",height="100%",content_padding=10,label="Analisis sintactico")
        self.titulo_tabla = ft.Text("Variables de clase", theme_style=ft.TextThemeStyle.TITLE_SMALL,text_align=ft.TextAlign.CENTER);
        self.titulo_tabla2 = ft.Text("Variables locales", theme_style=ft.TextThemeStyle.TITLE_SMALL,text_align=ft.TextAlign.CENTER);

        #Tablas
        
        self.class_var_table = ft.DataTable(        
            columns=[
                ft.DataColumn(ft.Text("Tipo")),
                ft.DataColumn(ft.Text("Identificador")),
                ft.DataColumn(ft.Text("Valor")),
            ],
            rows=[],
        )
        self.local_var_table = ft.DataTable(        
            columns=[
                ft.DataColumn(ft.Text("Tipo")),
                ft.DataColumn(ft.Text("Identificador")),
                ft.DataColumn(ft.Text("Valor")),
            ],
            rows=[],
        )
        #Contenedores
                
        self.c_buttons = ft.Container(
            content= ft.Row(
                [
                    self.btn_dec_asig,
                    self.btn_io,
                    self.btn_if,
                    self.btn_switch,
                    self.btn_dowhile,
                    self.btn_while,
                    self.btn_for,
                    self.btn_inicio,
                    self.btn_lexico,
                    self.btn_sintax,
                    self.btn_borrar,
                    self.btn_archivo,
                ],
                scroll=True,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                height=70
                
            ),alignment=ft.alignment.center,padding=10
        )
        self.c_text_input = ft.Container(
            content= ft.Column(
                [
                    self.text_input,
                ],
                scroll=ft.ScrollMode.ALWAYS
            ),
            width=300,
            height=500,
            margin=5,
            padding=5
        )
        self.c_text_output=ft.Container(
            content=self.text_output,
            width=300,
            height=500,
            margin=5,
            padding=5
        )
        self.c_text_output2 = ft.Container(
            content=self.text_output2,
            width=350,
            height=500,
            margin=5,
            padding=5
        )
        self.c_table2 = ft.Container(
            content= ft.Column(
                [
                    self.titulo_tabla2,
                    self.local_var_table
                ],
                scroll=ft.ScrollMode.ALWAYS
            ),
            width=350,
            height=500,
            margin=5,
            padding=5,
        )
        self.c_table = ft.Container(
             content= ft.Column(
                [
                    self.titulo_tabla,
                    self.class_var_table
                ],
                scroll=ft.ScrollMode.ALWAYS
            ),
            width=350,
            height=500,
            margin=5,
            padding=5,
        )

        self.main()
    
    def main(self) -> None:
        self.page.window_resizable = False
        self.page.window_height = 800
        self.page.window_width = 1800
        self.rows=[]
        self.page.add(self.c_buttons)
        self.page.add(
            ft.Row(
                [
                self.c_text_input,
                self.c_text_output,
                self.c_text_output2,
                self.c_table,
                self.c_table2
                ]
            )
        ) 
        self.page.title = "Analizador Java"
        self.page.overlay.append(self.pick_files_dialog)
        self.page.add(self.selected_files)
        self.page.update()
        
    #funciones de eventos ----------------------------------------------------------
    def pick_files_result(self,e: ft.FilePickerResultEvent):
        nuevo_archivo = ("".join(map(lambda f: f.path,e.files)) if e.files else "No hay archivo")
        self.action_carga_archivo(nuevo_archivo)
    
    def action_btn_dec_asig(self,e)->None:
        self.clear_table_var_class()
        self.clear_table_var_local()
        self.input = "src/resources/input.java"
        res = lf.leer_fichero(self.input)
        self.text_input.value = res
        self.page.update()
        
    def action_btn_io(self,e)->None:
        self.clear_table_var_class()
        self.clear_table_var_local()
        self.input = "src/resources/io.java"
        res = lf.leer_fichero(self.input)
        self.text_input.value = res
        self.page.update()
    def action_btn_switch(self,e)->None:
        self.clear_table_var_class()
        self.clear_table_var_local()
        self.input = "src/resources/Switch.java"
        res = lf.leer_fichero(self.input)
        self.text_input.value = res
        self.page.update()        
    def action_btn_dowhile(self,e)->None:
        self.clear_table_var_class()
        self.clear_table_var_local()
        self.input = "src/resources/DoWhile.java"
        res = lf.leer_fichero(self.input)
        self.text_input.value = res
        self.page.update()   
    def action_btn_while(self,e)->None:
        self.clear_table_var_class()
        self.clear_table_var_local()
        self.input = "src/resources/While.java"
        res = lf.leer_fichero(self.input)
        self.text_input.value = res
        self.page.update()   
    def action_btn_for(self,e)->None:
        self.clear_table_var_class()
        self.clear_table_var_local()
        self.input = "src/resources/For.java"
        res = lf.leer_fichero(self.input)
        self.text_input.value = res
        self.page.update()   
    def action_btn_inicio(self,e)->None:
        self.clear_table_var_class()
        self.clear_table_var_local()
        self.input = "src/resources/Inicio.java"
        res = lf.leer_fichero(self.input)
        self.text_input.value = res
        self.page.update()   
        
    def action_btn_if(self,e)->None:
        self.clear_table_var_class()
        self.clear_table_var_local()
        self.input = "src/resources/If.java"
        res = lf.leer_fichero(self.input)
        self.text_input.value = res
        self.page.update()  
        
    def action_analisis_lexico(self,e)->None:
        nuevo_texto = self.text_input.value
        lf.escritura_fichero(self.input,nuevo_texto)
        self.text_output.value = MyLexer(self.input)
        self.page.update()
        
    def action_analisis_sintax(self,e)->None:
        nuevo_texto = self.text_input.value
        lf.escritura_fichero(self.input,nuevo_texto)
        self.text_output2.value = MyParser(self.input)
        self.add_row_var_class()
        self.add_row_var_local()
        self.page.update()
    
    def action_borrar(self,e)->None:
        self.text_input.value = ""
        self.text_output.value = ""
        self.text_output2.value = ""
        self.clear_table_var_class()
        self.clear_table_var_local()
        self.page.update()

    def action_carga_archivo(self,path:str)->None:
        self.text_input.value = lf.leer_fichero(path)
        self.page.update()
        
    def add_row_var_class(self):
        self.clear_table_var_class()
        for ident in visitor.classVar:
            i = ident
            type = visitor.classVar[ident]['type']
            value = visitor.classVar[ident]['value']
            self.class_var_table.rows.insert(len(self.class_var_table.rows), 
                                   ft.DataRow([ft.DataCell(ft.Text(type)), 
                                               ft.DataCell(ft.Text(i)), 
                                               ft.DataCell(ft.Text(value))
                               ],))   
    def clear_table_var_class(self):
        tam = len(self.class_var_table.rows) -1
        for i in range(tam,-1,-1):
            self.class_var_table.rows.remove(self.class_var_table.rows[i])
        self.page.update()
        
        
        
        
    def add_row_var_local(self):
        self.clear_table_var_local()
        for ident in visitor.localVar:
            i = ident
            type = visitor.localVar[ident]['type']
            value = visitor.localVar[ident]['value']
            self.local_var_table.rows.insert(len(self.local_var_table.rows), 
                                   ft.DataRow([ft.DataCell(ft.Text(type)), 
                                               ft.DataCell(ft.Text(i)), 
                                               ft.DataCell(ft.Text(value))
                               ],))   
    def clear_table_var_local(self):
        tam = len(self.local_var_table.rows) -1
        for i in range(tam,-1,-1):
            self.local_var_table.rows.remove(self.local_var_table.rows[i])
        self.page.update()