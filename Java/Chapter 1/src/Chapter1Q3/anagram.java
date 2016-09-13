/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Chapter1Q3;

import java.util.HashMap;
import java.util.HashSet;

/**
 *
 * @author Chia
 */
public class anagram {
    public anagram() {
        
    }
    
    public static boolean isPermutation(String word, String other) {
        if(word == null || other == null) {
            return false;
        }
        if(word.length() != other.length()) {
            return false;
        }
        
        HashMap hm = new HashMap<String, Integer>();
        for(int character = 0; character < word.length(); character++) {
            if(hm.containsKey(word.charAt(character))) {
                int value = (int) hm.get(word.charAt(character)) + 1;
                hm.put(word.charAt(character), value);
            }
            else {
                hm.put(word.charAt(character), 1);
            }
        }
        for(int letter = 0; letter <  other.length(); letter++) {
            if(hm.containsKey(other.charAt(letter))) {
                if ((int) hm.get(other.charAt(letter)) == 1) {
                    hm.remove(other.charAt(letter));
                }
                else {
                    int value = (int) hm.get(other.charAt(letter)) - 1;
                    hm.put(other.charAt(letter), value);
                }
            }
            else {
                return false;
            }
        }
        return true;
    }
    
    public static void main(String[] args) {
        System.out.println(isPermutation("dog god", "god dog"));
    }
}
