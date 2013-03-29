import argparse
import os
import socket

import whisper

def run():
    info = get_info()
    sock = _socket_for_host_port
    for dirpath, dirnames, filenames in os.walk(info.whisper_path):
        print dirpath, dirnames, filenames
        for filename in filenames:
            if filename.endswith('.wsp'):
                path = os.path.join(dirpath, filename)
                print path
                metric_path = path.replace('/', '.')[:-4]

                time_info, values = whisper.fetch(path, 0)
                metrics = zip(range(*time_info), values)
                for time, value in metrics[:1000000]:
                    if value is not None:
                        line = '{} {} {}\n'.format(metric_path, value, time)
                        print line,
                        sock.sendall(line)
    sock.close()


def _socket_for_host_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    sock.connect((host, port))
    sock.settimeout(None)
    return sock

def get_info():
    parser = argparse.ArgumentParser(description='Send SQL results to Graphite')
    parser.add_argument('--graphite-host', metavar='graphite-host', type=str, default=None, help='Host to send metrics to')
    parser.add_argument('--graphite-port', metavar='graphite-port', type=int, default=2003, help='Graphite port to send metrics to')
    parser.add_argument('--graphite-prefix', metavar='graphite-prefix', type=str, default='', help='Prefix for metrics')
    parser.add_argument('--whisper-path', metavar='whisper-path', type=str, default='', help='Prefix for metrics')
    return parser.parse_args()


if __name__ == '__main__':
    run()
