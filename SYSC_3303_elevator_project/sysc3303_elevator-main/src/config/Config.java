/**
 * 
 */
package config;

/**
 * @author Group 9
 * 
 * Configuration class contains the configurations
 * of the system to be able to change values quickly.
 *
 */
public final class Config {

    /**
     * @param args
     */
    private Config() {}
    
    public static final int NUM_OF_ELEVATORS = 4;
    public static final int NUM_OF_FLOORS = 22;
    public static final int ELEVATOR_SCHEDULER_PORT = 25;
    public static final int FLOOR_SCHEDULER_PORT = 75;
    public static final int FLOOR_SUBSYS_PORT = 100;
    public static final String ELEVATOR_IP = "192.168.1.1";
    public static final String SCHEDULER_IP = "192.168.1.2";
    public static final String FLOOR_IP = "192.168.1.3";
    public static final String DEFAULT = "127.0.0.1";
    
}
