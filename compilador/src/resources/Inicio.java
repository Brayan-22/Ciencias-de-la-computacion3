public class Inicio {
    public static void main(String[] args) {
        int i = 0;
        while (i<10) {
            i++;
        }
        do {
            i++;
        } while (i<10);
        for (int j = 0; j < 10; j++) {
            System.out.println(j);
        }
        switch (i) {
            case 0:
                //hace algo
                break;
                //hace otro algo
            default:
                break;
        }
    }
}
