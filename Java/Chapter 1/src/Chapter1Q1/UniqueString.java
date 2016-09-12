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
        System.out.println(word);
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
        return false;
    }
    
    

    public static void main(String[] args) {        
        System.out.println(isUnique("Unique"));
        
        System.out.println(isUnique2(""));
    
    }

}
