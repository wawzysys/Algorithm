import java.util.*;
import java.io.*;

public class Main {
    static class Driver {
        int index;
        int D;
        int C;
        int L;
        int S;
        int T;

        Driver(int index, int D, int C, int L, int S) {
            this.index = index;
            this.D = D;
            this.C = C;
            this.L = L;
            this.S = S;
            this.T = computeTime();
        }

        private int computeTime() {
            int normalDistance = D - C;
            int normalTime = normalDistance / 10;
            int congestionTime = C / 2;
            int waitTime = (L * 15) / 2;
            return normalTime + congestionTime + waitTime;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line1 = br.readLine().trim();
        String line2 = br.readLine().trim();
        String line3 = br.readLine().trim();
        String line4 = br.readLine().trim();

        int[] D = parseLine(line1);
        int[] C = parseLine(line2);
        int[] L = parseLine(line3);
        int[] S = parseLine(line4);

        int N = D.length;
        List<Driver> drivers = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            drivers.add(new Driver(i + 1, D[i], C[i], L[i], S[i]));
        }
        Driver selected = getMinTimeDriver(drivers);

        while (true) {
            boolean found = false;
            Driver current = selected;
            Driver bestHigher = null;
            for (Driver d : drivers) {
                if (d.S > current.S && d.T <= current.T + 60) {
                    if (bestHigher == null) {
                        bestHigher = d;
                    } else {
                        if (d.S > bestHigher.S) {
                            bestHigher = d;
                        } else if (d.S == bestHigher.S && d.T < bestHigher.T) {
                            bestHigher = d;
                        }
                    }
                }
            }
            if (bestHigher != null) {
                selected = bestHigher;
                found = true;
            }
            if (!found) {
                break;
            }
        }
        System.out.println(selected.index + "," + selected.T);
    }

    private static int[] parseLine(String line) {
        String[] parts = line.split("[,.]");
        int[] arr = new int[parts.length];
        for (int i = 0; i < parts.length; i++) {
            arr[i] = Integer.parseInt(parts[i]);
        }
        return arr;
    }

    private static Driver getMinTimeDriver(List<Driver> drivers) {
        Driver minDriver = drivers.get(0);
        for (Driver d : drivers) {
            if (d.T < minDriver.T) {
                minDriver = d;
            } else if (d.T == minDriver.T && d.S > minDriver.S) {
                minDriver = d;
            }
        }
        return minDriver;
    }
}
