package floorSubsystem;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;
import types.InputEvents;

import static config.Config.*;

public class FloorSubsystem implements Runnable {
    Floor floorList[] = new Floor[NUM_OF_FLOORS];
    
    DatagramSocket receiveSocket;
    InetAddress ip;

    /**
     * Constructor for the FloorSubsystem class. Creates all the floors and buttons, 
     * as well as a UDP socket for receiving data from the scheduler.
     */
    public FloorSubsystem() {
        try {
            this.receiveSocket = new DatagramSocket(FLOOR_SUBSYS_PORT);
            this.ip = InetAddress.getByName(DEFAULT);
        } catch (UnknownHostException | SocketException e) {
            e.printStackTrace();
        }

        for (int i = 0; i < NUM_OF_FLOORS; i++) {
            this.floorList[i] = (new Floor(this, i+1));
        }

        for (Thread floor : this.floorList) {
            floor.start();
        }
    }

    /**
     * Called by the floors to send a elevator request to the scheduler.
     * Creates a new socket, sends the data, and closes the socket.
     * @param data
     */
    public void sendToScheduler(InputEvents data) {
        byte[] sendData = new String(data.getTime() + "," + data.getInitialFloor() + ","
                + (data.getMotorState().name()) + "," + data.getDestinationFloor() + "," + data.getError()).getBytes();
        
        try {
            DatagramSocket socket = new DatagramSocket();
            DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, ip, FLOOR_SCHEDULER_PORT);
            socket.send(sendPacket);
            socket.close();
        } catch (IOException | IllegalArgumentException e) {
            e.printStackTrace();
        }
    }
    
    /**
     * Waits to receive a packet from the scheduler and notifies the 
     * proper floor of an elevators arrival
     */
    public void getFromScheduler() {
        byte data[] = new byte[100];
        DatagramPacket receivePacket = new DatagramPacket(data, data.length);
        
        try {
            this.receiveSocket.receive(receivePacket);
        } catch (IOException | IllegalArgumentException e) {
            e.printStackTrace();
        }
        
        String receivedData[] = new String(receivePacket.getData()).trim().split(",");

        // index 0 is floorNumber/id and index 1 is if going up;
        boolean isGoingUp = false;

        if (receivedData[1].equals("up")) {
            isGoingUp = true;
        }
        
        int floorNum = Integer.parseInt(receivedData[0]);

        floorList[floorNum-1].elevatorArrived(isGoingUp);
    }

    
    /**
     * Parses data from a string and returns an array with the data
     * 
     * @param schedulerData The string, normally received from the scheduler
     * 
     * @return Parsed array of the input data.
     */
    public String[] parseData(String schedulerData) {
        String[] tokens = schedulerData.split(",");
        return tokens;
    }
    
    
    @Override
    public void run() {
        while(true) {
            getFromScheduler();
        }

    }
    
    
    public static void main(String[] args) {
        new FloorSubsystem();
    }
}
