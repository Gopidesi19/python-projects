pipeline {
    agent any
    stages{
        stage ("version"){
            steps{
                sh "python --version"
            }
        }
        stage ("Build"){
            steps{
                sh "Hello world!"
            }
        }
        stage ("test"){
            steps{
                echo "this stage has been tested"
            }
        }
        stage ("deploy"){
            steps{
                echo "python program has successfully deployed"
            }
        }
    }
}
