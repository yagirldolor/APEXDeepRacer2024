
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
    is_offtrack = params['is_offtrack']
    agent_x = params['x']
    agent_y = params['y']

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
    # Calculate the direction of the racing line based on the closest waypoints
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
        if (abs(PARAMS.prev_track_direction) - abs(track_direction)) > 0: #check this logic 
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

    ######Steering (avoid zigzag)
    abs_steering = abs(steering_angle)
    # Penalize for steering too much
    ABS_STEERING_THRESHOLD = 20.0
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    #has steering changed significantly from prev_steering_angle
    ##################################check this logic
    significant_steering_diff = False
    is_heading_right = True
    if direction_diff < 20:
        is_heading_right = False
    if PARAMS.prev_steering_angle is not None:
        if not(math.isclose(PARAMS.prev_steering_angle,steering_angle)):
            significant_steering_diff = True
    #Reward for not changing angle when heading in right direction
    if is_heading_right and significant_steering_diff is False:
        if direction_diff < 8:
            reward *= 2
        if direction_diff < 4:
            reward *= 2.5
        if PARAMS.prev_direction_diff is not None and PARAMS.prev_direction_diff > direction_diff:
            reward *= 3


    #######commenting this out, as it seems we should train with our reward function before we can determine this??
    ##### Steps and Progress, reward if car passes every n steps faster than expected??
    # Total num of steps we want the car to finish the lap, it will vary depends on the track length
    #TOTAL_NUM_STEPS = 300 #this should be according to our track (length: 46.16 meters, width: 1.07 meters)
    # Give additional reward if the car pass every 100 steps faster than expected
    #if (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100 :
    #    reward += 10.0
            
    ##### Update variables
        PARAMS.prev_steps = steps
        PARAMS.prev_speed = speed
        PARAMS.prev_direction_diff = direction_diff
        PARAMS.prev_steering_angle = steering_angle
        PARAMS.prev_progress = None
        PARAMS.prev_track_direction = track_direction
            
    ###############################################################################
    #######Penalize if agent is off track
    if is_offtrack is True:
        reward *= 0.5
    
    #######Following close to the racing line averaged
    total_following_distance = 0
    following_treshold = 1

    for race_line_x, race_line_y in race_line:
        distance_to_race_line_point = math.sqrt((agent_x - race_line_x)**2 + (agent_y - race_line_y)**2)
        total_following_distance += distance_to_race_line_point

    average_following_distance = total_following_distance / len(race_line)
    
    #reward following close to race line
    if average_following_distance < following_treshold:
        reward += 2
    #penalize if average following distance from race line is greater than 1
    else:
        reward += 0


    #######Check if agent is within left or ride side of track

    
    

    return float(reward)
