import java.util.Scanner;
public class c
{
   public static void main(String args[])
   {
    Scanner sc =new Scanner(System.in);
    int t=sc.nextInt();
    int s=sc.nextInt();
    int b=sc.nextInt();
    int l=(2*t*s*b*512)/1024;
    System.out.println(l+" KB");
   }
}