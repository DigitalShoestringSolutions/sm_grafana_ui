# init_SM.py
# initialisation scipt run on download of this Service Module

# Get location of this script

# Take init action:

# The following should probably be done within docker/volumes/environment variables,
#   but not being a docker expert the way I can get working now is using python.
#
# The purpose is to make the UserConfig/daashboards
#   available to the ServiceModules/Grafana docker container.


# Create hard nonsymbolic Unix link between the file in UserConfig and the SM:

from pathlib import Path
import os

# Note that due to the dubious exec(f.read()) that actually runs this script, 
#   Path(__file__) returns the Assembly/ShoestringAssembler location!

config_dashboards_dir_abs = Path(__file__).parents[3].joinpath("UserConfig/dashboards")
SM_dashboards_dir_abs = Path(__file__).parents[2].joinpath("Grafana/dashboard_ui/config/dashboards")

for dashboard in config_dashboards_dir_abs.rglob('*'):
    dest_path = SM_dashboards_dir_abs.joinpath(dashboard.relative_to(config_dashboards_dir_abs))
    
    if dashboard.is_dir():
        # Directory names with spaces are natively supported
        os.mkdir(dest_path)
    
    else:
        # Note how both "paths are in quotes" to support names with whitespace
        os.system('ln "' + str(dashboard) + '" "' + str(dest_path) + '"')
