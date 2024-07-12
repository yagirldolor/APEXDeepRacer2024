
import math

params = {
    "all_wheels_on_track": bool,  # flag to indicate if the agent is on the track
    "x": float,  # agent's x-coordinate in meters
    "y": float,  # agent's y-coordinate in meters
    "closest_objects": [int, int],
    # zero-based indices of the two closest objects to the agent's current position of (x, y).
    "closest_waypoints": [int, int],  # indices of the two nearest waypoints.
    "distance_from_center": float,  # distance in meters from the track center
    "is_crashed": bool,  # Boolean flag to indicate whether the agent has crashed.
    "is_left_of_center": bool,  # Flag to indicate if the agent is on the left side to the track center or not.
    "is_offtrack": bool,  # Boolean flag to indicate whether the agent has gone off track.
    "is_reversed": bool,  # flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
    "heading": float,  # agent's yaw in degrees
    "objects_distance": [float, ],
    # list of the objects' distances in meters between 0 and track_length in relation to the starting line.
    "objects_heading": [float, ],  # list of the objects' headings in degrees between -180 and 180.
    "objects_left_of_center": [bool, ],
    # list of Boolean flags indicating whether elements' objects are left of the center (True) or not (False).
    "objects_location": [(float, float), ],  # list of object locations [(x,y), ...].
    "objects_speed": [float, ],  # list of the objects' speeds in meters per second.
    "progress": float,  # percentage of track completed
    "speed": float,  # agent's speed in meters per second (m/s)
    "steering_angle": float,  # agent's steering angle in degrees
    "steps": int,  # number steps completed
    "track_length": float,  # track length in meters.
    "track_width": float,  # width of the track
    "waypoints": [(float, float), ]  # list of (x,y) as milestones along the track center

}


class State:
    def __init__(self):
        self.clear()

    def clear(self):
        self.speed = None
        self.steps = None
        self.direction_diff = None
        self.steering_angle = None
        self.progress = None
        self.straight_section = None


PREV = State()


