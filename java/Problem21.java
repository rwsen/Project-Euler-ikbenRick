// Project Euler 21

public class Problem21 {
    public static void main(String [] args) {
        // Evaluate the sum of all the amicable numbers under 10000
        int sum = 0;
        for(int i = 2; i < 10000; i++){
            if (amicable(i)){
                sum += i;   
                /* this calculates all pairs under 10000 twice, but it is not guaranteed that
                   both numbers of a pair are below 10000: we only count the numbers that are
                */
            }
        }
        System.out.println(sum);
    }

    public static boolean amicable(int number){
        int sumOfDivisors = summedDivisors(number);
        if(number == sumOfDivisors){
            return false;
        }
        int other = summedDivisors(sumOfDivisors);
        if(number == other){
            System.out.println("number: " + number + " \tsum: " + sumOfDivisors + " \tother: " + other);
        }
        return number == other;
    }

    public static int summedDivisors(int number) {
        // edge case: a number is not it's own divisor, thus dividing by 1 is skipped
        if (number == 1){
            return 1;
        }

        int i = 2;  // skip 1, since it always divides with the number
        int limit = (int)Math.ceil( Math.sqrt( (double)number ) );
        int sum = 1;

        // test neat divisibility for all integers up to the square root of the input number
        while(i < limit){
            if(number % i == 0){
                //System.out.print(i + "+");
                sum += i;
                //System.out.print(number/i + "+");
                sum += number / i;
            }
            i++;
        }

        // edge case: square root is a neat divisor
        if(Math.sqrt(number) % 1 == 0){
            //System.out.print( Math.sqrt(number) + "+");
            sum += Math.sqrt(number);
        }
        //System.out.print("= ");

        return sum;
    }
}