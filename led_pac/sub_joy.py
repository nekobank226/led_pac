import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
import pigpio

class JoySubscriber(Node):
    def __init__(self):
        super().__init__('joy_subscriber')

        # parameters setting
        joy_parameters = [
            ('button_x', 0),
            ('button_o', 1),
            ('button_t', 2)
        ]
        self.declare_parameters('', joy_parameters)

        self.BUTTON_JOY = []
        self.BUTTON_JOY.append(self.get_parameter('button_x').value)
        self.BUTTON_JOY.append(self.get_parameter('button_o').value)
        self.BUTTON_JOY.append(self.get_parameter('button_t').value)

        self.subscription = self.create_subscription(Joy, 'joy', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

        self.LED_PIN = [16, 20, 21]
        self.LED_STATUS = [False for _ in range( len(self.LED_PIN))]
        self.pi = pigpio.pi()
        for i in self.LED_PIN:
            self.pi.set_mode(i, pigpio.OUTPUT)

    def listener_callback(self, msg):
        for i in range( len(self.LED_PIN)):
            if msg.buttons[ self.BUTTON_JOY[i]]:
                self.LED_STATUS[i] = True
            else:
                self.LED_STATUS[i] = False
            self.pi.write(self.LED_PIN[i], self.LED_STATUS[i])
    
    def clear_led(self):
        for i in self.LED_PIN:
            self.pi.write(i, False)
    
def main(args=None):
    rclpy.init(args=args)


    joy_subscriber = JoySubscriber()
    try:
        rclpy.spin(joy_subscriber)
    except KeyboardInterrupt:
        joy_subscriber.clear_led()
        joy_subscriber.pi.stop()
        print('pigpio stop')
        joy_subscriber.destroy_node()
        print('joy_subscriber.destroy_node()')
        rclpy.shutdown()
        print('rclpy.shutdown()')

if __name__ == '__main__':
    main()
