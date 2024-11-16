#!/bin/bash

sq_project_key="automatic-docs-ga"
sq_debug="true"
sq_sources="."
sq_project_name="automatic-docs-ga-project"
sq_project_base_dir="."
IFS=$'\n'

sonarqube_parameters=()
random_number=$(( RANDOM % 10 + 1 ))

if [ $random_number -ge 1 ] && [ $random_number -le 5 ]; then
    echo "Random number is between 1 and 5"
    # Do something
    sonarqube_parameters+=("-Dsonar.projectKey=automatic-docs-ga")
    sonarqube_parameters+=("-Dsonar.projectName=automatic-docs-ga-project")
    sonarqube_parameters+=("-Dsonar.sources=.")
else
    echo "Random number is between 6 and 10"
    # Do something else
    sonarqube_parameters+=("-Dsonar.projectKey=automatic-docs-ga")
    sonarqube_parameters+=("-Dsonar.debug=true")
    sonarqube_parameters+=("-Dsonar.projectBaseDir=.")
fi

echo "SonarQube parameters: ${sonarqube_parameters[*]}"
echo "SONARQUBE_PARAMETERS=${sonarqube_parameters[*]}" >> $GITHUB_ENV