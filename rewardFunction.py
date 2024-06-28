
import math

race_line = [(0,0), (1,0)]

params = {
    "all_wheels_on_track": bool,        # flag to indicate if the agent is on the track
    "x": float,                            # agent's x-coordinate in meters
    "y": float,                            # agent's y-coordinate in meters
    "closest_objects": [int, int],         # zero-based indices of the two closest objects to the agent's current position of (x, y).
    "closest_waypoints": [int, int],       # indices of the two nearest waypoints.
    "distance_from_center": float,         # distance in meters from the track center 
    "is_crashed": bool,                 # Boolean flag to indicate whether the agent has crashed.
    "is_left_of_center": bool,          # Flag to indicate if the agent is on the left side to the track center or not. 
    "is_offtrack": bool,                # Boolean flag to indicate whether the agent has gone off track.
    "is_reversed": bool,                # flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
    "heading": float,                      # agent's yaw in degrees
    "objects_distance": [float, ],         # list of the objects' distances in meters between 0 and track_length in relation to the starting line.
    "objects_heading": [float, ],          # list of the objects' headings in degrees between -180 and 180.
    "objects_left_of_center": [bool, ], # list of Boolean flags indicating whether elements' objects are left of the center (True) or not (False).
    "objects_location": [(float, float),], # list of object locations [(x,y), ...].
    "objects_speed": [float, ],            # list of the objects' speeds in meters per second.
    "progress": float,                     # percentage of track completed
    "speed": float,                        # agent's speed in meters per second (m/s)
    "steering_angle": float,               # agent's steering angle in degrees
    "steps": int,                          # number steps completed
    "track_length": float,                 # track length in meters.
    "track_width": float,                  # width of the track
    "waypoints": [(float, float), ]        # list of (x,y) as milestones along the track center

}
class PARAMS:
    prev_speed = None
    prev_steps = None
    prev_direction_diff = None
    prev_steering_angle = None
    prev_progress = None
    prev_track_direction = None


def reward_function(params):
    ###############################################################################
    '''
        remember previous state of agent
    '''

    # Read input variables
    steps = params['steps']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    steering_angle = params['steering_angle']
    speed = params['speed']
    progress = params['progress']


    # Initialize the reward with typical value
    reward = 1.0

    # Reintialize previous parameters 
    if PARAMS.prev_steps is  None or steps < PARAMS.prev_steps:
        PARAMS.prev_speed = None
        PARAMS.prev_direction_diff = None
        PARAMS.prev_steering_angle = None
        PARAMS.prev_progress = None
        PARAMS.prev_track_direction = None
    

    ####### Closest waypoints for direction diff (track_direction - heading)
    # Calculate the direction of the center line based on the closest waypoints
    next_point = race_line[closest_waypoints[1]]
    prev_point = race_line[closest_waypoints[0]]
    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    # Convert to degree
    track_direction = math.degrees(track_direction)
    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff
    # Penalize the reward if the difference is too large
    DIRECTION_THRESHOLD = 10.0
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5
    
    ######Speed Reduction 
    speed_reduced = False
    if PARAMS.prev_speed is not None:
        if PARAMS.prev_speed > speed:
            speed_reduced = True

    if PARAMS.prev_track_direction is not None:
        track_turn = True
    #penalize if speed_reduced is True and track_turn is False:
    if speed_reduced is True and track_turn is False:
        reward *= .8
    #reward if speed_reduced is True and track_turn is True:
    if speed_reduced is True and track_turn is True:
        reward += 5
    #reward if speed_reduced is False and track_turn is False:  
    if speed_reduced is False and track_turn is False:
        reward += 3

    ##### Steps and Progress, reward if car passes every n steps faster than expected??
    # Total num of steps we want the car to finish the lap, it will vary depends on the track length
    TOTAL_NUM_STEPS = 300 #this should be according to our track
    # Give additional reward if the car pass every 100 steps faster than expected
    if (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100 :
        reward += 10.0


    ######Steering (avoid zigzag)
    if PARAMS.prev_steering_angle is not None:
        #compair prev steering to current and compute 
        steering_angle_diff = abs(PARAMS.prev_steering_angle) 

    abs_steering = abs(steering_angle)
    # Penalize for steering too much
    ABS_STEERING_THRESHOLD = 20.0
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8


    ##### Update variables
        PARAMS.prev_steps = steps
        PARAMS.prev_speed = speed
        PARAMS.prev_direction_diff = direction_diff
        PARAMS.prev_steering_angle = steering_angle
        PARAMS.prev_progress = None
        PARAMS.prev_track_direction = None
    

    return float(reward)
