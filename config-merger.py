#!/usr/bin/env python3

import argparse
import os
import socket
import glob
from os.path import basename


def create_arguments():
    parser = argparse.ArgumentParser(description='merge configs from one dir to one great config file')

    parser.add_argument('confd_directory', help='conf.d directory with configfiles')
    parser.add_argument('output_filename', help='output config filename')
    
    parser.add_argument('--verbose', help= 'print verbose output', action='store_true')

    args = parser.parse_args()
    return args

def get_config_files(config_files_dir, verbose):
    hostname = socket.gethostname()

    result_config_files = []

    founded_config_files = glob.glob(os.path.join(config_files_dir,"*.conf"))
    founded_config_files += glob.glob(os.path.join(config_files_dir, "*.%s" % hostname))

    founded_config_files.sort()

    for config_file in founded_config_files:
        filename = os.path.splitext(basename(config_file))[0]

        host_config_filename = os.path.join(config_files_dir, "%s.%s" % (filename, hostname))
        
        if verbose:
            print("config Filename for custom config: %s" % host_config_filename)

        if os.path.isfile(host_config_filename):
            result_config_files.append(host_config_filename)
            
            if verbose:
                print("use custom config")
        else:
            result_config_files.append(config_file)
        
            if verbose:
                print("use shared config")

    return result_config_files

def concat_config_files(config_files, output_filename, verbose):
    if verbose:
        print("output filename: %s" % output_filename)

    with open(output_filename, "wb") as outfile:
        for config_file in config_files:
            if verbose:
                print("concat %s to output config file" % config_file)

            with open(config_file, "rb") as infile:
                outfile.write(infile.read())


if __name__ == "__main__":
    args = create_arguments()

    if 'confd_directory' in args and 'output_filename' in args:
        config_files = get_config_files(args.confd_directory, args.verbose)

        concat_config_files(config_files, args.output_filename, args.verbose)

    
