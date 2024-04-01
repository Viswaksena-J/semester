import java.util.Scanner;

public class LexicalAnalyzerDFA {
    
    // DFA states
    private static final int STATE_START = 0;
    private static final int STATE_ID = 1;
    private static final int STATE_NUM = 2;
    private static final int STATE_ERROR = -1;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("Enter a lexeme: ");
            String lexeme = scanner.nextLine().trim();
            if (lexeme.isEmpty()) {
                break;
            }
            String token = getToken(lexeme);
            System.out.println("Token: " + token);
        }
        scanner.close();
    }

    public static String getToken(String lexeme) {
        int currentState = STATE_START;
        for (char c : lexeme.toCharArray()) {
            switch (currentState) {
                case STATE_START:
                    if (Character.isLetter(c) || c == '_') {
                        currentState = STATE_ID;
                    } else if (Character.isDigit(c)) {
                        currentState = STATE_NUM;
                    } else {
                        return "Not a valid lexeme";
                    }
                    break;
                case STATE_ID:
                    if (Character.isLetterOrDigit(c) || c == '_') {
                        currentState = STATE_ID;
                    } else {
                        return "Not a valid lexeme";
                    }
                    break;
                case STATE_NUM:
                    if (Character.isDigit(c)) {
                        currentState = STATE_NUM;
                    } else {
                        return "Not a valid lexeme";
                    }
                    break;
                default:
                    return "Not a valid lexeme";
            }
        }

        // Final state check
        switch (currentState) {
            case STATE_ID:
                return "<ID, " + lexeme + ">";
            case STATE_NUM:
                return "<NUM, " + lexeme + ">";
            default:
                return "Not a valid lexeme";
        }
    }
}
