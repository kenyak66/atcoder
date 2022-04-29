import java.util.Scanner;

class a {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        String S = sc.next();
        if (S.charAt(N - 1) == 'o')
            System.out.println("Yes");
        else
            System.out.println("No");
        sc.close();
    }
}