/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Chapter1Q5;

/**
 *
 * @author Chia
 */
public class Compression {
    public Compression() {
        
    }
    
    public static String compress(String word) {
        if(word == null) {
            return "";
        }
        if(word.equals("")) {
            return "";
        }
        String result = "";
        char currentChar = ' ';
        int count = 0;
        for(int character = 0; character < word.length(); character++) {
            if (currentChar == ' ') {
                currentChar = word.charAt(character);
                count++;
            }
            else if(currentChar == word.charAt(character)) {
                count++;
            } 
            else {
                result += currentChar;
                result += count;
                currentChar = word.charAt(character);
                count = 1;
            }
        }
        result += currentChar;
        result += count;
        return result;
    }
    
    public static void main(String[] args) {
         System.out.println(compress("aaaabbbccceee"));
    }
}