def reward_function(params):
    """
    Since we get a cumulative score from the score of this function...

    Every step where everything is done correctly will get 100 points.

    Crashed: -1000 points.  Figured whatever issue we had would be about 10 steps behind us.
    not left of center: -40 points.
    Heading:
        * If we're heading towards the goal (+-5 degrees) No deduction.
        * If we're heading towards the goal (+- 15 degrees) -10 points.
        * If we're off by (+-30 degrees), -20 points.
        * if we're off by +- 45 degrees, -40
        * Otherwise: -60 points.
    Straight section:
        Speed issues:
            * Slowing down: -40 points.
            * Speeding up while in a straight part: +10 points.
    Curves:
        Heading:
            * If we're not going towards the next waypoint
        Position:
            * If we're not in the inner part of the track: -40 points.
        Speed:
            * Only if at the start of a turn
                * Slowing down: + 10 points
                * Speeding up: -40 points.

    """

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
    crashed = params['is_crashed']
    left_of_center = params['is_left_of_center']

    # Initialize the reward with typical value
    reward = 100

    if crashed:
        return -1000


    # Reintialize previous parameters
    if PREV.steps is None or steps < PREV.steps:
        PREV.clear()

    ####### Closest waypoints for direction diff (track_direction - heading)
    # Calculate the direction of the racing line based on the closest waypoints
    next_point = race_line[closest_waypoints[1]]
    prev_point = race_line[closest_waypoints[0]]
    straight_section = next_point == prev_point
    # track_direction = get_direction_in_degrees(next_point, prev_point)
    car_direction = get_direction_in_degrees(next_point, (agent_x, agent_y))
    direction_diff = direction_diff_max_180_degrees(heading, car_direction)
    if direction_diff <= 5:
        pass
    elif direction_diff <= 15:
        reward = reward - 10
    elif direction_diff <= 30:
        reward = reward - 20
    elif direction_diff <= 45:
        reward = reward - 30
    else:
        reward = reward - 60

    if straight_section:
        if PREV.speed is not None:
            if PREV.speed > speed:
                reward = reward - 40
            elif PREV.speed < speed:  # We're going faster
                reward = reward + 10
    else:
        if PREV.straight_section is not None:
            if PREV.straight_section != straight_section:  # If we just started turning...
                if PREV.speed is not None:
                    if PREV.speed >= speed:
                        reward = reward - 40
                    else:
                        reward = reward + 10

    if closest_waypoints[1] in range(65,82):
        if not left_of_center:
            reward = reward + 40
    elif closest_waypoints[1] in range(58,65) or range(81, 92):
        pass
    else:
        if left_of_center:
            reward = reward + 40

    # Penalize the reward if the difference is too large
    # DIRECTION_THRESHOLD = 10.0
    # if direction_diff > DIRECTION_THRESHOLD:
    #     reward *= 0.5

    # ######Speed Reduction
    # speed_reduced = False
    # if PARAMS.prev_speed is not None:
    #     if PARAMS.prev_speed > speed:
    #         speed_reduced = True
    #
    # if PARAMS.prev_track_direction is not None:
    #     if (abs(PARAMS.prev_track_direction) - abs(track_direction)) > 0: #check this logic
    #         track_turn = True
    # #penalize if speed_reduced is True and track_turn is False:
    # if speed_reduced is True and track_turn is False:
    #     reward *= .8
    # #reward if speed_reduced is True and track_turn is True:
    # if speed_reduced is True and track_turn is True:
    #     reward += 5
    # #reward if speed_reduced is False and track_turn is False:
    # if speed_reduced is False and track_turn is False:
    #     reward += 3
    #
    # ######Steering (avoid zigzag)
    # abs_steering = abs(steering_angle)
    # # Penalize for steering too much
    # ABS_STEERING_THRESHOLD = 20.0
    # if abs_steering > ABS_STEERING_THRESHOLD:
    #     reward *= 0.8
    #
    # #has steering changed significantly from prev_steering_angle
    # ##################################check this logic
    # significant_steering_diff = False
    # is_heading_right = True
    # if direction_diff < 20:
    #     is_heading_right = False
    # if PARAMS.prev_steering_angle is not None:
    #     if not(math.isclose(PARAMS.prev_steering_angle,steering_angle)):
    #         significant_steering_diff = True
    # #Reward for not changing angle when heading in right direction
    # if is_heading_right and significant_steering_diff is False:
    #     if direction_diff < 8:
    #         reward *= 2
    #     if direction_diff < 4:
    #         reward *= 2.5
    #     if PARAMS.prev_direction_diff is not None and PARAMS.prev_direction_diff > direction_diff:
    #         reward *= 3
    #

    #######commenting this out, as it seems we should train with our reward function before we can determine this??
    ##### Steps and Progress, reward if car passes every n steps faster than expected??
    # Total num of steps we want the car to finish the lap, it will vary depends on the track length
    # TOTAL_NUM_STEPS = 300 #this should be according to our track (length: 46.16 meters, width: 1.07 meters)
    # Give additional reward if the car pass every 100 steps faster than expected
    # if (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100 :
    #    reward += 10.0

    ##### Update variables
    PREV.direction_diff = direction_diff
    PREV.speed = speed
    PREV.steering_angle = steering_angle
    PREV.steps = steps
    PREV.straight_section = straight_section
    PREV.progress = progress

    ###############################################################################
    #######Penalize if agent is off track
    # if is_offtrack is True:
    #     reward *= 0.5
    #
    # #######Following close to the racing line averaged
    # total_following_distance = 0
    # following_treshold = 1
    #
    # for race_line_x, race_line_y in race_line:
    #     distance_to_race_line_point = math.sqrt((agent_x - race_line_x)**2 + (agent_y - race_line_y)**2)
    #     total_following_distance += distance_to_race_line_point
    #
    # average_following_distance = total_following_distance / len(race_line)
    #
    # #reward following close to race line
    # if average_following_distance < following_treshold:
    #     reward += 2
    # #penalize if average following distance from race line is greater than 1
    # else:
    #     reward += 0

    #######Check if agent is within left or ride side of track

    return float(reward)


def direction_diff_max_180_degrees(heading, track_direction):
    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff
    return direction_diff


def get_direction_in_degrees(next_point, prev_point):
    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    # Convert to degree
    direction = math.degrees(direction)
    return round(direction, 0)


