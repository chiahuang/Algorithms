/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Chapter1Q1;

import java.util.ArrayList;

/**
 *
 * @author Chia
 */
public class UniqueString {

    public UniqueString() {

    }

    public static boolean isUnique(String word) {
        if (word == null) {
            return false;
        }
        if (word.equals("") || word.length() > 128) {
            return false;
        }
        ArrayList<Boolean> ascii = new ArrayList<Boolean>();
        for (int i = 0; i < 128; i++) {
            ascii.add(Boolean.FALSE);
        }
        for (int character = 0; character < word.length(); character++) {
            int asciiValue = (int) word.charAt(character);
            if (ascii.get(asciiValue)) {
                return false;
            }
            ascii.set(asciiValue, Boolean.TRUE);
        }
        return true;
    }

    public static boolean isUnique2(String word) {
        if (word == null) {
            return false;
        }
        if (word.length() > 128 || word.equals("")) {
            return false;
        }
        int checker = 0;
        for (int i = 0; i < word.length(); i++) {
            int value = word.charAt(i) - 'a';
            System.out.println(word.charAt(i));
            System.out.println(checker & (1 << value));
//            System.out.println("val: " + value + " " + word.charAt(i));
//            System.out.println(checker & (1 << value));
            if ((checker & (1 << value)) > 0) {
                return false;
            }
//            System.out.println("checker: " + checker);
            checker |= (1 << value);
//            System.out.println("checker after: " + checker);
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(isUnique("Unique"));
    }

}
