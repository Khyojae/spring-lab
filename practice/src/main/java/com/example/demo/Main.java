package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

@SpringBootApplication
public class Main {

    public static void main(String[] args) {
        // Spring 컨테이너 실행
        ApplicationContext context = SpringApplication.run(Main.class, args);

        // CoffeeMaker 빈 가져오기
        CoffeeMaker coffeeMaker = context.getBean(CoffeeMaker.class);

        // 사용
        coffeeMaker.makeCoffee();
    }
}
