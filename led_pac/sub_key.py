import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import pigpio

class KeyboardSubscriber(Node):
    def __init__(self):
        super().__init__('keyboard_subscriber')
        self.subscription = self.create_subscription(String, 'key_topic', self.listener_callback, 10)
        self.subscription

        self.LED_PIN = [16, 20, 21]
        self.LED_STATUS = [False for _ in range( len(self.LED_PIN))]
        self.pi = pigpio.pi()
        for i in self.LED_PIN:
            self.pi.set_mode(i, pigpio.OUTPUT)      

    def listener_callback(self, msg):
        self.get_logger().info('I heard: %s' % msg.data)
        num = int(msg.data)-1
        self.LED_STATUS[num] = not self.LED_STATUS[num]
        self.pi.write(self.LED_PIN[num], self.LED_STATUS[num])

    def clear_led(self):
        for i in self.LED_PIN:
            self.pi.write(i, False)

def main(args=None):
    rclpy.init(args=args)


    keyboard_subscriber = KeyboardSubscriber()
    try:
        rclpy.spin(keyboard_subscriber)
    except KeyboardInterrupt:
        keyboard_subscriber.clear_led()
        keyboard_subscriber.pi.stop()
        print('pigpio stop')
        keyboard_subscriber.destroy_node()
        print('keyboard_subscriber.destroy_node()')
        rclpy.shutdown()
        print('rclpy.shutdown()')
if __name__ == '__main__':
    main()
