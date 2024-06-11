import java.util.*;
class Factorial{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int fact=cal(n);
        System.out.print(fact);
    }
    public static int cal(int n){
        if(n==0){
            return 1;
        }
        else{
            return n*cal(n-1);
        }
    }
}
