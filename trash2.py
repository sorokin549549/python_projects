import cmd


class HelloWorld(cmd.Cmd):
    """Simple command processor example"""

    def do_count(self, line):
        for i in range(10000):
            print(i)

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    try:
        HelloWorld().cmdloop()
    except KeyboardInterrupt:
        print('Abort')