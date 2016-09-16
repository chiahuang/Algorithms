/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Chapter1Q6;

/**
 *
 * @author Chia
 */
public class Matrix {
    public Matrix() {
        
    }
    
    public static int[][] rotate(int row, int column) {
        int[][] matrix = new int[row][column];
        for(int i = 0; i < row; i++) {
            for(int j = 0; j < column; j++) {
                matrix[i][j] = column * i + j + 1;
                System.out.println(matrix[i][j]);
            }
        } 
       
        
        return null;
    }
    
    public static void main(String[] args) {
        System.out.println(rotate(3,3));
    }
}
