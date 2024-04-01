import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class LexicalAnalyzer {

    // Define token types
    private static final Map<String, String> tokenTypes = new HashMap<>();
    static {
        tokenTypes.put("if", "IF");
        tokenTypes.put("else", "ELSE");
        tokenTypes.put("(", "LPAREN");
        tokenTypes.put(")", "RPAREN");
        tokenTypes.put("<=", "LEQ");
        tokenTypes.put("=", "ASSIGN");
        tokenTypes.put("*", "MUL");
        tokenTypes.put("+", "ADD");
        tokenTypes.put(";", "SEMICOLON");
        // Add more token types as needed
    }

    public static void main(String[] args) {
        String inputFile = "./input.txt";
        String outputFile = "output.txt";
        analyzeLexemes(inputFile, outputFile);
    }

    public static void analyzeLexemes(String inputFile, String outputFile) {
        try (BufferedReader reader = new BufferedReader(new FileReader(inputFile));
             BufferedWriter writer = new BufferedWriter(new FileWriter(outputFile))) {
            String line;
            while ((line = reader.readLine()) != null) {
                line = line.trim();
                if (!line.isEmpty()) {
                    String[] tokens = line.split("\\s+|(?<=<=)|(?=<=)|(?<=\\+)|(?=\\+)|(?<=\\*)|(?=\\*)|(?<=\\()|(?=\\))|(?<=;)|(?=;)|(?<==)");
                    for (String token : tokens) {
                        if (tokenTypes.containsKey(token)) {
                            writer.write("<" + tokenTypes.get(token) + "," + token + ">");
                        } else if (token.matches("[a-zA-Z][a-zA-Z0-9]*")) {
                            writer.write("<ID," + token + ">");
                        } else if (token.matches("\\d+")) {
                            writer.write("<NUM," + token + ">");
                        }
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
