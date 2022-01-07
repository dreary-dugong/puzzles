import java.util.Scanner;


public class Coldputer{
	
	public static void main(String[] args){
		
		int num = 0;
		Scanner input = new Scanner(System.in);
		
		int numTemps = input.nextInt();
		input.nextLine();
		
		for(int i = 0; i < numTemps; i++){
			int currTemp = input.nextInt();
			if(currTemp < 0){
				num++;
			}
		}
		
		System.out.println(num);
	}
}