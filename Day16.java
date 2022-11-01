package day2;

import java.util.Scanner;

public class Day16 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String S = in.next();
        int start = in.nextInt();
        int end = in.nextInt();
        String sub = S.substring(start, end);
        System.out.println(sub);

    }
}
