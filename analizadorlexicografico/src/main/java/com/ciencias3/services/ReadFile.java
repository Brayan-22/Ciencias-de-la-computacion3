package com.ciencias3.services;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;

public class ReadFile {
    
    public static String readFile(String file) {
        StringBuilder str = new StringBuilder();
        try (FileReader fileReader = new FileReader(file)) {
            int character;
            while (true) {
                character = fileReader.read();
                if (character == -1) break;
                str.append((char)character);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return str.toString();
    }
    public static void writeFile(String nameFile,String text){
        File file = new File(nameFile);
        try {
            PrintWriter printWriter = new PrintWriter(file);
            
            printWriter.print(text);
            printWriter.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
