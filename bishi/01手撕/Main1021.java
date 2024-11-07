import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;

public class Main1021 {
    private static final int MAX_NUM = 100;
    private static final int NUM_THREADS = 5;
    private static final AtomicInteger number = new AtomicInteger(1);

    public static void main(String[] args) {
        // 创建固定大小的线程池
        ExecutorService executor = Executors.newFixedThreadPool(NUM_THREADS);

        // 提交5个任务到线程池
        for (int i = 0; i < NUM_THREADS; i++) {
            executor.submit(() -> {
                while (number.get() <= MAX_NUM) {
                    int currentNumber = number.getAndIncrement();
                    if (currentNumber <= MAX_NUM) {
                        System.out.println("Thread " + Thread.currentThread().getName() + " printed: " + currentNumber);
                    }
                }
            });
        }

        // 关闭执行器，不再接受新任务，等待已提交任务执行完毕
        executor.shutdown();
    }
}
