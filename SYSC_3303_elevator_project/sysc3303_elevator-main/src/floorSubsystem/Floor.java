package floorSubsystem;

import java.util.ArrayList;
import types.InputEvents;
import types.MotorState;

import java.util.Random;
/**
 * Floor class which requests elevators by sending UDP packets to the scheduler.
 * 
 * @author L4 Group 9
 */
public class Floor extends Thread {
    int floorNumber;
    FloorSubsystem subsys;
    ArrayList<InputEvents> events;
    FloorButton floorButtons[];
    Random rng;
    
    /**
     * Constructor for the Floor class. Initialized the floor number, a reference to
     * the scheduler, it's floor buttons, and an events queue.
     * 
     * @param floorNumber
     * @param scheduler
     */
    public Floor(FloorSubsystem subsys, int floorNumber) {
        this.floorNumber = floorNumber;
        this.subsys = subsys;
        this.events = new ArrayList<InputEvents>();
        
        // [0] is up, [1] is down
        floorButtons = new FloorButton[] {new FloorButton(), new FloorButton()};
        
        this.rng = new Random();
    }

    /**
     * Returns the floor number of the floor.
     * 
     * @return Floor number.
     */
    public int getFloorNumber() {
        return floorNumber;
    }

    /**
     * Reads from the input.txt file located in the same directory and parses the
     * data into InputEvent types and adds them to the floor queue.
     */
    public void readEvents() {
        String currentDir = System.getProperty("user.dir");
        
        ArrayList<InputEvents> arr = new ArrayList<InputEvents>();

        //arr.addAll(TxtFileReader.getEvents(currentDir + "/src/floorSubsystem/input.txt"));
        arr.addAll(TxtFileReader.getEvents(currentDir + "/src/floorSubsystem/input.txt"));
        
        for (int i = 0; i < arr.size(); i++) {
            InputEvents temp = arr.get(i);
            if (temp.getInitialFloor() == this.floorNumber) {
                this.events.add(temp);
            }
        }
    }
    
    
    /**
     * Removes an event from the queue and sends it to the scheduler.
     * The button for which direction is desired is lit up.
     */
    public void requestElevator() {
        InputEvents a = events.remove(0);
        
        // System.out.println("FLOOR #:"+floorNumber+ "--> Sending this message: "+a);
        subsys.sendToScheduler(a);

        if (a.getMotorState() == MotorState.UP)
            floorButtons[0].pressButton(); 
        else 
            floorButtons[1].pressButton();
    }
    
    
    /**
     * Returns the current event list of the floor.
     * 
     * @return events
     */
    public ArrayList<InputEvents> getEventList() {
        return events;
    }
    
    
    /**
     * Send a floor input event to the scheduler.
     * 
     * @param event Floor event to send to the scheduler.
     */
    public void sendEvent(InputEvents event) {
        // scheduler.addEvent(event);
    }
    
    
    /**
     * Invoked by the floor subsystem to notify the floor of
     * the arrival of an elevator.
     * 
     * @param goingUp Whether the arriving elevator is going up or down.
     */
    public void elevatorArrived(boolean goingUp) {
        System.out.println("Elevator arrived at floor " +floorNumber);
        
        if(goingUp) {
            floorButtons[0].pressButton();
        } else {
            floorButtons[1].pressButton();
        }
    }
    
    /**
     * Floor will wait for requests while it doesn't have any to send to the scheduler.
     */
    public void floorAwaitRequest() {
        try {
            synchronized(events) {
                //Will wait while it has no events to send to scheduler
                while(events.isEmpty()) {
                    events.wait(); 
                }
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    
    
    @Override
    public void run() {
    	this.readEvents();
        while (true) {
            while(!this.events.isEmpty()) {
                
                try {
                    Thread.sleep(rng.nextInt(3000)+3000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                
            	this.requestElevator();
            }
            
            //Floor will wait for more requests until an event is initiated
            floorAwaitRequest();
        }
    }
}
