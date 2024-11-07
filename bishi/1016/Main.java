class Main {
    public static void main(String[] args) {
        int[] arr1 = { 1, 3 };
        int[] arr2 = { 2 };
        Main main = new Main();
        double res = main.findMedianSortedArrays(arr1, arr2);
        System.out.println(res);
    }

    public double findMedianSortedArrays(int[] array1, int[] array2) {
        if (array1.length > array2.length) {
            int[] tmp = array1;
            array1 = array2;
            array2 = tmp;
        }

        int m = array1.length;
        int n = array2.length;
        int[] a = new int[m + 2];
        int[] b = new int[n + 2];
        a[0] = b[0] = Integer.MIN_VALUE;
        a[m + 1] = b[n + 1] = Integer.MAX_VALUE;
        System.arraycopy(array1, 0, a, 1, m);
        System.arraycopy(array2, 0, b, 1, n);
        int l = 0;
        int r = m + 1;
        while (l + 1 < r) {
            int i = (l + r) / 2;
            int j = (m + n + 1) / 2 - i;
            if (a[i] <= b[j + 1]) {
                l = i;
            } else {
                r = i;
            }
        }

        int i = l;
        int j = (m + n + 1) / 2 - i;
        int max1 = Math.max(a[i], b[j]);
        int min2 = Math.min(a[i + 1], b[j + 1]);
        return (m + n) % 2 > 0 ? max1 : (max1 + min2) / 2.0;
    }
}
