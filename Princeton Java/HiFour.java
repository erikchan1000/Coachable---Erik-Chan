public class HiFour {
    public static void main(String [] args) {
        String name1 = args[0];
        String name2 = args[1];
        String name3 = args[2];
        String name4 = args[3];
        String test = String.format("Hi %s, %s, %s, and %s.", name1, name2, name3, name4);

        System.out.println(test);
    }
}