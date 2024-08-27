import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<String>> solveNQueens(int n) {
        //return a 2d array of strings
        List<List<String>> result = new ArrayList<>();
        //create a board
        String[][] board = new String[n][n];
        //fill the board with '.'
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                board[i][j]=".";
            }
        }
        //call the recursive function
        solveNQueensHelper(board, 0, result);
        //return the result
        return result;
    }

    private void solveNQueensHelper(String[][] board, int i, List<List<String>> result) {
        //base case
        if(i == board.length){
            //add the board to the result
            result.add(construct(board));
            return;
        }
        //recursive case
        //iterate through the board
        for(int j = 0; j < board.length; j++){
            //check if the position is valid
            if(isValid(board, i, j)){
                //place the queen
                board[i][j] = "Q";
                //call the recursive function
                solveNQueensHelper(board, i+1, result);
                //remove the queen
                board[i][j] = ".";
            }
        }
    }

    private boolean isValid(String[][] board, int i, int j) {
        //check the column
        for(int k = 0; k < i; k++){
            if(board[k][j].equals("Q")){
                return false;
            }
        }
        //check the diagonal
        int k = i-1;
        int l = j-1;
        while(k >= 0 && l >= 0){
            if(board[k][l].equals("Q")){
                return false;
            }
            k--;
            l--;
        }
        //check the diagonal
        k = i-1;
        l = j+1;
        while(k >= 0 && l < board.length){
            if(board[k][l].equals("Q")){
                return false;
            }
            k--;
            l++;
        }
        //return true
        return true;
    }

    private List<String> construct(String[][] board) {
        //create a list of strings
        List<String> list = new ArrayList<>();
        //iterate through the board
        for(int i = 0; i < board.length; i++){
            //create a string
            String s = "";
            //iterate through the board
            for(int j = 0; j < board.length; j++){
                //add the board to the string
                s += board[i][j];
            }
            //add the string to the list
            list.add(s);
        }
        //return the list
        return list;
    }
}