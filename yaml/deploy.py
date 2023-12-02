#!/usr/bin/env python3
''''Set variables for deployment and application'''

import argparse
from importlib.resources import files
from yaml import safe_load

def load_config():
    '''Load YAML file.'''
    return safe_load(
        files('config')
        .joinpath('configuration.yml')
        .read_text(encoding='utf8')
    )


def main():
    '''Load config and set variables'''
    
    config = load_config()
    
    
    parser = argparse.ArgumentParser(
        description='Set Deploy and Application paramaeters',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('--deploy', type=str,
                        help='Deploy environment', required=True,
                        choices=config['deployments'])
    parser.add_argument('--application', type=str,
                        help='Application environment', required=True,
                        choices=config['applications'])
    args = parser.parse_args()

    
    environment = config['deploy'][args.deploy]['environment']
    datacenter =  config['deploy'][args.deploy]['datacenter']
    
    print(f"stage: {config['deploy'][args.deploy]['stage']}")
    print(f"environment: {environment}")
    print(f"subenvironment: {config['deploy'][args.deploy]['subEnvironment']}")
    print(f"datacenter: {datacenter}")
    print(f"portnumber: {config['deploy'][args.deploy]['portNumber']}")
    print(f"namespace: {config['namespace'][datacenter][environment][args.application]}")
    print(f"podnamespace: {config['podnamespace'][environment][args.application]}")

if __name__ == '__main__':
    main()
