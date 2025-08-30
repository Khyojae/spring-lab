package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.context.ApplicationContext;
import org.springframework.stereotype.Component;

@Component
public class PiApplication implements ApplicationRunner{
    @Autowired
    private Pi pi;



    @Override
    public void run(ApplicationArguments args) throws Exception {
        System.out.println("PI with 10000 points = " + pi.calculate(10000));
        System.out.println("PI with 10000 points = " + pi.calculate(100000));
        System.out.println("PI with 10000 points = " + pi.calculate(1000000));
        System.out.println("PI with 10000 points = " + pi.calculate(10000000));
        System.out.println("PI with 10000 points = " + pi.calculate(100000000));
    }
}



