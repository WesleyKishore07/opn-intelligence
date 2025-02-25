# common/config/base_config.py
import os
import sys

def get_service_port(service_name: str = None) -> int:
    """
    Get the actual running port of the service.
    For microservices, use the port specified in uvicorn command.
    """
    deployment_mode = os.getenv('DEPLOYMENT_MODE', 'monolith')

    if deployment_mode == 'microservice':
        # Get port from uvicorn arguments
        try:
            # Find --port argument in uvicorn command
            args = sys.argv
            if '--port' in args:
                port_index = args.index('--port') + 1
                if port_index < len(args):
                    return int(args[port_index])
        except:
            pass

    return 8080  # Default monolith port