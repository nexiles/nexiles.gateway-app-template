# activate virtualenv
source $(dirname $0)/bin/bootstrap.sh

JAVA_VERSION="1.7"
export JAVA_HOME=$(/usr/libexec/java_home -v$JAVA_VERSION)
