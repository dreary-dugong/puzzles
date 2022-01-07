import java.util.Scanner;


public class Speed{
	
	public static void main(String[] args){
		
		Scanner input = new Scanner(System.in);
		
		int numPairs = input.nextInt();
		input.nextLine();
		
		while(numPairs != -1){
			
			int totalDist = 0;
			int lastElapsed = 0;
			
			for(int i = 0; i < numPairs; i++){
				int currSpeed = input.nextInt();
				int currElapsed = input.nextInt();
				input.nextLine();
				
				totalDist += currSpeed * (currElapsed - lastElapsed);
				lastElapsed = currElapsed;
			}
			
			System.out.println(Integer.toString(totalDist) + " miles");
			
			numPairs = input.nextInt();
			input.nextLine();
		}
	}
}
		