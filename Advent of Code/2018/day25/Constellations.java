import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Constellations{
	
	public static void main(String[] args) throws FileNotFoundException{
		
		//read points from file
		final String fileName = "input.txt";
		Scanner input = new Scanner(new File(fileName));
		System.out.println("File found.");
		
		//get size of array for holding points
		int numPoints = 0;
		while (input.hasNextLine()){
			numPoints++;
			input.nextLine();
		}
		Point[] points = new Point[numPoints];
		System.out.println("File read.");
		
		//reread file and add points to array
		input = new Scanner(new File(fileName));
		int currIndex = 0;
		while (input.hasNextLine()){
			String[] coordStrings = input.nextLine().split(",");
			int x = Integer.parseInt(coordStrings[0]);
			int y = Integer.parseInt(coordStrings[1]);
			int z = Integer.parseInt(coordStrings[2]);
			int t = Integer.parseInt(coordStrings[3]);
			
			points[currIndex] = new Point(x,y,z,t);
			currIndex++;
		}
		System.out.println("\nParsed points.");
		System.out.println("Points: ");
		for (Point p : points){
			System.out.print(p);
		}
		System.out.print("\n");
		
		//create initial constellations array
		Constellation[] constellations = new Constellation[points.length];
		for (int i = 0; i < points.length; i++){
			Constellation currConst = new Constellation();
			currConst.addPoint(points[i]);
			constellations[i] = currConst;
		}
		System.out.println("\nCreated Constellation Array.");
		
		//main algorithm
		int numCompleteConstellations = 0;
		
		//loop through array until all constellations are complete
		while (constellations.length > 0){
			
			//compare the first constellation to the rest
			Constellation currConst = constellations[0];
			boolean combineConsts = false;
			for (int i = 1; i < constellations.length; i++){
				
				combineConsts = false;
				for (Point p1 : currConst.getPoints()){	
					for (Point p2 : constellations[i].getPoints()){
						
						if (manhattanDistance(p1, p2) < 4){
							combineConsts = true;
							break;
						}
					}
				}
				
				//combine constellations they match
				if (combineConsts){
					Constellation[] formerConstellations = constellations;
					constellations = new Constellation[constellations.length-1];
					constellations[0] = formerConstellations[0];
					
					for (Point p : formerConstellations[i].getPoints()){
						constellations[0].addPoint(p);
					}
					
					//reform constellations array
					for (int j = 1; j < i; j++){
						constellations[j] = formerConstellations[j];
					}
					for (int j = i+1; j < formerConstellations.length; j++){
						constellations[j-1] = formerConstellations[j];
					}
					break;
				}
			}
			
			//if the constellation couldn't combine with anything, it's complete
			if (!combineConsts){
				Constellation[] formerConstellations = constellations;
				constellations = new Constellation[constellations.length-1];
				for (int i = 1; i < formerConstellations.length; i++){
					constellations[i-1] = formerConstellations[i];
				}
				System.out.println("Found new constellation: ");
				System.out.println(formerConstellations[0]);
				numCompleteConstellations++;
			}
		}
		
		System.out.println("Number of complete constellations: " +
			numCompleteConstellations);
				
	}
	
	//return the manhattan distance between two 4D point objects
	private static int manhattanDistance(Point p1, Point p2){
		int result;
		result = Math.abs(p1.getX() - p2.getX()) + 
			Math.abs(p1.getY() - p2.getY()) + 
			Math.abs(p1.getZ() - p2.getZ()) +
			Math.abs(p1.getT() - p2.getT());
		return result;
	}
}