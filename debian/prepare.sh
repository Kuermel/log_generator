#!/bin/bash
self="prepare"
dst_dist="10.04"

function log {
    line=`date`" :${self}: $@"
    echo $line
#    echo $line >> $log_file
}

function die_with_error {
    if [ "$1" != "0" ]; then
        log $2
        exit 1
    fi
}


function start {
    log "--------------------------------------------start------------------------------------------------------------"
}

function finish {
    log "--------------------------------------------finish-----------------------------------------------------------"
}

function usage {
    echo "release.sh -n projectname -v 0.0.0 -p path_to_package_dir -r path_to_repository -t dst_dist"
    echo " -n : project_name"
    echo " -v : version"
    echo " -p : package path (temp path)"
    echo " -r : repository path"
    echo " -t : dst dist"
    exit 1
}

while getopts "n:v:r:p:t:" OPTION
do
     case $OPTION in
         h)
             usage
             ;;
         n)
             project_name=$OPTARG
             ;;
         v)
             version=$OPTARG
             ;;
         d)
             dependency_file=$OPTARG
             ;;
         r)
             repository_directory=$OPTARG
             ;;
         p)
             package_directory=$OPTARG
             ;;
         t)
             dst_dist=$OPTARG
             ;;
         ?)
             usage
             ;;
     esac
done

if [ "$project_name"x == "x" ] || [ "$version"x == "x" ] || [ "$repository_directory"x == "x" ] || [ "$package_directory"x == "x" ]; then
    usage
fi


function prepare_for_10 {
    log "Starting to copy from:${repository_directory} to ${package_directory}"
    rsync -a --exclude=.git --exclude=debian/ --exclude=.idea --exclude=.DS_Store ${repository_directory} ${package_directory}
    die_with_error $? "Copy Failed, resp:$?"
    log "Prepare end on ${package_directory}"
}

function prepare_for_12 {
    prepare_for_10
    log "Prepare for 12"
#    for file in cjson-64.so oracle-64.tar.gz
#    do
#        log "remove ${package_directory}/${file}"
#        rm ${package_directory}/$file
#    done
    log "Prepare end on ${package_directory} for 12"
}

rm -rf ${package_directory}

package_directory="${package_directory}/opt/log_generator/"
log "Starting to prepare ${package_directory} directory"
mkdir -p ${package_directory}
if [ "${dst_dist}" == "10.04" ]; then
    prepare_for_10
fi
if [ "${dst_dist}" == "12.04" ]; then
    prepare_for_12
fi
