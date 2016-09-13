/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Chapter1Q4;

/**
 *
 * @author Chia
 */
public class ReplaceString {
    public ReplaceString() {
        
    }
    
    public static String replace(String word) {
        if (word == null) {
            return "";
        }
        
        if (word.equals("")) {
            return "";
        }
        String result = "";
        for(int string = 0; string < word.length(); string++) {
            if(word.charAt(string) == ' ') {
                result += "%20";
            }
            else {
                result += word.charAt(string);
            }
        }
        return result;
    }
    
    public static void main(String[] args) {
        System.out.println(replace("School will begin next week!"));
        System.out.println(replace(null));
        System.out.println(replace("Algorithms is fun!"));
        System.out.println(replace(""));
    }
}
