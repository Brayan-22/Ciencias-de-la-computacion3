package com.ciencias3;

import java.io.ObjectInputStream;
import java.util.logging.Logger;

import com.ciencias3.services.ExpresionesRegulares;
import com.ciencias3.services.LoggerService;
import com.ciencias3.services.ReadFile;

/**
 * Hello world!
 *
 */
public class App 
{
    private static final Logger log = LoggerService.getLogger(App.class.getName());
    public static void main( String[] args )
    {
        ReadFile r = new ReadFile();
        log.info(r.readFile("analizadorlexicografico/src/main/resources/prueba.java"));
        r.writeFile("analizadorlexicografico/src/main/resources/file.txt", "HOLA MUNDO");
        r.writeFile("analizadorlexicografico/src/main/resources/file.txt", "HOLA MUNDO");
        ExpresionesRegulares.ejecutar();
    }
}
