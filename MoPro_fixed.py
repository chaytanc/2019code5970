# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 21:32:50 2018

@author: Noah
"""

import numpy as np
from scipy import interpolate
import interparc
import math
import matplotlib.pyplot as plt






#trajectory function, overall
def trajectory(points,tangents,scale,resolution,trackwidth,max_velocity,max_accel,max_decel,num_points,starting_velocity,end_velocity):
    #converting points and tangents into numpy arrays
    points = np.asarray(points)
    tangents = np.asarray(tangents)
    
    #call path_generation function to get points spaced evenly by TIME
    interpolated_x,interpolated_y = path_generation(points,tangents,resolution,scale)
    
    #call evenly_space function to create points evenly spaced by distance
    evenly_spaced_x,evenly_spaced_y,evenly_spaced = evenly_space(interpolated_x,interpolated_y,num_points)
    
    #create Center_Velocity Array
    Center_Velocity = [0 for i in range(num_points)]
    
    #First constraint based on curvature
    Center_Velocity = curvature_constraint(evenly_spaced_x,evenly_spaced_y,max_velocity,Center_Velocity,trackwidth)
    
    #calculate step size between points along path
    step_size = arc_length(evenly_spaced_x,evenly_spaced_y)
    
    #initialize Center_Velocity as zero
    Center_Velocity[0] = starting_velocity
    
    #Second and Third constraints based on max acceleration and deceleration
    Center_Velocity = acceleration_constraint(Center_Velocity,step_size,max_accel)
    
    Center_Velocity = deceleration_constraint(Center_Velocity,step_size,max_decel,end_velocity)
    
    #calculate time elapsed at each point
    time_elapsed = time(Center_Velocity,step_size)
    
    #coordinates for right and left paths and velocities for those paths
    rx,ry,lx,ly = offset_path(evenly_spaced_x,evenly_spaced_y,trackwidth,num_points,evenly_spaced)
    Right_Velocity,Left_Velocity,radius_right,radius_left = offset_velocity(Center_Velocity,evenly_spaced_x,evenly_spaced_y,trackwidth,rx,ry,lx,ly)
    
    #Center path initialization as numpy array, then definition with evenly spaced x and y
    Center_Path = np.zeros((num_points, 2), dtype = int)
    Center_Path[:,0] = evenly_spaced_x    
    Center_Path[:,1] = evenly_spaced_y

    #Right path initialization as numpy array, then definition with rx and ry
    Right_Path = np.zeros((num_points-1, 2), dtype = int)
    Right_Path[:,0] = rx    
    Right_Path[:,1] = ry
    
    #Left path initialization as numpy array, then definition with lx and ly
    Left_Path = np.zeros((num_points-1, 2), dtype = int)
    Left_Path[:,0] = lx    
    Left_Path[:,1] = ly

    CenP = [[0.0,0.0] for i in range(num_points-1)]
    
    for i in range(len(Center_Path)-1):
        CenP[i][0]=Center_Path[i][0]
        CenP[i][1]=Center_Path[i][1]
    CenP = np.array(CenP)
    Time = []
    CV = []
    for i in range(len(time_elapsed)-1):
        Time.append(time_elapsed[i])
    
    for i in range(len(Center_Velocity)-1):
        CV.append(Center_Velocity[i])

    #returns
    return CV,Right_Velocity,Left_Velocity,Time,Center_Path,Right_Path,Left_Path,radius_right,radius_left
   
#path generation function, generates points along a spline evenly spaced by time
def path_generation(points,tangents,resolution,scale):
    '''
    Compute and sample the cubic splines for a set of input points with
    optional information about the tangent (direction AND magnitude). The 
    splines are parametrized along the traverse line (piecewise linear), with
    the resolution being the step size of the parametrization parameter.
    The resulting samples have NOT an equidistant spacing.

    Arguments:      points: a list of n-dimensional points
                    tangents: a list of tangents
                    resolution: parametrization step size
    Returns:        interpolated_x: a list of x values
                    interpolated_y: a list of y values

    Notes: Lists points and tangents must have equal length. In case a tangent
           is not specified for a point, just pass None. For example:
                    points = [[0,0], [1,1], [2,0]]
                    tangents = [[1,1], None, [1,-1]]

    '''
    
    #getting inputs into correct data format
    resolution = float(resolution)
    points = np.asarray(points)
    
    #create variables equal to the number of input points
    nPoints, dim = points.shape
    
    #Scale up the tangents, longer "handle"
    tangents = np.dot(tangents, scale*np.eye(2))
    
    # Parametrization parameter s.
    
    # difference between points
    dp = np.diff(points, axis=0)
    
    # distance between points
    dp = np.linalg.norm(dp, axis=1)              
    
    # cumsum along the segments
    d = np.cumsum(dp)                            
    
    # add distance from first point
    d = np.hstack([[0],d])                       
    
    # length of point sequence
    l = d[-1]                                    
    
    # number of points in interpolated_x and interpolated_y
    nSamples = int(l/resolution)                 
    
    # sample parameter and step
    s,r = np.linspace(0,l,nSamples,retstep=True) 



    # Bring points and (optional) tangent information into correct format.
    assert(len(points) == len(tangents))
    data = np.empty([nPoints, dim], dtype=object)
    for i,p in enumerate(points):
        t = tangents[i]
        # Either tangent is None or has the same
        # number of dimensions as the point p.
        assert(t is None or len(t)==dim)
        fuse = list(zip(p,t) if t is not None else zip(p,))
        data[i,:] = fuse

    # Compute splines per dimension separately.
    samples = np.zeros([nSamples, dim])
    
    #interpolate points along spline
    for i in range(dim):
        poly = interpolate.BPoly.from_derivatives(d, data[:,i])
        samples[:,i] = poly(s)
    
    #convert samples into interpolated x and y
    interpolated_x = samples[:,0]
    interpolated_y = samples[:,1]
    
    #returns
    return interpolated_x, interpolated_y
    
    
#evenly space points along spline by distance
def evenly_space(interpolated_x,interpolated_y,num_points):
    #call interparc function
    evenly_spaced = interparc.interparc(num_points,interpolated_x,interpolated_y,"linear")
    
    #split evenly spaced into x and y
    evenly_spaced_x = evenly_spaced[:,0]
    evenly_spaced_y = evenly_spaced[:,1]
    
    #returns
    return evenly_spaced_x,evenly_spaced_y,evenly_spaced
 
    
#get radius of curvature of center path at every point
def getRadCurvature(x,y):
    
    #Create new numpy array where each value is the difference between values in x for dx or y for dy
    #this approximates the derivative, or slope, at all points
    dx = np.diff(x)
    dy = np.diff(y)
    dx = np.append(dx, dx[-1])
    dy = np.append(dy, dy[-1])
   
    #diagnostic plot of the derivative of the center path
    plt.plot(np.linspace(0, 700, len(dx)), dx)
    plt.plot(np.linspace(0, 700, len(dy)), dy)
    
    #reate new numpy array where each value is the difference between values in dx for ddx or dy for ddy
    #this approximates the second derivative, or concavity, at all points
    ddx = np.diff(dx)
    ddy = np.diff(dy)
    ddx = np.append(ddx, ddx[-1])
    ddy = np.append(ddy, ddy[-1])
    
    #diagnostic plot of second derivative of center path
    plt.plot(np.linspace(0, 700, len(ddx)), ddx)
    plt.plot(np.linspace(0, 700, len(ddy)), ddy)
    
    #initialize radCurvature array which will hold values for radius of curvature at all points
    radCurvature = [0 for i in range(len(dx))]
    
    #initialize curvature array, curvature is inverse of radius of curvature
    k = [0 for i in range (len(dx))]
    
    #curvature exuation for each point
    for i in range (len(dx)):
        k[i] = (abs(dx[i] * ddy[i] - ddx[i] * dy[i])) / (math.pow((math.pow(dx[i],2.0) + math.pow(dy[i],2.0)),(1.5)))
        
        
    #Remove possibility for division by zero
    for i in range(len(k)):
        if k[i] == 0:
            k[i] = .000001
        
    for i in range(len(k)):
        #Calculate the radius of curvature using k
        radCurvature[i] = 1/k[i]
    
    #eliminate all radii of curvature that would return too high a value
    for i in range(len(radCurvature)):
        if radCurvature[i] > 10000:
            radCurvature[i] = 10000
    
    #returns
    return radCurvature

#calculate max velocity constrained by curvature
def curvature_constraint(evenly_spaced_x,evenly_spaced_y,max_velocity,Center_Velocity,trackwidth):
    #calculate radius of curvature at each point
    radius_center = getRadCurvature(evenly_spaced_x,evenly_spaced_y)    
    
    for i in range(len(evenly_spaced_x)):
        #calculate radius of outer wheel by adding half the trackwidth of the robot to the center radius
        radius_outer_wheel = radius_center[i] + (trackwidth/2)
        
        #calculate maximum rotational velocity(alpha) based on max velocity
        alpha = max_velocity/radius_outer_wheel
        
        #calculate maximum possible center velocity for this turning radius
        Center_Velocity[i] = alpha * radius_center[i]
    
    #returns
    return Center_Velocity


#calculate arc length between evenly spaced points
def arc_length(xs,ys):
    #initialize and create variable for length of whole path
    arcLength = 0

    #iterate through all but last value, otherwise it would go out of range
    for i in range(0,len(xs)-1):
        #create point from parametricized x and y values
        a = np.array((xs[i],ys[i]))
        
        #create point from parametricized x and y values one ahead of a
        b = np.array((xs[i+1],ys[i+1]))
        
        #calculate length between points a and b
        arcLength += np.linalg.norm(a-b)

    #divide total arc length by number of points to get step size
    step_size = arcLength/(len(xs))
    
    #returns
    return step_size


#calculate new vmax constrained by acceleration
def acceleration_constraint(Center_Velocity,step_size,max_accel):
    
    for i in range (len(Center_Velocity)):
        #calculate maximum possible velocity based on max acceleration
        accel = math.sqrt((math.pow((Center_Velocity[i-1]),2.0))+2.0*max_accel*step_size) 
        
        #select minimum of the existing max velocity and the max velocity based on acceleration
        Center_Velocity[i] = min(accel,Center_Velocity[i])
    return Center_Velocity
    
#calculate new vmax constrained by deceleration
def deceleration_constraint(Center_Velocity,step_size,max_decel,end_velocity):
    Center_Velocity[-1] = end_velocity
    for i in range (len(Center_Velocity)-2,0,-1):
        decel = math.sqrt((math.pow((Center_Velocity[i+1]),2.0))-2.0*max_decel*step_size) 
        Center_Velocity[i] = min(decel,Center_Velocity[i])
        
    return Center_Velocity
        
#generate vmax_right and vmax_left from vmax
def offset_velocity(Center_Velocity,evenly_spaced_x,evenly_spaced_y,trackwidth,rx,ry,lx,ly): 
    #initialize right and left velocity arrays
    Right_Velocity = [0 for i in range (len(Center_Velocity)-1)]
    Left_Velocity = [0 for i in range (len(Center_Velocity)-1)]
    
    #calculate radius of curvature for right and left paths respectively, as well as center
    radius_right = getRadCurvature(rx,ry)
    radius_left = getRadCurvature(lx,ly)
    radius_center = getRadCurvature(evenly_spaced_x,evenly_spaced_y)
    
    for i in range(len(radius_right)):
        #if radius right is larger, it is the outside wheel and as such has a radius half the trackwidth larger than center
        if radius_right[i] > radius_left[i]:
            radius_right[i] = radius_center[i] + trackwidth/2
            radius_left[i] = radius_center[i] - trackwidth/2
        #vise versa
        elif radius_right[i] < radius_left[i]:
            radius_right[i] = radius_center[i] - trackwidth/2
            radius_left[i] = radius_center[i] + trackwidth/2
        #basically only if perfectly straight
        else:
            radius_right[i] = radius_center[i]
            radius_left[i] = radius_center[i]
            
    for i in range (len(Center_Velocity)-1):
        #calculate offset velocities based on angular velocity at each point    
        alpha = Center_Velocity[i]/radius_center[i]
        Right_Velocity[i] = alpha * radius_right[i]
        Left_Velocity[i] = alpha * radius_left[i]
    
    
    #returns
    return Right_Velocity,Left_Velocity,radius_right,radius_left
        
#calculate time elapsed at each point
def time(Center_Velocity,step_size):
    #initialize time array
    time = [0 for i in range (len(Center_Velocity))]
    
    for i in range (1,len(Center_Velocity),1):
        #calculate the time between each individual point
        time[i] = step_size/Center_Velocity[i]
        
    #initialize tie_elapsed and cumsum variables
    time_elapsed = []
    cumsum = 0
    
    for elt in time:
        #add all times up to certain point, get total time elapsed
        cumsum += elt
        time_elapsed.append(cumsum)
    
    #returns
    return time_elapsed


#offset points for right and left wheels
def offset_path(evenly_spaced_x,evenly_spaced_y,trackwidth,num_points,evenly_spaced):
    
    #using trwdth makes life easier, removes an operation later
    trwdth = trackwidth/2
    
    #call offset function to offset right and left paths, may have to switch signs here based on starting pos
    right_path = offset(evenly_spaced, trwdth)
    left_path = offset(evenly_spaced, -1*trwdth)
    
    #coordinates for right and left paths
    rx = [i[0] for i in right_path]
    ry = [i[1] for i in right_path]
    lx = [i[0] for i in left_path]
    ly = [i[1] for i in left_path]
    
    #returns
    return rx,ry,lx,ly

#basically determines which direction the robot is pointing, state = quadrant
def stately(evenly_spaced_x,evenly_spaced_y,state):
    
    #calculate difference between each x and y
    for i in range(len(state)):
        y_diff = evenly_spaced_y[i+1]-evenly_spaced_y[i]
        x_diff = evenly_spaced_x[i+1]-evenly_spaced_x[i]
         
        #determine which quadrant, or direction
        if y_diff > 0 and x_diff > 0:
            state[i] = 1
        if y_diff > 0 and x_diff < 0:
            state[i] = 2
        if y_diff < 0 and x_diff < 0:
            state[i] = 3
        if y_diff < 0 and x_diff > 0:
            state[i] = 4
    
    #returns        
    return state
            
        
#possible way to determine which way to offset the path    
def right_left_choose(state,evenly_spaced_x,evenly_spaced_y,num_points):
    
    #call stately function
    state = stately(evenly_spaced_x,evenly_spaced_y,state)

    #initialize arrays, will end up being 1 or -1
    pos_neg_right = [1 for i in range (len(state))]
    pos_neg_left = [1 for i in range (len(state))]
    
    #flip all if it starts pointing down
    if state[0] == 3 or state[0] == 4:
        for i in range (pos_neg_right):
            pos_neg_right[i] = pos_neg_right[i] * -1
            pos_neg_left[i] = pos_neg_left[i] * -1

    #determine which way to offset, right or left
    for i in range (len(state),1,1):
        if state[i-1] == 1 and state [i] == 4:
            pos_neg_right[i] = pos_neg_right[i] * -1
            pos_neg_left[i] = pos_neg_left[i] * -1
        if state[i-1] == 4 and state [i] == 1:
            pos_neg_right[i] = pos_neg_right[i] * -1
            pos_neg_left[i] = pos_neg_left[i] * -1  
        if state[i-1] == 2 and state [i] == 3:
            pos_neg_right[i] = pos_neg_right[i] * -1
            pos_neg_left[i] = pos_neg_left[i] * -1 
        if state[i-1] == 3 and state [i] == 2:
            pos_neg_right[i] = pos_neg_right[i] * -1
            pos_neg_left[i] = pos_neg_left[i] * -1  
            
    #returns
    return pos_neg_right, pos_neg_left
        
#this offset function is more useful  
def offset(coordinates, distance):
    #iterate through all coordinates
    coordinates = iter(coordinates)
    
    x1, y1 = next(coordinates)
    
    #shorten this variable
    z = distance
    
    #initialize points array
    points = []
    for x2, y2 in coordinates:
        # tangential slope approximation
        try:
            #slope of curve at that point
            slope = (y2 - y1) / (x2 - x1)
            
            # perpendicular slope
            pslope = -1/slope  
        #if x2-x1 is 0
        except ZeroDivisionError:
            continue
        #calculate an x and y in the middle
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2

        sign = ((pslope > 0) == (x1 > x2)) * 2 - 1

        #changed x and y
        delta_x = sign * z / ((1 + pslope**2)**0.5)
        delta_y = pslope * delta_x

        points.append((mid_x + delta_x, mid_y + delta_y))
        x1, y1 = x2, y2
    
    #returns
    return points
            
       
    
    