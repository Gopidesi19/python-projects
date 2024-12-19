pipeline {
    agent any
    stages{
        stage ("checkout"){
            steps{
                checkout scmGit(branches: [[name: '*/feature']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Gopidesi19/python-projects.git']])
            }
        }
        
    }
}
