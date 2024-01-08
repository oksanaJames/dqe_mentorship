pipeline {
    agent any
    parameters {
        string (defaultValue: '.', description: 'By default all tests will be executed unless the name is specified', name: 'pytestFileName')
        string (defaultValue: 'check_website.robot', description: 'By default all tests will be executed unless the name is specified', name: 'robotFileName')
    }
    stages {
        stage('Clone code from Git') {
            steps {
                // The below will clone your repo and will be checked out to master branch by default.
                git credentialsId: 'auto-credentials', url: 'https://github.com/oksanaJames/dqe_mentorship.git', branch: 'main'
            }
        }
        stage("Install environment") {
            steps {
                withPythonEnv("python") {
                    bat 'python --version'
                    bat 'pip install -r requirements.txt'
                }
            }
        }
        stage('Run pytests tests') {
            steps {
                catchError {
                    // Run test inside virtual environment
                    withPythonEnv('python') {
                        bat "python -m pytest tests\\\\${pytestFileName} --junitxml=results.xml"
                    }
                }
                echo currentBuild.result
            }
        }
        stage('Run robot tests') {
            steps {
                catchError {
                // Run test inside virtual environment
                    withPythonEnv('python') {
                        bat "python -m robot tests\\robot\\\\${robotFileName}"
                    }
                }
                echo currentBuild.result
                script {
                      step(
                        [
                          $class                    : 'RobotPublisher',
                          outputPath                : '',
                          outputFileName            : "*.xml",
                          reportFileName            : "report.html",
                          logFileName               : "log.html",
                          disableArchiveOutput      : false,
                          passThreshold             : 100,
                          unstableThreshold         : 95.0,
                          otherFiles                : "*.png"
                        ]
                    )
                }
            }
        }
    }
    post {
        always {
            junit 'results.xml'
            archiveArtifacts artifacts: '*.xml, *.html'
        }
    }
}