import java.util.Scanner; 
class S{
    public static void main (String[] Args) { 
        Scanner sc = new Scanner (System.in);
        int n = sc.nextInt();
        int ans = 2; 
        for (int i = 2; i<= Math.sqrt(n);i++) {
            if (n % i == 0) ans += 2; 
        }
        if ((int)Math.sqrt(n) == Math.sqrt(n)) ans--;
        System.out.print(ans);
                sc.close();

    }
    
}
