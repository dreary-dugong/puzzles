import java.util.Scanner;
import java.io.*;

public class puzzle2{
	
	public static void main(String[] args) throws IOException{
		
		//read input file
		File inputFile = new File("input1.txt");
		Scanner input = new Scanner(inputFile);
		
		input.nextLine(); //skip departure time from puzzle1
		
		String[] ids = input.nextLine().split(",");
		input.close();
		
		System.out.println("FIle read successfully.");
		System.out.println("BusIds: " + arrayToString(ids));
		
		//iterate over ids and count how many are numeric
		int numNumeric = 0;
		for (String id : ids){
			if (!id.equals("x")){
				numNumeric++;
			}
		}
		
		//put numeric ids in array
		int[] busIds = new int[numNumeric]; //numeric bus Ids
		int[] idPos = new int[numNumeric]; //position of each id in original list
		int counter = 0; //count how many numeric ids we've added so far
		for (int i = 0; i < ids.length; i++){
			if (!ids[i].equals("x")){
				busIds[counter] = Integer.parseInt(ids[i]);
				idPos[counter] = i;
				counter++;
			}
		}
		
		System.out.println("\nIds converted to ints.");
		System.out.println("Integer ids: " + intArrayToString(busIds));
		System.out.println("Id positions: " + intArrayToString(idPos));
		
		//find largest id and its index
		int maxId = 0;
		int maxPos = 0; 
		for(int i = 0; i < busIds.length; i++){
			if(busIds[i] > maxId){
				maxId = busIds[i];
				maxPos = idPos[i];
			}
		}
		
		System.out.println("\nLargest id found.");
		System.out.println("Largest Id: " + maxId);
		System.out.println("Max Id Position: " + maxPos);
		
		//start the real work
		int base = maxId - maxPos;
		long currN = base;
		boolean found = false;
		while(!found){
			found = true;
			currN += maxId;
			for(int i = 0; i < busIds.length; i++){
				if((currN + idPos[i]) % busIds[i] != 0){
					found = false;
				}
			}
		}
		
		
		System.out.println("\nSolution found.");
		System.out.println("Solution: " + currN);
	}
	
	private static String intArrayToString(int[] array){
		StringBuilder output = new StringBuilder();
		output.append('[');
		for(int item : array){
			output.append(item);
			output.append(",");
		}
		output.setCharAt(output.length() - 1, ']');
		return output.toString();
	}
	
	private static <K> String arrayToString(K[] array){
		StringBuilder output = new StringBuilder();
		output.append('[');
		for(K item : array){
			output.append(item);
			output.append(",");
		}
		output.setCharAt(output.length() - 1, ']');
		return output.toString();
	}
}		