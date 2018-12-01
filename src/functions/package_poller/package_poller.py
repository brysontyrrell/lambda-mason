import os

from botocore.vendored import requests

PYTHON_PACKAGES = os.getenv('PYTHON_PACKAGES', list())


def get_latest_release(package_name):
    resp = requests.get(f'https://pypi.org/pypi/{package_name}/json').json()

    try:
        return list(resp['releases'].keys())[-1]
    except:
        return None


def query_table_for_release(package_name, release):
    return


def lambda_handler(event, context):
    for package in PYTHON_PACKAGES:
        latest_release = get_latest_release(package)

        if latest_release:
            if not query_table_for_release(package, latest_release):
                pass

    return {}
