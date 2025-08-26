package com.example.demo.domain;

import jakarta.persistence.*;

@Entity // 엔티티 크래스임을 선언
@Table(name = "users")
public class User {

    @Id  //pk 선언
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String username;

    @Column(nullable = false)
    private String password;


}
