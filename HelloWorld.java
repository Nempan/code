import javax.swing.JOptionPane;
import java.util.Scanner;

public class HelloWorld {
    public static void main(String[] args){

        System.out.println("Vad heter du?");

        Scanner tgb = new Scanner(System.in);
        String namn;
        namn = tgb.nextLine();

        System.out.println("Hej " + namn + "!");
        
        

        
        
    }
}
