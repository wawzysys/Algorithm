

public class Main {
    public static void main(String[] args) {
        try{
            int i = 2 / 0;
            System.out.println(i);
        }catch (Exception e){
            System.out.print("a");
            throw new RuntimeException();
        }finally {
            System.out.print("b");
        }
        System.out.print("c");
    }
}
