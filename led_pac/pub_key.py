import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class KeyboardPublisher(Node):
    def __init__(self):
        super().__init__('keyboard_publisher')
        self.publisher_ = self.create_publisher(String, 'key_topic', 10)
        self.msg = String()

    def pub_key_input(self):
        self.get_logger().info('number 1~3 plz')
        self.msg.data = input('topic number :')
        if 1 <= int(self.msg.data) <= 3:
            self.publisher_.publish(self.msg)
            self.get_logger().info('Publishing: %s' %self.msg.data)
        else:
            self.get_logger().info('number error')

def main(args=None):
    rclpy.init(args=args)


    keyboard_publisher = KeyboardPublisher()
    try:
        print('pub key node start')
        while True:
            keyboard_publisher.pub_key_input()
    finally:
        keyboard_publisher.destroy_node()
        print('keyboard_publisher.destroy_node()')
        rclpy.shutdown()
        print('rclpy.shutdown()')

if __name__ == '__main__':
    main()
