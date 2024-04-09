package com.ciencias3.services;

import java.io.IOException;
import java.util.logging.FileHandler;
import java.util.logging.Formatter;
import java.util.logging.LogRecord;
import java.util.logging.Logger;

public class LoggerService {
    private LoggerService(){}

    public static Logger getLogger(String className){
        try {
            FileHandler fileHandler = new FileHandler("analizadorlexicografico/src/main/resources/app.log");
            fileHandler.setFormatter(new Formatter() {
                @Override
                public String format(LogRecord msg) {
                    return msg.getMessage();
                }
            });
            Logger log = Logger.getLogger(className);
            log.addHandler(fileHandler);
            return log;
        } catch (IOException e) {
            e.printStackTrace();
            return Logger.getLogger(className);
        }
    }
}
