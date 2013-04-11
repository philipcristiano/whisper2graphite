import argparse
import os
import socket

import whisper

def run():
    info = get_info()
    sock = _socket_for_host_port(info.graphite_host, info.graphite_port)
    for path in paths_in_directory(info.whisper_path):
        if path.endswith('.wsp'):
            print path
            metric_path = path.replace('/', '.')[:-4]

            try:
                time_info, values = whisper.fetch(path, 0)
            except whisper.CorruptWhisperFile:
                print 'Corrupt, skipping'
                continue
            metrics = zip(range(*time_info), values)
            for time, value in metrics:
                if value is not None:
                    line = '{} {} {}\n'.format(metric_path, value, time)
                    sock.sendall(line)
    sock.close()

def paths_in_directory(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            yield path


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
