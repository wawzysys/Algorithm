import java.util.ArrayList;
import java.util.List;

public class IPLocator {

    // 定义IP区间类
    static class IPRange {
        long start;      // 起始IP（整数表示）
        long end;        // 结束IP（整数表示）
        String region;   // 地区名

        public IPRange(String startIP, String endIP, String region) {
            this.start = ipToLong(startIP);
            this.end = ipToLong(endIP);
            this.region = region;
        }
    }

    // 将IP地址转换为长整数
    public static long ipToLong(String ip) {
        String[] parts = ip.split("\\.");
        long res = 0;
        for (int i = 0; i < 4; i++) {
            res = (res << 8) + Long.parseLong(parts[i]);
        }
        return res;
    }
    
    // 自定义归并排序算法
    // 自行实现了采用归并排序来对IP区间进行排序
    public static void sort(List<IPRange> list, int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;
            sort(list, left, mid);
            sort(list, mid + 1, right);
            merge(list, left, mid, right);
        }
    }

    // 合并两个已排序的子数组
    // 对所有的 IPRange 对象按照 start（起始IP）进行排序，
    // 确保IP区间按起始IP递增顺序排列。这对于后续的二分查找非常重要。
    //mergeSort 方法：

    // 递归地将列表分割为左右两部分，直到每个子列表只有一个元素。
    // 递归结束后，调用 merge 方法将两个有序的子列表合并成一个有序的列表。
    // merge 方法：

    // 负责将两个已排序的子列表（leftList 和 rightList）合并回原列表 list 中。
    // 通过比较两个子列表的起始IP，将较小的IP地址放入合并后的列表中。
    public static void merge(List<IPRange> list, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        // 创建临时数组
        List<IPRange> leftList = new ArrayList<>();
        List<IPRange> rightList = new ArrayList<>();

        for (int i = 0; i < n1; i++) {
            leftList.add(list.get(left + i));
        }
        for (int j = 0; j < n2; j++) {
            rightList.add(list.get(mid + 1 + j));
        }

        // 合并临时数组回原列表
        int i = 0, j = 0;
        int k = left;
        while (i < n1 && j < n2) {
            if (leftList.get(i).start <= rightList.get(j).start) {
                list.set(k, leftList.get(i));
                i++;
            } else {
                list.set(k, rightList.get(j));
                j++;
            }
            k++;
        }

        // 复制剩余元素
        while (i < n1) {
            list.set(k, leftList.get(i));
            i++;
            k++;
        }
        while (j < n2) {
            list.set(k, rightList.get(j));
            j++;
            k++;
        }
    }

    // 查询IP对应的地区
    public static String findRegion(List<IPRange> ipRanges, String ip) {
        long ipLong = ipToLong(ip);
        int left = 0;
        int right = ipRanges.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            IPRange range = ipRanges.get(mid);
            if (ipLong < range.start) {
                right = mid - 1;
            } else if (ipLong > range.end) {
                left = mid + 1;
            } else {
                return range.region;
            }
        }
        return ""; // 不存在
    }

    public static void main(String[] args) {
        // 初始化IP区间列表
        List<IPRange> ipRanges = new ArrayList<>();
        ipRanges.add(new IPRange("180.160.198.0", "186.175.24.28", "上海"));
        ipRanges.add(new IPRange("101.80.40.0", "107.95.210.2", "上海"));
        ipRanges.add(new IPRange("110.240.0.0", "110.255.255.255", "河北"));
        ipRanges.add(new IPRange("14.104.89.100", "50.111.210.1", "重庆"));
        // ... 添加其他约100万条数据

        // 自定义归并排序对IP区间按起始IP排序
        sort(ipRanges, 0, ipRanges.size() - 1);

        // 测试查询
        String[] testIPs = {"181.1.1.1", "101.79.255.255", "110.250.100.100", "14.104.89.100"};
        for (String testIP : testIPs) {
            String region = findRegion(ipRanges, testIP);
            System.out.println("IP " + testIP + " 对应的地区: " + (region.isEmpty() ? "不存在" : region));
        }
    }
}
