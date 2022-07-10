import logging
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie

from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncLogger import SyncLogger

# URI to the Crazyflie to connect to
uri = 'radio://0/100/2M/E7E7E7E7E7'

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)

def log_stab_callback(timestamp, data, logconf):
    print('[%d][%s]: %s' % (timestamp, logconf.name, data))

def simple_log_async(scf, logconf):
    cf = scf.cf
    cf.log.add_config(logconf)
    logconf.data_received_cb.add_callback(log_stab_callback)
    logconf.start()
    time.sleep(5)
    logconf.stop()

(...)

if __name__ == '__main__':
    # Initialize the low-level drivers
    cflib.crtp.init_drivers()

    lg_stab = LogConfig(name='Stabilizer', period_in_ms=10)
    
    # quaternion
    # lg_stab.add_variable('kalman.q1', 'float')
    # lg_stab.add_variable('kalman.q2', 'float')
    # lg_stab.add_variable('kalman.q3', 'float')
    # lg_stab.add_variable('kalman.q0', 'float')
    # lg_stab.add_variable('stateEstimate.qx', 'float')
    # lg_stab.add_variable('stateEstimate.qy', 'float')
    # lg_stab.add_variable('stateEstimate.qz', 'float')
    # lg_stab.add_variable('stateEstimate.qw', 'float')
    
    # linear velocity
    # lg_stab.add_variable('kalman.statePX', 'float')
    # lg_stab.add_variable('kalman.statePY', 'float')
    # lg_stab.add_variable('kalman.statePZ', 'float')
    lg_stab.add_variable('stateEstimate.vx', 'float')
    lg_stab.add_variable('stateEstimate.vy', 'float')
    lg_stab.add_variable('stateEstimate.vz', 'float')
   
    # position
    # lg_stab.add_variable('kalman.stateX', 'float')
    # lg_stab.add_variable('kalman.stateY', 'float')
    # lg_stab.add_variable('kalman.stateZ', 'float')
    # lg_stab.add_variable('stateEstimate.x', 'float')
    # lg_stab.add_variable('stateEstimate.y', 'float')
    # lg_stab.add_variable('stateEstimate.z', 'float')
    
    # # angular velocity
    # lg_stab.add_variable('gyro.x', 'float')
    # lg_stab.add_variable('gyro.y', 'float')
    # lg_stab.add_variable('gyro.z', 'float')
    # lg_stab.add_variable('stateEstimateZ.rateRoll', 'float')
    # lg_stab.add_variable('stateEstimateZ.ratePitch', 'float')
    # lg_stab.add_variable('stateEstimateZ.rateYaw', 'float')

    

    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:

        simple_log_async(scf, lg_stab)
