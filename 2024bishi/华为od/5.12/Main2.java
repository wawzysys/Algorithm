import java.util.Scanner;

public class Main2 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] black = new int[722];
        int bsize = 0;
        String b = sc.nextLine();
        String[] blackTokens = b.split(" ");
        for (String token : blackTokens) {
            black[bsize++] = Integer.parseInt(token);
        }

        int[] white = new int[722];
        int wsize = 0;
        String w = sc.nextLine();
        String[] whiteTokens = w.split(" ");
        for (String token : whiteTokens) {
            white[wsize++] = Integer.parseInt(token);
        }
        int[][] board = new int[19][19];
        for (int i = 0; i < bsize; i += 2) {
            int x = black[i];
            int y = black[i + 1];
            board[x][y] = 1;
        }
        for (int i = 0; i < wsize; i += 2) {
            int x = white[i];
            int y = white[i + 1];
            board[x][y] = 2;
        }

        int bcnt = 0;
        int wcnt = 0;

        int[][] offsets = {
                { -1, 0 },
                { 1, 0 },
                { 0, -1 },
                { 0, 1 }
        };

        for (int i = 0; i < 19; i++) {
            for (int j = 0; j < 19; j++) {

                if (board[i][j] == 0) {
                    boolean isB = false;
                    boolean isW = false;

                    for (int[] offset : offsets) {
                        int newI = i + offset[0];
                        int newJ = j + offset[1];

                        if (newI < 0 || newI >= 19 || newJ < 0 || newJ >= 19) {
                            continue;
                        }

                        if (board[newI][newJ] == 1) {
                            isB = true;
                        }

                        if (board[newI][newJ] == 2) {
                            isW = true;
                        }
                    }
                    if (isB) {
                        bcnt++;
                    }
                    if (isW) {
                        wcnt++;
                    }
                }
            }
        }
        System.out.println(bcnt + " " + wcnt);
    }
}
