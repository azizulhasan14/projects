package floorSubsystem;
import java.io.IOException;
import java.util.ArrayList;

//import types.ErrorHandler;
import types.EventsHandler;
import types.InputEvents;

import java.io.BufferedReader;
import java.io.FileReader;

/**
 * This class is responsible for handling the reading of external text files
 * @author Group
 */
public class TxtFileReader {
	/**
	 * getEvents is a method that scans through a text file
	 * and retrieves a list of InputEvents -> a list of the events/orders for the elevator 
	 * @param filePath -> local path to the text file 
	 * @return eventList -> ArrayList<InputEvents> of events for for the elevator
	 */
	public static ArrayList<InputEvents> getEvents(String filePath) {
		ArrayList<InputEvents> eventList = new ArrayList<InputEvents>();
		try {
			BufferedReader fileReader = new BufferedReader(new FileReader(filePath));
			String readLine;
			readLine = fileReader.readLine();
			while (readLine != null) {
			    EventsHandler event = new EventsHandler(readLine.split("\\|")[1]);
				eventList.add(event); //adds current event to the array list
				readLine = fileReader.readLine();
			}
			fileReader.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return eventList; //return ArrayList of InputEvents
	}
}