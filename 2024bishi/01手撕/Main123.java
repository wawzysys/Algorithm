public class Main {
    public static void main(String[] args) {
        int[] data = { 1, 1, 2, 3, 1, 4, 4, 4, 5 };
        for (int i = 0; i < data.length; i++) {
            System.out.print(data[i]);
            if (i != data.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println(" ");
        int n = data.length;
        if (n == 0) {
            return;
        }
        int writeIndex = 1;
        for (int readIndex = 1; readIndex < n; readIndex++) {
            if (data[readIndex] != data[writeIndex - 1]) {
                data[writeIndex] = data[readIndex];
                writeIndex++;
            }
        }
        System.out.println(writeIndex);
        for (int i = 0; i < data.length; i++) {
            System.out.print(data[i]);
            if (i != data.length - 1) {
                System.out.print(", ");
            }
        }

    }
}
