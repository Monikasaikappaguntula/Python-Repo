import java.util.Scanner;
public class t
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int x1=sc.nextInt();
        int x2=sc.nextInt();
        int y1=sc.nextInt();
        int y2=sc.nextInt();
        if((x1+x2)<(y1+y2))
        {
            System.out.println(x1+x2);
        }
        else
        System.out.println(y1+y2);
    }
}