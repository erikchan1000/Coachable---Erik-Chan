public class SumThree {
    public static void main(String [] args) {
        System.out.print(args[0] + " + " + args[1] + " + " + args[2] + " = ");
        int res = Integer.parseInt(args[0]) + Integer.parseInt(args[1]) + Integer.parseInt(args[2]);

        System.out.print(res);
    }
}
