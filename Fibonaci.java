import java.util.*;
class Fibonaci{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int ans=fibo(n);
        System.out.print(ans);
    }
    public static int fibo(int n){
        if(n<=1){
            return 0;
        }
        if(n==2){
            return 1;
        }
        return fibo(n-1)+fibo(n-2);
    }
}
