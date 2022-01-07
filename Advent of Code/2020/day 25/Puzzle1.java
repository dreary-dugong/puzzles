import java.io.*;
import java.util.Scanner;


public class Puzzle1{
	
	
	public static void main(String[] args) throws IOException{
		
		
		//read input
		Scanner scan = new Scanner(new File(args[0]));
		int DOOR_PUBLIC = scan.nextInt();
		scan.nextLine();
		int CARD_PUBLIC = scan.nextInt();
		scan.close();
		System.out.println("\nPublic keys read.\n");
		
		//processing		
		boolean foundCardLoopSize = false;
		boolean foundDoorLoopSize = false;
		long doorLoop = 0;
		long cardLoop = 0;
		long currLoopSize = 1;
		
		
		while (!(foundCardLoopSize && foundDoorLoopSize)){
			long currValue = transform(7, currLoopSize);
			if(currValue == DOOR_PUBLIC){
				foundDoorLoopSize = true;
				doorLoop = currLoopSize;
				System.out.println("Found door loop size: " + doorLoop);
			}
			if(currValue == CARD_PUBLIC){
				foundCardLoopSize = true;
				cardLoop = currLoopSize;
				System.out.println("Found card loop size: " + cardLoop);
			}
			currLoopSize++;
		}
		
		//now find the encryption key
		long key1 = transform(DOOR_PUBLIC, cardLoop);
		long key2 = transform(CARD_PUBLIC, doorLoop);
		
		if(key1 == key2){
			System.out.println("Found key: " + key1);
		} else{
			System.out.println("Error. Non-matching keys. Found: " + key1 + 
				" and " + key2);
		}
	}
	
	private static long transform(int subject, long loopSize){
		long value = 1;
		for(long i = 0; i < loopSize; i++){
			value *= subject;
			value = value % 20201227;
		}
		return value;
	}
}
	
	
		
		