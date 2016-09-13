/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Chapter1Q2;

/**
 *
 * @author Chia
 */
public class reverseString {

    public reverseString() {

    }

    public static String reverse(String word, boolean recursion) {
        if (word == null) {
            return null;
        }
        if (word.equals("")) {
            return "";
        }
        if (recursion) {
            if (word.equals("")) {
                return "";
            }
            else {
                return word.charAt(word.length()-1) + reverse(word.substring(0, word.length()-1), true);
            }

        } else {
            StringBuilder sb = new StringBuilder();
            for (int character = word.length() - 1; character >= 0; character--) {
                sb.append(word.charAt(character));
            }
            return sb.toString();
        }
    }

    public static void main(String[] args) {
        System.out.println(reverse("pokemon", false));
        System.out.println(reverse("creator", true));
    }
}
