import java.util.*;

class LRUCache {
    private final int capacity;
    private final LinkedHashMap<Integer, Object> cache;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new LinkedHashMap<Integer, Object>(capacity, 0.75f, true) {
            @Override
            protected boolean removeEldestEntry(Map.Entry<Integer, Object> eldest) {
                return size() > LRUCache.this.capacity;
            }
        };
    }

    public void query(int key) {
        if (cache.containsKey(key)) {
            cache.get(key);
        }
    }

    public void insert(int key) {
        cache.put(key, null);
    }

    public void delete(int key) {
        cache.remove(key);
    }

    public List<Integer> getCacheKeys() {
        List<Integer> keys = new ArrayList<>(cache.keySet());
        Collections.sort(keys);
        return keys;
    }
}

public class Main {
    public static List<Integer> lruCacheOperations(int capacity, List<String> operations) {
        LRUCache lruCache = new LRUCache(capacity);
        for (String op : operations) {
            String[] parts = op.split(" ");
            String action = parts[0];
            int key = Integer.parseInt(parts[1]);
            switch (action) {
                case "Q":
                    lruCache.query(key);
                    break;
                case "A":
                    lruCache.insert(key);
                    break;
                case "D":
                    lruCache.delete(key);
                    break;
            }
        }
        return lruCache.getCacheKeys();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int c = scanner.nextInt();
        int m = scanner.nextInt();
        scanner.nextLine(); // Consume newline character

        List<String> operations = new ArrayList<>();
        for (int i = 0; i < m; ++i) {
            operations.add(scanner.nextLine());
        }

        List<Integer> result = lruCacheOperations(c, operations);
        ;
        for (int i = 0; i < result.size(); ++i) {
            if (i > 0)
                System.out.print(" ");
            System.out.print(result.get(i));
        }
        System.out.println();
    }
}
