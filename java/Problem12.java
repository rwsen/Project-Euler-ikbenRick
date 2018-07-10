// Project Euler 12

public class Problem12 {
    public static void main(String [] args) {
        int number = 0;
        int triangle = 0;
        int best = 1; // for reporting purposes

        while(true){
            // calculate next triangle number
            number++;
            triangle += number;
            int count = factors(triangle);
            if(count > best){
                best = count;
                System.out.println("triangle number " + triangle + 
                                   " has " + count + " factors");
            }
            if(count > 500){
                break;
            }
        }
    }

    public static int factors(int number) {
        int i = 1;
        int limit = (int)Math.ceil( Math.sqrt( (double)number ) );
        int count = 0;

        // test neat divisibility for all integers up to the square root of the input number
        while(i < limit){
            if(number % i == 0){
                count += 2;
            }
            i++;
        }

        // edge case: square root is neatly divisible
        if (Math.sqrt( (double)number ) % 1 == 0){
            count++;
        }

        return count;
    }
}