import java.util.Scanner;
public class RobberLanguage {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Skriv ordet som ska bli rövar språk: ");

        String input = scanner.nextLine();
        String consonants = "bcdfghjklmnpqrstvwxz";
        StringBuilder translated = new StringBuilder();

        for (int i = 0; i < input.length(); i++) {
            char currentChar = input.charAt(i);
            String currentCharLower = String.valueOf(currentChar).toLowerCase();

            if (consonants.contains(currentCharLower)) {
                translated.append(currentChar);
                if (Character.isUpperCase(currentChar)) {
                    translated.append('o');
                } else {
                    translated.append('o');
                }
                translated.append(currentCharLower);
            } else {
                translated.append(currentChar);
            }
        }

        System.out.println("Rövarspråk " + translated.toString());

        scanner.close();
    }
}