# The "racing line" -- if the "current" waypoints are the same, we're in a straight section.
race_line = [(4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.64726513, 4.02573627),
             (4.49639465, 4.25406806),
             (4.31762026, 4.46074704),
             (4.11276646, 4.64362302),
             (3.88480731, 4.80145781),
             (3.63735951, 4.93401168),
             (3.37421192, 4.99620344),
             (-2.21452466, 4.99620344),
             (-2.21452466, 4.99620344),
             (-2.21452466, 4.99620344),
             (-2.21452466, 4.99620344),
             (-2.21452466, 4.99620344),
             (-2.21452466, 4.99620344),
             (-2.21452466, 4.99620344),
             (-2.21452466, 4.99620344),
             (-2.21452466, 4.99620344),
             (-2.21452466, 4.99620344),
             (-2.21452466, 4.99620344),
             (-2.21452466, 4.99620344),
             (-2.21452466, 4.99620344),
             (-2.21452466, 4.99620344),
             (-2.21452466, 4.99620344),
             (-2.21452466, 4.99620344),
             (-2.21452466, 4.99620344),
             (-2.21452466, 4.99620344),
             (-2.21452466, 4.99620344),
             (-2.48214072, 4.88368091),
             (-2.7376457, 4.74962676),
             (-2.97790503, 4.59364784),
             (-3.19932651, 4.41592724),
             (-3.39793063, 4.21728064),
             (-3.56948617, 3.99927202),
             (-3.70970261, 3.76436176),
             (-3.8144654, 3.5160408),
             (-3.88010525, 3.25889379),
             (-3.90369807, 2.99853155),
             (-3.88338439, 2.74134336),
             (-3.81867186, 2.49405034),
             (-3.71065356, 2.26309631),
             (-3.56206116, 2.05397584),
             (-3.37709432, 1.87064387),
             (-3.1610252, 1.71514958),
             (-2.91964874, 1.58758019),
             (-2.65870118, 1.48630335),
             (-2.38337817, 1.4083949),
             (-2.09804597, 1.3500745),
             (-1.80617775, 1.30697632),
             (-1.51050684, 1.27413393),
             (-1.2128427, 1.24728315),
             (-0.91848458, 1.21850524),
             (-0.62770432, 1.18088399),
             (-0.3435595, 1.12825048),
             (-0.06971888, 1.05505266),
             (0.18936547, 0.95665763),
             (0.42864746, 0.83007134),
             (0.64265044, 0.67419774),
             (0.82576951, 0.49001254),
             (0.97267095, 0.28059367),
             (1.07870653, 0.05094148),
             (1.14028268, -0.19238106),
             (1.15515087, -0.44172127),
             (1.12260284, -0.68887714),
             (1.04356209, -0.9256952),
             (0.92055939, -1.14472282),
             (0.75757314, -1.33987662),
             (0.55972135, -1.50702911),
             (0.33282191, -1.64438097),
             (0.08291151, -1.75256453),
             (-0.1840835, -1.83464756),
             (-0.46370743, -1.89380113),
             (-0.75192085, -1.93460342),
             (-1.04615967, -1.96037343),
             (-1.34425231, -1.97492178),
             (-1.64464396, -1.98168856),
             (-1.94628298, -1.98353201),
             (-2.24705063, -1.98830638),
             (-2.545381, -2.00075668),
             (-2.83936108, -2.02545287),
             (-3.12665573, -2.06671158),
             (-3.40439636, -2.12855277),
             (-3.66855705, -2.21538692),
             (-3.91599567, -2.32834963),
             (-4.14201349, -2.46949171),
             (-4.34128599, -2.63958509),
             (-4.5087402, -2.83714517),
             (-4.63984981, -3.05856009),
             (-4.7308792, -3.29841976),
             (-4.77906393, -3.54994174),
             (-4.78273219, -3.80543687),
             (-4.74140351, -4.05679504),
             (-4.65588529, -4.2960187),
             (-4.52834302, -4.51583206),
             (-4.36228001, -4.71033978),
             (-4.16236057, -4.87563229),
             (-3.93405446, -5.01018292),
             (-3.68313683, -5.11487279),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.68435579, -5.02785761),
             (3.93154115, -4.90343346),
             (4.15783683, -4.75046627),
             (4.35932211, -4.56903719),
             (4.53300407, -4.3608311),
             (4.67732671, -4.12884918),
             (4.79247506, -3.87693241),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086),
             (4.76996403, 3.77863086)]
