#!/bin/bash

HOST=$(hostname)

CONFIG_FILES=()

printUsage() {
cat << EndOfMessage
Config Merger
	-d directory with input files
	-o output config file
EndOfMessage
}

buildConfigFile() {
	for file in ${CONFIG_DIR}/*.conf
	do
		LOCAL_CONFIG="${file%.conf}.${HOST}"
		if [[ ! -f $LOCAL_CONFIG ]]; then
			CONFIG_FILES+=($file)
		fi
	done

	for file in ${CONFIG_DIR}/*.$HOST
	do
		CONFIG_FILES+=($file)
	done

	for config_file in ${CONFIG_FILES[@]}
	do
		CAT_FILES+="${config_file} "
	done

	$(cat ${CAT_FILES} > ${OUTPUT_CONFIG_FILE})

	echo "Your config file for the ${HOST} host is available under ${OUTPUT_CONFIG_FILE}"
}

while getopts ":h:d:o:" options; do
  case $options in
    o ) OUTPUT_CONFIG_FILE=$OPTARG          
        ;;
    d ) if [ -d $OPTARG ] ;then
	        CONFIG_DIR=$OPTARG
		else
			echo "${OPTARG} is not a directory"
			exit 1
        fi
        ;;
    h ) printUsage
        exit 0
        ;;
   \?) printUsage
        exit 1;;
  esac
done

buildConfigFile
