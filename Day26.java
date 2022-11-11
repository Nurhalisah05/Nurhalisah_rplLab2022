/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package day2;

import java.util.Scanner;

/**
 *
 * @author ASUS
 */
public class Day26 {
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        double nilai  = sc.nextDouble();
  
        if (nilai >=80){
            System.out.println("A");
        }else if (nilai >=60){
            System.out.println("B");
        }else if (nilai >=40){
            System.out.println("C");
        }else {
            System.out.println("E");
        }
    }
    
}
