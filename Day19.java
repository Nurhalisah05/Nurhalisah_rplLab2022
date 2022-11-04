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
public class Day19 {

    public static void main(String[] args) {
        int nilai1, nilai2, nilai3;
        double hasil;
        System.out.println("MENGHITUNG NILAI-RATA RATA NILAI");
        Scanner DataIn = new Scanner(System.in);
        System.out.print("Nilai Ujian Ke-1 : ");
        nilai1 = DataIn.nextInt();

        System.out.print("Nilai Ujian Ke-2 : ");
        nilai2 = DataIn.nextInt();

        System.out.print("Nilai Ujian Ke-3 : ");
        nilai3 = DataIn.nextInt();

        hasil = (nilai1 + nilai2 + nilai3) / 3;

        System.out.println("Nilai Rata-Rata      : " + hasil);
    }

}
