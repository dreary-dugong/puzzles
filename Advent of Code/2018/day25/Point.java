public class Point{
	
	private final int X;
	private final int Y;
	private final int Z;
	private final int T;
	
	//constructor
	public Point(int x, int y, int z, int t){
		X = x;
		Y = y;
		Z = z;
		T = t;
	}
	
	//accessors
	public int getX(){
		return X;
	}
	public int getY(){
		return Y;
	}
	public int getZ(){
		return Z;
	}
	public int getT(){
		return T;
	}
	
	//special methods
	//return readable string representation of the object
	public String toString(){
		String result = "(" + X + ", " + Y + ", " + Z + ", " + T + ")";
		return result;
	}
}
		
		