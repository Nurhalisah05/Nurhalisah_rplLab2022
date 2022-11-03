package day2;

import java.util.Scanner;

public class Day18 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int angka1, angka2, choice, result = 0;
        System.out.println("Program Kalkulator Sederhana");
        System.out.println("1. Penjumlahan");
        System.out.println("2. Pengurangan");
        System.out.println("3. Pembagian");
        System.out.println("4. Perkalian");
        System.out.println("5. Sisa Bagi");
        System.out.println("-----------------------------");

        // input data
        System.out.print("Masukan Angka Pertama: ");
        angka1 = input.nextInt();
        System.out.print("Masukan Angka Kedua: ");
        angka2 = input.nextInt();

        // Pilihan Operasi
        System.out.print("Masukan Operasi: ");
        choice = input.nextInt();

        switch (choice) {
            case 1:
                result = angka1 + angka2;
                break;
            case 2:
                result = angka1 - angka2;
                break;
            case 3:
                result = angka1 / angka2;
                break;
            case 4:
                result = angka1 * angka2;
                break;
            case 5:
                result = angka1 % angka2;
                break;
            default:
                System.out.println("Salah Memasukan Pilihan Harap Baca Pilihan di Menu");
        }
        System.out.println("Hasil: " + result);
    }

}
