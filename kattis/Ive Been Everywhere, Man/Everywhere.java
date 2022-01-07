import java.util.Scanner;

public class Everywhere{
	
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		
		int numTests = input.nextInt();
		input.nextLine();
		
		for(int i = 0; i < numTests; i++){
			
			int numCities = input.nextInt();
			input.nextLine();
			
			String[] cities = new String[numCities];
			int numUnique = 0;
			
			for(int j = 0; j < numCities; j++){
				String currCity = input.nextLine();
				boolean found = false;
				for(String city:cities){
					if(currCity.equals(city)){
						found = true;
					}
				}
				if(!found){
					numUnique++;
					cities[j] = currCity;
				}
			}
			
			System.out.println(numUnique);
		}
	}
}