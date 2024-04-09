package com.ciencias3.services;

import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class ExpresionesRegulares {
    static String msg = "el dia de hoy es viernes 2024-03-01";
    static String regex = "[0-9]+";

    public static void ejecutar(){
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(msg);
        while (matcher.find()) {
            String match = matcher.group();
            System.out.println(match);
        }
    }
}
