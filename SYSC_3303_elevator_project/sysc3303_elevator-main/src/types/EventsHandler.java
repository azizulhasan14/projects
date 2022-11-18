package types;
import java.time.LocalTime;

/**
 * This class is responsible for handling successful elevator events/orders with "user" keyword
 * Meaning that this class handles events with no faults/errors
 * This class implements the interface InputEvents
 * @author Group
 */

public class EventsHandler implements InputEvents {
	private LocalTime time; //Event time
	private int initialFloor; //Initial floor, floor that requested the elevator
	private int destinationFloor;//Destination of the elevator/user
	private String error; //error type
	private MotorState motorState;
	
	/**
	 * EventsHandler constructor
	 * takes input event that was extracted from txt file and arranges it in the desired format
	 * example of input from txt file-> ["10:35:00.00","1","Up","2"]
	 * @param input -> input line from the txt file
	 */
	public EventsHandler(String input) {
		String[] inputs = input.split(",");
		this.time = LocalTime.parse(inputs[0]);
		this.initialFloor = Integer.valueOf(inputs[1]);
		this.motorState = inputs[2].equalsIgnoreCase("Up") ? MotorState.UP : MotorState.DOWN;
		this.destinationFloor = Integer.valueOf(inputs[3]);
		if(inputs.length == 4) {
		    this.error = "NA";
		}else if(inputs[4].equals("Serious")) {
			this.error = "Serious";
		}else if(inputs[4].equals("Trivial")){
			this.error = "Trivial";
		}else {
			this.error = "NA";
		}
	}

	//Get time
	@Override
	public LocalTime getTime() {
		return this.time;
	}


	//Get the initial floor that requested the elevator
	@Override
	public int getInitialFloor() {
		return this.initialFloor;
	}


	//Get the destination of the elevator
	@Override
	public int getDestinationFloor() {
		return this.destinationFloor;
	}
	
	
	//Get error code
	public String getError() {
		return this.error;
	}
	
	
	/*
	 * Get the elevator
	 * returns -1 because this is only needed when we have a faulty event/elevator
	 * */
	@Override
	public int getElevator() {
		return -1;
	}
	
	//Print results
	@Override
	public String toString() {
		if(error.equals("NA")) {
			return "Time: " + time + "\nFloor: " + initialFloor + "\nFloor-button: " + motorState.name() + "\nDestination: " + destinationFloor + "\n";
		}else {
			return "Time: " + time + "\nFloor: " + initialFloor + "\nFloor-button: " + motorState.name() + "\nDestination: " + destinationFloor + "\nError: " + error + "\n";
		}
	}

	@Override
	public MotorState getMotorState() {
		return this.motorState;
	}

	
	@Override 
	public boolean equals(Object obj) {
	    if (obj == this)
            return true;
            
        if (obj == null || !(obj instanceof EventsHandler)) 
            return false;
        EventsHandler testEvents = (EventsHandler) obj;
	   
	    if(!(testEvents.getTime().equals(this.getTime()))) return false;
	    if(!(testEvents.getInitialFloor() == this.getInitialFloor())) return false;
	    if(!(testEvents.getDestinationFloor() == this.getDestinationFloor())) return false;
	    if(!(testEvents.getError().equals(this.getError()))) return false;
	    if(!(testEvents.getElevator() == this.getElevator())) return false;

	    return true;
	}
}
