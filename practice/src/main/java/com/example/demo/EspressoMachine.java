package com.example.demo;

import org.springframework.stereotype.Component;

@Component
public class EspressoMachine implements com.example.demo.CoffeeMachine {
    @Override
   public String brew(){
       return "Brewing coffee with Espresso Machine";
   }
}