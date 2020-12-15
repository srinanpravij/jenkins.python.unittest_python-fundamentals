// Powered by Infostretch

timestamps {

node () {

	stage ('python_test - Checkout') {
 	 checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '', url: 'https://github.com/srinanpravij/jenkins.python.unittest_python-fundamentals.git']]])
	}
	stage ('python_test - Build') {

       powershell "python -m unittest discover -s ./src/test/ -p '*_test.py'"

	}
}
}