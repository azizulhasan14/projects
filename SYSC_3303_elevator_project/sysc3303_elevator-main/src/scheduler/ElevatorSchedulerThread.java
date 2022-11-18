package scheduler;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;

import display.GUI;
import types.MotorState;

/**
 * This thread is created for elevator request
 */
public class ElevatorSchedulerThread extends Thread {
    
    private GUI display;
    private Scheduler scheduler;
    private DatagramPacket receivePacket, sendPacket;
    private DatagramSocket socket;
    InetAddress floorSubsysIp;
    private int floorSubsysPort;
    
    boolean isRunning = true;
    
    /**
     * Creates a thread for the elevators to communicate to regarding elevator requests.
     * 
     * @param scheduler The scheduler to make the request to.
     * @param display The GUI of the application.
     * @param floorSubsysIp The IP of the floor subsystem.
     * @param receivePort The port at which this class receives requests.
     * @param floorSubsysPort The port at which the floor subsystem receives requests.
     */
    public ElevatorSchedulerThread(Scheduler scheduler, GUI display, String floorSubsysIp, int receivePort, int floorSubsysPort) {
        this.display = display;
        this.scheduler = scheduler;
        this.floorSubsysPort = floorSubsysPort;
        
        try {
            this.socket = new DatagramSocket(receivePort);
            this.floorSubsysIp = InetAddress.getByName(floorSubsysIp);
        } catch (SocketException | UnknownHostException e) {
            e.printStackTrace();
        }
    }

    public void shutDown() {
        isRunning  = false;
    }

    public String receiveRequest() {
        byte[] data = new byte[100];

        receivePacket = new DatagramPacket(data, data.length);
        try {
            socket.receive(receivePacket);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return new String(receivePacket.getData()).trim();
    }

    public void evaluateRequest(String command, int elevatorId, int floorNum, String direction) {
        switch (command) {

        // An elevator has arrived at a new floor and is requesting more jobs
        case "seekWork":
            this.handleSeekWork(elevatorId, floorNum, direction);
            break;
        
        // An elevator looking for events while moving to initial event floor
        case "seekFartherWork":
            this.handleSeekFartherWork(elevatorId, floorNum, direction);
            break;

        // An elevator has arrived at one of its target floors
        case "arrived":
            this.handleArrived(elevatorId, floorNum, direction);
            break;
        }
    }

    
    /**
     * Handles the seekWork command from the elevator. Picks up events on the way
     * to the elevators initial event's destination floor.
     * 
     * @param elevatorId The elevator's ID
     * @param currentFloor The current floor of the elevator
     * @param direction The direction of the elevator.
     */
    private void handleSeekWork(int elevatorId, int currentFloor, String direction) {
        try {
            String response;

            //Convert the direction string into the enum
            MotorState state = stringToMotorState(direction);
            
            if(display != null)
                display.setFloorStatus(null, elevatorId, currentFloor);
            
            response = scheduler.scheduleEvents(currentFloor, state);
            
            byte[] message = response.getBytes();
            sendPacket = new DatagramPacket(message, message.length, receivePacket.getAddress(), receivePacket.getPort());
            socket.send(sendPacket);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    /**
     * Parses a string into the enum MotorState
     * @param direction Direction of elevator as a string.
     * 
     * @return Direction equivalent as an enum.
     */
    private MotorState stringToMotorState(String direction) {
        MotorState state = null;
        
        if(direction.equals("IDLE")) {
            state = MotorState.IDLE;
        }else if (direction.equals("UP")) {
            state =  MotorState.UP;
        }else if (direction.equals("DOWN")) {
            state = MotorState.DOWN;
        }
        
        return state;
    }
    
    
    /**
     * Seeks more work for the elevator while it is traveling to its first event's initial floor.
     * 
     * @param elevatorId The ID of the elevator
     * @param currentFloor The current floor the elevator is at.
     * @param direction The direction the elevator is traveling.
     */
    private void handleSeekFartherWork(int elevatorId, int currentFloor, String direction) {
        MotorState state = stringToMotorState(direction);
        
        if(display != null)
            display.setFloorStatus(null, elevatorId, currentFloor);
        
        String response;
        response = scheduler.pickUpFartherEvent(elevatorId, currentFloor, state);
        
        byte[] message = response.getBytes();
        sendPacket = new DatagramPacket(message, message.length, receivePacket.getAddress(), receivePacket.getPort());
        
        try {
            socket.send(sendPacket);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    /**
     * Handles when an elevator has arrived at a target floor.
     * 
     * @param currentFloor The floor the elevator is at.
     * @param direction The direction of the elevator.
     */
    private void handleArrived(int elevatorId, int currentFloor, String direction) {
        byte[] message = new String(currentFloor+ "," +direction).getBytes();
        
        try {
            DatagramPacket sendPacket = new DatagramPacket(message, message.length, floorSubsysIp, this.floorSubsysPort);
            DatagramSocket socket = new DatagramSocket();
            socket.send(sendPacket);
            socket.close();
            
            if(display != null) {
                display.writeToLog("The " +direction+ " button light turned off for floor " +currentFloor);
                display.setFloorStatus("arrived", elevatorId, currentFloor);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    /**
     * Handles the types of faults for the elevators.
     * 
     * @param elevatorId The elevator ID.
     * @param serious True when error is serious, false when trivial.
     */
    private void handleFault(int elevatorId, boolean serious) {
        if(serious) {
            if(display != null) {
                display.writeToLog("Elevator "+elevatorId+ " experienced a fault, shutting down.");
                display.closeElevator(elevatorId);
            }
                
        } else {
            if(display != null) {
                display.writeToLog("Elevator " +elevatorId+ " is experiencing issues operating its doors.");
                display.jamElevator(elevatorId);
            }
                
        }
    }
    
    @Override
    public void run() {
        while(isRunning) {
            String parsedData[] = receiveRequest().split(",");
            
            String command = parsedData[0];
            int elevatorId = Integer.parseInt(parsedData[1]);
            
            //Handle if fault before we move on
            if(command.equals("fault")) {
                handleFault(elevatorId, true);
            } else if(command.equals("trivial")) {
                handleFault(elevatorId, false);
            } else {
                int floorNum = Integer.parseInt(parsedData[2]);
                String direction = parsedData[3];

                evaluateRequest(command, elevatorId, floorNum, direction);
            }
        }
        System.out.println("scheduler thread shutting down");
        socket.close();
    }
}
