# Local CheckMK Checks for HL1 und Source Dedicated Servers

### Requirements
- Python 3.8 or higher
- for HL1 games https://pypi.org/project/rHLDS/
- for Source Games https://pypi.org/project/pysrcds/

### Install
Local check has to be installed on the right folder as local check on a client. For example on a debian: `/usr/lib/check_mk_agent/local`

### Important Notes
In the variable checkname are not any spaces allowed! Otherwise CheckMK parse the check wrong!
