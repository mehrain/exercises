public class Variables {
    public static void main(String[] args) {
        int passengers = 5;
        int busTickets = passengers;
        System.out.println(passengers);
        System.out.println(busTickets);

        passengers = passengers + 10;

        System.out.println(passengers);

        String annoucement = "There are " + passengers + " passengers on the bus.";
        System.out.println(annoucement);

        char grade = 'A';
        System.out.println(grade);  
    }
}