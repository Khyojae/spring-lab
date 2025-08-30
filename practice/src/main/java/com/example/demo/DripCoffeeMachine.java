package com.example.demo;

import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Component;

@Component("dripCoffeeMachine")

public class DripCoffeeMachine implements com.example.demo.CoffeeMachine {
    @Override
    public String brew(){
        return "Brewing coffee with Drip coffee Machine";
    }
}
