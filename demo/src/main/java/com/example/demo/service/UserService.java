package com.example.demo.service;

import com.example.demo.repository.UserRepository;
import org.springframework.stereotype.Service;

@Service
public class UserService {
    private final UserRepository userRepository;

    public UserRepository(UserRepository userRepository){
        this.userRepository = userRepository;
    }
}
