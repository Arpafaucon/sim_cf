#!/usr/bin/env python

import rospy
import crazyflie
import time
import uav_trajectory

if __name__ == '__main__':
    print('starting...')
    rospy.init_node('test_high_level')
    rospy.loginfo('Node started...')
    # print('Node started')
    cf = crazyflie.Crazyflie("crazyflie", "/crazyflie")
    rospy.loginfo('connected to CF')
    cf.setParam("commander/enHighLevel", 1)
    rospy.loginfo('parameters sent to CF')

    rospy.loginfo('Taking off...')
    cf.takeoff(targetHeight = 0.5, duration = 10.0)
    rospy.loginfo('Taking off...command sent')
    time.sleep(20.0)

    # cf.land(targetHeight = 0.0 , duration = 4.0)
    # time.sleep(20.0)
    # rospy.spin()
    rospy.loginfo('Moving...')
    cf.goTo(goal = [0.5, 0.0, 0.0], yaw=0.2, duration = 2.0, relative = True)
    rospy.loginfo('Moving...sent')
    time.sleep(15.0)

    rospy.loginfo('Landing...')
    cf.land(targetHeight = 0.0, duration = 2.0)
    time.sleep(15.0)


    rospy.loginfo('Custom trajectory...')
    
    traj1 = uav_trajectory.Trajectory()
    traj1.loadcsv("takeoff.csv")

    traj2 = uav_trajectory.Trajectory()
    traj2.loadcsv("figure8.csv")

    print(traj1.duration)

    cf.uploadTrajectory(0, 0, traj1)
    cf.uploadTrajectory(1, len(traj1.polynomials), traj2)
    rospy.loginfo('Custom trajectory...uploaded')

    cf.startTrajectory(0, timescale=1.0)
    time.sleep(traj1.duration * 2.0)

    cf.startTrajectory(1, timescale=2.0)
    time.sleep(traj2.duration * 2.0)
    rospy.loginfo('Custom trajectory...started')

    cf.startTrajectory(0, timescale=1.0, reverse=True)
    time.sleep(traj1.duration * 1.0)

    cf.stop()

    rospy.loginfo('Script stopped')