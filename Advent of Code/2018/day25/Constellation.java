public class Constellation{
	private int numPoints;
	private Point[] points;
	
	//constructor
	public Constellation(){
		numPoints = 0;
		points = new Point[256];
	}
	
	//mutators
	public void addPoint(Point np){
		//add point to array
		points[numPoints] = np;
		numPoints++;
		
		//expand the array if necessary
		if (numPoints == points.length){
			Point[] tempArray = points;
			points = new Point[points.length*2];
			
			for (int i = 0; i < tempArray.length; i++) {
				points[i] = tempArray[i];
			}
		}
	}
	
	//accessors
	public Point[] getPoints(){
		Point[] result = new Point[numPoints];
		for (int i = 0; i < numPoints; i++){
			result[i] = points[i];
		}
		return result;
	}
	
	//special methods
	//return a readble string representation of the object
	public String toString(){
		String result  = "";
		for (int i = 0; i < numPoints; i++){
			result += points[i].toString() + "\n";
		}
		return  result;
	}
		
}
				
	
		